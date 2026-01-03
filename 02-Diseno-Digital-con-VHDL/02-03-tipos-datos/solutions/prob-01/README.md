# Soluciones Detalladas: Tipos de Datos (VHDL-03)

```
::METADATA::
tipo: indice-soluciones
tema: vhdl-03-tipos-datos
actualizado: 2026-01-03
::END::
```

## Estructura de Niveles de Solución

| Nivel | Archivo | Contenido |
|-------|---------|-----------|
| 1️⃣ | [`VHDL-03-Respuestas.md`](../VHDL-03-Respuestas.md) | Solo respuestas finales |
| 2️⃣ | Esta carpeta `prob-01/` | Soluciones paso a paso |
| 3️⃣ | Secciones "Conceptos Clave" | Explicación profunda del método |

---

## Índice de Soluciones Detalladas

### Nivel 1: Tipos Predefinidos ⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 1.1 | Tipos escalares | [VHDL-03-Sol-Problema-1.1.md](VHDL-03-Sol-Problema-1.1.md) | ⭐ |
| 1.2 | std_logic vs bit | [VHDL-03-Sol-Problema-1.2.md](VHDL-03-Sol-Problema-1.2.md) | ⭐ |
| 1.3 | Literales y constantes | [VHDL-03-Sol-Problema-1.3.md](VHDL-03-Sol-Problema-1.3.md) | ⭐ |

### Nivel 2: Arrays y Vectores ⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 2.1 | std_logic_vector | [VHDL-03-Sol-Problema-2.1.md](VHDL-03-Sol-Problema-2.1.md) | ⭐⭐ |
| 2.2 | Slicing y concatenación | [VHDL-03-Sol-Problema-2.2.md](VHDL-03-Sol-Problema-2.2.md) | ⭐⭐ |
| 2.3 | Arrays multidimensionales | [VHDL-03-Sol-Problema-2.3.md](VHDL-03-Sol-Problema-2.3.md) | ⭐⭐ |

### Nivel 3: Tipos Numéricos ⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 3.1 | signed vs unsigned | [VHDL-03-Sol-Problema-3.1.md](VHDL-03-Sol-Problema-3.1.md) | ⭐⭐ |
| 3.2 | Conversiones de tipos | [VHDL-03-Sol-Problema-3.2.md](VHDL-03-Sol-Problema-3.2.md) | ⭐⭐ |
| 3.3 | Operaciones aritméticas | [VHDL-03-Sol-Problema-3.3.md](VHDL-03-Sol-Problema-3.3.md) | ⭐⭐ |

### Nivel 4: Tipos Definidos por Usuario ⭐⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 4.1 | Enumerados (FSM) | [VHDL-03-Sol-Problema-4.1.md](VHDL-03-Sol-Problema-4.1.md) | ⭐⭐⭐ |
| 4.2 | Subtipos | [VHDL-03-Sol-Problema-4.2.md](VHDL-03-Sol-Problema-4.2.md) | ⭐⭐⭐ |
| 4.3 | Records | [VHDL-03-Sol-Problema-4.3.md](VHDL-03-Sol-Problema-4.3.md) | ⭐⭐⭐ |

---

## Jerarquía de Tipos en VHDL

```
                        TIPOS
                          │
          ┌───────────────┼───────────────┐
          │               │               │
      ESCALARES      COMPUESTOS       ACCESO
          │               │               │
    ┌─────┴─────┐    ┌────┴────┐         │
    │           │    │         │      punteros
DISCRETOS   REALES  ARRAY   RECORD
    │           │
┌───┴───┐   ┌───┴───┐
│       │   │       │
INTEGER BIT REAL PHYSICAL
ENUM   BOOLEAN
```

---

## Conversiones Comunes

### Diagrama de Conversión

```
              std_logic_vector
                    │
         ┌─────────┼─────────┐
         │         │         │
         ▼         ▼         ▼
     unsigned   signed    integer
         │         │         │
         └────┬────┘         │
              │              │
              └──────┬───────┘
                     │
            to_integer / to_unsigned
            to_signed / std_logic_vector
```

### Tabla de Funciones

| De | A | Función |
|----|---|---------|
| std_logic_vector | unsigned | `unsigned(slv)` |
| std_logic_vector | signed | `signed(slv)` |
| unsigned | std_logic_vector | `std_logic_vector(u)` |
| signed | std_logic_vector | `std_logic_vector(s)` |
| unsigned | integer | `to_integer(u)` |
| signed | integer | `to_integer(s)` |
| integer | unsigned | `to_unsigned(i, bits)` |
| integer | signed | `to_signed(i, bits)` |

---

## Bibliotecas Requeridas

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;  -- std_logic, std_logic_vector
use IEEE.NUMERIC_STD.ALL;      -- signed, unsigned, aritmética
-- NO usar: use IEEE.STD_LOGIC_ARITH.ALL; (obsoleta)
-- NO usar: use IEEE.STD_LOGIC_UNSIGNED.ALL; (no estándar)
```

---

## Navegación

| ⬅️ Respuestas | 🏠 Intro | ➡️ Problemas |
|:-------------:|:--------:|:------------:|
| [VHDL-03-Respuestas.md](../VHDL-03-Respuestas.md) | [VHDL-03-Intro.md](../../VHDL-03-Intro.md) | [VHDL-03-Problemas.md](../../problems/VHDL-03-Problemas.md) |
