# 📖 Schreibwerkstatt

**BMAD-Modul für KI-gestützte Roman-Entwicklung**

> Schreibe Romane mit einem Team spezialisierter KI-Agenten — von der Synopsis bis zum fertigen E-Book.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![BMAD Compatible](https://img.shields.io/badge/BMAD-v6-blue.svg)](https://github.com/bmad-code-org/BMAD-METHOD)

---

## Was ist das?

Schreibwerkstatt ist ein [BMAD](https://github.com/bmad-code-org/BMAD-METHOD)-kompatibles Modul das den Prozess des Romanschreibens in spezialisierte Rollen aufteilt — genau wie BMAD es für Software-Entwicklung tut.

Statt dass eine KI alles alleine macht, arbeiten **7 spezialisierte Agenten** zusammen:

| Agent | Rolle | Was er tut |
|-------|-------|-----------|
| 🎭 **Dramaturg** (Dr. Dramatis) | Plot-Architekt | Synopsis, Kapitelplan, Spannungsbögen |
| ✍️ **Autor** (Quill) | Prosa-Schreiber | Kapitel nach Bibel und Plan schreiben |
| 🔴 **Lektor** (Rotfeder) | Qualitätsprüfer | Sprache, Stil, Konsistenz |
| 🧠 **Figurenprüfer** (Persona) | Charakter-Psychologin | Figurenkonsistenz, Motivation, Arcs |
| ⏱️ **Kontinuitätsprüfer** (Chronos) | Archivar | Plotholes, Zeitlinien, Logik |
| 🔮 **Motivjäger** (Symbolon) | Literaturwissenschaftler | Motive, Symbole, Themen |
| 🎯 **Floskel-Killer** | Adversarial Review | Klischees, Fuellmuster, repetitive Patterns |
| 🤖 **KI-Muster-Erkennung** | Perplexity Gate | Erkennt AI-Slop |

## Features

- **Bibel-System**: Single Source of Truth für Figuren, Orte, Stil und Motive
- **State-Management**: Versionierter Zustand pro Kapitel (wer weiß was, wer fühlt was)
- **Review-Pipeline**: Jedes Kapitel durchläuft eine Qualitätsprüfung mit Human-in-the-Loop
- **KI-Muster-Erkennung**: Erkennt typische KI-Formulierungen und schlägt Alternativen vor
- **Export**: EPUB, DOCX und Markdown
- **Deutsch-first**: Komplett auf Deutsch, mit englischer Unterstützung

## Schnellstart

### Standalone (ohne BMAD)

```bash
git clone https://github.com/Kenearos/schreibwerkstatt.git
cd schreibwerkstatt
bash scripts/setup.sh
claude
```

Dann sage: **"Hilfe"**

### Als BMAD-Modul

```bash
# In einem bestehenden BMAD-Projekt:
npx bmad-method install
# → Wähle "Schreibwerkstatt" aus der Modulliste
```

> **Hinweis:** Die Integration in den offiziellen BMAD-Installer ist geplant. Aktuell funktioniert die Standalone-Installation.

## Projektstruktur

```
schreibwerkstatt/
├── CLAUDE.md                    # Orchestrator (Herzstück)
├── module.yaml                  # BMAD-Modul-Definition
├── bibel/                       # 📚 Single Source of Truth
│   ├── stil.md                  #    Tonalität, Regeln, verbotene Wörter
│   ├── motive.md                #    Motivregister und Symbolik
│   ├── figuren/                 #    Eine Datei pro Figur
│   │   └── _vorlage.md          #    Template
│   └── orte/                    #    Eine Datei pro Ort
│       └── _vorlage.md          #    Template
├── geschichte/                  # 📋 Planung
│   ├── synopsis.md              #    Handlungsübersicht
│   └── plan.md                  #    Kapitelplan mit Beats
├── zustand/                     # 🔄 State-Management
│   ├── aktuell.md               #    Globaler Projektzustand
│   └── kapitel/                 #    Pro-Kapitel-Zustand
├── skills/                      # 🤖 BMAD-Skills
│   ├── sw-setup/                #    Setup-Workflow
│   ├── dramaturg/               #    Plot & Struktur
│   ├── autor/                   #    Prosa schreiben
│   ├── lektor/                  #    Lektorat
│   ├── figurenprufer/           #    Figurenkonsistenz
│   ├── kontinuitaetsprufer/     #    Plotholes & Logik
│   ├── motivjaeger/             #    Motive & Symbole
│   ├── stilprufer/              #    Stilanalyse
│   ├── floskel-killer/           #    Anti-Klischee & Pattern-Scan
│   ├── ki-muster-erkennung/     #    Anti-AI-Slop
│   └── kapitel-export/          #    EPUB/DOCX/MD Export
├── agents/                      # 🎭 Agent-Definitionen (YAML)
├── scripts/                     # ⚙️ Setup & Export-Scripts
└── _bmad-output/                # 📁 Generierte Dateien
    ├── kapitel/                 #    Geschriebene Kapitel
    └── export/                  #    EPUB, DOCX, MD
```

## Workflow

```
1. Bibel füllen     → Figuren, Orte, Stil, Motive definieren
2. Synopsis         → Mit dem Dramaturg die Handlung entwickeln
3. Kapitelplan      → Beats und Spannungsbögen planen
4. Schreiben        → Kapitel für Kapitel mit dem Autor
5. Review           → Lektor, Figurenprüfer, Kontinuität, Motive
6. Floskel-Check    → Klischees, Moment-Inflation, vage Emotionen finden
7. KI-Check         → AI-Slop erkennen und umschreiben
8. Export           → EPUB, DOCX oder Markdown
```

Jeder Schritt ist ein **Gate** — du entscheidest ob es weitergeht.

## Voraussetzungen

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (empfohlen)
- Python 3.8+ (für Export-Funktionen)
- Optional: `python-docx`, `ebooklib` (für DOCX/EPUB-Export)

## Inspiration

Schreibwerkstatt kombiniert Ideen aus:

- **[BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD)** — Multi-Agent-Architektur und Modul-System
- **[Claude Book](https://github.com/topics/claude-book)** — Bibel-System, Perplexity Gate, State-Management
- **Klassische Lektoratsprozesse** — Review-Pipeline mit spezialisierten Rollen

## Contributing

Pull Requests willkommen! Besonders gesucht:

- Neue Agenten (z.B. Worldbuilder, Dialog-Coach)
- Verbesserungen an der KI-Muster-Erkennung
- Übersetzungen (aktuell: Deutsch, geplant: English)
- Bessere Export-Templates

## Lizenz

[MIT](LICENSE) — Mach damit was du willst.

---

*Gebaut mit 🖊️ und KI von [Kenearos](https://github.com/Kenearos)*
