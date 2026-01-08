<!--
::METADATA::
type: reference
topic_id: meta-audit-files
file_id: audit-file-list
status: stable
audience: both
last_updated: 2026-01-08
-->

# Lista de Archivos Obligatorios por Subtema

La siguiente lista sirve como referencia para el validador automático y para revisiones manuales.

---

## Mínimos en Cada Subtema

### Archivos de Configuración
| Archivo | Propósito | Obligatorio |
|---------|-----------|-------------|
| `manifest.json` | Metadatos y mapa de recursos | ✅ Sí |
| `[PREFIX]-XX-directives.md` | Instrucciones para IA | ✅ Sí |

### Contenido Principal
| Archivo | Propósito | Obligatorio |
|---------|-----------|-------------|
| `[PREFIX]-XX-Intro.md` | Punto de entrada del subtema | ✅ Sí |
| `[PREFIX]-XX-Resumen-Formulas.md` | Cheatsheet/resumen | ✅ Sí |

### Carpetas Semánticas
| Carpeta | Propósito | Obligatorio |
|---------|-----------|-------------|
| `theory/` | Desarrollo teórico | ✅ Sí |
| `methods/` | Procedimientos | ✅ Sí |
| `problems/` | Ejercicios | ✅ Sí |
| `solutions/` | Respuestas | ✅ Sí |
| `applications/` | Casos de uso | ⚪ Opcional |
| `media/` | Recursos visuales | ⚪ Opcional |
| `diagnostic/` | Evaluaciones previas | ⚪ Opcional |
| `Notas/` | Sandbox (zona libre) | ⚪ Opcional |

---

## Campos Requeridos en `manifest.json`

### Campos Obligatorios

```json
{
  "id": "prefijo-xx-nombre-subtema",
  "topic": "Nombre Legible del Tema",
  "type": "learning_module",
  "status": "draft|review|stable|active|published",
  "tags": ["tag1", "tag2", "tag3"]
}
```

| Campo | Tipo | Descripción | Ejemplo |
|-------|------|-------------|---------|
| `id` | string | Identificador único | `"dd-01-sistemas-numericos"` |
| `topic` | string | Nombre legible | `"Sistemas Numéricos"` |
| `type` | string | Tipo de módulo | `"learning_module"` |
| `status` | string | Estado actual | `"published"` |
| `tags` | array | Etiquetas de búsqueda | `["binario", "conversion"]` |

### Campos Recomendados

```json
{
  "last_updated": "YYYY-MM-DD",
  "human_purpose": "Descripción del objetivo de aprendizaje",
  "difficulty": "básico|intermedio|avanzado",
  "estimated_time": "X-Y horas",
  "prerequisites": [],
  "learning_objectives": [],
  "resource_map": {
    "entry_point": "[PREFIX]-XX-Intro.md",
    "main_theory": "theory/[PREFIX]-XX-Teoria-*.md",
    "cheat_sheet": "[PREFIX]-XX-Resumen-Formulas.md",
    "methods": ["methods/*.md"],
    "problems": "problems/[PREFIX]-XX-Problemas.md",
    "answers": "solutions/[PREFIX]-XX-Respuestas.md",
    "solutions": ["solutions/[PREFIX]-XX-Soluciones-Desarrolladas.md"]
  },
  "ai_contract": {
    "strict_mode": true,
    "directives_file": "[PREFIX]-XX-directives.md",
    "default_output": "markdown",
    "allowed_tasks": ["explain_concept", "generate_problems", "verify_solution"],
    "solution_guidelines": {
      "require_context": true,
      "step_by_step": true
    }
  },
  "references": []
}
```

---

## Archivos Deseables (No Bloqueantes)

- Tablas de tiempos o verdad en `media/` si aplica
- Diagramas en `media/` referenciados desde `theory/` o `solutions/`
- Tests o simulaciones en `applications/` cuando existan
- `media/generated/` para recursos auto-generados
- `Notas/README.md` con directivas de zona sandbox

---

## Estructura de `solutions/`

Sistema de 3 niveles:

| Nivel | Archivo | Contenido |
|-------|---------|-----------|
| 1 | `[PREFIX]-XX-Respuestas.md` | Solo resultados finales |
| 2 | `[PREFIX]-XX-Soluciones-Desarrolladas.md` | Resultados con contexto breve |
| 3 | `prob-XX/` | Desarrollo completo por problema |

---

## Validación Automática

El script `tools/validate_repo.py` verifica:

1. ✅ Existencia de `manifest.json` en cada subtema
2. ✅ Campos obligatorios en manifests
3. ✅ Nomenclatura correcta de archivos
4. ✅ Prefijos válidos por módulo (DD, VHDL, MCU)
5. ✅ Bloques `::METADATA::` en archivos `.md`
6. ✅ Enlaces internos no rotos

---

## Prefijos por Módulo

| Módulo | Prefijo | Rango de Subtemas |
|--------|---------|-------------------|
| 01-Diseno-Digital | `DD` | DD-01 a DD-07 |
| 02-Diseno-Digital-con-VHDL | `VHDL` | VHDL-01 a VHDL-07 |
| 03-Microcontroladores | `MCU` | MCU-01 a MCU-07 |

---

> 📅 **Última actualización:** 2026-01-08
