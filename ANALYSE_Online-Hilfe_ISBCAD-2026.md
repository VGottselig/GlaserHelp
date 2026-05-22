# Gründliche Analyse & Bewertung der Online-Hilfe für ISBCAD 2026

*Stand: 22. Mai 2026 — Autor: automatisierter Voll-Scan (875 Seiten) + manuelle Stichproben*

---

## 0. Executive Summary

Die Online-Hilfe zu **ISBCAD 2026** ist ein umfangreiches, mit *Help & Manual* erzeugtes CHM-Projekt mit **875 HTML-Themen, 1.890 Index-Einträgen und ~3.700 Abbildungen**. Sie deckt das gesamte Produktspektrum (Konstruktion, Bewehrung, Listen, Zusatzprogramme) systematisch ab.

**Gesamtbewertung:** **gut bis sehr gut** — solide Substanz mit klarer Struktur, sehr hoher technischer Integrität (keine toten Links, keine fehlenden Bilder) und einheitlichem Aufbau aller Seiten. Schwächen liegen weniger im Großen als in vielen kleinen Defekten und in einer technischen Basis, die für 2026 sichtbar in die Jahre kommt.

**Die fünf wichtigsten Befunde**

1. **17 defekte Sprungmarken** im Inhaltsverzeichnis (`#node5`, `#node6` … `#node20`) zeigen ins Leere — alle in der Themengruppe „Konstruktion 1 → Kreis / Teilkreis".
2. **Drei Holzbau-Seiten teilen sich denselben (falschen) `<title>`** „Darstellung der Dachausmittlung (Dialog)" — obwohl sie unterschiedliche Inhalte (Dachausmittlung, Sparrenbeschriftung, Sparrenverteilung) behandeln.
3. **44 distinkte Titel werden mehrfach vergeben** (bis zu 5×), z. B. „Verlegung löschen" (5 Seiten). Bei einer Volltextsuche oder im Verlauf kann der Anwender die Themen nicht eindeutig auseinanderhalten.
4. **Stichproben-Tippfehler in „Neu in ISBCAD 2026"**: „einzeilgen" (statt „einzeiligen") und „Sparrenverbeschriftung" (statt „Sparrenbeschriftung") sind in der für Marketing/Update-Kommunikation wichtigsten Seite präsent.
5. **Technische Basis veraltet**: Zeichensatz `iso-8859-1` (statt UTF-8), inline-CSS in jeder einzelnen Datei, CHM-Format (auf modernen Windows-Installationen mit zunehmenden Anzeige-Einschränkungen).

Weitere systematische Befunde, Empfehlungen und Detailtabellen folgen in den Abschnitten 1–7.

---

## 1. Produktcharakter — was die Hilfe über ISBCAD verrät

### 1.1 Was ist ISBCAD?

ISBCAD ist ein **2D-CAD-System mit integriertem Bewehrungsprogramm** für den Stahlbetonbau, vertrieben von der **Glaser CAD GmbH** (Hannover; Support +49 511 592931-0). Das Produkt wird in **drei Ausbaustufen** ausgeliefert:

- **Konstruktions- und Bewehrungsprogramm** (Vollausbau)
- **Konstruktionsprogramm** (nur 2D-CAD)
- **Bewehrungsprogramm** (nur Bewehrung)

### 1.2 Was macht ISBCAD aus — das Alleinstellungsprofil aus Hilfe-Sicht

Die Hilfe stellt das Produkt durch **Hauptmenü-Module** vor (Konstruktion 1/2/3, Bewehrungsprogramm: Matten/Formstahl/Formmatten, Listen, Zusatzprogramme). Aus den Inhalten lassen sich folgende **Besonderheiten und Schwerpunkte** ablesen — die Reihenfolge entspricht der Sichtbarkeit in der Hilfe:

| Bereich | Funktionsschwerpunkt |
|---|---|
| **Stahlbetonbewehrung** | Formstahl, Matten und Formmatten als drei eigenständige Bewehrungsarten; Biegeformen, Staffeln, Bogenstaffeln, Voutenverlegung, Verlegung im Schnitt |
| **Konformität EC2** | Mindestverankerungs- und Übergreifungslängen nach Eurocode 2, Expositionsklassen, Betondeckung nach EC2 |
| **Listen & Auszüge** | Stückliste, Stahlliste (umfangreich konfigurierbar), Bauteilfaktoren, „Laufende Meter"-Berechnung |
| **Modellaustausch** | DWG/DXF Import/Export, **IFC Section Tool** (in 2026 neu entwickelt), PDF-Vektorimport/-export, DGN-Export, DSTV-Import |
| **Statik-Schnittstellen** | Datenaustausch mit *Pollux Statik, Dlubal, Frilo, RIB, Scia, Infograph, Cubus, MB AEC, pcae* (Belege siehe Hilfe → externe Links) |
| **Spezial-Branchen** | **Holzbau** (Dachausmittlung, Sparrenverteilung), **Stahlbau-Varianten**, **BAMTEC-Bewehrungsteppiche**, Hüllflächen-/Massenberechnung |
| **FEM-Anbindung** | as-Werte-Dialoge, as-Linien, FEM-Datensätze, Bewehrungsvorschläge aus FEM-Programmen |
| **Plangestaltung** | Über 100 Schraffurarten, Maßstabsbereiche, Blattrahmen, Planköpfe nach EC2 |
| **Schutzmechanismus** | Schutzschlüssel (CodeMeter-Dongle), eigener „LKT"-Schutz, eDocPrinter PDF Pro lizenziert mitausgeliefert |
| **Russland-Sonderdarstellung** | Eigene Positionierung „im russischen Stil" — Hinweis auf internationale Anwender |

### 1.3 Was ist typisch für ISBCAD?

- **Befehls-/Tastenkürzel-Sprache**: Funktionen werden mit Kürzeln wie `[ Konst 1 | Texte | SucErs ]`, `[ Formst | Detail | Durchbrüche ]`, `[ ForZus ]`, `[ TxtSet ]`, `[ VeForm ]`, `[ VKN ein ]` referenziert. Das ist für Profi-Anwender effizient, für Neulinge aber eine Lernhürde.
- **Sehr feingranulare Funktionsstruktur**: 875 Themen für ein einzelnes Produkt ist überdurchschnittlich tief gegliedert.
- **Anlehnung an Statiker-Sprache**: Begriffe wie *Positionierung, Verlegung, Auszug, Biegeform, Staffel, Fächer, Harfe* prägen die Hilfe — das passt zur Zielgruppe Bauingenieure/Konstrukteure.
- **„So wie"-Logik**: Eigene Schaltfläche zur Übernahme von Eigenschaften (Strichtyp, Stift, Maßstab) von vorhandenen Elementen — ein typischer Workflow.
- **Anrede konsequent „Sie"** (995 Treffer von „Sie können", 1.709 × „Klicken Sie", 803 × „Wählen Sie", 1.142 × „Geben Sie"). Du-Form und Gender-Doppelformen kommen praktisch nicht vor (nur ein einziger Beleg für „Anwendende"; sonst durchgehend „Anwender", „Benutzer").

### 1.4 Was ist neu in 2026?

Die Seite *„Neu in ISBCAD 2026"* (17.4 kB Text) listet u. a.:

- **Textfelder** als Ersatz für Blocktexte (mit Suchen & Ersetzen)
- **Mehrfach-Ansichten** der Zeichenfläche (bis zu 4 parallele Ausschnitte)
- **Zeichenfläche um Systemwinkel drehen** statt nur Systemwinkel ändern
- **IFC Section Tool** komplett neu (2D-Schnittvorschau, Undo/Redo, erweiterte Exporteinstellungen)
- **Stückliste**: Faktor anzeigen/ändern, Texte > 50 Zeichen erlaubt, alphanumerische Sortierung
- **Verbesserte Maßstabskorrektur** (Schraffurfaktor & Maßketten optional mit-korrigiert)
- **Verbesserte Text-Zwischenablage** (Reihenfolge und Anordnung erhalten)
- Diverse Detailverbesserungen bei Durchbrüchen, Voutenverlegung, eDocPrinter, ForZus

---

## 2. Struktur & Navigation

### 2.1 Quantitative Übersicht

| Metrik | Wert |
|---|---|
| HTML-Themen gesamt | **875** (787 `.htm` + 88 `.xhtm`) |
| Themen im Inhaltsverzeichnis (`.hhc`) | 770 |
| Einträge im Stichwortindex (`.hhk`) | 1.890 |
| Themen, die weder in TOC noch Index erreichbar sind | 87 |
| Eingebettete Abbildungen (PNG/GIF/JPG) | 3.691 |
| Externe Hyperlinks | 63 (zu 46 verschiedenen URLs) |
| Größtes Einzel-Thema | `top_historie.htm` (193 kB) |
| Hierarchie-Tiefe | bis zu 5 Ebenen |

### 2.2 Top-Level-Gliederung (11 Hauptkapitel)

1. Willkommen bei ISBCAD 2026
2. Was ist ISBCAD?
3. Neu in ISBCAD 2026
4. Programmoberfläche
5. Konfiguration und Einrichtung
6. Grundlagen der Bedienung
7. Datei- und Ausgabefunktionen
8. **Konstruktionsprogramm** (Konst 1, 2, 3)
9. **Bewehrungsprogramm** (Matten, Formstahl, Formmatten)
10. Listen, Systemeinstellungen und weitere Konstruktionsfunktionen
11. Hauptmenü - Programmmodule / Zusatzprogramme / Hilfe / Support

Die Gliederung folgt **konsequent dem Programmmenü** des Produkts — das ist ein großer Pluspunkt für Wiedererkennbarkeit und Kontexthilfe, hat aber den Nachteil, dass dieselbe Funktion in mehreren Menüpfaden vorkommen kann und dann mehrfach dokumentiert ist.

### 2.3 Befund: Defekte Sprungmarken im Inhaltsverzeichnis

**17 Einträge im Inhaltsverzeichnis (TOC) zeigen auf `#nodeN`-Anker, die in den Zielseiten nicht existieren.** Das heißt: Wer in der Hilfe-Navigation auf diese Einträge klickt, landet zwar auf der richtigen Seite, scrollt aber nicht zum gewünschten Abschnitt. Beispiele:

```
konst1_kr_teilkreis_stichmas.htm#node5
konst1_kr_tangentezeichnendieanzweikreisenanliegt.htm#node18
konst1_kr_parallelenkreisoderteilkreiszeichnen.htm#node11
konst1_kr_kreis_2_kreise_tangente.htm#node20
konst1_kr_teilkreis_2_punkte_radius.htm#node6
konst1_kr_kreisandreitangentenzeichnen.htm#node10
konst1_kr_kreis_2_kreise_mit_radius.htm#node19
konst1_kr_kreisoderteilkreislschen.htm#node17
konst1_kr_teilkreiszwischenmarkierungenlschen.htm#node16
konst1_kr_teilkreiszwischenmarkierungenersetzen.htm#node14
```

Alle 17 Treffer liegen im Themenblock **„Konstruktion 1 → Kreis/Teilkreis"** und betreffen Unterkapitel zu Kreis- und Teilkreis-Konstruktionen. Vermutlich wurde ein Bündel von zuvor mit Sprungmarken nummerierten Abschnitten neu strukturiert, ohne die TOC anzupassen.

**Empfehlung:** Entweder Anker in den Zielseiten ergänzen oder die `#nodeN`-Suffixe aus der `OnlineHilfe_DE.hhc` entfernen.

### 2.4 Befund: 44 mehrfach vergebene Themen-Titel

44 verschiedene `<title>`-Werte werden von zwei oder mehr Seiten geteilt. Die Top-10:

| Titel | # Seiten |
|---|---:|
| Verlegung löschen | 5 |
| Positionsnummern umsortieren | 4 |
| Verlegung ändern | 4 |
| Alle Positionen neu durchzählen | 3 |
| Positionen in Reihe bringen | 3 |
| Lücke in Positionsreihenfolge schaffen | 3 |
| Verlegung generieren | 3 |
| Verknüpfung erstellen und bearbeiten | 3 |
| **Darstellung der Dachausmittlung (Dialog)** | **3** (defekt — siehe 2.5) |
| Biegeform an der Schalkante ableiten | 2 |

Die meisten dieser Duplikate sind inhaltlich gewollt — z. B. existieren „Verlegung löschen" eigenständig in Formstahl, Formmatten, Matten und in der jeweiligen Schnitt-Variante. **Aber**: weil der Browser-Tab, der Verlauf, die Index-Auflistung und die CHM-Volltextsuche nur den Titel zeigen, kann der Anwender die Varianten nicht auseinanderhalten. **Empfehlung**: Disambiguierender Suffix wie *„Verlegung löschen (Formstahl)"*, *„Verlegung löschen (Matten)"* usw.

### 2.5 Befund: Drei Holzbau-Seiten mit demselben (falschen) Titel

Eindeutig ein Copy-Paste-Fehler. Die drei Seiten haben unterschiedliche Inhalte, aber **identische `<title>`-Zeile**:

| Dateiname | `<title>` (alle gleich!) | Tatsächlicher Inhalt (H1) |
|---|---|---|
| `rd_holzbau-einstellungen_dachausmittlung.htm` | „Darstellung der Dachausmittlung (Dialog)" | Holzbau-Einstellungen – Dachausmittlung |
| `rd_holzbau-einstellungen_sparrenbeschriftung.htm` | „Darstellung der Dachausmittlung (Dialog)" | Holzbau-Einstellungen – Sparrenbeschriftung |
| `rd_holzbau-einstellungen_sparrenverteilung.htm` | „Darstellung der Dachausmittlung (Dialog)" | Holzbau-Einstellungen – Sparrenverteilung |

**Empfehlung:** Sofort fixen — `<title>` jeweils an den H1-Text anpassen.

### 2.6 Befund: Orphan-Dateien im Auslieferungspaket

**87 Seiten liegen im Verzeichnis, sind aber weder im Inhaltsverzeichnis noch im Index gelistet.** Davon haben **79 Dateien gar keinen eingehenden Link** aus irgendeiner anderen Hilfe-Seite. Sie sind aus der Hilfe heraus also nicht erreichbar. Einige Gruppen:

- **Alte Versionshistorie-Snippets**: `_des_neu-in-isbcad-2012.xhtm`, `_des_neu-in-isbcad-2014.xhtm`, `_des_neu-in-isbcad-2015.xhtm`, `_des_neu-in-version-2011.xhtm`, `_des_neu-in-version-2016.xhtm`. Vermutlich in der Quelle als „Snippet" eingebunden, vom Generator aber als eigenständige Seite mitgeschrieben.
- **Drei `_todo_`-Dateien**: `_todo_darstellung-eines-wandaufbaus-aendern.xhtm`, `_todo_hoehe-aus-zeichung-abgreifen_(huellflaechen).xhtm`, `_todo_waende-konfigurieren.xhtm`. Das Präfix `_todo_` deutet auf Work-in-Progress hin — entweder bewusste Konvention oder altes WIP, das mitgeliefert wurde.
- **Diverse `_rd_*.xhtm`, `_tsk_*.xhtm`, `_rk_*.xhtm`**: vermutlich Help-&-Manual-Snippets (Topic-Includes), die als eigenständige Datei mit erzeugt werden.

**Empfehlung:** Quellprojekt prüfen — Snippets entweder vom Export ausschließen oder bewusst belassen und entsprechend dokumentieren. Auf jeden Fall die `_todo_`-Dateien überprüfen und entweder integrieren oder löschen.

### 2.7 Befund: Tippfehler im Dateinamen

`tsk_verlegungung-bearbeiten_(durchmesser-in-schnittdarstellung).htm` — „Verlegungung" ist eine doppelte Endung. Der `<title>` der Seite ist allerdings korrekt („Durchmesser in Schnittdarstellung — Verlegung bearbeiten"), der Tippfehler ist also nur in der URL/Datei sichtbar. Sollte vor dem Umbenennen geprüft werden, ob Lesezeichen-/Verlinkungskompatibilität betroffen ist.

---

## 3. Inhalt & Sprache

### 3.1 Sprachstil und Anrede

Die Hilfe verwendet einen **konsistent professionellen, zielgruppengerechten Stil** im *Sie*-Stil. Die häufigsten Verbformen aus Imperativ-Anweisungen sind:

| Phrase | Häufigkeit |
|---|---:|
| Klicken Sie | 1.709 |
| Geben Sie | 1.142 |
| Sie können | 995 |
| Wählen Sie | 803 |
| Anweisungen mit `§`-Listenzeichen | 3.432 |

Das Sprachniveau ist **angemessen technisch** für die Doppelzielgruppe Statiker/Bauingenieure und CAD-Konstrukteure. Begriffe wie *Übergreifungslänge*, *Verankerung*, *Expositionsklasse*, *Bauteilfaktor*, *Stiftnummer*, *Folienautomatik* werden benutzt, ohne sie jedes Mal zu definieren — das ist für die Zielgruppe richtig, könnte aber für Einsteiger durch ein **Glossar** ergänzt werden. Ein solches Glossar konnte im Verzeichnis nicht gefunden werden.

### 3.2 Befund: Bestätigte Tippfehler

| Wort | Korrektur | Wo gefunden | Sichtbarkeit |
|---|---|---|---|
| **einzeilgen** | einzeiligen | `top_neuheiten.htm` („Neu in ISBCAD 2026") | **hoch** — Marketing-Seite |
| **Sparrenverbeschriftung** | Sparrenbeschriftung | `rd_holzbau-einstellungen_sparrenbeschriftung.htm` | mittel |
| **Verlegungung** (im Dateinamen) | Verlegung | `tsk_verlegungung-bearbeiten_...htm` | nur in URL |

Die per Regex überprüften klassischen Fehlerquellen (altdt. *daß/muß/läßt*, *Standart*, *seperat*, *Auzug*, *zusätlich*, *natuerlich* u. v. m.) ergaben **null Treffer** — der Großteil des Korpus ist rechtschreiblich sauber. Über das Gesamtkorpus von ~2,6 Mio. Zeichen ist die festgestellte Fehlerrate sehr niedrig, deutet aber auf **Lücken in der Korrekturlese-Disziplin gerade bei zuletzt geänderten Seiten** hin (Neuheiten-Seite!).

### 3.3 Befund: Marken-Inkonsistenzen „ISBCAD"

| Schreibweise | Vorkommen |
|---|---:|
| `ISBCAD` (korrekt) | 916× |
| `isbcad` (kleinbuchstabig) | 11× |
| `isb cad` (mit Leerzeichen) | 15× |

Die Lower-Case-Treffer kommen aus Pfaden und Dateinamen, die als sichtbarer Text gezeigt werden (z. B. `con_isbcad_feedback.htm`, `des_isb_logfiles.htm`). 26 Markenfehler bei einer Marke, die ~900× korrekt geschrieben ist, ist ein **niedriges, aber leicht behebbares** Problem.

### 3.4 Befund: Mehrfach-Verbformen und Konsistenz

- **wählen/auswählen**: 902 Treffer — beide Formen werden synonym verwendet. Empfehlung: einheitliche Verwendung („wählen Sie X im Dialog … aus" vs. „wählen Sie X" konsistent regeln).
- **Anwender** (13×) vs. **Anwendende** (1×) vs. **Benutzer** (5×) vs. **Benutzende** (0×): drei verschiedene Begriffe für die Zielperson, keine gendersensitive Linie. Empfehlung: redaktionelle Leitlinie festlegen.
- **662 verdächtige Klammer-Leerzeichen**: Pattern `( ` oder ` )` (Leerzeichen direkt nach öffnender oder vor schließender Klammer). Manche sind gewollt (z. B. um Tastenfolge `[ Esc ]` darzustellen), andere sind echte Layoutfehler. Lohnt eine gezielte Korrektur.

### 3.5 Sprachliche Stärken (positiv)

- **Konsistente Strukturmuster**: Jede Aufgaben-Seite hat „So wird's gemacht:" → §-Liste → Verweise. Das ist eine starke, lerneffiziente Konvention.
- **„Siehe:" und „Zugehörige Referenzen:"** als Querverweis-Anker werden überall eingesetzt — gut für die Vernetzung.
- **Tastenfolge-Notation** `[ Konst 1 | Texte | SucErs ]` ist im Produkt verankert und in der Hilfe konsequent durchgehalten.
- **Hinweise/Tipps/Achtung-Boxen** (mit eigenen Icons `20x20_hinweis.png`, `20x20_tipp.png`, `20x20_achtung.png`) sind eine etablierte Konvention.

---

## 4. Vollständigkeit & Lücken

### 4.1 Befund: Sehr kurze (fast leere) Themen

Sechs Themen liegen **unter 200 Zeichen tatsächlichem Inhalt** und sind faktisch Platzhalter:

| Datei | Inhalt | Bewertung |
|---|---|---|
| `dat_zeichnung_plotten.htm` | „Entspricht den Funktionen in Zeichnung drucken, jedoch wird hier ein anderes Ausgabeprofil vorgeschlagen." | Stub — könnte als Re-Direct oder Abschnitt in `dat_zeichnung_drucken.htm` aufgehen |
| `rd_systemdaten_ausgabeeinheiten.htm` | „Maßketten Optionen. Zugehörige Referenz: Systemdaten" | extrem dünn |
| `des_revision.htm` | „Revision ISBCAD 2026 Ausgabe: 2026.1.b Letzte Überarbeitung: 10.04.2026" | als Versions-Stempel ok |
| `konst3_sonprg.htm` | „Sonderprogramme — Spezielle Programmierungen; nur auf besondere Anfrage lieferbar." | Stub, aber bewusst — informiert über Kunden-Sonderlösungen |
| `mattenzusammenfassung.htm` | „Zusammenfassen und Entflechten von Matten. Funktionen Beschreibung Matten zusammenfassen…" | nur Funktions-Liste, keine Erklärung |
| `formst_bipos_gost.htm` | „Diese spezielle Darstellungsart wird nur in Russland verwendet" | Stub für GOST-Norm |

Weitere 26 Seiten liegen im Bereich 200–500 Zeichen — überwiegend „Verwerfen"-, „Beenden"- oder „Letzte rückgängig machen"-Funktionen, die naturgemäß kurz sein dürfen.

### 4.2 Befund: Drei `_todo_*`-Dateien im Auslieferungspaket

Wie unter 2.6 beschrieben, sind drei Dateien mit `_todo_`-Präfix vorhanden. Ihre Inhalte sind teils vollständig (Wandaufbau-Anweisungen, Höhe abgreifen) — sie könnten also in die reguläre Hilfe verlinkt werden. Aktuell sind sie aus der Hilfe heraus **nicht erreichbar**.

### 4.3 Befund: Sechs `.xhtm`-Snippets mit technischen Titeln

In den Topic-Includes (`.xhtm`) blieb in einigen Fällen der **interne Quelldatei-Name als `<title>`** stehen, statt eines lesbaren Titels:

- `_tsk_biegeform-definieren.xhtm` → `<title>` = „TSK_Biegeform-definieren"
- `_tsk_zusatztext-hinzuf-formmatt.xhtm` → `<title>` = „TSK_Zusatztext-hinzuf-Formmatten"

Wenn diese Seiten als Popup oder Inline-Include angezeigt werden, ist das unkritisch — aber wenn sie über Suche direkt angesteuert werden, bekommt der Anwender einen verwirrenden technischen Titel zu sehen.

### 4.4 Tatsächliche Abdeckung

Im Vergleich zur Top-Level-Menü-Struktur sind **alle Programmbereiche dokumentiert**: Konstruktion 1/2/3, Bewehrungsprogramm in allen Varianten, Listen, Stahlbau, Holzbau, IFC Section Tool, Hauptmenü-Module, Zusatzprogramme (BAMTEC, Planköpfe, Trassierung, Planverwaltung, Variantenprogramme, ISBVIEW, eDocPrinter). Im Stichwortindex sind 1.890 Schlagwörter erfasst — das ist überdurchschnittlich.

**Was eher fehlt** (in der Hilfe nicht oder nur am Rande gefunden):

- **Glossar / Begriffsverzeichnis**: nicht vorhanden. Begriffe wie *as-Werte*, *LKT*, *VKN*, *Verlegefaktor*, *Voute* werden im Kontext genutzt, aber nicht zentral erklärt.
- **Tastenkürzel-Übersicht**: existiert als „Hotkeys"-Eintrag, aber kein zentrales Cheatsheet.
- **Schritt-für-Schritt-Tutorial**: in der Hilfe wird auf eine externe PDF („Erste Schritte" über Menüleiste) und YouTube-Videos verwiesen — innerhalb der CHM also keine durchgängige Tour.
- **Lizenz- und Aktivierungs-Dokumentation**: nur indirekt über „Schutzmechanismus LKT" und CodeMeter-Dongle abgedeckt.
- **Fehlermeldungen-Referenz**: keine zentrale Übersicht typischer Fehlertexte und Lösungen.
- **Barrierearmut**: keine Hinweise auf Screenreader-Unterstützung, Tastatur-Bedienung über Maus hinaus, Kontrast-Einstellungen.

---

## 5. Technik & Format

### 5.1 Auslieferungsformat & Werkzeug

| Aspekt | Wert | Bewertung |
|---|---|---|
| Autoring-Tool | **Help & Manual** (alle 875 Seiten) | etabliertes Werkzeug, gut |
| Ausgabeformat | Microsoft HTML Help (.chm) | **veraltet** — Microsoft empfiehlt Migration seit Jahren |
| Doctype | `<!DOCTYPE html>` (HTML5) | ok |
| Zeichensatz deklariert | `iso-8859-1` (Latin-1) | **veraltet** — sollte UTF-8 sein |
| Stylesheet | `isbcad_style.css` + Inline-`<style>` in **jeder** Datei | suboptimal — Wartungslast |
| `<font>`-Tag verwendet | 0 Treffer | gut, kein 90er-Jahre-HTML |
| Defekte interne Links | **0** | hervorragend |
| Fehlende Bilder | **0** | hervorragend |

### 5.2 Befund: CHM als Auslieferungsformat ist in 2026 ein Risiko

- Microsoft pflegt die `hh.exe`-Anzeige seit Jahren nicht mehr aktiv weiter.
- CHM blockiert standardmäßig JavaScript und manche CSS-Funktionen aus Sicherheitsgründen.
- Bei Auslieferung an Kunden in **Citrix-/Terminalserver-Umgebungen** oder bei **Network-Pfaden** muss CHM oft per `MOTW`-Trick freigegeben werden.
- Web-Help (HTML5-Multi-Page) wäre für 2026 zeitgemäßer und ist von Help & Manual als Ausgabeformat unterstützt.

**Empfehlung**: Zusätzliche Webhelp-/PDF-Variante prüfen (Help & Manual unterstützt Multi-Format-Export aus dem gleichen Quellprojekt). Damit könnte ISBCAD die Hilfe sogar online (z. B. unter `help.isbcad.de`) zugänglich machen — was die Auffindbarkeit über Google massiv verbessern würde.

### 5.3 Befund: Inline-CSS in jeder Datei

Jede der 875 Seiten enthält einen `<style>`-Block — vermutlich vom Generator erzeugt für „eigenständig anzeigbare" Themen. Das bläht die Datei-Größen auf und macht Designänderungen nur über das Quellprojekt sinnvoll. Bei einem CSS-Bug muss jede Seite neu generiert werden.

### 5.4 Befund: Charset-Deklaration vs. echte Kodierung

Im `<meta>`-Tag steht `charset=iso-8859-1`, gespeichert sind die Dateien aber typisch als CP-1252 (Windows-Latin-1, das Sonderzeichen wie „typografische Anführungszeichen" zusätzlich kennt). Bei strenger Browser-Interpretation kann das zu kleinen Glitches führen. Im Scan wurden allerdings **keine** Encoding-Fehler (Mojibake wie `Ã¤`) gefunden — d. h. in der Praxis funktioniert es.

**Empfehlung**: in 2026 auf **UTF-8** umstellen — Help & Manual unterstützt das seit langem.

### 5.5 Externe Links — Pflege-Risiko

63 externe Links zu 46 verschiedenen Zielen. Darunter Partner-Statik-Anbieter, Standard-Verbände (Baustahlgewebe, ISB e.V., BVBS) und YouTube-Playlists. **Risiko**: Externe URLs altern (HTTP → HTTPS, Reorganisation). Eine **regelmäßige Link-Check-Routine** (z. B. monatlich) wäre sinnvoll.

Zwei kleine technische Inkonsistenzen aufgefallen:

- Manche externe Links nutzen `http://` statt `https://` (z. B. `http://www.schoeck.de`, `http://www.halfen.de`, `http://www.bvbs.de`).
- Die URL `https://www.baustahlgewebe.com/` wird in mehreren Varianten verwendet (`/`, `/index.php/de/`, ohne abschließenden Slash).

---

## 6. Stärken-/Schwächen-Profil

### Stärken (was sehr gut gelingt)

- **Komplette und systematische Abdeckung** aller Programmmodule mit 875 Themen und 1.890 Indexeinträgen.
- **Technische Integrität**: keine toten Links, keine fehlenden Bilder, keine Encoding-Fehler im Anwender-sichtbaren Bereich.
- **Klare didaktische Struktur**: Aufgaben-Seiten folgen alle dem Muster Beschreibung → „So wird's gemacht:" → §-Schritte → Querverweise.
- **Konsistente Notation** für Tastenfolgen `[ Modul | Untermenü | Funktion ]`.
- **Visuell unterstützt**: 3.700+ Abbildungen, durchschnittlich 4 pro Seite — sehr bildreich.
- **Konventionen-Seite vorhanden** (`des_konventionen.htm`), die das Layout der Boxen (Hinweis/Tipp/Achtung) erklärt.
- **Saubere Verwendung von „Sie"-Anrede** ohne Stilbrüche.
- **Versions-/Revision-Hinweis** vorhanden (`des_revision.htm`).

### Schwächen (priorisierte Liste)

| # | Schwäche | Schweregrad | Aufwand zur Behebung |
|---|---|---|---|
| 1 | 17 defekte `#nodeN`-Sprungmarken im TOC | mittel | klein (TOC bereinigen) |
| 2 | Drei Holzbau-Seiten mit identischem falschen Titel | mittel | trivial |
| 3 | Tippfehler „einzeilgen" auf der „Neu in 2026"-Seite | hoch (Sichtbarkeit) | trivial |
| 4 | 44 mehrfach vergebene Titel ohne Disambiguierung | mittel | mittel (Titel-Audit) |
| 5 | 87 Orphan-Dateien im Auslieferungspaket | klein | klein–mittel |
| 6 | Drei `_todo_*.xhtm` mit WIP-Konvention im Ship-Paket | klein | trivial |
| 7 | Sechs `.xhtm`-Snippets mit technischen `TSK_*`-Titeln | klein | trivial |
| 8 | Iso-8859-1 statt UTF-8 | klein (kein Anwenderschaden) | mittel (Re-Generieren) |
| 9 | CHM als Hauptformat in 2026 | strategisch | groß (Workflow-Änderung) |
| 10 | Sechs nahezu leere Themen-Stubs | klein | klein |
| 11 | Inkonsistente Marken-Schreibweise „isbcad"/„isb cad" (26 Treffer) | sehr klein | klein |
| 12 | Begriffs-Inkonsistenzen (wählen/auswählen, Anwender/Benutzer) | sehr klein | mittel |
| 13 | Kein zentrales Glossar | mittel | groß (Inhalt schreiben) |
| 14 | Externe Links teils mit `http://` statt `https://` | klein | trivial |
| 15 | Inline-CSS in jeder einzelnen Datei | sehr klein | mittel (Generator-Settings) |

---

## 7. Empfohlene Maßnahmen — priorisiert

### Sofort (≤ 1 Tag Aufwand, hoher sichtbarer Effekt)

1. **Tippfehler „einzeilgen" → „einzeiligen"** auf der Neuheiten-Seite korrigieren. *(Quelle: `top_neuheiten.htm`, Abschnitt „Verbesserte Text-Zwischenablage".)*
2. **Tippfehler „Sparrenverbeschriftung" → „Sparrenbeschriftung"** korrigieren. *(Quelle: `rd_holzbau-einstellungen_sparrenbeschriftung.htm`.)*
3. **Drei Holzbau-Titel** in den jeweiligen Quelldateien auf den tatsächlichen H1-Text anpassen.
4. **17 defekte `#nodeN`-Anker** im Inhaltsverzeichnis-Eintrag bereinigen (entweder Anker setzen oder Suffix entfernen).
5. **Drei `_todo_*.xhtm`** im Quellprojekt prüfen — entweder freischalten und verlinken, oder löschen.

### Mittel-/Kurzfrist (Wochenaufwand)

6. **Titel-Audit der 44 mehrfach vergebenen `<title>`-Werte**: jedem Duplikat einen klärenden Klammer-Zusatz geben („… (Formstahl)" / „… (Matten)" usw.).
7. **Sechs Themen-Stubs** entweder ausbauen oder durch Re-Direct auf den vollständigen Artikel ersetzen.
8. **Marken-Konsistenz**: 26 Lower-Case-Vorkommen von „isbcad"/„isb cad" suchen & ersetzen.
9. **Begriffs-Glossar** als neue Hilfeseite anlegen (as-Werte, LKT, VKN, Voute, Verlegefaktor, Bauteilfaktor, BAMTEC, Expositionsklasse, IFC, DSTV, GOST u. a.).
10. **Externer-Link-Audit**: alle 46 URLs prüfen, `http` → `https`, URL-Variationen vereinheitlichen.
11. **Six `_tsk_*.xhtm`** mit `TSK_…`-Titel: lesbare Titel setzen.
12. **`OnlineHilfe_DE.hhk`** auf 1.890 Einträge prüfen — Doppeleinträge und tote Verweise stichprobenhaft kontrollieren.

### Strategisch (Monate, Roadmap)

13. **Zusätzliches Web-Help-Ausgabeformat** aus dem Help-&-Manual-Projekt generieren und unter `help.isbcad.de` veröffentlichen — verbessert Findbarkeit über Google, ist auf Tablets/Mobil bedienbar.
14. **Migration auf UTF-8** im Quellprojekt — beseitigt latenten Encoding-Risikofall.
15. **Zentrale Inline-Styles eliminieren** (im Generator-Template auf externe CSS-Datei umstellen) — reduziert die Dateigrößen erheblich.
16. **Reguläres Qualitätsgate** vor jedem Release: automatischer Scan (Link-/Image-/Anker-Check, Titel-Duplikate, Tippfehler-Wortliste). Die in diesem Bericht eingesetzte Methode lässt sich in einen einfachen Python-Build-Step gießen.
17. **Tutorial-Modul** in die Hilfe integrieren — die PDF-„Erste Schritte" als HTML-Tour mit interaktiven Verweisen umsetzen.

---

## 8. Zusammenfassende Bewertung

| Dimension | Bewertung (Schulnote) | Begründung |
|---|---|---|
| Inhalt & Sprache | **2** (gut) | Konsistenter, professioneller Stil; sehr niedrige Tippfehler-Rate; Begriffs-Inkonsistenzen sind mild |
| Struktur & Navigation | **2–3** (gut bis befriedigend) | Logische Gliederung an Programmmenü; aber 17 defekte Anker, 44 mehrdeutige Titel |
| Vollständigkeit | **2** (gut) | Sehr breite Abdeckung; nur sechs echte Stubs; Glossar/Tutorial-Lücke |
| Technik & Format | **3** (befriedigend) | Saubere Link-/Bild-Integrität, aber Iso-8859-1, Inline-CSS und CHM-Format sind 2026 nicht mehr State of the Art |
| Produktcharakter & Profil | **2** (gut) | Schwerpunkt Stahlbeton-Bewehrung + EC2-Konformität + IFC + Statik-Schnittstellen ist deutlich erkennbar |
| **Gesamtnote** | **2** (gut) | Solide Substanz, viele Detailbefunde, niedriger Aufwand für Schnellverbesserungen |

Die Online-Hilfe zu ISBCAD 2026 ist insgesamt **eine wertige, gut gepflegte Dokumentation**. Mit etwa **einer Personenwoche Korrekturaufwand** lassen sich die wichtigsten Befunde (Punkte 1–10 in Abschnitt 7) abarbeiten und damit das wahrgenommene Qualitätsniveau spürbar anheben. Mittelfristig (innerhalb von ISBCAD 2027) lohnt sich der Schritt zu einem **Web-Help-Format** als Ergänzung oder Ersatz zum klassischen CHM.

---

*Methodik: Voll-Scan aller 875 HTML-Themen + Inhaltsverzeichnis (`.hhc`) + Stichwortindex (`.hhk`) per Python (regex-basiert), kombiniert mit manuellen Stichproben von 25 zufällig ausgewählten Seiten plus gezielten Verifikationen aller Auffälligkeiten. Korpus-Größe: ~2,6 Mio. Zeichen Reintext.*
