"""Arregla manifests y nombres de Intro/directives para seguir la nomenclatura.

- Renombra *Intro.md a PREFIJO-XX-Intro.md (DD, VHDL, MCU).
- Renombra _directives.md a PREFIJO-XX-directives.md.
- Agrega campos requeridos a manifest.json (title, slug, area, topics, required_files, updated_at).
- Sincroniza resource_map.entry_point y cheat_sheet con los nombres nuevos.
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[2]
AREA_MAP = {
    "01-Diseno-Digital": ("dd", "DD"),
    "02-Diseno-Digital-con-VHDL": ("vhdl", "VHDL"),
    "03-Microcontroladores": ("mcu", "MCU"),
}


def derive_num(sub: Path) -> str:
    parts = sub.name.split("-")
    if len(parts) >= 2 and parts[1].isdigit():
        return f"{int(parts[1]):02d}"
    return "00"


def derive_slug(sub: Path) -> str:
    parts = sub.name.split("-", 2)
    if len(parts) >= 3:
        return parts[2]
    return sub.name


def update_manifest(man_path: Path, area_code: str, prefix: str, num: str, intro_name: str, resumen_name: Optional[str]) -> None:
    try:
        data = json.loads(man_path.read_text(encoding="utf-8"))
    except Exception:
        data = {}

    data["title"] = data.get("topic") or data.get("title") or intro_name.replace(".md", "")
    data["slug"] = data.get("slug") or derive_slug(man_path.parent)
    data["area"] = area_code

    topics = data.get("topics") or data.get("tags") or data.get("subtopics") or []
    data["topics"] = topics

    required = ["manifest.json", intro_name]
    if resumen_name:
        required.append(resumen_name)
    data["required_files"] = required

    data["updated_at"] = date.today().isoformat()

    rm = data.get("resource_map") or {}
    rm["entry_point"] = intro_name
    if resumen_name:
        rm["cheat_sheet"] = resumen_name
    data["resource_map"] = rm

    man_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def process_sub(sub: Path, area_code: str, prefix: str) -> None:
    num = derive_num(sub)

    intro = next(sub.glob("*Intro.md"), None)
    intro_name = f"{prefix}-{num}-Intro.md"
    if intro and intro.name != intro_name:
        intro.rename(sub / intro_name)
    elif not intro:
        intro = sub / intro_name

    directives = sub / "_directives.md"
    directives_name = f"{prefix}-{num}-directives.md"
    if directives.exists():
        directives.rename(sub / directives_name)

    resumen = next(sub.glob("*Resumen-Formulas.md"), None)
    resumen_name = resumen.name if resumen else None

    man = sub / "manifest.json"
    if man.exists():
        update_manifest(man, area_code, prefix, num, intro_name, resumen_name)


def main() -> None:
    for folder, (area_code, prefix) in AREA_MAP.items():
        base = ROOT / folder
        if not base.exists():
            continue
        for sub in sorted(base.iterdir()):
            if sub.is_dir():
                process_sub(sub, area_code, prefix)


if __name__ == "__main__":
    main()
