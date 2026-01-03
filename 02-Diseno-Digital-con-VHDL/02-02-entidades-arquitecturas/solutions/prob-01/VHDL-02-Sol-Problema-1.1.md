<!--
::METADATA::
type: detailed_solution
topic_id: vhdl-02-entidades-arquitecturas
problem_id: 1.1
file_id: solucion-problema-1-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 2
tags: [solucion, VHDL, entidad, NAND]
-->

> 🏠 **Navegación:** [← Índice](./README.md) | [Problema 1.2 →](./VHDL-02-Sol-Problema-1.2.md)

---

# Solución Detallada: Problema 1.1

## Enunciado
Escribir la entidad para una compuerta NAND de 3 entradas.

---

## Paso 1: Especificación

### Tabla de Verdad NAND 3 Entradas

| A | B | C | Y = (ABC)' |
|:-:|:-:|:-:|:----------:|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | **0** |

### Interfaz Requerida

| Puerto | Dirección | Tipo | Descripción |
|--------|:---------:|------|-------------|
| A | in | std_logic | Entrada 1 |
| B | in | std_logic | Entrada 2 |
| C | in | std_logic | Entrada 3 |
| Y | out | std_logic | Salida NAND |

---

## Paso 2: Solución - Entidad

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity nand3_gate is
    port (
        A : in  std_logic;
        B : in  std_logic;
        C : in  std_logic;
        Y : out std_logic
    );
end entity nand3_gate;
```

---

## Paso 3: Arquitectura (Bonus)

### Opción 1: Dataflow (Directa)

```vhdl
architecture dataflow of nand3_gate is
begin
    Y <= not (A and B and C);
end architecture dataflow;
```

### Opción 2: Dataflow (Operador NAND)

```vhdl
architecture dataflow_v2 of nand3_gate is
begin
    Y <= A nand B nand C;  -- ⚠️ Cuidado: asociatividad
end architecture dataflow_v2;
```

> ⚠️ **Nota:** `A nand B nand C` se evalúa como `(A nand B) nand C`, que NO es igual a `not(A and B and C)`. Usar la primera opción.

### Opción 3: Behavioral (Proceso)

```vhdl
architecture behavioral of nand3_gate is
begin
    process(A, B, C)
    begin
        if A = '1' and B = '1' and C = '1' then
            Y <= '0';
        else
            Y <= '1';
        end if;
    end process;
end architecture behavioral;
```

---

## Paso 4: Código Completo

```vhdl
--------------------------------------------------------------------------------
-- Archivo: nand3_gate.vhd
-- Descripción: Compuerta NAND de 3 entradas
-- Autor: [Estudiante]
-- Fecha: 2026-01-03
--------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity nand3_gate is
    port (
        A : in  std_logic;  -- Entrada 1
        B : in  std_logic;  -- Entrada 2
        C : in  std_logic;  -- Entrada 3
        Y : out std_logic   -- Salida NAND
    );
end entity nand3_gate;

architecture dataflow of nand3_gate is
begin
    Y <= not (A and B and C);
end architecture dataflow;
```

---

## Paso 5: Testbench (Verificación)

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity nand3_gate_tb is
end entity nand3_gate_tb;

architecture test of nand3_gate_tb is
    signal A, B, C, Y : std_logic;
begin
    -- Instancia del DUT
    DUT: entity work.nand3_gate
        port map (A => A, B => B, C => C, Y => Y);
    
    -- Estímulos
    process
    begin
        A <= '0'; B <= '0'; C <= '0'; wait for 10 ns;
        A <= '0'; B <= '0'; C <= '1'; wait for 10 ns;
        A <= '0'; B <= '1'; C <= '0'; wait for 10 ns;
        A <= '0'; B <= '1'; C <= '1'; wait for 10 ns;
        A <= '1'; B <= '0'; C <= '0'; wait for 10 ns;
        A <= '1'; B <= '0'; C <= '1'; wait for 10 ns;
        A <= '1'; B <= '1'; C <= '0'; wait for 10 ns;
        A <= '1'; B <= '1'; C <= '1'; wait for 10 ns;
        wait;
    end process;
end architecture test;
```

---

## Alternativa: Versión Genérica

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity nand_n is
    generic (
        N : positive := 3  -- Número de entradas
    );
    port (
        inputs : in  std_logic_vector(N-1 downto 0);
        Y      : out std_logic
    );
end entity nand_n;

architecture dataflow of nand_n is
begin
    Y <= not (and inputs);  -- VHDL-2008: reducción AND
end architecture dataflow;
```

---

## Conceptos Clave

| Concepto | Aplicación |
|----------|------------|
| Entidad | Define interfaz (puertos) |
| Puertos `in` | Entradas, solo lectura |
| Puerto `out` | Salida, solo escritura |
| `std_logic` | Tipo estándar para 1 bit |
| `not`, `and` | Operadores lógicos |

---

## Errores Comunes

| Error | Problema | Solución |
|-------|----------|----------|
| Olvidar `library IEEE` | Tipo no reconocido | Agregar declaración |
| Usar `nand` en cascada | Resultado incorrecto | Usar `not(and...)` |
| Puerto sin modo | Error de sintaxis | Especificar `in`/`out` |
| Falta `;` en último puerto | Error de sintaxis | Verificar puntuación |

---

> 💡 **Tip:** La compuerta NAND es universal: cualquier función lógica puede implementarse usando solo NANDs.
