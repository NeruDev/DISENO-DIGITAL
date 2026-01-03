# Nomenclatura y metadatos estandar

Reglas para nombrar archivos, carpetas y metadatos en el repositorio.

## Esquema de nombres
- Formato: [PREFIJO]-[XX]-[Contenido].md
  - PREFIJO: DD para Diseno Digital, VHDL para la serie VHDL, MCU para Microcontroladores.
  - XX: numero de tema con dos digitos (01, 02, ...).
  - Contenido: descriptor corto en kebab-case (Intro, Resumen-Formulas, Problemas, Soluciones, etc.).
- Ejemplos: DD-03-Resumen-Formulas.md, VHDL-02-Intro.md, MCU-04-Problemas.md.

## Carpetas por tema
- 01-Diseno-Digital/XX-subtema/
- 02-Diseno-Digital-con-VHDL/XX-subtema/
- 03-Microcontroladores/XX-subtema/
- Dentro de cada subtema: applications/, media/, methods/, problems/, solutions/, theory/, y archivos raiz *-Intro.md, *-Resumen-Formulas.md, manifest.json.

## Metadatos obligatorios (front matter)
```
---
title: "Titulo del archivo"
level: 1 | 2 | 3
prerequisites: ["DD-01-Intro"]
tags: ["logica", "compuertas"]
summary: "Descripcion breve (<= 200 chars)."
---
```
- Colocar al inicio de los archivos de contenido (no en manifiestos).
- `level` sigue el sistema de niveles descrito en ia-contract.md.

## Manifiestos (manifest.json)
- Presencia obligatoria en cada subtema.
- Campos minimos: title, slug, area (dd | vhdl | mcu), topics (lista), required_files (lista), updated_at (ISO8601).
- El script tools/validate_repo.py verifica su existencia y esquema basico.

## Versionado y convenciones
- No mezclar idiomas en un mismo archivo; preferir espanol neutro.
- Evitar espacios en nombres de archivo y carpeta.
- Usar guiones y numeros consistentes; no inventar nuevos prefijos sin documentar aqui primero.
