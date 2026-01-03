<!--
::METADATA::
type: detailed_solution
topic_id: vhdl-02-entidades-arquitecturas
problem_id: 1.2
file_id: solucion-problema-1-2
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 2
tags: [solucion, VHDL, entidad, multiplexor, MUX]
-->

> 🏠 **Navegación:** [← Problema 1.1](./VHDL-02-Sol-Problema-1.1.md) | [Problema 1.3 →](./VHDL-02-Sol-Problema-1.3.md)

---

# Solución Detallada: Problema 1.2

## Enunciado
Escribir la entidad para un multiplexor 4:1 con:
- 4 entradas de datos de 8 bits
- Selector de 2 bits
- 1 salida de 8 bits

---

## Paso 1: Especificación

### Diagrama de Bloques

```
            ┌─────────────┐
  D0[7:0] ──┤             │
  D1[7:0] ──┤   MUX 4:1   ├── Y[7:0]
  D2[7:0] ──┤    8-bit    │
  D3[7:0] ──┤             │
            └──────┬──────┘
                   │
            SEL[1:0]
```

### Tabla de Funcionamiento

| SEL[1:0] | Y[7:0] |
|:--------:|:------:|
| 00 | D0 |
| 01 | D1 |
| 10 | D2 |
| 11 | D3 |

### Listado de Puertos

| Puerto | Dirección | Ancho | Descripción |
|--------|:---------:|:-----:|-------------|
| D0 | in | 8 bits | Entrada de datos 0 |
| D1 | in | 8 bits | Entrada de datos 1 |
| D2 | in | 8 bits | Entrada de datos 2 |
| D3 | in | 8 bits | Entrada de datos 3 |
| SEL | in | 2 bits | Selector |
| Y | out | 8 bits | Salida |

---

## Paso 2: Solución - Entidad

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux4to1_8bit is
    port (
        D0  : in  std_logic_vector(7 downto 0);  -- Entrada 0
        D1  : in  std_logic_vector(7 downto 0);  -- Entrada 1
        D2  : in  std_logic_vector(7 downto 0);  -- Entrada 2
        D3  : in  std_logic_vector(7 downto 0);  -- Entrada 3
        SEL : in  std_logic_vector(1 downto 0);  -- Selector
        Y   : out std_logic_vector(7 downto 0)   -- Salida
    );
end entity mux4to1_8bit;
```

---

## Paso 3: Arquitecturas Posibles

### Opción 1: Con WITH-SELECT (Dataflow)

```vhdl
architecture dataflow of mux4to1_8bit is
begin
    with SEL select
        Y <= D0 when "00",
             D1 when "01",
             D2 when "10",
             D3 when "11",
             (others => 'X') when others;
end architecture dataflow;
```

### Opción 2: Con WHEN-ELSE (Dataflow)

```vhdl
architecture dataflow_v2 of mux4to1_8bit is
begin
    Y <= D0 when SEL = "00" else
         D1 when SEL = "01" else
         D2 when SEL = "10" else
         D3 when SEL = "11" else
         (others => 'X');
end architecture dataflow_v2;
```

### Opción 3: Con CASE (Behavioral)

```vhdl
architecture behavioral of mux4to1_8bit is
begin
    process(D0, D1, D2, D3, SEL)
    begin
        case SEL is
            when "00"   => Y <= D0;
            when "01"   => Y <= D1;
            when "10"   => Y <= D2;
            when "11"   => Y <= D3;
            when others => Y <= (others => 'X');
        end case;
    end process;
end architecture behavioral;
```

---

## Paso 4: Código Completo

```vhdl
--------------------------------------------------------------------------------
-- Archivo: mux4to1_8bit.vhd
-- Descripción: Multiplexor 4:1 de 8 bits
-- Autor: [Estudiante]
-- Fecha: 2026-01-03
--------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux4to1_8bit is
    port (
        D0  : in  std_logic_vector(7 downto 0);
        D1  : in  std_logic_vector(7 downto 0);
        D2  : in  std_logic_vector(7 downto 0);
        D3  : in  std_logic_vector(7 downto 0);
        SEL : in  std_logic_vector(1 downto 0);
        Y   : out std_logic_vector(7 downto 0)
    );
end entity mux4to1_8bit;

architecture dataflow of mux4to1_8bit is
begin
    with SEL select
        Y <= D0 when "00",
             D1 when "01",
             D2 when "10",
             D3 when others;  -- Incluye "11" y metavalores
end architecture dataflow;
```

---

## Paso 5: Versión Genérica (Avanzado)

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity mux_generic is
    generic (
        WIDTH     : positive := 8;   -- Ancho de datos
        SEL_WIDTH : positive := 2    -- Ancho de selector (2^SEL_WIDTH entradas)
    );
    port (
        data_in : in  std_logic_vector((2**SEL_WIDTH)*WIDTH-1 downto 0);
        sel     : in  std_logic_vector(SEL_WIDTH-1 downto 0);
        data_out: out std_logic_vector(WIDTH-1 downto 0)
    );
end entity mux_generic;

architecture behavioral of mux_generic is
begin
    process(data_in, sel)
        variable idx : integer;
    begin
        idx := to_integer(unsigned(sel));
        data_out <= data_in((idx+1)*WIDTH-1 downto idx*WIDTH);
    end process;
end architecture behavioral;
```

---

## Verificación

### Testbench

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux4to1_8bit_tb is
end entity;

architecture test of mux4to1_8bit_tb is
    signal D0, D1, D2, D3, Y : std_logic_vector(7 downto 0);
    signal SEL : std_logic_vector(1 downto 0);
begin
    DUT: entity work.mux4to1_8bit
        port map (D0, D1, D2, D3, SEL, Y);
    
    process
    begin
        D0 <= x"AA"; D1 <= x"BB"; D2 <= x"CC"; D3 <= x"DD";
        
        SEL <= "00"; wait for 10 ns;  -- Y = AA
        assert Y = x"AA" report "Error SEL=00" severity error;
        
        SEL <= "01"; wait for 10 ns;  -- Y = BB
        assert Y = x"BB" report "Error SEL=01" severity error;
        
        SEL <= "10"; wait for 10 ns;  -- Y = CC
        assert Y = x"CC" report "Error SEL=10" severity error;
        
        SEL <= "11"; wait for 10 ns;  -- Y = DD
        assert Y = x"DD" report "Error SEL=11" severity error;
        
        report "Test completado exitosamente" severity note;
        wait;
    end process;
end architecture test;
```

---

## Conceptos Clave

| Concepto | Aplicación |
|----------|------------|
| `std_logic_vector` | Buses de n bits |
| `downto` | Orden MSB a LSB (convención) |
| `with-select` | Selección concurrente |
| `when others` | Manejo de metavalores |
| `(others => 'X')` | Agregado para vectores |

---

## Comparación de Estilos

| Estilo | Ventaja | Desventaja |
|--------|---------|------------|
| `with-select` | Compacto, claro | Solo un selector |
| `when-else` | Prioridad implícita | Más verbose |
| `case` en proceso | Flexible | Más código |

---

> 💡 **Tip:** Para MUX combinacionales, `with-select` es la forma más legible. Para lógica con prioridad, usar `when-else`.
