"""Genera un indice wiki enlazando modulos y glosario.

Salida: WIKI/WIKI_INDEX.md con enlaces a Intro y Resumen de cada subtema.
"""
from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[2]
WIKI_INDEX = ROOT / "WIKI" / "WIKI_INDEX.md"

AREAS: Dict[str, str] = {
    "01-Diseno-Digital": "Diseno Digital",
    "02-Diseno-Digital-con-VHDL": "Diseno Digital con VHDL",
    "03-Microcontroladores": "Microcontroladores",
}


def collect_entries() -> List[Tuple[str, Path, Path | None, Path | None]]:
    entries: List[Tuple[str, Path, Path | None, Path | None]] = []
    for folder, label in AREAS.items():
        base = ROOT / folder
        if not base.exists():
            continue
        for sub in sorted(base.iterdir()):
            if not sub.is_dir():
                continue
            intro = next(sub.glob("*Intro.md"), None)
            resumen = next(sub.glob("*Resumen-Formulas.md"), None)
            entries.append((label, sub, intro, resumen))
    return entries


def to_relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def render(entries: List[Tuple[str, Path, Path | None, Path | None]]) -> str:
    lines: List[str] = []
    lines.append("# WIKI_INDEX")
    lines.append("")
    lines.append("Indice generado automaticamente. No editar a mano.")
    lines.append("")
    current_area = None
    for area, sub, intro, resumen in entries:
        if area != current_area:
            lines.append(f"## {area}")
            current_area = area
        intro_link = f"[{sub.name} (Intro)]({to_relative(intro)})" if intro else "(falta Intro)"
        res_link = f"[Resumen]({to_relative(resumen)})" if resumen else "(falta Resumen)"
        lines.append(f"- {intro_link} · {res_link}")
    lines.append("")
    lines.append("Recursos globales:")
    glossary = ROOT / "GLOSSARY" / "README.md"
    if glossary.exists():
        lines.append(f"- [Glosario]({to_relative(glossary)})")
    wiki_readme = ROOT / "WIKI" / "README.md"
    if wiki_readme.exists():
        lines.append(f"- [Portal WIKI]({to_relative(wiki_readme)})")
    return "\n".join(lines) + "\n"


def write_index() -> None:
    entries = collect_entries()
    content = render(entries)
    WIKI_INDEX.write_text(content, encoding="utf-8")
    print(f"Generado {WIKI_INDEX}")


def main() -> int:
    write_index()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
