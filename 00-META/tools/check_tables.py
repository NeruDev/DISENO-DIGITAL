#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para validar tablas Markdown y detectar problemas de formato.

Detecta:
- Columnas desalineadas
- Uso incorrecto del símbolo | (conflicto con valor absoluto LaTeX)
- Filas con número incorrecto de columnas
- Tablas sin encabezado de separación

Uso: python check_tables.py [directorio_base]
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Optional
from dataclasses import dataclass


@dataclass
class TableIssue:
    """Representa un problema detectado en una tabla."""
    file_path: str
    line_number: int
    issue_type: str
    description: str
    suggestion: str


def find_markdown_files(base_dir: str) -> List[Path]:
    """Encuentra todos los archivos .md en el directorio dado."""
    excludes = ['.git', 'node_modules', '.venv']
    files = []
    for f in Path(base_dir).rglob("*.md"):
        if not any(excl in str(f) for excl in excludes):
            files.append(f)
    return files


def extract_tables(content: str) -> List[Tuple[int, List[str]]]:
    """
    Extrae tablas Markdown del contenido.
    
    Retorna lista de tuplas (línea_inicio, filas_de_tabla).
    """
    lines = content.split('\n')
    tables = []
    current_table = []
    table_start = -1
    
    for i, line in enumerate(lines, 1):
        # Detectar línea que parece parte de tabla (contiene | y no está en bloque de código)
        if '|' in line and not line.strip().startswith('```'):
            if not current_table:
                table_start = i
            current_table.append((i, line))
        else:
            if current_table and len(current_table) >= 2:
                tables.append((table_start, current_table))
            current_table = []
            table_start = -1
    
    # Capturar última tabla si existe
    if current_table and len(current_table) >= 2:
        tables.append((table_start, current_table))
    
    return tables


def count_columns(row: str) -> int:
    """Cuenta el número de columnas en una fila de tabla."""
    # Remover | inicial y final si existen
    row = row.strip()
    if row.startswith('|'):
        row = row[1:]
    if row.endswith('|'):
        row = row[:-1]
    
    # Dividir por | pero ignorar \| (escape)
    # Patrón simple: contar | que no estén precedidos por \
    parts = re.split(r'(?<!\\)\|', row)
    return len(parts)


def is_separator_row(row: str) -> bool:
    """Verifica si una fila es el separador de encabezado (---|---|---)."""
    row = row.strip().strip('|')
    # Debe contener solo -, :, | y espacios
    return bool(re.match(r'^[\s\-:|]+$', row)) and '-' in row


def check_latex_pipe_conflict(row: str) -> Optional[str]:
    """
    Detecta uso problemático de | en contexto LaTeX.
    
    Retorna sugerencia si hay conflicto, None si está bien.
    """
    # Buscar patrones problemáticos dentro de contexto matemático
    # Patrón: $...|...$ o \(...|...\)
    math_patterns = [
        (r'\$[^$]*\|[^$]*\$', 'Usar \\lvert y \\rvert en lugar de | dentro de $...$'),
        (r'\\\([^)]*\|[^)]*\\\)', 'Usar \\lvert y \\rvert en lugar de | dentro de \\(...\\)'),
    ]
    
    for pattern, suggestion in math_patterns:
        if re.search(pattern, row):
            return suggestion
    
    return None


def validate_table(table_start: int, table_rows: List[Tuple[int, str]]) -> List[TableIssue]:
    """
    Valida una tabla Markdown y retorna lista de problemas.
    """
    issues = []
    
    if len(table_rows) < 2:
        return issues
    
    # Verificar que existe fila separadora
    has_separator = False
    separator_index = -1
    for i, (line_num, row) in enumerate(table_rows):
        if is_separator_row(row):
            has_separator = True
            separator_index = i
            break
    
    if not has_separator:
        issues.append(TableIssue(
            file_path="",
            line_number=table_start,
            issue_type="MISSING_SEPARATOR",
            description="Tabla sin fila separadora de encabezado",
            suggestion="Agregar fila con |---|---|---| después del encabezado"
        ))
        return issues
    
    # Contar columnas del encabezado
    header_line, header_row = table_rows[0]
    header_cols = count_columns(header_row)
    
    # Verificar consistencia de columnas
    for line_num, row in table_rows:
        if is_separator_row(row):
            continue
        
        row_cols = count_columns(row)
        if row_cols != header_cols:
            issues.append(TableIssue(
                file_path="",
                line_number=line_num,
                issue_type="COLUMN_MISMATCH",
                description=f"Fila tiene {row_cols} columnas, encabezado tiene {header_cols}",
                suggestion="Verificar que todas las filas tengan el mismo número de columnas"
            ))
        
        # Verificar conflictos con LaTeX
        latex_issue = check_latex_pipe_conflict(row)
        if latex_issue:
            issues.append(TableIssue(
                file_path="",
                line_number=line_num,
                issue_type="LATEX_PIPE_CONFLICT",
                description="Posible conflicto de | con notación LaTeX",
                suggestion=latex_issue
            ))
    
    return issues


def check_tables_in_file(file_path: Path) -> List[TableIssue]:
    """
    Verifica todas las tablas en un archivo Markdown.
    """
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return [TableIssue(
            file_path=str(file_path),
            line_number=0,
            issue_type="READ_ERROR",
            description=f"Error leyendo archivo: {e}",
            suggestion="Verificar permisos y codificación del archivo"
        )]
    
    tables = extract_tables(content)
    all_issues = []
    
    for table_start, table_rows in tables:
        issues = validate_table(table_start, table_rows)
        for issue in issues:
            issue.file_path = str(file_path)
        all_issues.extend(issues)
    
    return all_issues


def check_all_tables(base_dir: str) -> Tuple[int, int, List[TableIssue]]:
    """
    Verifica todas las tablas en archivos Markdown.
    
    Retorna:
        Tupla con (total_tablas, tablas_con_problemas, lista_issues)
    """
    md_files = find_markdown_files(base_dir)
    all_issues = []
    total_tables = 0
    files_with_issues = set()
    
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            tables = extract_tables(content)
            total_tables += len(tables)
            
            issues = check_tables_in_file(md_file)
            if issues:
                files_with_issues.add(str(md_file))
                all_issues.extend(issues)
        except Exception:
            pass
    
    return total_tables, len(files_with_issues), all_issues


def main():
    """Punto de entrada principal."""
    base_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    print(f"🔍 Verificando tablas Markdown en: {os.path.abspath(base_dir)}")
    print("-" * 60)
    
    total_tables, files_with_issues, issues = check_all_tables(base_dir)
    
    print(f"📊 Total de tablas encontradas: {total_tables}")
    print(f"📁 Archivos con problemas: {files_with_issues}")
    print(f"⚠️  Total de problemas: {len(issues)}")
    print("-" * 60)
    
    if issues:
        print("\n🔴 PROBLEMAS DETECTADOS:\n")
        
        # Agrupar por archivo
        issues_by_file: Dict[str, List[TableIssue]] = {}
        for issue in issues:
            if issue.file_path not in issues_by_file:
                issues_by_file[issue.file_path] = []
            issues_by_file[issue.file_path].append(issue)
        
        for file_path, file_issues in issues_by_file.items():
            # Mostrar ruta relativa
            try:
                rel_path = Path(file_path).relative_to(Path(base_dir).resolve())
            except ValueError:
                rel_path = file_path
            
            print(f"📄 {rel_path}")
            for issue in file_issues:
                print(f"   Línea {issue.line_number}: [{issue.issue_type}]")
                print(f"      {issue.description}")
                print(f"      💡 {issue.suggestion}")
            print()
        
        sys.exit(1)
    else:
        print("\n✅ Todas las tablas están correctamente formateadas.")
        sys.exit(0)


if __name__ == "__main__":
    main()
