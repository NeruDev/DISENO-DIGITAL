#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para validar la presencia del bloque ::METADATA:: en archivos Markdown.
Verifica que cada .md contenga los campos mínimos requeridos.

Uso: python validate_metadata.py [directorio_base]
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Optional


# Campos mínimos requeridos en el bloque METADATA
REQUIRED_FIELDS = ['type', 'topic_id', 'file_id', 'last_updated']

# Patrones válidos para el campo 'type'
VALID_TYPES = ['theory', 'method', 'problem', 'solution', 'reference', 'module-index']


def find_markdown_files(base_dir: str) -> List[Path]:
    """Encuentra todos los archivos .md en el directorio dado."""
    excludes = ['.git', 'node_modules', '00-META/templates']
    files = []
    for f in Path(base_dir).rglob("*.md"):
        # Excluir archivos en directorios de plantillas
        if not any(excl in str(f) for excl in excludes):
            files.append(f)
    return files


def extract_metadata(content: str) -> Optional[Dict[str, str]]:
    """
    Extrae el bloque ::METADATA:: del contenido Markdown.
    
    Retorna un diccionario con los campos encontrados, o None si no existe.
    """
    # Buscar el bloque de comentario con METADATA
    pattern = r'<!--\s*::METADATA::\s*(.*?)-->'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        return None
    
    metadata_text = match.group(1)
    metadata = {}
    
    # Parsear campos key: value
    for line in metadata_text.strip().split('\n'):
        line = line.strip()
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()
    
    return metadata


def validate_metadata(metadata: Dict[str, str]) -> List[str]:
    """
    Valida que el metadata contenga los campos requeridos.
    
    Retorna lista de errores encontrados.
    """
    errors = []
    
    for field in REQUIRED_FIELDS:
        if field not in metadata:
            errors.append(f"Campo requerido faltante: '{field}'")
        elif not metadata[field] or metadata[field] in ['YYYY-MM-DD', 'prefijo-xx-nombre', 'slug-del-archivo']:
            errors.append(f"Campo '{field}' tiene valor placeholder sin rellenar")
    
    # Validar que 'type' tenga un valor válido
    if 'type' in metadata:
        type_value = metadata['type']
        # El valor puede contener opciones separadas por |, tomar el primero si es placeholder
        if '|' in type_value:
            errors.append(f"Campo 'type' contiene opciones sin seleccionar: {type_value}")
        elif type_value not in VALID_TYPES:
            errors.append(f"Valor de 'type' no válido: {type_value}")
    
    return errors


def check_metadata(base_dir: str) -> Tuple[int, int, List[str]]:
    """
    Verifica todos los archivos Markdown por presencia de METADATA.
    
    Retorna:
        Tupla con (total_archivos, archivos_sin_metadata, lista_errores)
    """
    md_files = find_markdown_files(base_dir)
    base_path = Path(base_dir).resolve()
    
    total_files = len(md_files)
    files_without_metadata = 0
    all_errors = []
    
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            metadata = extract_metadata(content)
            
            # Calculate relative path safely
            try:
                rel_path = md_file.relative_to(base_path)
            except ValueError:
                rel_path = md_file.name
            
            if metadata is None:
                files_without_metadata += 1
                all_errors.append(f"  {rel_path}: Sin bloque ::METADATA::")
            else:
                errors = validate_metadata(metadata)
                for error in errors:
                    all_errors.append(f"  {rel_path}: {error}")
                    
        except Exception as e:
            all_errors.append(f"  Error leyendo {md_file}: {e}")
    
    return total_files, files_without_metadata, all_errors


def main():
    """Punto de entrada principal."""
    base_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    print(f"Validando METADATA en: {os.path.abspath(base_dir)}")
    print("-" * 50)
    
    total, without_meta, errors = check_metadata(base_dir)
    
    print(f"Total de archivos .md: {total}")
    print(f"Archivos sin METADATA: {without_meta}")
    
    if errors:
        print("\nProblemas encontrados:")
        for error in errors:
            print(error)
        # No salir con error en scaffolding, solo advertir
        print("\n⚠ Se encontraron archivos con metadata incompleta (normal en scaffolding).")
        sys.exit(0)
    else:
        print("\n✓ Todos los archivos tienen METADATA válido.")
        sys.exit(0)


if __name__ == "__main__":
    main()
