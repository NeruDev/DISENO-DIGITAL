<!--
::METADATA::
type: reference
topic_id: meta-ia-contract
file_id: ia-contract
status: stable
audience: ai_context
last_updated: 2026-01-08
-->

# Contrato IA — Diseño Digital (Constitución)

Este documento define el marco operativo para agentes de IA que trabajen en este repositorio. Prioriza consistencia, trazabilidad y seguridad semántica.

---

## 1. Estructura del Repositorio

| # | Prefijo | Módulo | Descripción |
|---|---------|--------|-------------|
| 01 | `DD` | Diseño Digital | Fundamentos de lógica digital, circuitos combinacionales y secuenciales |
| 02 | `VHDL` | Diseño Digital con VHDL | Descripción de hardware, síntesis y simulación |
| 03 | `MCU` | Microcontroladores | Arquitectura, programación y aplicaciones embebidas |

---

## 2. Sistema de Nomenclatura

**Patrón:** `[PREFIJO]-[XX]-[Contenido]-[Tipo].md`

| Componente | Descripción | Ejemplo |
|------------|-------------|---------|
| **PREFIJO** | 2-4 letras del módulo | `DD`, `VHDL`, `MCU` |
| **XX** | Número de subtema (01-99) | `01`, `02`, `07` |
| **Contenido** | Descriptor en kebab-case | `Teoria-SistemasNumericos` |
| **Tipo** | Categoría del archivo | `Intro`, `Problemas`, `Respuestas` |

**Ejemplos válidos:**
- `DD-01-Intro.md`
- `VHDL-03-Teoria-TiposDatos.md`
- `MCU-05-Problemas.md`

---

## 3. Estructura Obligatoria por Subtema

Cada subtema DEBE contener:

| Archivo/Carpeta | Propósito | Obligatorio |
|-----------------|-----------|-------------|
| `manifest.json` | Metadatos y mapa de recursos | ✅ Sí |
| `[PREFIX]-XX-directives.md` | Instrucciones específicas | ✅ Sí |
| `[PREFIX]-XX-Intro.md` | Punto de entrada | ✅ Sí |
| `[PREFIX]-XX-Resumen-Formulas.md` | Cheatsheet | ✅ Sí |
| `theory/` | Desarrollo teórico | ✅ Sí |
| `methods/` | Procedimientos | ✅ Sí |
| `problems/` | Ejercicios | ✅ Sí |
| `solutions/` | Respuestas | ✅ Sí |
| `applications/` | Casos de uso | ⚪ Opcional |
| `media/` | Recursos visuales | ⚪ Opcional |
| `Notas/` | Sandbox (zona libre) | ⚪ Opcional |

---

## 4. Alcance y Objetivos

- Garantizar que el repositorio crezca de forma coherente y verificable.
- Permitir a las IAs asistir en redacción, validación, generación de problemas y soluciones.
- Preservar la fidelidad matemática: no inventar notación ni resultados.

---

## 5. Roles y Tareas Permitidas

✅ **PERMITIDO:**
- Explicar conceptos con referencias a archivos existentes
- Generar problemas y soluciones en el sistema de niveles (1, 2, 3)
- Redactar resúmenes, glosarios y enlaces cruzados hacia GLOSSARY/ y WIKI/
- Proponer mejoras de estructura, nomenclatura y metadatos

⛔ **PROHIBIDO:**
- Introducir notación no estándar o ambigua
- Modificar resultados matemáticos sin justificación o evidencia
- Borrar contexto existente (metadatos, manifiestos) salvo orden explícita
- Insertar dependencias externas sin consenso

---

## 6. Sistema de Niveles para Problemas y Soluciones

| Nivel | Nombre | Contenido | Ubicación |
|-------|--------|-----------|-----------|
| 1 | Esqueleto | Planteamiento, variables, supuestos, resultado esperado | `solutions/[PREFIX]-XX-Respuestas.md` |
| 2 | Respuesta rápida | Tabla con resultados, fórmula final, pasos mínimos | `solutions/[PREFIX]-XX-Soluciones-Desarrolladas.md` |
| 3 | Desarrollo completo | Demostraciones, diagramas, pasos detallados | `solutions/prob-XX/` |

---

## 7. Reglas de Generación de Contenido

- **SIEMPRE** dar contexto antes de resolver
- Usar notación estándar según `notation-cheatsheet.md`
- Validar contra bibliografía en `bibliografia-general.md`
- Formato de soluciones: `**N)** *Contexto:* [explicación]`

---

## 8. Interacción con Humanos

- Siempre citar rutas de archivo relativas al repositorio
- Preguntar antes de alterar contenido sensible o borrar material
- Responder en el idioma del archivo destino (por defecto español neutro)

---

## 9. Interacción con Herramientas

- Ejecutar validaciones locales antes de confirmar cambios (ver `repo-tests.md`)
- Mantener scripts y plantillas en `00-META/` sincronizados con el árbol de contenidos
- Herramientas disponibles en `00-META/tools/`:
  - `validate_repo.py` — Auditor de estructura
  - `link_knowledge_base.py` — Auto-vinculador
  - `check_tables.py` — Validador de tablas
  - `check_links.py` — Verificador de enlaces
  - `validate_metadata.py` — Validador de metadatos

---

## 10. Estilo y Consistencia

- Usar ASCII por defecto; LaTeX solo donde aporte claridad
- En tablas con LaTeX, preferir `\lvert ... \rvert` en lugar de `|`
- Nunca mezclar `$` y `\(` en la misma celda
- Referenciar definiciones con enlaces internos al glosario

---

## 11. Salvaguardas

- Ante falta de contexto, detenerse y pedir instrucciones
- Documentar supuestos y fuentes al generar contenido nuevo
- Conservar versionado: no sobrescribir plantillas ni manifiestos sin respaldo

---

## 12. Zona Sandbox (Notas/)

Las carpetas `Notas/` dentro de cada subtema son **ZONAS EXENTAS** de validación:

| Acción | Comportamiento |
|--------|----------------|
| Validar nomenclatura | ⛔ OMITIR |
| Sugerir correcciones | ⛔ OMITIR |
| Solicitar metadatos | ⛔ OMITIR |
| Leer contenido | ✅ PERMITIDO |
| Integrar información | ✅ Como contexto |

---

> 📅 **Última actualización:** 2026-01-08  
> 📄 **Versión:** 2.0
