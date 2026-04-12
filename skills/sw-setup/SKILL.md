---
skillId: bmad-sw-setup
skillName: Schreibwerkstatt Setup
skillType: workflow
description: |
  Richtet die Schreibwerkstatt ein und erstellt die Projektstruktur
  mit Bibel-Templates, Zustandsdateien und Konfiguration.
  Trigger: setup, einrichten, schreibwerkstatt starten, projekt anlegen
---

# Schreibwerkstatt Setup

## Überblick

Dieses Setup erstellt die komplette Projektstruktur für dein Romanprojekt. Nach dem Setup hast du:

- Eine **Bibel** mit Templates für Figuren, Orte, Stil und Motive
- Ein **Zustandssystem** das den Fortschritt pro Kapitel trackt
- Eine **Geschichte**-Struktur für Synopsis und Kapitelplan
- Einen **Output**-Ordner für fertige Kapitel und Exporte

## Workflow

### Schritt 1: Projektkonfiguration

Frage den Nutzer nach:
1. **Projektname** — Wie heißt der Roman?
2. **Genre** — z.B. Dark Romance, Fantasy, Thriller, Lit-Fiction
3. **Erzählperspektive** — Ich-Erzähler, Dritte Person Limited, etc.
4. **Zeitform** — Präsens oder Präteritum
5. **Sprache** — Deutsch oder English
6. **Kapitellänge** — kurz/mittel/lang

### Schritt 2: Bibel initialisieren

Erstelle die Bibel-Dateien aus den Templates:

```
bibel/
├── stil.md          ← Tonalität, verbotene Wörter, Stilregeln
├── motive.md        ← Motivregister und Symbolik
├── figuren/
│   └── _vorlage.md  ← Template für neue Figuren
└── orte/
    └── _vorlage.md  ← Template für neue Orte
```

### Schritt 3: Geschichte-Struktur anlegen

```
geschichte/
├── synopsis.md      ← Pitch, Prämisse, Handlungsübersicht
└── plan.md          ← Kapitelübersicht mit Beats
```

### Schritt 4: Zustandssystem initialisieren

```
zustand/
├── aktuell.md       ← Globaler Projektzustand
└── kapitel/         ← Pro-Kapitel-Zustand (wird beim Schreiben gefüllt)
```

### Schritt 5: Bestätigung

Zeige dem Nutzer die erstellte Struktur und erkläre die nächsten Schritte:
1. Bibel füllen (Figuren, Orte, Stil definieren)
2. Synopsis schreiben
3. Kapitelplan erstellen
4. Erstes Kapitel mit dem **Autor**-Agenten schreiben

<HALT>
Warte auf Nutzereingabe bevor du fortfährst.
