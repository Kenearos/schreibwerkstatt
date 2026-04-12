---
skillId: bmad-sw-stilprufer
skillName: Stilprüfer
skillType: workflow
description: |
  Automatisierte Analyse von Stilkonsistenz, Sprachqualität und
  Lesbarkeit. Trigger: Stil prüfen, Sprachanalyse, Lesbarkeit,
  Wortwiederholungen, Satzstruktur, stilistische Analyse
---

# Stilprüfer

## Überblick

Der Stilprüfer ist ein Workflow-Skill der ein Kapitel systematisch auf sprachliche Qualität analysiert. Er ist weniger subjektiv als der Lektor — er arbeitet regelbasiert.

## Prüfregeln

### 1. Wortwiederholungen

- Prüfe jeden Absatz auf Wörter die mehr als 2x vorkommen (ausgenommen Funktionswörter)
- Prüfe aufeinanderfolgende Sätze auf gleiche Satzanfänge
- Prüfe die Seite auf "Lieblingswörter" die zu oft auftauchen

### 2. Satzstruktur

- Berechne die durchschnittliche Satzlänge
- Identifiziere Abschnitte mit zu wenig Variation (alle Sätze gleich lang)
- Finde Schachtelsätze mit mehr als 3 Nebensätzen
- Identifiziere Passivkonstruktionen (wenn in `bibel/stil.md` als unerwünscht markiert)

### 3. Verbotene Wörter und Phrasen

Prüfe gegen die Sperrliste aus `bibel/stil.md`:
- Verbotene Wörter
- Verbotene Phrasen
- KI-typische Formulierungen (Kreuzreferenz mit `ki-muster-erkennung`)

### 4. Dialog-Qualität

- Prüfe ob Dialog-Tags variiert werden (nicht immer "sagte")
- Aber auch: Nicht zu kreativ ("hauchte", "zischte", "donnerte" in jedem Satz)
- Prüfe ob Dialoge natürlich klingen oder nach Exposition riechen

### 5. Sinneseindrücke

- Werden alle fünf Sinne genutzt (nicht nur visuell)?
- Gibt es Absätze die rein abstrakt sind ohne ein konkretes Bild?

## Output

Der Stilprüfer gibt einen Bericht aus mit:

```
=== STILPRÜFUNG: Kapitel XX ===

WORTWIEDERHOLUNGEN:
- "dunkel" 7x in Kapitel (Absätze 2, 5, 8, 12, 15, 22, 28)
- "plötzlich" 4x — auf Sperrliste!

SATZSTRUKTUR:
- Durchschnittliche Satzlänge: 14 Wörter
- Variation: gut / monoton / chaotisch
- Schachtelsätze: 3 gefunden (Absätze 7, 19, 31)

SPERRLISTE:
- "plötzlich" (4x) — VERBOTEN
- "irgendwie" (2x) — VERBOTEN
- "ein Schauer lief über den Rücken" (1x) — KLISCHEE

DIALOG:
- 85% "sagte" als Tag — zu monoton
- 2 Expositions-Dialoge erkannt (Absätze 14, 26)

SINNE:
- Visuell: ████████ 80%
- Auditiv: ███░░░░░ 30%
- Taktil:  ██░░░░░░ 20%
- Olfaktorisch: ░░░░░░░░ 0%
- Gustatorisch: ░░░░░░░░ 0%
```
