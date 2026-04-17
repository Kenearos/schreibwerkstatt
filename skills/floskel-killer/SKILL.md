---
skillId: bmad-sw-floskel-killer
skillName: Floskel-Killer
skillType: workflow
description: |
  Adversarial Prose Review: Systematischer Scan gegen Klischees,
  Fuellmuster, vage Emotionen, Moment-Inflation und strukturelle
  Ticks. Arbeitet gegen eine quantitative Blacklist mit Schwellenwerten.
  Trigger: Floskel-Check, Floskel-Killer, Klischees pruefen,
  Floskeln finden, Anti-Floskel, Cliche-Check
---

# Floskel-Killer — Adversarial Prose Review

## Ueberblick

Der Floskel-Killer ist ein gnadenloser Review-Workflow der jedes Kapitel
systematisch auf wiederkehrende Schwaechemuster prueft. Er arbeitet
regelbasiert mit quantitativen Schwellen — keine Diskussion, nur Zahlen.

Ergaenzt den Lektor (subjektive Qualitaet) und die KI-Muster-Erkennung
(AI-Slop). Der Floskel-Killer konzentriert sich auf **repetitive Muster
die dem Autor selbst nicht auffallen**.

## Inputs

- **Kapiteltext** (Pflicht) — Das zu pruefende Kapitel
- **Vorheriges Kapitel** (Optional) — Fuer kapiteluebergreifende Wiederholungs-Erkennung
- **Stil-Bibel** (Pflicht) — `bibel/stil.md` fuer projektspezifische Regeln

## Pruefkategorien

### 1. Moment-Inflation

Alle Varianten von zeitlichen Fuellwoertern die Spannung verduennen.

| Verboten | Stattdessen |
|----------|-------------|
| "Fuer einen Moment" | Direkt zeigen was passiert |
| "In diesem Moment" | Streichen — die Szene steht fuer sich |
| "Eine Sekunde verging, zwei" | Koerperreaktion statt Countdown |
| "Die Zeit schien stillzustehen" | Ein Detail extrem scharf beschreiben |
| "Fuer einen Bruchteil einer Sekunde" | Einzige scharfe Wahrnehmung |

**Schwelle:** Max 1x "Moment" pro Kapitel.

### 2. Vage Emotionsumschreibungen

Die Kapitulation des Autors — wenn du es nicht zeigen kannst, zeig es durch den Koerper.

| Verboten | Stattdessen |
|----------|-------------|
| "Etwas, das er/sie nicht benennen konnte/wollte" | Koerperreaktion: Hals eng, Haende feucht |
| "Ein Gefuehl, das keine Berechtigung hatte" | Handlung zeigt Unangemessenheit |
| "Etwas dazwischen" | Konkreter Widerspruch: "Ihr Mund laechelte. Ihre Faeuste nicht." |
| "Er/sie wusste nicht, was er/sie fuehlte" | Widerspruechliche Koerperreaktionen |
| "Etwas Warmes und Gefaehrliches" | Konkret: WAS ist warm? WO ist die Gefahr? |

**Schwelle:** ZERO Toleranz.

### 3. Konjunktiv-Vergleichs-Ueberlast

"Als wuerde/haette/koennte" sind Weichzeichner.

| Verboten (bei Haeufung) | Stattdessen |
|--------------------------|-------------|
| "Als wuerde jede Bewegung Schmerz verursachen" | "Jede Bewegung kostete sie." — Indikativ. |
| "Als haette jemand..." | Direkt beschreiben was sichtbar ist |
| "Als koennte er/sie durch X blicken" | Konkretes Verhalten zeigen |
| "Als waere er/sie aus Stein/Granit/Eis" | Spezifisches Detail statt generischer Haerte |

**Schwelle:** Max 3 pro Szene. In Action-/Spannungsszenen: null.

### 4. Atmosphaere-Formeln

Wiederholte Atmosphaere-Bilder brechen die Immersion.

| Verboten | Stattdessen |
|----------|-------------|
| "Die Worte hingen in der Luft" | Reaktion auf die Worte zeigen |
| "Die Nacht senkte sich wie ein Vorhang" | Konkretes Licht-Detail |
| "Die Finsternis wuchs/kroch/frass" | Konkreter Gegenstand verschwindet im Dunkeln |
| "Schwer wie Gewitterwolken" | Spezifisches Bild fuer die Szene |
| "X legte sich wie eine Decke ueber Y" | Taktiles Bild passend zur Szene |

**Schwelle:** Kein Bild darf sich im Roman wiederholen.

### 5. Strukturelle Ticks

Syntaktische Muster die dem Autor unsichtbar, der Leserin aber sichtbar sind.

| Verboten | Stattdessen |
|----------|-------------|
| "Er/sie bemerkte nicht, dass..." (Haeufung) | Max 1x pro Kapitel. Handlung direkt zeigen. |
| "Bevor er/sie antworten konnte, war X weg" | Antwort zulassen ODER Flucht als bewusste Entscheidung |
| "Nicht X. Nicht Y. Sondern Z." | Versteckte Dreier-Aufzaehlung — nur die Aussage selbst |
| "Seine/ihre Stimme war..." (als Szenen-Einstieg) | Dialog direkt, Wirkung durch Reaktion |

**Schwelle:** Jedes Pattern max 1x pro Szene.

### 6. Leitmotiv-Abnutzung

Leitmotive funktionieren durch sparsamen Einsatz.

Empfohlene Schwellen (anpassbar in `bibel/stil.md`):

| Leitmotiv-Typ | Max. Frequenz |
|----------------|---------------|
| Charakter-Metaphern (z.B. "Mauern", "Maske") | 1x pro Kapitel |
| Sinnes-Leitmotive (z.B. Gerueche) | 1x pro Szene mit der Person |
| Koerper-Details (z.B. Augenfarbe) | 1x pro POV-Abschnitt |
| Mantra/Catchphrase | 2x pro Kapitel |

## Meta-Regeln

1. **Einmal-und-nie-wieder**: Keine Formulierung darf woertlich identisch ein zweites Mal im Roman erscheinen
2. **Koerper-vor-Kopf**: Emotion zuerst physisch zeigen, dann optional reflektieren
3. **Spezifik schlaegt Abstraktion**: Konkretes Detail > vage Beschreibung
4. **Stille-Verbot**: Keine unbeschriebene Stille — wenn Stille wirken soll, ein Geraeusch dagegenstellen
5. **3-Satz-Fenster**: Innerhalb von 3 aufeinanderfolgenden Saetzen darf kein Pattern doppelt vorkommen

## Pruefprozess

### Schritt 1: Kontext laden
1. Lies `bibel/stil.md` — Projektspezifische Ergaenzungen und Sperrlisten
2. Lies den Kapiteltext
3. Optional: Lies das vorherige Kapitel fuer kapiteluebergreifende Pruefung

### Schritt 2: 6-Kategorien-Scan
Durchlaufe den gesamten Text und markiere jeden Fund mit:
- Absatz-/Zeilennummer
- Kategorie (1-6)
- Exaktes Zitat
- Schweregrad

### Schritt 3: Kapiteluebergreifender Check (falls vorheriges Kapitel vorhanden)
- Woertlich identische Formulierungen
- Identische Metaphern/Vergleiche
- Identische Satzstrukturen in analogen Szenen

### Schritt 4: Meta-Regeln pruefen
- Koerper-vor-Kopf-Verstoesse
- Abstrakte Beschreibungen ohne konkretes Detail
- Stille ohne Gegengeraeusch
- 3-Satz-Fenster-Verstoesse

### Schritt 5: Report

```
=== FLOSKEL-REPORT: Kapitel [NN] ===

KRITISCH (muss gefixt werden)
| # | Stelle | Kategorie | Zitat | Problem | Fix-Vorschlag |
|---|--------|-----------|-------|---------|---------------|

WARNUNG (sollte gefixt werden)
| # | Stelle | Kategorie | Zitat | Problem | Fix-Vorschlag |
|---|--------|-----------|-------|---------|---------------|

HINWEIS (koennte besser sein)
| # | Stelle | Kategorie | Zitat | Problem | Fix-Vorschlag |
|---|--------|-----------|-------|---------|---------------|

STATISTIK
- Moment-Woerter: X (erlaubt: 1)
- Vage Emotionen: X (erlaubt: 0)
- Konjunktiv-Vergleiche: X/Szene (erlaubt: 3)
- Atmosphaere-Formeln: X wiederholte
- Strukturelle Ticks: X
- Leitmotiv-Ueberschreitungen: X

VERDICT: [BESTANDEN / NACHARBEIT NOETIG / GRUNDUEBERARBEITUNG]
```

## Schweregrad-Klassifikation

- **KRITISCH**: Woertliche Wiederholung aus vorherigem Kapitel, Tell-statt-Show, >5 Funde einer Kategorie
- **WARNUNG**: Pattern ueberschreitet Schwelle, vage Emotion ohne Koerperreaktion
- **HINWEIS**: Einzelne Konjunktiv-Haeufung, Leitmotiv an der Grenze
