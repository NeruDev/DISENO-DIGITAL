<!--
::METADATA::
type: reference
topic_id: meta-nomenclatura
file_id: nomenclatura-estandar
status: stable
audience: both
last_updated: 2026-01-08
-->

# Nomenclatura y Metadatos Estándar

Reglas para nombrar archivos, carpetas y metadatos en el repositorio.

---

## 1. Esquema de Nombres de Archivos

### Patrón Principal

```
[PREFIJO]-[XX]-[Contenido]-[Tipo].md
```

| Componente | Descripción | Valores |
|------------|-------------|---------|
| **PREFIJO** | Identificador del módulo | `DD`, `VHDL`, `MCU` |
| **XX** | Número de tema (2 dígitos) | `01`, `02`, ... `07` |
| **Contenido** | Descriptor en kebab-case | `Teoria-SistemasNumericos` |
| **Tipo** | Categoría del archivo | `Intro`, `Problemas`, `Respuestas` |

### Prefijos Autorizados

| Módulo | Prefijo | Descripción |
|--------|---------|-------------|
| 01-Diseno-Digital | `DD` | Diseño Digital básico |
| 02-Diseno-Digital-con-VHDL | `VHDL` | Diseño con VHDL |
| 03-Microcontroladores | `MCU` | Microcontroladores |

> ⚠️ **No inventar nuevos prefijos** sin documentar aquí primero.

### Ejemplos Válidos

```
DD-01-Intro.md
DD-03-Resumen-Formulas.md
DD-04-Teoria-CircuitosCombinacionales.md
VHDL-02-Intro.md
VHDL-05-Metodos-Procesos.md
MCU-04-Problemas.md
MCU-06-Respuestas.md
```

---

## 2. Estructura de Carpetas por Tema

```
XX-Modulo/
├── 00-Index.md
├── XX-01-subtema/
│   ├── manifest.json
│   ├── [PREFIX]-01-directives.md
│   ├── [PREFIX]-01-Intro.md
│   ├── [PREFIX]-01-Resumen-Formulas.md
│   ├── theory/
│   │   └── [PREFIX]-01-Teoria-*.md
│   ├── methods/
│   │   └── [PREFIX]-01-Metodos-*.md
│   ├── problems/
│   │   └── [PREFIX]-01-Problemas.md
│   ├── solutions/
│   │   ├── [PREFIX]-01-Respuestas.md
│   │   ├── [PREFIX]-01-Soluciones-Desarrolladas.md
│   │   └── prob-XX/
│   ├── applications/
│   ├── media/
│   │   └── generated/
│   └── Notas/
│       └── README.md
└── XX-02-subtema/
```

---

## 3. Sistema de Metadatos `::METADATA::`

Todo archivo `.md` debe comenzar con un bloque de metadatos en comentario HTML:

```markdown
<!--
::METADATA::
type: [tipo]
topic_id: [id-del-tema]
file_id: [nombre-archivo]
status: [estado]
audience: [audiencia]
last_updated: YYYY-MM-DD
-->
```

### Campos Obligatorios

| Campo | Descripción | Valores |
|-------|-------------|---------|
| `type` | Tipo de contenido | Ver tabla siguiente |
| `topic_id` | ID del tema padre | `dd-01-sistemas-numericos` |
| `file_id` | ID único del archivo | `DD-01-Intro` |
| `status` | Estado del documento | `draft`, `review`, `stable`, `active` |
| `audience` | Público objetivo | `student`, `ai_context`, `both` |
| `last_updated` | Fecha de actualización | `2026-01-08` |

### Tipos Válidos (`type`)

| Tipo | Descripción | Ubicación |
|------|-------------|-----------|
| `index` | Punto de entrada | `*-Intro.md` |
| `theory` | Desarrollo teórico | `theory/*.md` |
| `method` | Procedimiento | `methods/*.md` |
| `problem` | Enunciados | `problems/*.md` |
| `solution` | Soluciones | `solutions/*.md` |
| `answer-key` | Tabla de respuestas | `*-Respuestas.md` |
| `cheatsheet` | Resumen/fórmulas | `*-Resumen-*.md` |
| `reference` | Documento de referencia | `00-META/*.md` |
| `module-index` | Índice de módulo | `00-Index.md` |
| `sandbox` | Zona libre | `Notas/README.md` |

### Ejemplo Completo

```markdown
<!--
::METADATA::
type: theory
topic_id: dd-01-sistemas-numericos
file_id: DD-01-Teoria-SistemasNumericos
status: stable
audience: both
last_updated: 2026-01-08
difficulty: 1
tags: [binario, conversion, numeracion]
search_keywords: "sistemas numéricos, binario, hexadecimal"
-->

# Teoría de Sistemas Numéricos

[Contenido...]
```

---

## 4. Metadatos Front Matter (Alternativo)

Para compatibilidad con algunos sistemas, también se acepta YAML front matter:

```yaml
---
title: "Título del archivo"
level: 1 | 2 | 3
prerequisites: ["DD-01-Intro"]
tags: ["logica", "compuertas"]
summary: "Descripción breve (<= 200 chars)."
---
```

> ⚠️ Preferir `::METADATA::` sobre YAML front matter para consistencia.

---

## 5. Manifiestos (`manifest.json`)

### Campos Mínimos Requeridos

```json
{
  "id": "dd-01-sistemas-numericos",
  "topic": "Sistemas Numéricos",
  "type": "learning_module",
  "status": "published",
  "tags": ["binario", "conversion", "hexadecimal"]
}
```

### Esquema Completo Recomendado

```json
{
  "id": "[prefijo]-[xx]-[nombre]",
  "topic": "[Nombre legible]",
  "type": "learning_module",
  "status": "active",
  "last_updated": "YYYY-MM-DD",
  "human_purpose": "[Descripción del objetivo]",
  "tags": ["tag1", "tag2"],
  "difficulty": "básico|intermedio|avanzado",
  "estimated_time": "X-Y horas",
  "resource_map": {
    "entry_point": "[PREFIX]-XX-Intro.md",
    "main_theory": "theory/[PREFIX]-XX-Teoria-*.md",
    "cheat_sheet": "[PREFIX]-XX-Resumen-Formulas.md",
    "methods": ["methods/*.md"],
    "problems": "problems/[PREFIX]-XX-Problemas.md",
    "answers": "solutions/[PREFIX]-XX-Respuestas.md"
  },
  "ai_contract": {
    "strict_mode": true,
    "directives_file": "[PREFIX]-XX-directives.md"
  }
}
```

---

## 6. Convenciones Generales

### Nombres de Archivo
- ✅ Usar guiones (`-`) como separadores
- ✅ Usar números de 2 dígitos (`01`, `02`)
- ✅ Usar PascalCase para descriptores (`SistemasNumericos`)
- ❌ No usar espacios en nombres
- ❌ No usar caracteres especiales (`ñ`, `á`, etc.)
- ❌ No mezclar idiomas en un mismo archivo

### Idioma
- Preferir español neutro en contenido
- Términos técnicos pueden mantenerse en inglés cuando sea estándar

### Versionado
- No inventar nuevos prefijos sin documentar
- Documentar cambios en `audit-table-issues.md`
- Ejecutar `validate_repo.py` antes de commits

---

## 7. Sistema de Enlaces

### Sintaxis Obligatoria

```markdown
[Texto visible](ruta/relativa/archivo.md)
[Texto visible](ruta/relativa/archivo.md#ancla)
```

### Ejemplos por Tipo

| Destino | Sintaxis |
|---------|----------|
| Mismo directorio | `[Intro](DD-01-Intro.md)` |
| Subdirectorio | `[Teoría](theory/DD-01-Teoria.md)` |
| Glosario | `[término](../../glossary.md#termino)` |
| Entre módulos | `[VHDL](../02-Diseno-Digital-con-VHDL/02-01-introduccion-vhdl/)` |

### Header de Navegación Estándar

```markdown
> 🏠 **Navegación:** [← Volver al Índice](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)
```

---

> 📅 **Última actualización:** 2026-01-08  
> 📄 **Versión:** 2.0
