#!/usr/bin/env python3
"""
Schreibwerkstatt — Markdown Export
Kombiniert alle Kapitel in eine einzelne Markdown-Datei.
"""

import re
import sys
from pathlib import Path

def find_project_root():
    current = Path.cwd()
    while current != current.parent:
        if (current / "CLAUDE.md").exists() and (current / "bibel").exists():
            return current
        current = current.parent
    return Path.cwd()

def get_chapters(kapitel_dir):
    chapters = []
    for f in sorted(kapitel_dir.glob("*.md")):
        if f.name.startswith("_"):
            continue
        content = f.read_text(encoding="utf-8")
        chapters.append({"content": content, "file": f.name})
    return chapters

def get_metadata(root):
    synopsis = root / "geschichte" / "synopsis.md"
    metadata = {"title": "Unbenannter Roman", "author": "Unbekannt"}
    if synopsis.exists():
        content = synopsis.read_text(encoding="utf-8")
        title_match = re.search(r"## Arbeitstitel\s*\n+(.+)", content)
        if title_match:
            title = title_match.group(1).strip().strip("<!--").strip("-->").strip()
            if title:
                metadata["title"] = title
    return metadata

def export_markdown(root, output_path):
    kapitel_dir = root / "_bmad-output" / "kapitel"
    if not kapitel_dir.exists() or not list(kapitel_dir.glob("*.md")):
        print("Keine Kapitel gefunden in _bmad-output/kapitel/")
        sys.exit(1)

    chapters = get_chapters(kapitel_dir)
    metadata = get_metadata(root)

    lines = []
    lines.append(f"# {metadata['title']}")
    lines.append("")
    lines.append(f"*{metadata['author']}*")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Inhaltsverzeichnis
    lines.append("## Inhaltsverzeichnis")
    lines.append("")
    for i, ch in enumerate(chapters, 1):
        first_line = ch["content"].strip().split("\n")[0]
        title = first_line.lstrip("# ").strip()
        lines.append(f"{i}. {title}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Kapitel
    for ch in chapters:
        lines.append(ch["content"])
        lines.append("")
        lines.append("---")
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Markdown erstellt: {output_path}")
    print(f"   {len(chapters)} Kapitel, {metadata['title']}")

if __name__ == "__main__":
    root = find_project_root()
    metadata = get_metadata(root)
    filename = metadata["title"].lower().replace(" ", "-") + ".md"
    output = root / "_bmad-output" / "export" / filename
    output.parent.mkdir(parents=True, exist_ok=True)
    export_markdown(root, output)
