# Pruebas y checklist del repositorio

Esta guia describe las validaciones automaticas y las verificaciones manuales que mantienen saludable la base de conocimiento.

## Validaciones automaticas
- `python 00-META/tools/validate_repo.py`: revisa manifiestos, nombres y presencia de archivos clave.
- `python scripts/check_links.py`: detecta enlaces rotos internos.
- `python scripts/validate_metadata.py`: valida esquemas de metadatos segun plantillas.
- `python 00-META/tools/link_knowledge_base.py`: regenera el indice WIKI.

## Checklist manual rapido
- Manifest.json actualizado con `updated_at` reciente y campos requeridos.
- Intro y Resumen-Formulas presentes en cada subtema.
- Enlaces al glosario funcionan desde nuevos archivos.
- Las tablas LaTeX renderizan correctamente (sin `|` crudos en entornos matematicos).
- No hay archivos huérfanos ni duplicados de nombre similar.

## Flujo sugerido antes de un commit
1. Ejecutar los cuatro comandos de validacion anteriores.
2. Corregir errores reportados.
3. Agregar notas breves en el mensaje de commit mencionando subtemas tocados.

## Indicadores de salud
- Ninguna advertencia en validate_repo.py.
- Sin enlaces rotos en check_links.py.
- WIKI_INDEX actualizado y legible.
