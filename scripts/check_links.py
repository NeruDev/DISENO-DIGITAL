#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para validar enlaces relativos entre archivos Markdown.
Verifica que todos los enlaces internos apunten a archivos existentes.

Uso: python check_links.py [directorio_base]
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple
from urllib.parse import urlparse


def find_markdown_files(base_dir: str) -> List[Path]:
    """Encuentra todos los archivos .md en el directorio dado."""
    return list(Path(base_dir).rglob("*.md"))


def is_external_link(link: str) -> bool:
    """Determina si un enlace es externo usando urllib.parse."""
    parsed = urlparse(link)
    # Es externo si tiene scheme (http, https, mailto, etc.) o es un enlace de anclaje puro
    return bool(parsed.scheme) or link.startswith('#')


def extract_links(content: str) -> List[str]:
    """Extrae enlaces relativos del contenido Markdown."""
    # Patrón para enlaces markdown: [texto](ruta)
    pattern = r'\[([^\]]*)\]\(([^)]+)\)'
    links = []
    for match in re.finditer(pattern, content):
        link = match.group(2)
        # Ignorar enlaces externos usando urllib.parse
        if not is_external_link(link):
            # Remover anclas del enlace
            link = link.split('#')[0] if '#' in link else link
            if link:
                links.append(link)
    return links


def validate_link(source_file: Path, link: str, base_dir: Path) -> bool:
    """Valida si un enlace relativo apunta a un archivo existente."""
    # Resolver ruta relativa desde el archivo fuente
    source_dir = source_file.parent
    target_path = (source_dir / link).resolve()
    return target_path.exists()


def check_links(base_dir: str) -> Tuple[int, int, List[str]]:
    """
    Verifica todos los enlaces en archivos Markdown.
    
    Retorna:
        Tupla con (total_enlaces, enlaces_rotos, lista_errores)
    """
    base_path = Path(base_dir).resolve()
    md_files = find_markdown_files(base_dir)
    
    total_links = 0
    broken_links = 0
    errors = []
    
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            links = extract_links(content)
            
            # Calculate relative path safely
            try:
                rel_path = md_file.relative_to(base_path)
            except ValueError:
                rel_path = md_file.name
            
            for link in links:
                total_links += 1
                if not validate_link(md_file, link, base_path):
                    broken_links += 1
                    errors.append(f"  {rel_path}: enlace roto -> {link}")
        except Exception as e:
            errors.append(f"  Error leyendo {md_file}: {e}")
    
    return total_links, broken_links, errors


def main():
    """Punto de entrada principal."""
    base_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    print(f"Verificando enlaces en: {os.path.abspath(base_dir)}")
    print("-" * 50)
    
    total, broken, errors = check_links(base_dir)
    
    print(f"Total de enlaces encontrados: {total}")
    print(f"Enlaces rotos: {broken}")
    
    if errors:
        print("\nErrores encontrados:")
        for error in errors:
            print(error)
        sys.exit(1)
    else:
        print("\n✓ Todos los enlaces son válidos.")
        sys.exit(0)


if __name__ == "__main__":
    main()
