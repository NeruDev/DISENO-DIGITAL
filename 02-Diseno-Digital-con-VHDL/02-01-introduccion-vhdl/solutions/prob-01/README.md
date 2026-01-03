# Soluciones Detalladas: Introducción a VHDL (VHDL-01)

```
::METADATA::
tipo: indice-soluciones
tema: vhdl-01-introduccion
actualizado: 2026-01-03
::END::
```

## Estructura de Niveles de Solución

| Nivel | Archivo | Contenido |
|-------|---------|-----------|
| 1️⃣ | [`VHDL-01-Respuestas.md`](../VHDL-01-Respuestas.md) | Solo respuestas finales |
| 2️⃣ | Esta carpeta `prob-01/` | Soluciones paso a paso |
| 3️⃣ | Secciones "Conceptos Clave" | Explicación profunda del método |

---

## Índice de Soluciones Detalladas

### Nivel 1: Conceptos Básicos ⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 1.1 | Historia y estándares VHDL | [VHDL-01-Sol-Problema-1.1.md](VHDL-01-Sol-Problema-1.1.md) | ⭐ |
| 1.2 | Verdadero/Falso conceptos | [VHDL-01-Sol-Problema-1.2.md](VHDL-01-Sol-Problema-1.2.md) | ⭐ |
| 1.3 | Identificadores válidos | [VHDL-01-Sol-Problema-1.3.md](VHDL-01-Sol-Problema-1.3.md) | ⭐ |

### Nivel 2: Tipos de Datos ⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 2.1 | Valores de std_logic | [VHDL-01-Sol-Problema-2.1.md](VHDL-01-Sol-Problema-2.1.md) | ⭐⭐ |
| 2.2 | Declaración de señales | [VHDL-01-Sol-Problema-2.2.md](VHDL-01-Sol-Problema-2.2.md) | ⭐⭐ |
| 2.3 | downto vs to | [VHDL-01-Sol-Problema-2.3.md](VHDL-01-Sol-Problema-2.3.md) | ⭐⭐ |

### Nivel 3: Estructura de Archivos ⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 3.1 | Orden de secciones | [VHDL-01-Sol-Problema-3.1.md](VHDL-01-Sol-Problema-3.1.md) | ⭐⭐ |
| 3.2 | Completar código OR | [VHDL-01-Sol-Problema-3.2.md](VHDL-01-Sol-Problema-3.2.md) | ⭐⭐ |

---

## Clasificación de Dificultad VHDL

| Nivel | Símbolo | Descripción | Temas |
|:-----:|:-------:|-------------|-------|
| 1 | ⭐ | Básico | Conceptos, historia, sintaxis |
| 2 | ⭐⭐ | Intermedio | Tipos, señales, estructura |
| 3 | ⭐⭐⭐ | Avanzado | Código completo, debugging |

---

## Referencia Rápida VHDL

### Estructura Básica de Archivo

```vhdl
-- 1. Bibliotecas
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- 2. Entidad (interfaz)
entity nombre is
    port (
        entrada : in  std_logic;
        salida  : out std_logic
    );
end entity;

-- 3. Arquitectura (comportamiento)
architecture behavioral of nombre is
begin
    -- Código aquí
end architecture;
```

### Valores de std_logic (IEEE 1164)

| Valor | Significado | Uso |
|:-----:|-------------|-----|
| 'U' | No inicializado | Simulación |
| 'X' | Forzado desconocido | Conflicto |
| '0' | Forzado bajo | Lógica |
| '1' | Forzado alto | Lógica |
| 'Z' | Alta impedancia | Tri-state |
| 'W' | Débil desconocido | Pull |
| 'L' | Débil bajo | Pull-down |
| 'H' | Débil alto | Pull-up |
| '-' | Don't care | Síntesis |

---

## Navegación

| ⬅️ Respuestas | 🏠 Intro | ➡️ Problemas |
|:-------------:|:--------:|:------------:|
| [VHDL-01-Respuestas.md](../VHDL-01-Respuestas.md) | [VHDL-01-Intro.md](../../VHDL-01-Intro.md) | [VHDL-01-Problemas.md](../../problems/VHDL-01-Problemas.md) |
