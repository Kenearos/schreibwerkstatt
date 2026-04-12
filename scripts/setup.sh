#!/bin/bash
# Schreibwerkstatt Setup Script
# Erstellt die Projektstruktur und installiert Abhängigkeiten

set -e

echo "╔══════════════════════════════════════╗"
echo "║    📖 Schreibwerkstatt Setup         ║"
echo "║    BMAD Modul für Roman-Entwicklung  ║"
echo "╚══════════════════════════════════════╝"
echo ""

# Prüfe Python
if ! command -v python3 &> /dev/null; then
    echo "⚠️  Python 3 nicht gefunden. Export-Funktionen benötigen Python 3.8+"
    echo "   Installiere Python: sudo apt install python3 python3-pip"
else
    PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
    echo "✅ Python $PYTHON_VERSION gefunden"
fi

# Prüfe Claude Code
if command -v claude &> /dev/null; then
    CLAUDE_VERSION=$(claude --version 2>&1 || echo "unbekannt")
    echo "✅ Claude Code gefunden: $CLAUDE_VERSION"
else
    echo "⚠️  Claude Code nicht gefunden."
    echo "   Installiere: npm install -g @anthropic/claude-code"
fi

# Erstelle Ausgabe-Verzeichnisse
echo ""
echo "📁 Erstelle Verzeichnisse..."
mkdir -p _bmad-output/kapitel
mkdir -p _bmad-output/export
mkdir -p zustand/kapitel
echo "   ✅ _bmad-output/kapitel/"
echo "   ✅ _bmad-output/export/"
echo "   ✅ zustand/kapitel/"

# Installiere Python-Abhängigkeiten (optional)
echo ""
read -p "📦 Python-Pakete für Export installieren? (EPUB/DOCX) [j/N] " install_deps
if [[ "$install_deps" =~ ^[jJyY]$ ]]; then
    echo "   Installiere python-docx und ebooklib..."
    pip3 install python-docx ebooklib --break-system-packages 2>/dev/null || \
    pip3 install python-docx ebooklib 2>/dev/null || \
    echo "   ⚠️  Installation fehlgeschlagen. Versuche: pip3 install python-docx ebooklib"
    echo "   ✅ Python-Pakete installiert"
else
    echo "   ⏭️  Übersprungen (kann später mit pip3 install python-docx ebooklib nachgeholt werden)"
fi

# Git initialisieren falls nötig
echo ""
if [ ! -d ".git" ]; then
    read -p "📋 Git-Repository initialisieren? [J/n] " init_git
    if [[ ! "$init_git" =~ ^[nN]$ ]]; then
        git init
        echo "   ✅ Git-Repository initialisiert"
    fi
else
    echo "✅ Git-Repository existiert bereits"
fi

echo ""
echo "════════════════════════════════════════"
echo "✅ Setup abgeschlossen!"
echo ""
echo "Nächste Schritte:"
echo "  1. Starte Claude Code:  claude"
echo "  2. Sage:                Hilfe"
echo "  3. Fülle die Bibel:     bibel/stil.md, bibel/figuren/, bibel/orte/"
echo "  4. Erstelle Synopsis:   'Synopsis entwickeln'"
echo "════════════════════════════════════════"
