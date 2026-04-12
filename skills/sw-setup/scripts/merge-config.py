#!/usr/bin/env python3
"""
Schreibwerkstatt — Config Merger
Mergt die Modul-Konfiguration in die BMAD _config/config.yaml
"""

import sys
from pathlib import Path

def merge_config():
    """Mergt Schreibwerkstatt-Config in die BMAD-Konfiguration."""
    project_root = Path.cwd()
    config_file = project_root / "_config" / "config.yaml"
    module_config = Path(__file__).parent.parent / "assets" / "module.yaml"

    if not config_file.exists():
        print("Keine BMAD _config/config.yaml gefunden — überspringe Merge")
        return

    if not module_config.exists():
        print("Keine module.yaml gefunden")
        sys.exit(1)

    config_content = config_file.read_text(encoding="utf-8")
    module_content = module_config.read_text(encoding="utf-8")

    # Prüfe ob Schreibwerkstatt bereits konfiguriert ist
    if "schreibwerkstatt" in config_content.lower() or "code: sw" in config_content:
        print("Schreibwerkstatt bereits in Konfiguration vorhanden")
        return

    # Append module config
    separator = "\n\n# === Schreibwerkstatt Module ===\n"
    config_content += separator + module_content

    config_file.write_text(config_content, encoding="utf-8")
    print("Schreibwerkstatt-Konfiguration gemergt")

if __name__ == "__main__":
    merge_config()
