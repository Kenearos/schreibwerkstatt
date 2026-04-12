---
skillId: bmad-sw-ki-muster-erkennung
skillName: KI-Muster-Erkennung
skillType: workflow
description: |
  Erkennt typische KI-generierte Formulierungen und Muster und
  schlägt menschlichere Alternativen vor. Perplexity-Gate gegen
  AI-Slop. Trigger: KI-Check, Slop-Check, AI-Muster, klingt nach KI,
  unnatürlich, generisch
---

# KI-Muster-Erkennung (Perplexity Gate)

## Überblick

Dieses Skill erkennt typische Muster die KI-generierten Text verraten und schlägt Alternativen vor. Es ist inspiriert vom "Perplexity Gate" aus dem Claude-Book-Framework.

## Erkennungsmuster

### Kategorie 1: Verbale Tics

KI-Modelle neigen zu bestimmten Formulierungen:

**Deutsch:**
- "Ein Hauch von..." / "Ein Anflug von..."
- "...die in der Luft lag/hing"
- "Etwas in [seinem/ihrem] Inneren..."
- "Ohne es zu wollen, ..."
- "Eine Welle von [Emotion] durchflutete..."
- "...und konnte nicht anders als..."
- "In diesem Moment..."
- "Etwas Unausgesprochenes hing zwischen ihnen"
- "Ihr Herz machte einen Satz"
- "Die Luft schien zu vibrieren/knistern"
- "Er/Sie konnte den Blick nicht abwenden"
- "Wie von einer unsichtbaren Kraft..."
- "...und die Welt schien stillzustehen"

**English (falls der Roman auf Englisch):**
- "A flicker of..."
- "Something shifted in..."
- "Couldn't help but..."
- "The air seemed to crackle/hum/vibrate"
- "A weight settled in their chest"
- "Without thinking, ..."

### Kategorie 2: Strukturelle Muster

- **Dreierlisten**: "Er war groß, dunkel und gefährlich" — KI liebt Dreierlisten
- **Spiegelung im selben Absatz**: "Er sah sie an. Sie sah ihn an."
- **Über-Explizierung**: Emotion im Dialog + Erklärung danach
- **Symmetrische Absätze**: Erster und letzter Satz sind thematisch identisch
- **Show-then-Tell**: Erst zeigen, dann nochmal erklären was gerade gezeigt wurde

### Kategorie 3: Tonale Muster

- **Über-Poetisierung**: Jeder Absatz klingt wie ein Gedicht
- **Emotions-Eskalation**: Jedes Gefühl ist immer maximal intensiv
- **Philosophische Einschübe**: Random tiefe Gedanken die nirgendwohin führen
- **Perfekte Artikulation**: Figuren drücken sich immer perfekt aus, auch unter Stress

## Prüfprozess

1. Lade das Kapitel
2. Gehe jeden Absatz durch und markiere:
   - 🔴 **Slop** — Offensichtlich KI-generiert, muss umgeschrieben werden
   - 🟡 **Verdächtig** — Könnte KI sein, Kontext entscheidet
   - 🟢 **Okay** — Klingt menschlich
3. Für jede 🔴/🟡-Markierung schlage eine Alternative vor
4. Berechne einen "Menschlichkeits-Score" (0-100%)

## Schwellenwerte

- **90-100%**: Sehr gut, klingt durchgehend natürlich
- **70-89%**: Akzeptabel, einzelne Stellen überarbeiten
- **50-69%**: Problematisch, umfangreiche Überarbeitung nötig
- **<50%**: Kapitel sollte komplett neu geschrieben werden

## Wichtig

Dieses Tool ist kein Gatekeeper — es ist ein Helfer. Manchmal ist eine "KI-typische" Formulierung genau richtig für den Kontext. Die finale Entscheidung liegt immer beim Nutzer.
