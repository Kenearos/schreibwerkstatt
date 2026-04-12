#!/usr/bin/env python3
"""
Schreibwerkstatt — EPUB Export
Kombiniert alle Kapitel zu einem EPUB E-Book.
"""

import os
import re
import sys
from pathlib import Path

def find_project_root():
    """Findet das Projektstammverzeichnis."""
    current = Path.cwd()
    while current != current.parent:
        if (current / "CLAUDE.md").exists() and (current / "bibel").exists():
            return current
        current = current.parent
    return Path.cwd()

def get_chapters(kapitel_dir):
    """Liest alle Kapitel in der richtigen Reihenfolge."""
    chapters = []
    for f in sorted(kapitel_dir.glob("*.md")):
        if f.name.startswith("_"):
            continue
        content = f.read_text(encoding="utf-8")
        # Extrahiere Titel aus erster Zeile
        lines = content.strip().split("\n")
        title = lines[0].lstrip("# ").strip() if lines else f.stem
        body = "\n".join(lines[1:]).strip() if len(lines) > 1 else ""
        chapters.append({"title": title, "body": body, "file": f.name})
    return chapters

def get_metadata(root):
    """Liest Metadaten aus der Synopsis."""
    synopsis = root / "geschichte" / "synopsis.md"
    metadata = {
        "title": "Unbenannter Roman",
        "author": "Unbekannt",
        "language": "de"
    }
    if synopsis.exists():
        content = synopsis.read_text(encoding="utf-8")
        # Versuche Titel zu extrahieren
        title_match = re.search(r"## Arbeitstitel\s*\n+(.+)", content)
        if title_match:
            title = title_match.group(1).strip().strip("<!--").strip("-->").strip()
            if title:
                metadata["title"] = title
    return metadata

def export_epub(root, output_path):
    """Erstellt eine EPUB-Datei."""
    try:
        from ebooklib import epub
    except ImportError:
        print("❌ ebooklib nicht installiert!")
        print("   Installiere mit: pip3 install ebooklib")
        sys.exit(1)

    kapitel_dir = root / "_bmad-output" / "kapitel"
    if not kapitel_dir.exists() or not list(kapitel_dir.glob("*.md")):
        print("❌ Keine Kapitel gefunden in _bmad-output/kapitel/")
        sys.exit(1)

    chapters = get_chapters(kapitel_dir)
    metadata = get_metadata(root)

    book = epub.EpubBook()
    book.set_identifier("schreibwerkstatt-" + metadata["title"].lower().replace(" ", "-"))
    book.set_title(metadata["title"])
    book.set_language(metadata["language"])
    book.add_author(metadata["author"])

    # CSS
    style = epub.EpubItem(
        uid="style",
        file_name="style/default.css",
        media_type="text/css",
        content="""
        body { font-family: Georgia, serif; line-height: 1.6; margin: 1em; }
        h1 { text-align: center; margin-top: 2em; }
        p { text-indent: 1.5em; margin: 0.3em 0; }
        p:first-of-type { text-indent: 0; }
        .scene-break { text-align: center; margin: 1.5em 0; }
        """.encode("utf-8")
    )
    book.add_item(style)

    epub_chapters = []
    for i, ch in enumerate(chapters, 1):
        c = epub.EpubHtml(
            title=ch["title"],
            file_name=f"kapitel_{i:02d}.xhtml",
            lang=metadata["language"]
        )
        # Konvertiere Markdown zu einfachem HTML
        html_body = ch["body"]
        html_body = re.sub(r"\*\*\*|---", '<p class="scene-break">* * *</p>', html_body)
        paragraphs = html_body.split("\n\n")
        html_body = "\n".join(f"<p>{p.strip()}</p>" for p in paragraphs if p.strip())

        c.content = f"<h1>{ch['title']}</h1>\n{html_body}".encode("utf-8")
        c.add_item(style)
        book.add_item(c)
        epub_chapters.append(c)

    # Inhaltsverzeichnis
    book.toc = [(c, c.title) for c in epub_chapters]
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ["nav"] + epub_chapters

    epub.write_epub(str(output_path), book)
    print(f"✅ EPUB erstellt: {output_path}")
    print(f"   {len(chapters)} Kapitel, {metadata['title']}")

if __name__ == "__main__":
    root = find_project_root()
    metadata = get_metadata(root)
    filename = metadata["title"].lower().replace(" ", "-") + ".epub"
    output = root / "_bmad-output" / "export" / filename
    output.parent.mkdir(parents=True, exist_ok=True)
    export_epub(root, output)
