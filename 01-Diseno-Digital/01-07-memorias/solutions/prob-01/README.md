# Soluciones Detalladas: Memorias (DD-07)

```
::METADATA::
tipo: indice-soluciones
tema: dd-07-memorias
actualizado: 2026-01-03
::END::
```

## Estructura de Niveles de Solución

| Nivel | Archivo | Contenido |
|-------|---------|-----------|
| 1️⃣ | [`DD-07-Respuestas.md`](../DD-07-Respuestas.md) | Solo respuestas finales |
| 2️⃣ | Esta carpeta `prob-01/` | Soluciones paso a paso |
| 3️⃣ | Secciones "Conceptos Clave" | Explicación profunda del método |

---

## Índice de Soluciones Detalladas

### Nivel 1: ROM

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 1.1 | Diseño ROM básica | [DD-07-Sol-Problema-1.1.md](DD-07-Sol-Problema-1.1.md) | ⭐⭐ |
| 1.2 | ROM para funciones | [DD-07-Sol-Problema-1.2.md](DD-07-Sol-Problema-1.2.md) | ⭐⭐ |
| 1.3 | Expansión de ROM | [DD-07-Sol-Problema-1.3.md](DD-07-Sol-Problema-1.3.md) | ⭐⭐ |

### Nivel 2: RAM

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 2.1 | Celda SRAM básica | [DD-07-Sol-Problema-2.1.md](DD-07-Sol-Problema-2.1.md) | ⭐⭐ |
| 2.2 | Ciclos de lectura/escritura | [DD-07-Sol-Problema-2.2.md](DD-07-Sol-Problema-2.2.md) | ⭐⭐ |
| 2.3 | Banco de memoria | [DD-07-Sol-Problema-2.3.md](DD-07-Sol-Problema-2.3.md) | ⭐⭐⭐ |

### Nivel 3: PLD

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 3.1 | PAL diseño | [DD-07-Sol-Problema-3.1.md](DD-07-Sol-Problema-3.1.md) | ⭐⭐ |
| 3.2 | PLA diseño | [DD-07-Sol-Problema-3.2.md](DD-07-Sol-Problema-3.2.md) | ⭐⭐⭐ |
| 3.3 | GAL/CPLD | [DD-07-Sol-Problema-3.3.md](DD-07-Sol-Problema-3.3.md) | ⭐⭐⭐ |

---

## Referencia de Memorias

### Clasificación

```
                    MEMORIAS
                       │
          ┌────────────┼────────────┐
          │            │            │
       VOLÁTIL    NO VOLÁTIL      PLD
          │            │            │
     ┌────┴────┐  ┌────┴────┐  ┌───┴───┐
     │         │  │         │  │       │
   SRAM     DRAM ROM    Flash PAL    PLA
```

### Comparativa

| Tipo | Volátil | Escritura | Velocidad | Costo |
|------|:-------:|:---------:|:---------:|:-----:|
| SRAM | Sí | Sí | Muy alta | Alto |
| DRAM | Sí | Sí | Alta | Medio |
| ROM | No | No* | Alta | Bajo |
| EEPROM | No | Sí | Media | Medio |
| Flash | No | Sí | Alta | Bajo |

### Fórmulas de Capacidad

**Capacidad total:**
$$C = 2^n \times m \text{ bits}$$

Donde:
- $n$ = bits de dirección
- $m$ = ancho de palabra

**Ejemplo:** ROM 4K×8
- Direcciones: $4K = 4096 = 2^{12}$ → 12 bits
- Datos: 8 bits
- Capacidad: $4096 \times 8 = 32,768$ bits = 4 KB

---

## Navegación

| ⬅️ Respuestas | 🏠 Intro | ➡️ Problemas |
|:-------------:|:--------:|:------------:|
| [DD-07-Respuestas.md](../DD-07-Respuestas.md) | [DD-07-Intro.md](../../DD-07-Intro.md) | [DD-07-Problemas.md](../../problems/DD-07-Problemas.md) |
