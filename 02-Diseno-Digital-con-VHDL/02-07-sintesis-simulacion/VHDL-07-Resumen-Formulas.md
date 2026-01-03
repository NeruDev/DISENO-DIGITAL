<!--
::METADATA::
type: reference
topic_id: vhdl-07-sintesis-simulacion
file_id: resumen-sintesis-simulacion
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [cheatsheet, VHDL, síntesis, simulación, testbench]
search_keywords: "resumen, síntesis, simulación, testbench, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./02-07-Intro.md)

---

# 📋 Cheatsheet: Síntesis y Simulación

## Código Sintetizable vs No Sintetizable

| ✅ Sintetizable | ❌ No Sintetizable |
|-----------------|-------------------|
| `std_logic`, `unsigned` | `real`, `file` |
| `if`, `case`, `for` | `wait for X ns` |
| `rising_edge(clk)` | Múltiples relojes |
| Operaciones +, -, * | División por variable |
| `after` (ignorado) | `report`, `assert` |

---

## Plantilla Testbench

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_dut is
end entity;

architecture sim of tb_dut is
    constant CLK_PERIOD : time := 10 ns;
    signal clk : std_logic := '0';
    signal reset : std_logic := '1';
begin
    -- DUT
    UUT: entity work.design
        port map (clk => clk, reset => reset);
    
    -- Reloj
    clk <= not clk after CLK_PERIOD/2;
    
    -- Estímulos
    STIM: process
    begin
        reset <= '1';
        wait for 100 ns;
        reset <= '0';
        -- Tests aquí
        wait;
    end process;
end architecture;
```

---

## Generadores

### Reloj
```vhdl
clk <= not clk after CLK_PERIOD/2;
```

### Reset
```vhdl
process begin
    reset <= '1';
    wait for 100 ns;
    reset <= '0';
    wait;
end process;
```

---

## Assert

```vhdl
assert condición
    report "mensaje"
    severity note|warning|error|failure;
```

### Ejemplo
```vhdl
assert output = expected
    report "Error: esperado " & to_hstring(expected)
    severity error;
```

---

## Evitar Latches

```vhdl
process(all_inputs)
begin
    -- DEFAULT PRIMERO
    output <= '0';
    
    if condition then
        output <= '1';
    end if;
end process;
```

---

## Inferencia de Hardware

| Código | Hardware |
|--------|----------|
| `rising_edge(clk)` | Flip-flop |
| `when-else` | MUX |
| `case` | Decodificador |
| `+`, `-` | Sumador |
| `*` | Multiplicador/DSP |

---

## Proceso Síncrono Correcto

```vhdl
process(clk, reset)
begin
    if reset = '1' then
        q <= '0';  -- Reset async
    elsif rising_edge(clk) then
        q <= d;    -- Registro
    end if;
end process;
```

---

## Lista de Sensibilidad

| Tipo | Lista |
|------|-------|
| Secuencial | `(clk)` o `(clk, reset)` |
| Combinacional | Todas las entradas leídas |

---

## Warnings Críticos

| Warning | Causa | Solución |
|---------|-------|----------|
| Latch inferred | if sin else | Agregar default |
| Incomplete sensitivity | Lista incompleta | Agregar señales |
| Multi-driven | Múltiples drivers | Revisar diseño |

---

## Procedimiento Útil

```vhdl
procedure wait_cycles(
    signal clk : std_logic;
    n : positive
) is
begin
    for i in 1 to n loop
        wait until rising_edge(clk);
    end loop;
end procedure;
```

---

## Leer Archivo

```vhdl
use std.textio.all;

process
    file f : text open read_mode is "data.txt";
    variable l : line;
    variable val : integer;
begin
    while not endfile(f) loop
        readline(f, l);
        read(l, val);
        -- usar val
    end loop;
    wait;
end process;
```

---

## Detener Simulación

```vhdl
-- VHDL-2008
std.env.stop;

-- O con wait infinito
wait;
```

---

## Comandos ModelSim

```tcl
# Compilar
vcom design.vhd
vcom tb.vhd

# Simular
vsim tb
run -all
```

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante síntesis y verificación
-->
