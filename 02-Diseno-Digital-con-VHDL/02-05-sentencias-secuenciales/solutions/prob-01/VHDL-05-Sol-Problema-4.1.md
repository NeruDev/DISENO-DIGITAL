<!--
::METADATA::
type: detailed_solution
topic_id: vhdl-05-sentencias-secuenciales
problem_id: 4.1
file_id: solucion-problema-4-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 3
tags: [solucion, VHDL, flip-flop, proceso, sincrono]
-->

> 🏠 **Navegación:** [← Índice](./README.md) | [Problema 4.2 →](./VHDL-05-Sol-Problema-4.2.md)

---

# Solución Detallada: Problema 4.1

## Enunciado
Implementar un Flip-Flop D con reset síncrono y asíncrono en VHDL.

---

## Parte A: Flip-Flop D con Reset Síncrono

### Descripción
El reset **síncrono** solo actúa en el flanco de reloj.

### Código VHDL

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ff_d_sync_reset is
    port (
        clk   : in  std_logic;
        reset : in  std_logic;  -- Reset síncrono
        d     : in  std_logic;
        q     : out std_logic
    );
end entity ff_d_sync_reset;

architecture behavioral of ff_d_sync_reset is
begin
    process(clk)  -- Solo clk en lista de sensibilidad
    begin
        if rising_edge(clk) then
            if reset = '1' then
                q <= '0';
            else
                q <= d;
            end if;
        end if;
    end process;
end architecture behavioral;
```

### Diagrama de Timing

```
CLK    ─┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐
        └┘  └┘  └┘  └┘  └┘  └┘  └┘  

RESET  ─────────┐     ┌─────────────
                └─────┘

D      ───┐  ┌──────┐     ┌─────────
          └──┘      └─────┘

Q      ───┐        ┌──────┐     ┌───
          └────────┘      └─────┘
                   ↑
              Reset toma efecto
              en el flanco
```

---

## Parte B: Flip-Flop D con Reset Asíncrono

### Descripción
El reset **asíncrono** actúa inmediatamente, sin esperar el reloj.

### Código VHDL

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ff_d_async_reset is
    port (
        clk   : in  std_logic;
        reset : in  std_logic;  -- Reset asíncrono (activo alto)
        d     : in  std_logic;
        q     : out std_logic
    );
end entity ff_d_async_reset;

architecture behavioral of ff_d_async_reset is
begin
    process(clk, reset)  -- reset EN lista de sensibilidad
    begin
        if reset = '1' then
            q <= '0';  -- Reset inmediato
        elsif rising_edge(clk) then
            q <= d;
        end if;
    end process;
end architecture behavioral;
```

### Diagrama de Timing

```
CLK    ─┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐
        └┘  └┘  └┘  └┘  └┘  └┘  └┘  

RESET  ─────────┐     ┌─────────────
                └─────┘

D      ───┐  ┌──────┐     ┌─────────
          └──┘      └─────┘

Q      ───┐     ┌──────────────┐
          └─────┘              └────
              ↑
         Reset INMEDIATO
         (sin esperar clk)
```

---

## Comparación Síncrono vs Asíncrono

| Característica | Reset Síncrono | Reset Asíncrono |
|----------------|:--------------:|:---------------:|
| Lista de sensibilidad | Solo `clk` | `clk, reset` |
| Timing | En flanco de clk | Inmediato |
| Prioridad | `if` dentro de `rising_edge` | `if` antes de `rising_edge` |
| Recursos FPGA | Puede usar más LUTs | Usa pin async del FF |
| Glitches | Inmune | Susceptible |
| Timing analysis | Más simple | Requiere constraints |

---

## Parte C: Reset Asíncrono Activo Bajo

### Código VHDL

```vhdl
architecture behavioral of ff_d_async_reset_n is
begin
    process(clk, reset_n)  -- reset_n = activo bajo
    begin
        if reset_n = '0' then
            q <= '0';
        elsif rising_edge(clk) then
            q <= d;
        end if;
    end process;
end architecture behavioral;
```

> 💡 **Convención:** Sufijo `_n` indica activo bajo.

---

## Parte D: Registro de N bits

### Código VHDL

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity register_n is
    generic (
        WIDTH : positive := 8
    );
    port (
        clk   : in  std_logic;
        reset : in  std_logic;
        en    : in  std_logic;  -- Enable
        d     : in  std_logic_vector(WIDTH-1 downto 0);
        q     : out std_logic_vector(WIDTH-1 downto 0)
    );
end entity register_n;

architecture behavioral of register_n is
begin
    process(clk, reset)
    begin
        if reset = '1' then
            q <= (others => '0');
        elsif rising_edge(clk) then
            if en = '1' then
                q <= d;
            end if;
        end if;
    end process;
end architecture behavioral;
```

---

## Testbench

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_ff_d is
end entity;

architecture test of tb_ff_d is
    constant CLK_PERIOD : time := 10 ns;
    signal clk, reset, d, q : std_logic;
begin
    -- DUT
    DUT: entity work.ff_d_async_reset
        port map (clk => clk, reset => reset, d => d, q => q);
    
    -- Clock
    clk <= not clk after CLK_PERIOD/2 when now < 200 ns else '0';
    
    -- Estímulos
    process
    begin
        reset <= '1'; d <= '0';
        wait for 25 ns;
        
        reset <= '0';
        wait for 10 ns;
        
        d <= '1';
        wait for 30 ns;
        
        d <= '0';
        wait for 20 ns;
        
        -- Test reset asíncrono
        d <= '1';
        wait for 15 ns;
        reset <= '1';  -- Reset en medio de ciclo
        wait for 5 ns;
        reset <= '0';
        
        wait for 50 ns;
        wait;
    end process;
end architecture;
```

---

## Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| `rising_edge(clk)` | Detecta flanco positivo (VHDL-93+) |
| `clk'event and clk='1'` | Equivalente (VHDL-87) |
| Lista de sensibilidad | Determina tipo de reset |
| `(others => '0')` | Inicializa vector a ceros |
| Enable (`en`) | Retención condicional de valor |

---

## Errores Comunes

| Error | Problema | Solución |
|-------|----------|----------|
| Reset no en sensibilidad | Reset síncrono no deseado | Agregar `reset` a la lista |
| `elsif` vs `else if` | Error de sintaxis | Usar `elsif` |
| Latch inferido | Falta `else` en combinacional | Agregar caso por defecto |
| Múltiples drivers | Señal asignada en varios procesos | Un proceso por señal |

---

> 💡 **Tip:** Para FPGAs modernos, se recomienda reset síncrono por mejor timing. El reset asíncrono es preferido en ASICs y cuando se requiere recovery instantáneo.
