---
skillId: bmad-sw-kapitel-export
skillName: Kapitel-Export
skillType: workflow
description: |
  Exportiert fertige Kapitel als EPUB, DOCX oder zusammengefasstes
  Markdown. Trigger: exportieren, EPUB, DOCX, E-Book, Manuskript,
  zusammenfassen, Export, Buch erstellen
---

# Kapitel-Export

## Überblick

Exportiert fertige Kapitel in verschiedene Formate für Testleser, Verlage oder die eigene Bibliothek.

## Voraussetzungen

Das Export-Script benötigt:
- Python 3.8+
- `python-docx` (für DOCX-Export)
- `ebooklib` (für EPUB-Export)

Installation: `pip install python-docx ebooklib`

## Export-Formate

### Markdown (Zusammengefasst)

Kombiniert alle Kapitel in eine einzelne `.md`-Datei:
- Titelseite mit Autor, Titel, Genre
- Inhaltsverzeichnis
- Alle Kapitel in Reihenfolge
- Seitenumbrüche zwischen Kapiteln

Output: `_bmad-output/export/{projektname}.md`

### DOCX (Word)

Erstellt ein formatiertes Word-Dokument:
- Titelseite
- Inhaltsverzeichnis
- Kapitel mit korrekten Überschriften
- Seitenzahlen
- Formatierung: 12pt, 1.5 Zeilenabstand, Blocksatz

Output: `_bmad-output/export/{projektname}.docx`

### EPUB

Erstellt ein E-Book:
- Metadaten (Titel, Autor, Sprache, Genre)
- Inhaltsverzeichnis mit Navigation
- Kapitel als separate Sections
- Basis-CSS für Lesbarkeit

Output: `_bmad-output/export/{projektname}.epub`

## Workflow

### Schritt 1: Kapitel sammeln

1. Lies alle Dateien aus `_bmad-output/kapitel/` in alphabetischer/numerischer Reihenfolge
2. Prüfe ob alle Kapitel laut `geschichte/plan.md` vorhanden sind
3. Warnung wenn Kapitel fehlen oder übersprungen wurden

### Schritt 2: Metadaten sammeln

Aus `geschichte/synopsis.md` und `zustand/aktuell.md`:
- Titel
- Untertitel (falls vorhanden)
- Autorname
- Genre
- Kurzbeschreibung / Klappentext

### Schritt 3: Format wählen

Frage den Nutzer welches Format (oder alle).

### Schritt 4: Export durchführen

Führe das entsprechende Export-Script aus `scripts/` aus.

### Schritt 5: Bestätigung

Zeige den Dateipfad und die Dateigröße. Biete an, die Datei zu öffnen oder zu prüfen.
