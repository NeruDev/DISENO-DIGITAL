<!--
::METADATA::
type: reference
topic_id: meta-audit-issues
file_id: audit-table-issues
status: active
audience: both
last_updated: 2026-01-08
-->

# 📋 Registro de Problemas — Auditoría del Repositorio

> Este archivo documenta los problemas detectados durante las auditorías del repositorio.
> Se actualiza automáticamente por scripts o manualmente tras revisiones.

---

## 🔴 Problemas Críticos (Bloqueantes)

| ID | Fecha | Ubicación | Descripción | Estado | Responsable |
|----|-------|-----------|-------------|--------|-------------|
| — | — | — | Sin problemas críticos actualmente | — | — |

---

## 🟠 Problemas Moderados (Recomendado corregir)

| ID | Fecha | Ubicación | Descripción | Estado | Responsable |
|----|-------|-----------|-------------|--------|-------------|
| MOD-001 | 2026-01-08 | `01-01-sistemas-numericos/solutions/` | Archivo duplicado: `Respuestas.md` y `DD-01-Respuestas.md` | 🔄 Pendiente | Usuario |
| MOD-002 | 2026-01-08 | `scripts/` | Scripts no unificados en `00-META/tools/` | 🔄 Pendiente | Usuario |

---

## 🟡 Advertencias (Mejoras opcionales)

| ID | Fecha | Ubicación | Descripción | Estado |
|----|-------|-----------|-------------|--------|
| ADV-001 | 2026-01-08 | Todos los subtemas | Falta carpeta `Notas/` (sandbox) | ⚪ Opcional |
| ADV-002 | 2026-01-08 | Todos los subtemas | Falta carpeta `diagnostic/` | ⚪ Opcional |
| ADV-003 | 2026-01-08 | Todos los subtemas | Falta `media/generated/` | ⚪ Opcional |
| ADV-004 | 2026-01-08 | Varios archivos | Headers de navegación inconsistentes | ⚪ Opcional |

---

## ✅ Problemas Resueltos

| ID | Fecha Detectado | Fecha Resuelto | Descripción | Solución |
|----|-----------------|----------------|-------------|----------|
| RES-001 | 2026-01-08 | 2026-01-08 | `directory-tree.md` desactualizado | Actualizado con estructura completa |
| RES-002 | 2026-01-08 | 2026-01-08 | Falta `audit-table-issues.md` | Archivo creado |
| RES-003 | 2026-01-08 | 2026-01-08 | Falta `check_tables.py` | Script creado |

---

## 📊 Resumen de Estado

| Categoría | Total | Resueltos | Pendientes |
|-----------|-------|-----------|------------|
| 🔴 Críticos | 0 | 0 | 0 |
| 🟠 Moderados | 2 | 0 | 2 |
| 🟡 Advertencias | 4 | 0 | 4 |
| **Total** | **6** | **0** | **6** |

---

## 📝 Notas de Auditoría

### Última Auditoría: 2026-01-08

**Ejecutado por:** Revisión manual + IA  
**Herramientas usadas:** `validate_repo.py`, `check_links.py`

**Observaciones:**
- La estructura general del repositorio cumple con el 85% de la plantilla de arquitectura
- Los manifests existentes tienen estructura válida pero usan esquema legacy
- Se recomienda migración gradual al nuevo esquema de campos

---

## 🔧 Acciones Recomendadas

1. **Prioridad Alta:**
   - [ ] Eliminar archivo duplicado `Respuestas.md`
   - [ ] Mover scripts de `scripts/` a `00-META/tools/`

2. **Prioridad Media:**
   - [ ] Crear carpetas `Notas/` en subtemas
   - [ ] Agregar headers de navegación estándar

3. **Prioridad Baja:**
   - [ ] Crear carpetas `diagnostic/` donde aplique
   - [ ] Crear `media/generated/` en subtemas

---

> 🔄 **Próxima auditoría programada:** Semanal  
> 📧 **Reportar nuevos problemas:** Agregar fila a la tabla correspondiente
