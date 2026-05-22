# 2do-Liste für den technischen Redakteur — Online-Hilfe ISBCAD 2026

*Basis: Vollanalyse vom 22.05.2026 (`ANALYSE_Online-Hilfe_ISBCAD-2026.md`)*
*Quellprojekt: Help & Manual — Ausgabeziel: `OnlineHilfe_DE.chm`*

---

## Lese-Anleitung

**Spalten je Aufgabe**

| Symbol | Bedeutung |
|---|---|
| ☐ | offen — bitte abhaken bei Erledigung |
| **P1** | Sofort (sichtbar im ausgelieferten Produkt) |
| **P2** | Strukturelle Konsistenz |
| **P3** | Qualitätsverbesserung |
| **P4** | Modernisierung (mit Entwicklung abstimmen) |
| ⏱ | Aufwandsschätzung (S = < 30 min, M = 1–4 h, L = 1–3 Tage, XL = > 3 Tage) |

**Arbeitsweise-Hinweis**: Alle Pfadangaben beziehen sich auf das **Quellprojekt im Help & Manual**, nicht auf die generierten Ausgabedateien. Korrigieren Sie immer in der Quelle und regenerieren Sie anschließend die CHM-Ausgabe.

---

## P1 — Sofort sichtbare Fehler

*Diese Punkte sind in der ausgelieferten Hilfe als Mangel sichtbar. Mit überschaubarem Aufwand große Wirkung.*

### 1.1 Tippfehler korrigieren

- ☐ **P1 ⏱ S** — Tippfehler **„einzeilgen"** → **„einzeiligen"**
  - **Datei**: `top_neuheiten.htm` (Quelltopic: *Neu in ISBCAD 2026*)
  - **Abschnitt**: „Verbesserte Text-Zwischenablage"
  - **Suchstring**: `einzeilgen`
  - **Kontext**: *„untereinander abgesetzten einzeilgen Texten erhalten"*
  - **Korrektur**: `einzeiligen`
  - **Hinweis**: Höchste Sichtbarkeit, weil Marketing-/Update-Seite.

- ☐ **P1 ⏱ S** — Tippfehler **„Sparrenverbeschriftung"** → **„Sparrenbeschriftung"**
  - **Datei**: `rd_holzbau-einstellungen_sparrenbeschriftung.htm`
  - **Suchstring**: `Sparrenverbeschriftung`
  - **Korrektur**: `Sparrenbeschriftung` (das doppelte „ver" entfernen)

- ☐ **P1 ⏱ S** — Dateiname-Typo **„verlegungung"** → **„verlegung"**
  - **Datei**: `tsk_verlegungung-bearbeiten_(durchmesser-in-schnittdarstellung).htm`
  - **Aktion**: Datei im Quellprojekt umbenennen auf `tsk_verlegung-bearbeiten_(durchmesser-in-schnittdarstellung).htm`
  - **Vorsicht**: Vor dem Umbenennen prüfen, ob externe Verweise auf den alten Dateinamen existieren (Kundenlesezeichen, Verlinkungen im Programmcode für Kontexthilfe). Bei Unsicherheit: alten Dateinamen als Alias-Redirect beibehalten.

### 1.2 Drei Holzbau-Seiten mit identischem Titel reparieren

Alle drei Seiten zeigen denselben (falschen) `<title>` „Darstellung der Dachausmittlung (Dialog)", obwohl sie jeweils ein anderes Holzbau-Thema dokumentieren. Im Browser-Tab, im CHM-Verlauf und in der Volltextsuche werden sie dadurch ununterscheidbar.

- ☐ **P1 ⏱ S** — Titel anpassen `rd_holzbau-einstellungen_dachausmittlung.htm`
  - **Aktuell**: „Darstellung der Dachausmittlung (Dialog)"
  - **Soll**: „Holzbau-Einstellungen – Dachausmittlung (Dialog)"

- ☐ **P1 ⏱ S** — Titel anpassen `rd_holzbau-einstellungen_sparrenbeschriftung.htm`
  - **Aktuell**: „Darstellung der Dachausmittlung (Dialog)"
  - **Soll**: „Holzbau-Einstellungen – Sparrenbeschriftung (Dialog)"

- ☐ **P1 ⏱ S** — Titel anpassen `rd_holzbau-einstellungen_sparrenverteilung.htm`
  - **Aktuell**: „Darstellung der Dachausmittlung (Dialog)"
  - **Soll**: „Holzbau-Einstellungen – Sparrenverteilung (Dialog)"

### 1.3 17 defekte Sprungmarken im Inhaltsverzeichnis bereinigen

Im TOC zeigen 17 Einträge auf `#nodeN`-Anker, die in den Zielseiten nicht existieren. Klick funktioniert (Seite öffnet), aber Scroll-Ziel wird nicht angesteuert.

**Entscheidung treffen**: entweder (A) Anker in den Zielseiten ergänzen oder (B) `#nodeN`-Suffix im TOC entfernen. Empfehlung: **Option B**, weil die Themen jeweils einseitig sind und ein Anker keinen Mehrwert bietet.

- ☐ **P1 ⏱ M** — In `OnlineHilfe_DE.hhc` (Quellprojekt: Inhaltsverzeichnis-Editor) die `#nodeN`-Suffixe entfernen bei folgenden 17 Einträgen — alle im Block **„Konstruktion 1 → Kreis/Teilkreis"**:

  - `konst1_kr_teilkreis_stichmas.htm#node5`
  - `konst1_kr_teilkreis_2_punkte_radius.htm#node6`
  - `konst1_kr_teilkreisendpunktverschieben.htm#node7`
  - `konst1_kr_teilkreismitstartpunktwinkelundradiuszeichnen.htm#node8`
  - `konst1_kr_teilkreisdurchdreipunktezeichnen.htm#node9`
  - `konst1_kr_kreisandreitangentenzeichnen.htm#node10`
  - `konst1_kr_parallelenkreisoderteilkreiszeichnen.htm#node11`
  - `konst1_kr_kreisanzweitangentenmitradiuszeichnen.htm#node12`
  - `konst1_kr_ellipsezeichnen.htm#node13`
  - `konst1_kr_teilkreiszwischenmarkierungenersetzen.htm#node14`
  - `konst1_kr_kreisoderteilkreisndern.htm#node15`
  - `konst1_kr_teilkreiszwischenmarkierungenlschen.htm#node16`
  - `konst1_kr_kreisoderteilkreislschen.htm#node17`
  - `konst1_kr_tangentezeichnendieanzweikreisenanliegt.htm#node18`
  - `konst1_kr_kreis_2_kreise_mit_radius.htm#node19`
  - `konst1_kr_kreis_2_kreise_tangente.htm#node20`
  - `konst1_kr_kreis_3_kreise.htm#node21`

  **Hinweis**: in Help & Manual genügt es meist, in der TOC-Einstellung des jeweiligen Eintrags den Anker-Wert leer zu lassen.

### 1.4 `_todo_`-Dateien klären

Drei Dateien tragen das Präfix `_todo_` und sind nicht in TOC/Index gelistet. Inhaltlich sind sie aber teils vollständig. Entweder fertigstellen + verlinken oder löschen.

- ☐ **P1 ⏱ M** — Entscheiden und umsetzen für:
  - `_todo_darstellung-eines-wandaufbaus-aendern.xhtm` (309 Zeichen — Anweisungstext zu Wandaufbau-Liste)
  - `_todo_hoehe-aus-zeichung-abgreifen_(huellflaechen).xhtm` (822 Zeichen — Höhe aus Zeichnung; Hinweis: **Tippfehler im Dateinamen**: „zeichung" statt „zeichnung")
  - `_todo_waende-konfigurieren.xhtm` (837 Zeichen — Wandaufbau konfigurieren)
  - **Aktion 1**: Inhalte prüfen, ob aktuell und korrekt
  - **Aktion 2**: Bei Übernahme: in regulären Snippet überführen (Präfix `_todo_` entfernen), in das relevante Hilfe-Topic einbinden
  - **Aktion 3**: Bei Verwerfen: aus Quellprojekt entfernen

### 1.5 Stub-Seiten ausbauen oder umleiten

- ☐ **P1 ⏱ M** — `dat_zeichnung_plotten.htm` (nur 17 Zeichen sinnvoller Inhalt)
  - **Aktuell**: lediglich Verweis auf „Zeichnung drucken"
  - **Empfehlung**: Entweder als richtiges Topic ausführen (Unterschiede zu „drucken" beschreiben) oder als Topic löschen und den TOC-Eintrag direkt auf `dat_zeichnung_drucken.htm` umlenken.

- ☐ **P1 ⏱ M** — `rd_systemdaten_ausgabeeinheiten.htm` (51 Zeichen)
  - **Aktuell**: „Maßketten Optionen. Zugehörige Referenz: Systemdaten"
  - **Empfehlung**: vollständige Beschreibung der Ausgabe-Einheiten-Einstellungen ergänzen (Kontext aus dem Programm: welche Einheiten, welche Standardwerte, wofür benutzt).

- ☐ **P1 ⏱ S** — `mattenzusammenfassung.htm` (196 Zeichen)
  - **Aktuell**: nur eine Funktions-Liste ohne Erklärung
  - **Empfehlung**: kurze Einleitung zum Thema „Mattenzusammenfassung" + Verweise auf die einzelnen Funktionsseiten.

- ☐ **P3 ⏱ S** — `konst3_sonprg.htm` (129 Zeichen — *„Sonderprogramme; nur auf besondere Anfrage lieferbar"*)
  - **Empfehlung**: belassen, aber einen Hinweis ergänzen, **wie** Kunden eine Anfrage stellen (Telefon, E-Mail, Glaser-Auftragsentwicklung-Seite verlinken).

- ☐ **P3 ⏱ S** — `formst_bipos_gost.htm` (210 Zeichen)
  - **Aktuell**: „Diese spezielle Darstellungsart wird nur in Russland verwendet"
  - **Empfehlung**: kurz erklären, **was** GOST-Stil von der DIN-Darstellung unterscheidet (ein Satz reicht), damit deutsche Anwender nicht versehentlich aktivieren.

---

## P2 — Strukturelle Konsistenz

### 2.1 Disambiguierung der 44 mehrfach vergebenen Titel

Aktuell gibt es 44 Titel, die von 2 bis 5 verschiedenen Topics geteilt werden. Im CHM-Verlauf, im Index und in der Volltextsuche ist eine eindeutige Identifikation für den Anwender unmöglich. Lösung: jedem Duplikat einen klärenden Klammer-Suffix geben.

**Vorgehensvorschlag**: Bei jeder Mehrfach-Gruppe wird der Hauptkontext im Klammer-Suffix ergänzt (Formstahl / Formmatten / Matten / Verlegung im Schnitt …). Beispiele unten.

#### Gruppe „Verlegung löschen" (5 Topics)
- ☐ **P2 ⏱ S** — `formst_vedusn_loesche.htm` → Titel **„Verlegung löschen (Durchmesser in Schnittdarstellung)"**
- ☐ **P2 ⏱ S** — `formst_veform_loesche.htm` → **„Verlegung löschen (Formstahl)"**
- ☐ **P2 ⏱ S** — `formst_vestaf_loesche.htm` → **„Verlegung löschen (Staffel)"**
- ☐ **P2 ⏱ S** — `tsk_verlegung-loeschen_(formmatten).htm` → **„Verlegung löschen (Formmatten)"**
- ☐ **P2 ⏱ S** — `_tsk_verlegung-im-schnitt-loeschen.xhtm` → **„Verlegung im Schnitt löschen"** *(falls eigenständig sichtbar)*

#### Gruppe „Verlegung ändern" (4 Topics)
- ☐ **P2 ⏱ S** — `formst_vedusn_aendere.htm` → **„Verlegung ändern (Durchmesser in Schnittdarstellung)"**
- ☐ **P2 ⏱ S** — `formst_veform_aendere.htm` → **„Verlegung ändern (Formstahl)"**
- ☐ **P2 ⏱ S** — `formst_vestaf_aendere.htm` → **„Verlegung ändern (Staffel)"**
- ☐ **P2 ⏱ S** — `_tsk_verlegung-im-schnitt-aendern.xhtm` → **„Verlegung im Schnitt ändern"**

#### Gruppe „Positionsnummern umsortieren" (4 Topics)
- ☐ **P2 ⏱ S** — `formma_aendpos_umpos.htm` → **„Positionsnummern umsortieren (Formmatten)"**
- ☐ **P2 ⏱ S** — `formst_aendpos_umpos.htm` → **„Positionsnummern umsortieren (Formstahl)"**
- ☐ **P2 ⏱ S** — `matten_aendern_umpos.htm` → **„Positionsnummern umsortieren (Matten)"**
- ☐ **P2 ⏱ S** — `_tsk_positionen-umsortieren.xhtm` → **„Positionen umsortieren"**

#### Gruppe „Verlegung generieren" (3 Topics)
- ☐ **P2 ⏱ S** — `formst_vedusn_generi.htm` → **„Verlegung generieren (Durchmesser in Schnittdarstellung)"**
- ☐ **P2 ⏱ S** — `formst_vestaf_generi.htm` → **„Verlegung generieren (Staffel)"**
- ☐ **P2 ⏱ S** — `_tsk_verlegung-im-schnitt-neu-generieren.xhtm` → **„Verlegung im Schnitt neu generieren"**

#### Gruppe „Alle Positionen neu durchzählen" (3 Topics)
- ☐ **P2 ⏱ S** — `formma_aendpos_allpos.htm` → **„… (Formmatten)"**
- ☐ **P2 ⏱ S** — `formst_aendpos_allpos.htm` → **„… (Formstahl)"**
- ☐ **P2 ⏱ S** — `matten_aendern_allpos.htm` → **„… (Matten)"**

#### Gruppe „Positionen in Reihe bringen" (3 Topics)
- ☐ **P2 ⏱ S** — `formma_aendpos_reihe.htm` → **„… (Formmatten)"**
- ☐ **P2 ⏱ S** — `formst_aendpos_reihe.htm` → **„… (Formstahl)"**
- ☐ **P2 ⏱ S** — `tsk_position-in-reihe.htm` → ggf. Konsolidieren oder ebenfalls disambiguieren

#### Gruppe „Lücke in Positionsreihenfolge schaffen" (3 Topics)
- ☐ **P2 ⏱ S** — `formma_luecke.htm` → **„… (Formmatten)"**
- ☐ **P2 ⏱ S** — `luecke.htm` → **„… (allgemein)"** oder Dateiname-Klärung
- ☐ **P2 ⏱ S** — `tsk_luecke-einfuegen.htm` → **„… (Aufgabenanleitung)"**

#### Gruppe „Verknüpfung erstellen und bearbeiten" (3 Topics)
- ☐ **P2 ⏱ S** — `formst_vedusn_vkn.htm` → **„… (Durchmesser in Schnittdarstellung)"**
- ☐ **P2 ⏱ S** — `formst_veform_vkn.htm` → **„… (Formstahl)"**
- ☐ **P2 ⏱ S** — `formst_vestaf_vkn.htm` → **„… (Staffel)"**

#### Restliche Duplikatpaare (je 2 Topics)
*Pro Paar je 2 Aufgaben — Klammer-Suffix nach Kontext setzen:*

- ☐ **P2 ⏱ S** — „Hüllflächen": `_rd_huellflaechen_(bauteileinstellungen).xhtm` (RD) / `konst1_huellflaechen.htm`
- ☐ **P2 ⏱ S** — „Darstellung der Holzverbindungen konfigurieren": `_tsk_darstellung-ausgemittelter-dachlinien-konfigurieren.xhtm` *(hier offenbar ein Copy-Paste-Titel-Fehler — bitte zusätzlich auf inhaltliche Stimmigkeit prüfen!)* / `rd_holzbau-einstellungen_holzverbindung.htm`
- ☐ **P2 ⏱ S** — „Verlegung erzeugen": `_tsk_verlegung-erzeugen-formma.xhtm` / `_tsk_verlegung-erzeugen-formst.xhtm` → Suffix `(Formmatten)` / `(Formstahl)`
- ☐ **P2 ⏱ S** — „Biegeform an der Schalkante ableiten": `biegeform_an_der_schalkante_ab.htm` / `formst_biform_forabl.htm`
- ☐ **P2 ⏱ S** — „Biegeform aus einer Typentabelle erzeugen": `biegeform_aus_einer_typentabel.htm` / `formst_biform_fortyp.htm`
- ☐ **P2 ⏱ S** — „Biegeform aus Geometrie-Polygon erzeugen": `biegeform_aus_geometrie-polygo.htm` / `formst_biform_forgeo.htm`
- ☐ **P2 ⏱ S** — „Biegerollendurchmesser anzeigen": `biegerollendurchmesser.htm` / `formst_biform_biedur.htm`
- ☐ **P2 ⏱ S** — „Allgemeine Vorgehensweise": `con_formmatten.htm` → **„Allgemeine Vorgehensweise (Formmatten)"** / `con_formstahl.htm` → **„Allgemeine Vorgehensweise (Formstahl)"**
- ☐ **P2 ⏱ S** — „Abfrage- und Eingabeleiste": `des_abfrage-_und_eingabezeile.htm` / `des_abfrageleiste.htm` → eventuell **zusammenführen**, da identisches Thema
- ☐ **P2 ⏱ S** — „BAMTEC (Bewehrungsteppiche)": `des_bamtec.htm` / `konst3_bewehrungsteppiche_bamtec.htm` → Konsolidieren oder eindeutig disambiguieren
- ☐ **P2 ⏱ S** — „Verlegung im Verknüpfungsmodus": `des_verknuepfung.htm` (Formstahl) / `des_verknuepfung_matten.htm` (Matten) → Suffix ergänzen
- ☐ **P2 ⏱ S** — „Einzelne Position löschen": `einzelne_position_loeschen.htm` / `formst_biform_loe_pos.htm`
- ☐ **P2 ⏱ S** — „Positionierungsstil konfigurieren": `formma_bipos_defpos.htm` / `formst_bipos_defpos.htm`
- ☐ **P2 ⏱ S** — „Fächer": `formma_bipos_faecher.htm` (Formmatten) / `formst_bipos_faecher.htm` (Formstahl)
- ☐ **P2 ⏱ S** — „Harfe": analog
- ☐ **P2 ⏱ S** — „Positionierung löschen": analog
- ☐ **P2 ⏱ S** — „Rundstahl und Matten frei positionieren": analog
- ☐ **P2 ⏱ S** — „Positionierung verschieben": analog
- ☐ **P2 ⏱ S** — „Einzelne Position ändern": `formst_aendpos_einpos.htm` / `matten_aendern_einpos.htm`
- ☐ **P2 ⏱ S** — „Zusatztext für die Biegeliste hinzufügen": `formst_biform_bilitx.htm` / `zusatztext_fuer_biegeliste_ein.htm` → ggf. Konsolidieren
- ☐ **P2 ⏱ S** — „Geometrie dehnen": `formst_biform_dehgeo.htm` / `geometrie_dehnen.htm` → ggf. Konsolidieren
- ☐ **P2 ⏱ S** — „Auszugsform kopieren": `formst_biform_forkop.htm` / `vorhandene_form_kopieren.htm` → ggf. Konsolidieren
- ☐ **P2 ⏱ S** — „Informationen zu Auszügen anzeigen": `formst_biform_info.htm` / `informationen_ueber_rundstahla.htm` → ggf. Konsolidieren
- ☐ **P2 ⏱ S** — „Lücke in einer Verlegung erzeugen": `formst_vedusn_luecke.htm` / `formst_vestaf_luecke.htm` → Suffix
- ☐ **P2 ⏱ S** — „Stahlquerschnitt angeben/ermitteln": `formst_veform_ab_n.htm` / `formst_vestaf_ab_n.htm` → Suffix
- ☐ **P2 ⏱ S** — „Form auswählen und Verlegerichtung definieren": `formst_veform_waehfor.htm` / `formst_vestaf_waehfor.htm` → Suffix
- ☐ **P2 ⏱ S** — „Hilfspunkt löschen": `hilfspunkte_loeschen_r.htm` / `hilfspunkte_loeschen_u.htm` → erläutern (rechte/untere Menüleiste?)
- ☐ **P2 ⏱ S** — „Textpunkte setzen": `hilfspunkte_textpunkte.htm` / `hilfspunkte_textpunkte_unteres_menue.htm` → Suffix
- ☐ **P2 ⏱ S** — „Linie parallel verschieben": `konst1_linie_parallel_verschieben.htm` / `linien_linien_parallel_verschieben.htm` → konsolidieren oder disambiguieren
- ☐ **P2 ⏱ S** — „Bewehrung dehnen": `konst3_bewdeh.htm` / `rm_bewehrung-dehnen.htm`
- ☐ **P2 ⏱ S** — „Mattenverlegung ändern": `matten_verlegebereich_aendern.htm` / `mattenverlegung_aendern.htm`
- ☐ **P2 ⏱ S** — „Einstellungen für die Verlegung": `rd_bamtec_einstellungen.htm` (BAMTEC) / `rm_einstellungen-fuer-die-verlegung.htm`
- ☐ **P2 ⏱ S** — „Positionierung ändern": `tsk_aendern_bipos_formma.htm` (Formmatten) / `tsk_aendern_bipos_formst.htm` (Formstahl)
- ☐ **P2 ⏱ S** — „Örtlich zu biegende Bewehrung erzeugen/ändern": `tsk_formma_oertbie.htm` / `tsk_formst_oertbie.htm` → Suffix
- ☐ **P2 ⏱ S** — „Örtlich zu biegende Bewehrung entfernen": `tsk_formma_oertbie_loesche.htm` / `tsk_formst_oertbie_loesche.htm` → Suffix

### 2.2 Snippet-Titel auf lesbare Form bringen

16 Snippet-Dateien (`.xhtm`) tragen technische `TSK_…`/`RD_…`-Titel statt eines menschenlesbaren Titels. Wenn diese Snippets als Popup angezeigt werden, ist das harmlos — aber sobald sie in der Volltextsuche oder im Index erscheinen, wirken sie unprofessionell.

- ☐ **P2 ⏱ M** — Snippet-Titel anpassen (oder Snippets in andere Topics einbinden, sodass eigener Titel irrelevant wird):

  - `_rd_abmessungen-fuer-listenmatt.xhtm` (aktuell „RD_Abmessungen-für-Listenmatten") → „Abmessungen für Listenmatten"
  - `_tsk_alle-positionen-neu.xhtm` → „Alle Positionen neu durchzählen"
  - `_tsk_anfangswinkel-definieren.xhtm` → „Anfangswinkel definieren"
  - `_tsk_auszugsform-ausrichten.xhtm` → „Auszugsform ausrichten"
  - `_tsk_biegeform-definieren.xhtm` → „Biegeform definieren"
  - `_tsk_echtdarstellung-absetzen.xhtm` → „Echtdarstellung absetzen"
  - `_tsk_einzelne-pos-aendern.xhtm` → „Einzelne Position ändern"
  - `_tsk_endwinkel-definieren.xhtm` → „Endwinkel definieren"
  - `_tsk_luecke-schaffen.xhtm` → „Lücke schaffen"
  - `_tsk_mattentyp-und-abstand-form.xhtm` → „Mattentyp und Abstand (Formmatten)"
  - `_tsk_positionen-in-reihenfolge.xhtm` → „Positionen in Reihenfolge bringen"
  - `_tsk_staffel-ausrichten-und-ver.xhtm` → „Staffel ausrichten und Verlegefaktor angeben"
  - `_tsk_stahlquerschnitt-ermitteln.xhtm` → „Stahlquerschnitt ermitteln"
  - `_tsk_verknuepfung.xhtm` → „Verknüpfung erstellen und bearbeiten"
  - `_tsk_zusatztext-hinzuf-formmatt.xhtm` → „Zusatztext hinzufügen (Formmatten)"
  - `_tsk_zusatztext-hinzufuegen.xhtm` → „Zusatztext hinzufügen"

### 2.3 Marken-Konsistenz „ISBCAD"

26 Stellen in 16 Dateien schreiben die Marke klein („isbcad") oder mit Leerzeichen („isb cad") statt der Hausschreibweise **ISBCAD**.

- ☐ **P2 ⏱ M** — Korrekturen pro Datei (jeweils im Body-Text prüfen, nicht in URLs/Pfaden):

  **Klein-Schreibweise „isbcad"**:
  - `con_isbcad_feedback.htm`
  - `des_isb_logfiles.htm`
  - `des_manuelle-aktualisierung.htm`
  - `top_planverwaltung.htm`
  - `tsk_log_per_email.htm`
  - `tsk_rds_aktualisieren.htm`

  **Schreibweise mit Leerzeichen „isb cad"** (zwei der Treffer sind in archivierten Versionshinweisen — dort historisch korrekt):
  - `_des_neu-in-isbcad-2014.xhtm` *(historisch — belassen)*
  - `_des_neu-in-isbcad-2015.xhtm` *(historisch — belassen)*
  - `_des_neu-in-version-2011.xhtm` *(historisch — belassen)*
  - `_des_neu-in-version-2016.xhtm` *(historisch — belassen)*
  - `dat_dwg_dxf_dateien_importieren.htm` *(korrigieren)*
  - `des_plankoepfe-nach-ec2.htm` *(korrigieren)*
  - `matten_vorratsmatten.htm` *(korrigieren)*
  - `rm_betonstahltabelle.htm` *(korrigieren)*
  - `top_historie.htm` *(prüfen — kann Historien-Bezug sein)*
  - `tsk_schraffur-importieren.htm` *(korrigieren)*

  **Globaler Such- und Ersetz-Lauf** im Quellprojekt:
  - Suche (regex, Body): `\bisb cad\b` → `ISBCAD`
  - Suche (regex, Body): `\bisbcad\b` → `ISBCAD`
  - **Achtung**: Treffer in URLs (`isbcad.de`), Dateipfaden (`/isbcad/…`) und Datei-Endungs-Listen NICHT ersetzen — vorher mit Vorschau-/Differenz-Modus arbeiten.

### 2.4 Orphan-Dateien aufräumen

79 Dateien liegen im Output-Verzeichnis, sind aber nicht in TOC/Index und werden nicht verlinkt. Die meisten sind H&M-Snippets (Topic-Includes), die der Generator zusätzlich als eigenständige Datei mit ausschreibt.

- ☐ **P2 ⏱ M** — H&M-Project-Setting prüfen: Können Snippet-Topics vom Build-Output ausgeschlossen werden? (in H&M: „Build" → Topic-Eigenschaften → „Aus Output ausschließen").

- ☐ **P3 ⏱ S** — Archivierte Versionshinweise prüfen — sollen sie aus der 2026er-Auslieferung entfernt werden?
  - `_des_neu-in-isbcad-2012.xhtm`
  - `_des_neu-in-isbcad-2014.xhtm`
  - `_des_neu-in-isbcad-2015.xhtm`
  - `_des_neu-in-version-2011.xhtm`
  - `_des_neu-in-version-2016.xhtm`
  - **Empfehlung**: in eine separate „Historie"-Sektion einsortieren statt aus Output zu entfernen — historische Versionshinweise haben Wert für Anwender, die von älteren Versionen aufrüsten.

- ☐ **P3 ⏱ S** — Verbleibende „Andere"-Orphans prüfen:
  - `des_matten-verlegearten.htm`
  - `formst_vedusn_ab_n.htm`
  - `rd_querschnitt.htm`
  - Sind diese erreichbar gemeint oder Altlasten?

---

## P3 — Qualitätsverbesserungen

### 3.1 Begriffs-Konsistenz

- ☐ **P3 ⏱ M** — **Redaktionelle Leitlinie festlegen und im Wiki/Confluence ablegen**: „wählen" vs. „auswählen" — beides kommt zusammen ~900× vor. Beispiel-Regel: *„Sie wählen X im Dialog aus"* (mit „aus"-Trennung als Standard).

- ☐ **P3 ⏱ M** — **Personen-Bezeichnung vereinheitlichen**: aktuell mischt die Hilfe „Anwender" (13×), „Anwendende" (1×), „Benutzer" (5×). Empfehlung: konsistent „Anwender" oder konsistent „Anwendende" — abhängig von Glasers Gender-Leitlinie.

- ☐ **P3 ⏱ L** — **Glossar-Topic** als neue Seite anlegen mit Begriffsdefinitionen:
  - *as-Werte, as-Linien, as-Texte* (FEM-Bewehrungswerte)
  - *LKT* (Schutzmechanismus)
  - *VKN* (Verknüpfung)
  - *Voute*
  - *Verlegefaktor, Bauteilfaktor*
  - *BAMTEC* (Bewehrungsteppich)
  - *Expositionsklasse*
  - *Auszug, Auszugsform*
  - *Staffel, Bogenstaffel, Fächer, Harfe*
  - *Position, Positionierung, Positionsnummer*
  - *Hüllfläche*
  - *Folienautomatik*
  - *DSTV, BVBS, IFC, GOST*
  - Glossar im TOC unter „Hilfe" oder als Anhang einordnen.

### 3.2 Klammer-Whitespace-Audit

662 Treffer für Klammer-Leerzeichen-Auffälligkeiten (`( ` oder ` )`). Manche sind bewusst (z. B. `[ Esc ]` als Tastenfolge), andere echte Tippfehler.

- ☐ **P3 ⏱ L** — **Regex-gestützte Stichprobe** in 30 zufälligen Topics: prüfen, welche Fälle Konvention sind und welche echte Fehler. Anschließend ggf. zentral korrigieren.
  - Regex zum Aufspüren: `[^\[\s]\(\s|\s\)[^\]\s]`
  - Erwartet wird: Korrekturen sind selten, aber die Konsistenz steigt sichtbar.

### 3.3 Externe Links bereinigen

63 externe Links auf 46 verschiedene Ziele. Pflege-Risiko.

- ☐ **P3 ⏱ M** — `http://` → `https://` umstellen, wo das Ziel-Schema funktioniert:
  - `http://www.schoeck.de` → `https://www.schoeck.de`
  - `http://www.halfen.de` → `https://www.halfen.de`
  - `http://www.bvbs.de` → `https://www.bvbs.de`
  - `http://tripla.de/` → `https://tripla.de/`
  - **Vorher prüfen**: ob die HTTPS-Version aufrufbar ist.

- ☐ **P3 ⏱ S** — URL-Schema vereinheitlichen bei `baustahlgewebe.com` (aktuell in drei Varianten: `/`, `/index.php/de/`, ohne Slash). Auf eine Schreibweise reduzieren.

- ☐ **P3 ⏱ M** — **Wartungsroutine**: monatlicher automatischer Link-Check des CHM-Output mit einem Tool wie `linkchecker` oder `lychee`. Skript-Beispiel im Anhang.

### 3.4 Glossar-Querverweise

- ☐ **P3 ⏱ L** — Nachdem das Glossar steht (3.1): in den 50–80 wichtigsten Topics gezielt Glossar-Verlinkungen auf Erstvorkommen der Begriffe einbauen.

---

## P4 — Modernisierung (in Abstimmung mit Entwicklung)

*Diese Punkte gehen über reine Redaktion hinaus und brauchen Abstimmung mit der Software-Entwicklung und/oder Geschäftsleitung. Sie sind hier aufgeführt, damit Sie sie auf der Agenda haben.*

- ☐ **P4 ⏱ XL** — **Quellprojekt von ISO-8859-1 auf UTF-8 umstellen** (Help & Manual unterstützt das). Eliminiert latente Encoding-Risiken.

- ☐ **P4 ⏱ XL** — **Web-Help als zusätzliches Ausgabeformat** evaluieren — H&M kann Multi-Format-Export. Vorteile: SEO über Google, Mobil-tauglich, kein CHM-Sicherheits-Gefrickel bei Kunden mit modernen Win-Setups.
  - Möglicher Hosting-Pfad: `help.isbcad.de` oder Sub-Verzeichnis auf `glasercad.de`.

- ☐ **P4 ⏱ XL** — **Inline-CSS aus Generator-Template entfernen**, externes Stylesheet (`isbcad_style.css`) als alleinige Quelle. Reduziert Dateigrößen pro Topic erheblich.

- ☐ **P4 ⏱ L** — **Tutorial-Modul** entwickeln: das heute als externe PDF („Erste Schritte") gelieferte Tutorial in HTML-Tour-Format überführen, mit Querverweisen in die Themen.

- ☐ **P4 ⏱ L** — **Fehlermeldungen-Referenz** — eine zentrale Übersicht typischer ISBCAD-Fehlermeldungen mit Lösungswegen anlegen. Reduziert Supportanfragen.

- ☐ **P4 ⏱ M** — **Hotkeys-Cheatsheet** als druckbare PDF im Anhang der Hilfe.

- ☐ **P4 ⏱ L** — **IFC-/BIM-Workflow-Topic** als neuen Top-Level-Abschnitt anlegen, sobald die Software entsprechende Funktionen erhält (siehe Produktanalyse, BIM-Strategie). Aktuell wird das nur durch das IFC Section Tool partiell abgedeckt.

---

## Wiederkehrende Wartungsroutinen

*Diese Routinen sollten in den Release-Prozess eingebaut werden.*

### Pro Release-Zyklus (jährlich)

- ☐ **R1** — Vor jedem Major-Release: **automatisches Tippfehler-Screening** der „Neu in …"-Seite mit Wortlisten (siehe Anhang).
- ☐ **R2** — **TOC-Sprungmarken-Verifikation**: prüfen, dass alle `#xxx`-Anker in TOC-Einträgen in den Zielseiten existieren (Skript im Anhang).
- ☐ **R3** — **Titel-Duplikate-Check**: bei jedem Release einmal über alle `<title>` laufen, neue Duplikate identifizieren.
- ☐ **R4** — **Externer-Link-Audit**: alle 46 externen Ziele auf Erreichbarkeit prüfen.
- ☐ **R5** — **Orphan-Datei-Audit**: Verzeichnis vs. TOC/Index abgleichen.
- ☐ **R6** — **Stub-Audit**: Topics unter 200 Zeichen identifizieren, prüfen, ob inhaltlich abgeschlossen oder noch auszubauen.
- ☐ **R7** — **`_todo_`-Dateien**: müssen bei jedem Release auf 0 sein.

### Monatlich

- ☐ **M1** — Link-Check des Live-CHM mit `linkchecker` oder vergleichbar.
- ☐ **M2** — Sichtung von Support-Tickets nach Hinweisen auf unklare oder fehlende Hilfe-Topics.
- ☐ **M3** — Sichtung von ISBCAD.NOLT-Ideen für Hilfe-relevante Themen (Doku-Lücken werden dort oft als Feature-Requests formuliert).

---

## Pre-Release-Checkliste (für ISBCAD 2027)

Vor Freigabe einer neuen ISBCAD-Version:

- ☐ Alle Tippfehler in der „Neu in …"-Seite gegen Lektorat geprüft (zwei-Augen-Prinzip)
- ☐ Alle neuen Topics haben einen lesbaren `<title>` (keine `TSK_…`-Notation)
- ☐ Alle neuen TOC-Einträge zeigen auf existierende Seiten und Anker
- ☐ Alle neuen Bilder eingebunden und im Output enthalten
- ☐ Versionsinfo in `des_revision.htm` aktualisiert
- ☐ Externe Links zu Glaser-Domains zeigen auf 2027-er Produktseiten
- ☐ Skripte aus dem Anhang gegen das frisch gebaute CHM laufen lassen
- ☐ Stichprobe: 25 zufällige Topics manuell sichten (auf Layout-Brüche prüfen)

---

## Anhang A — Hilfsskripte

### A.1 TOC-Anker-Validator (Python)

Prüft, dass alle `#nodeN`-Anker im Inhaltsverzeichnis in den Zielseiten existieren.

```python
import re, os

with open('OnlineHilfe_DE.hhc', 'rb') as f:
    hhc = f.read().decode('cp1252', errors='replace')

# Anker-Verweise extrahieren
refs = re.findall(r'param name="Local" value="([^"]+\.htm)#([^"]+)"', hhc)
missing = []
for fname, anchor in refs:
    if not os.path.exists(fname):
        missing.append((fname, anchor, 'Datei fehlt'))
        continue
    with open(fname, 'rb') as f:
        text = f.read().decode('cp1252', errors='replace')
    if (f'name="{anchor}"' not in text 
        and f'id="{anchor}"' not in text):
        missing.append((fname, anchor, 'Anker fehlt'))

if missing:
    print(f"Defekte TOC-Anker: {len(missing)}")
    for f, a, r in missing:
        print(f"  {f}#{a}: {r}")
else:
    print("Alle TOC-Anker OK ✓")
```

### A.2 Titel-Duplikat-Check (Python)

```python
import re, glob
from collections import defaultdict

titles = defaultdict(list)
for fp in glob.glob('*.htm') + glob.glob('*.xhtm'):
    with open(fp, 'rb') as f:
        text = f.read().decode('cp1252', errors='replace')
    m = re.search(r'<title>([^<]*)</title>', text)
    if m:
        titles[m.group(1).strip()].append(fp)

for t, files in sorted(titles.items(), key=lambda x: -len(x[1])):
    if len(files) > 1:
        print(f"{len(files)}x  '{t}'")
        for f in files:
            print(f"    {f}")
```

### A.3 Tippfehler-Wortliste

Diese Wortliste als Such-Regex gegen den Korpus laufen lassen. Bei einem Treffer manuell prüfen — viele Wörter können auch korrekt sein.

```
\beinzeilgen?\b           # einzeilgen → einzeiligen
\bverlegungung\w*\b       # verlegungung → verlegung
\bSparrenverbeschriftung\b  # → Sparrenbeschriftung
\bzeichung\b              # → zeichnung (kommt in _todo_-Dateinamen vor)
\bdaß\b|\bmuß\b|\bläßt\b   # altdt. ß
\bStandart\b              # → Standard
\bseperat\b               # → separat
\bAuzug\b|\bAusuzug\b      # → Auszug
\bzusätlich\w*\b           # → zusätzlich
\b\w+ungung\b              # doppelte -ung-Endung
```

### A.4 Stub-Detektor (Python)

```python
import re, glob

def body_text_len(text):
    m = re.search(r'<body[^>]*>(.*?)</body>', text, re.DOTALL|re.IGNORECASE)
    if not m: return 0
    body = m.group(1)
    body = re.sub(r'<style.*?</style>', '', body, flags=re.DOTALL|re.IGNORECASE)
    body = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL|re.IGNORECASE)
    plain = re.sub(r'<[^>]+>', ' ', body)
    plain = re.sub(r'&[a-zA-Z#0-9]+;', ' ', plain)
    plain = re.sub(r'^Navigation:.*?»', '', plain, count=1)
    plain = re.sub(r'\s+', ' ', plain).strip()
    return len(plain), plain[:100]

for fp in sorted(glob.glob('*.htm') + glob.glob('*.xhtm')):
    with open(fp, 'rb') as f:
        text = f.read().decode('cp1252', errors='replace')
    n, preview = body_text_len(text)
    if n < 200:
        print(f"{n:4d}  {fp}  -- {preview}")
```

---

## Anhang B — Aufwandsschätzung gesamt

| Block | Aufgaben | Aufwand gesamt |
|---|---:|---|
| P1 — Sofort sichtbare Fehler | 25 | **ca. 1,5 Personentage** |
| P2 — Strukturelle Konsistenz | ~70 | **ca. 3 Personentage** |
| P3 — Qualitätsverbesserungen | 7 + Stichproben | **ca. 3–5 Personentage** |
| P4 — Modernisierung | 7 | **40+ Personentage** (mit Entwicklung) |
| **Summe ohne P4** | | **ca. 7–10 Personentage** |

**Empfehlung**: P1 und 2.1 (Titel-Disambiguierung) zuerst — innerhalb einer Woche umsetzbar und sichtbar wirksam. P2.2–2.4 und P3 als „Background-Tasks" über die nächsten 1–2 Monate.

---

## Anhang C — Ansprechpartner für offene Fragen

Bei Unsicherheit zu einzelnen Punkten:

- **Inhaltliche Korrekturen Bewehrung/Konstruktion** → Kundenbeirat einbinden
- **Technische Build-/Output-Fragen** → Entwicklungsteam (H&M-Projektkonfiguration)
- **Marken-Schreibweisen** → Marketing/Astrid Kiesel
- **CHM ↔ Web-Help-Strategie (P4)** → Geschäftsleitung

---

*Dieses Dokument ist als Living Document gedacht. Bitte den Status der Aufgaben aktuell halten und das Dokument nach jedem Release fortschreiben.*
