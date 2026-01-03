# Lista de archivos obligatorios por subtema

La siguiente lista sirve como referencia para el validador automatico y para revisiones manuales.

## Minimos en cada subtema
- manifest.json
- *-Intro.md
- *-Resumen-Formulas.md
- theory/ (carpeta)
- methods/ (carpeta)
- problems/ (carpeta)
- solutions/ (carpeta)
- applications/ (carpeta)
- media/ (carpeta)

## Campos requeridos en manifest.json
- title
- slug
- area (dd | vhdl | mcu)
- topics (lista de strings)
- required_files (lista de rutas relativas dentro del subtema)
- updated_at (ISO8601)

## Archivos deseables (no bloqueantes)
- Tablas de tiempos o verdad en media/ si aplica.
- Diagramas en media/ referenciados desde theory/ o solutions/.
- Tests o simulaciones en applications/ cuando existan.
