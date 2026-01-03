"""Validador basico de estructura y metadatos del repositorio.

Comprobaciones:
- Existencia de manifest.json en cada subtema.
- Coincidencia de nombres con el patron estandar.
- Presencia de archivos minimos por subtema (Intro y Resumen-Formulas).
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable, List, Tuple

ROOT = Path(__file__).resolve().parents[2]
NAME_PATTERN = re.compile(r"^(DD|VHDL|MCU)-\d{2}-[A-Za-z0-9-]+\.md$")
AREAS = {
    "01-Diseno-Digital": "dd",
    "02-Diseno-Digital-con-VHDL": "vhdl",
    "03-Microcontroladores": "mcu",
}
REQUIRED_FILES = ["manifest.json", "*Intro.md", "*Resumen-Formulas.md"]


def iter_subtopics() -> Iterable[Tuple[str, Path]]:
    for folder, area in AREAS.items():
        base = ROOT / folder
        if not base.exists():
            continue
        for sub in sorted(base.iterdir()):
            if sub.is_dir():
                yield area, sub


def check_manifest(path: Path) -> List[str]:
    issues: List[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - defensive
        issues.append(f"{path}: no se puede leer JSON ({exc})")
        return issues

    for field in ("title", "slug", "area", "topics", "required_files", "updated_at"):
        if field not in data:
            issues.append(f"{path}: falta campo obligatorio '{field}'")
    if data.get("area") and data.get("area") not in AREAS.values():
        issues.append(f"{path}: area invalida '{data.get('area')}'")
    if not isinstance(data.get("topics", []), list):
        issues.append(f"{path}: 'topics' debe ser lista")
    if not isinstance(data.get("required_files", []), list):
        issues.append(f"{path}: 'required_files' debe ser lista")
    return issues


def check_required_files(sub: Path) -> List[str]:
    issues: List[str] = []
    for pattern in REQUIRED_FILES:
        matches = list(sub.glob(pattern))
        if not matches:
            issues.append(f"{sub}: falta archivo que coincide con '{pattern}'")
    return issues


def check_names(sub: Path) -> List[str]:
    issues: List[str] = []
    for file in sub.glob("*.md"):
        if not NAME_PATTERN.match(file.name):
            issues.append(f"{file}: nombre no cumple el patron {NAME_PATTERN.pattern}")
    return issues


def validate() -> List[str]:
    issues: List[str] = []
    for area, sub in iter_subtopics():
        manifest = sub / "manifest.json"
        if not manifest.exists():
            issues.append(f"{sub}: falta manifest.json")
        else:
            issues.extend(check_manifest(manifest))
        issues.extend(check_required_files(sub))
        issues.extend(check_names(sub))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida estructura del repo")
    parser.add_argument("--root", type=Path, default=ROOT, help="Ruta raiz del repo")
    args = parser.parse_args()

    if args.root != ROOT:
        globals()["ROOT"] = args.root

    issues = validate()
    if not issues:
        print("OK: estructura valida")
        return 0

    print("Errores encontrados:")
    for msg in issues:
        print(f"- {msg}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
