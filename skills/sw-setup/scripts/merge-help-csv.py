#!/usr/bin/env python3
"""
Schreibwerkstatt — Help CSV Merger
Mergt die module-help.csv in die BMAD help.csv
"""

import csv
import sys
from pathlib import Path

def merge_help():
    """Mergt Schreibwerkstatt-Hilfe in die BMAD help.csv."""
    project_root = Path.cwd()
    bmad_help = project_root / "_config" / "help.csv"
    module_help = Path(__file__).parent.parent / "assets" / "module-help.csv"

    if not module_help.exists():
        print("Keine module-help.csv gefunden")
        sys.exit(1)

    # Lese Modul-Einträge
    with open(module_help, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        module_rows = list(reader)

    if not bmad_help.exists():
        # Keine BMAD help.csv — erstelle neue
        bmad_help.parent.mkdir(parents=True, exist_ok=True)
        with open(bmad_help, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(module_rows)
        print(f"Help CSV erstellt mit {len(module_rows)} Einträgen")
        return

    # Lese bestehende Einträge
    with open(bmad_help, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        existing_header = next(reader)
        existing_rows = list(reader)

    # Prüfe auf Duplikate (nach canonicalId)
    existing_ids = {row[0] for row in existing_rows if row}
    new_rows = [row for row in module_rows if row and row[0] not in existing_ids]

    if not new_rows:
        print("Alle Schreibwerkstatt-Einträge bereits vorhanden")
        return

    # Append neue Einträge
    with open(bmad_help, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(new_rows)

    print(f"{len(new_rows)} neue Einträge hinzugefügt")

if __name__ == "__main__":
    merge_help()
