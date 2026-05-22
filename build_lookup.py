#!/usr/bin/env python3
"""
Erzeugt eine Lookup-Datei (LOOKUP.md) aus allen .htm-Dateien
der ISBCAD-2026-Online-Hilfe.

Pro Datei extrahiert:
  - Titel       (aus <title> oder <h1>/p_Task/p_Heading1)
  - Pfad        (aus Breadcrumb <p class="crumbs">)
  - Beschreibung(aus <meta name="description"> ODER p_Task_Info / p_A_Allgemein,
                 je nachdem welcher Text vollstaendiger ist)
  - Keywords    (aus <meta name="keywords">)

Format pro Eintrag (gut grep- und scanbar):
    ### dateiname.htm
    - Titel: ...
    - Pfad: ...
    - Beschreibung: ...
    - Keywords: ...
"""

from __future__ import annotations

import html
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT  = ROOT / "LOOKUP.md"

# --- Regex-Patterns -----------------------------------------------------------

RE_TITLE     = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
RE_META_DESC = re.compile(
    r'<meta\s+name="description"\s+content="([^"]*)"',
    re.IGNORECASE,
)
RE_META_KW   = re.compile(
    r'<meta\s+name="keywords"\s+content="([^"]*)"',
    re.IGNORECASE,
)
RE_CRUMBS    = re.compile(
    r'<p\s+class="crumbs">(.*?)</p>',
    re.IGNORECASE | re.DOTALL,
)
# Titel: ganzer Paragraph, da der Text oft auf mehrere <span>s aufgeteilt
# ist (z.B. "aS" mit Tiefstellung des S = 3 spans).
RE_P_TASK    = re.compile(
    r'<p\s+class="p_Task"[^>]*>(.*?)</p>',
    re.IGNORECASE | re.DOTALL,
)
RE_P_HEAD1   = re.compile(
    r'<h1\s+class="p_Heading1"[^>]*>(.*?)</h1>',
    re.IGNORECASE | re.DOTALL,
)
# Beschreibung: ganzer Paragraph (analog Titel-Problem).
RE_P_TASK_INFO = re.compile(
    r'<p\s+class="p_Task_Info"[^>]*>(.*?)</p>',
    re.IGNORECASE | re.DOTALL,
)
RE_P_A_ALLG    = re.compile(
    r'<p\s+class="p_A_Allgemein"[^>]*>(.*?)</p>',
    re.IGNORECASE | re.DOTALL,
)
# Dialog-Beschreibungen tragen oft die beste Funktionsbeschreibung
RE_P_DIALOG    = re.compile(
    r'<p\s+class="p_R_Dialog_Info"[^>]*>(.*?)</p>',
    re.IGNORECASE | re.DOTALL,
)
RE_TAGS      = re.compile(r"<[^>]+>")
RE_WS        = re.compile(r"\s+")


def strip_tags(s: str) -> str:
    """
    Entfernt HTML-Tags, dekodiert Entities, normalisiert Whitespace.
    Inline-Tags (span/b/i/em/strong/sub/sup/a/font/u/small) werden
    spurlos entfernt, damit z.B. <span>a</span><span sub>S</span> zu
    'aS' wird (statt 'a S '). Block-Tags werden zu Leerzeichen.
    """
    if not s:
        return ""
    s = re.sub(
        r"</?(?:span|b|i|em|strong|sub|sup|a|font|u|small)(?:\s[^>]*)?>",
        "",
        s,
        flags=re.IGNORECASE,
    )
    s = RE_TAGS.sub(" ", s)
    s = html.unescape(s)
    s = s.replace(" ", " ")
    s = RE_WS.sub(" ", s).strip()
    return s


def read_file(path: Path) -> str:
    """
    Liest mit Fallback-Encodings.
    Help & Manual deklariert ISO-8859-1, schreibt aber in Wirklichkeit
    Windows-1252 (z.B. 0x96 = en-dash '–', 0x91/92 = Smart Quotes).
    Daher cp1252 zuerst — als Superset von ISO-8859-1 fuer Druckzeichen.
    """
    for enc in ("utf-8", "cp1252", "iso-8859-1"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    return path.read_bytes().decode("cp1252", errors="replace")


def extract_crumbs(raw: str) -> str:
    """
    Holt den Navigations-Pfad und reduziert ihn auf 'A > B > C'.
    Entfernt das Wort 'Navigation:' und leere Segmente.
    """
    m = RE_CRUMBS.search(raw)
    if not m:
        return ""
    txt = strip_tags(m.group(1))
    txt = re.sub(r"^Navigation:\s*", "", txt, flags=re.IGNORECASE)
    # ">" wird im HTML als &gt; codiert und vorher zu '>' entitiy-decoded
    parts = [p.strip() for p in txt.split(">") if p.strip()]
    # Filter offensichtliche Platzhalter aus dem Help-&-Manual-Output
    parts = [p for p in parts
             if "keine" not in p.lower() or "uebergeordnet" not in p.lower()]
    parts = [p for p in parts if p and p != "Navigation:"]
    return " > ".join(parts)


def extract_title(raw: str, meta_title: str) -> str:
    """
    Bevorzugt den menschlich formatierten Titel aus dem Body
    (p_Task / p_Heading1). Faellt auf <title> zurueck. Wenn der
    Body-Titel verdaechtig kurz ist (<= 2 Zeichen), wird ebenfalls
    auf <title> zurueckgegriffen.
    """
    for rx in (RE_P_TASK, RE_P_HEAD1):
        m = rx.search(raw)
        if m:
            cand = strip_tags(m.group(1))
            if cand and len(cand) > 2:
                return cand
    return strip_tags(meta_title)


def _meta_is_truncated(meta: str) -> bool:
    """Help&Manual schneidet meta-Description bei ~160 Zeichen ab."""
    if not meta:
        return False
    # Endet ohne sauberen Satzabschluss -> wahrscheinlich abgeschnitten
    if meta.endswith("...") or meta.endswith("…"):
        return True
    last = meta.rstrip()[-1:]
    return len(meta) >= 150 and last not in ".!?:)"


def _meta_is_noisy(meta: str) -> bool:
    """
    Manche meta-Descriptions starten mit Icon-Beschriftungen aus dem
    p_Aufruf-Bereich (z.B. 'oder', 'B-akt_...').
    """
    return bool(re.match(r"^(oder|B-akt|Icon|\s)", meta))


def extract_description(raw: str, meta_desc: str) -> str:
    """
    Waehlt den vollstaendigsten Beschreibungstext aus:
      1. Body-Paragraphen (p_Task_Info, p_R_Dialog_Info, p_A_Allgemein),
         ggf. die ersten 2 zusammengesetzt.
      2. meta-Description, sofern sauber und vollstaendig.
    """
    meta = strip_tags(meta_desc)

    body_candidates: list[str] = []
    for rx in (RE_P_TASK_INFO, RE_P_DIALOG, RE_P_A_ALLG):
        for m in rx.finditer(raw):
            t = strip_tags(m.group(1))
            if t and len(t) > 10:
                body_candidates.append(t)

    # Kombiniere bis zu 2 Body-Absaetze, sofern Platz da ist
    body = ""
    if body_candidates:
        body = body_candidates[0]
        if len(body) < 180 and len(body_candidates) > 1:
            body = (body + " " + body_candidates[1]).strip()

    # Entscheidungs-Logik
    if body and (_meta_is_truncated(meta) or _meta_is_noisy(meta)):
        chosen = body
    elif body and len(body) >= len(meta):
        chosen = body
    else:
        chosen = meta or body

    return shorten(chosen, max_chars=260)


def shorten(s: str, max_chars: int) -> str:
    """Schneidet sauber an Satz- oder Wortgrenze."""
    if len(s) <= max_chars:
        return s
    cut = s[:max_chars]
    # bevorzugt nach Satzende abschneiden
    for sep in (". ", "; ", ", "):
        idx = cut.rfind(sep)
        if idx > max_chars * 0.6:
            return cut[: idx + 1].rstrip() + " ..."
    # sonst an letztem Leerzeichen
    idx = cut.rfind(" ")
    if idx > 0:
        return cut[:idx].rstrip() + " ..."
    return cut + " ..."


def extract_keywords(raw: str) -> str:
    """
    Liest Keywords aus dem meta-Tag und reduziert sie:
    - exakte Duplikate (case-insensitive) entfernen
    - Suffix-Varianten wie "Biegeform" + "Biegeform Formmatten" zusammenlegen:
      wenn der laengere Term mit dem kuerzeren beginnt, kuerzeren behalten
    - Limit: maximal 5 Keywords (Kontext steht ohnehin im Pfad)
    """
    m = RE_META_KW.search(raw)
    if not m:
        return ""
    txt = html.unescape(m.group(1))
    parts = [p.strip() for p in txt.split(",") if p.strip()]

    # exakte Dedup
    seen: set[str] = set()
    uniq: list[str] = []
    for p in parts:
        k = p.lower()
        if k not in seen:
            seen.add(k)
            uniq.append(p)

    # Suffix-Dedup: wenn ein laengerer Term mit einem schon vorhandenen
    # kuerzeren beginnt, ueberspringen.
    pruned: list[str] = []
    for p in uniq:
        if any(p.lower().startswith(q.lower() + " ")
               or p.lower().startswith(q.lower() + "-")
               for q in pruned):
            continue
        pruned.append(p)

    return ", ".join(pruned[:5])


def process_file(path: Path) -> dict[str, str]:
    raw = read_file(path)

    meta_title = ""
    m = RE_TITLE.search(raw)
    if m:
        meta_title = m.group(1)

    meta_desc = ""
    m = RE_META_DESC.search(raw)
    if m:
        meta_desc = m.group(1)

    return {
        "file":  path.name,
        "title": extract_title(raw, meta_title),
        "path":  extract_crumbs(raw),
        "desc":  extract_description(raw, meta_desc),
        "kw":    extract_keywords(raw),
    }


def format_entry(e: dict[str, str]) -> str:
    lines = [f"### {e['file']}"]
    if e["title"]:
        lines.append(f"- Titel: {e['title']}")
    if e["path"]:
        lines.append(f"- Pfad: {e['path']}")
    if e["desc"]:
        lines.append(f"- Beschreibung: {e['desc']}")
    if e["kw"]:
        lines.append(f"- Keywords: {e['kw']}")
    return "\n".join(lines)


def main() -> int:
    htm_files = sorted(
        p for p in ROOT.iterdir()
        if p.is_file() and p.suffix.lower() in (".htm", ".html")
    )
    if not htm_files:
        print("Keine .htm-Dateien gefunden.", file=sys.stderr)
        return 1

    entries: list[dict[str, str]] = []
    for p in htm_files:
        try:
            entries.append(process_file(p))
        except Exception as exc:  # noqa: BLE001
            print(f"WARN {p.name}: {exc}", file=sys.stderr)

    # Header der Lookup-Datei (kurz erklaeren, wie die Datei zu nutzen ist)
    header = (
        "# ISBCAD 2026 - Online-Hilfe Lookup\n"
        "\n"
        f"Index ueber {len(entries)} Hilfethemen. Jeder Eintrag verweist auf "
        "eine HTML-Datei im selben Verzeichnis. Der Chatbot waehlt anhand von "
        "**Titel**, **Pfad** (Menue-Kontext), **Beschreibung** und "
        "**Keywords** die passende Datei aus und liest deren Inhalt fuer die "
        "vollstaendige Antwort.\n"
        "\n"
        "Format pro Eintrag:\n"
        "```\n"
        "### dateiname.htm\n"
        "- Titel: kurzer Funktionsname\n"
        "- Pfad: Menue > Untermenue > Funktion\n"
        "- Beschreibung: 1-3 Saetze, was die Funktion macht\n"
        "- Keywords: kommagetrennte Schlagworte\n"
        "```\n"
        "\n"
        "---\n"
    )

    body = "\n\n".join(format_entry(e) for e in entries)
    OUT.write_text(header + "\n" + body + "\n", encoding="utf-8")

    print(f"OK: {len(entries)} Eintraege -> {OUT}")
    print(f"Groesse: {OUT.stat().st_size / 1024:.1f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
