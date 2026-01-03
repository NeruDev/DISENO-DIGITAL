<!--
::METADATA::
type: solution
topic_id: vhdl-07-sintesis-simulacion
file_id: respuestas-sintesis-simulacion
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [respuestas, soluciones, VHDL, síntesis, testbench]
search_keywords: "respuestas, soluciones, síntesis, testbench"
-->

> 🏠 **Navegación:** [← Problemas](../problems/VHDL-07-Problemas.md)

---

# Respuestas: Síntesis y Simulación

## Nivel 1: Conceptos Básicos

### Respuesta 1.1

**Simulación Funcional:**
- Verifica comportamiento lógico
- Sin retardos (o retardos delta)
- Rápida
- Pre-síntesis

**Simulación Temporal (Post-layout):**
- Incluye retardos reales
- Verifica timing
- Más lenta
- Post place & route

### Respuesta 1.2

`real` no es sintetizable porque:
- Requiere representación de punto flotante
- No tiene correspondencia directa en hardware digital
- El hardware para floating-point es muy complejo

### Respuesta 1.3

Se infiere un **flip-flop con enable**:
- `q` es un flip-flop D
- `en` es la señal de habilitación
- Cuando `en='0'`, `q` mantiene su valor

---

## Nivel 2: Testbench Básico

### Respuesta 2.1

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_inverter is
end entity;

architecture sim of tb_inverter is
    signal a, y : std_logic;
begin
    -- DUT
    UUT: entity work.inverter
        port map (a => a, y => y);
    
    -- Estímulos
    process
    begin
        a <= '0';
        wait for 10 ns;
        assert y = '1' report "Error: 0 -> no produce 1" severity error;
        
        a <= '1';
        wait for 10 ns;
        assert y = '0' report "Error: 1 -> no produce 0" severity error;
        
        report "Test completado";
        wait;
    end process;
end architecture;
```

### Respuesta 2.2

```vhdl
constant CLK_PERIOD : time := 10 ns;  -- 100 MHz = 10 ns período
signal clk : std_logic := '0';

-- Opción 1
clk <= not clk after CLK_PERIOD / 2;

-- Opción 2
CLK_GEN: process
begin
    clk <= '0';
    wait for 5 ns;
    clk <= '1';
    wait for 5 ns;
end process;
```

### Respuesta 2.3

```vhdl
signal reset : std_logic := '1';

RESET_GEN: process
begin
    reset <= '1';
    wait for 200 ns;
    reset <= '0';
    wait;  -- Proceso termina
end process;
```

---

## Nivel 3: Generadores de Estímulos

### Respuesta 3.1

```vhdl
signal counter_out : std_logic_vector(2 downto 0);

STIM: process
begin
    wait for 100 ns;  -- Esperar reset
    
    for i in 0 to 7 loop
        counter_out <= std_logic_vector(to_unsigned(i, 3));
        wait for CLK_PERIOD;
    end loop;
    
    wait;
end process;
```

### Respuesta 3.2

```vhdl
-- VHDL no tiene rand() nativo
-- Opciones:
-- 1. Usar LFSR (Linear Feedback Shift Register)
-- 2. Usar ieee.math_real.uniform (solo simulación)

use ieee.math_real.all;

process
    variable seed1, seed2 : positive := 1;
    variable rand_val : real;
    variable rand_int : integer;
begin
    uniform(seed1, seed2, rand_val);  -- 0.0 a 1.0
    rand_int := integer(rand_val * 255.0);
    data <= std_logic_vector(to_unsigned(rand_int, 8));
    wait for CLK_PERIOD;
end process;
```

---

## Nivel 4: Verificación con Assert

### Respuesta 4.1

```vhdl
-- Sumador de 4 bits: a + b = sum
process
    variable expected : unsigned(4 downto 0);
begin
    -- Test
    a <= "0101";  -- 5
    b <= "0011";  -- 3
    wait for 10 ns;
    
    expected := unsigned('0' & a) + unsigned('0' & b);
    
    assert unsigned(sum) = expected
        report "Suma incorrecta: " & 
               integer'image(to_integer(unsigned(a))) & " + " &
               integer'image(to_integer(unsigned(b))) & " = " &
               integer'image(to_integer(unsigned(sum))) &
               " (esperado: " & integer'image(to_integer(expected)) & ")"
        severity error;
    wait;
end process;
```

### Respuesta 4.2

```vhdl
-- Verificar reset
process
begin
    reset <= '1';
    wait for CLK_PERIOD;
    assert output = '0' report "Reset no funciona" severity error;
    reset <= '0';
    
    -- Aplicar entrada
    input <= '1';
    wait for CLK_PERIOD;
    wait for CLK_PERIOD;
    wait for CLK_PERIOD;
    assert valid_out = '1' 
        report "Salida no aparece después de 3 ciclos" 
        severity error;
    wait;
end process;
```

### Respuesta 4.3

- `severity error`: Reporta error pero la simulación **continúa**
- `severity failure`: Reporta error y la simulación puede **detenerse** (depende del simulador)

---

## Nivel 5: Código Sintetizable

### Respuesta 5.1

```vhdl
signal a, b, c : real;        -- ❌ NO sintetizable
signal d : std_logic;         -- ✅ OK
signal e : integer range 0 to 100;  -- ✅ OK

process(clk)
begin
    if rising_edge(clk) then
        c <= a + b;           -- ❌ NO (real)
        wait for 10 ns;       -- ❌ NO (wait en proceso síncrono)
        d <= '1';             -- ✅ OK
        e <= e / 2;           -- ⚠️ OK si es potencia de 2
    end if;
end process;
```

### Respuesta 5.2

```vhdl
process(sel, a, b, c, d)
begin
    y <= d;  -- Default (o cualquier valor)
    case sel is
        when "00" => y <= a;
        when "01" => y <= b;
        when "10" => y <= c;
        when others => y <= d;  -- ¡Agregar others!
    end case;
end process;
```

### Respuesta 5.3

Falta `c` en la lista de sensibilidad:

```vhdl
process(a, b, c)  -- Agregar c
begin
    if c = '1' then
        y <= a and b;
    else
        y <= a or b;
    end if;
end process;
```

---

## Nivel 6: Testbench para FSM

### Respuesta 6.1

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_fsm is
end entity;

architecture sim of tb_fsm is
    type state_type is (IDLE, RUN, DONE);
    signal clk, reset, start, finish : std_logic := '0';
    signal current_state : state_type;
    
    constant CLK_PERIOD : time := 10 ns;
begin
    UUT: entity work.my_fsm
        port map (
            clk => clk,
            reset => reset,
            start => start,
            finish => finish,
            state_out => current_state
        );
    
    clk <= not clk after CLK_PERIOD / 2;
    
    STIM: process
    begin
        -- Reset inicial
        reset <= '1';
        wait for 2 * CLK_PERIOD;
        assert current_state = IDLE report "Reset a IDLE falló" severity error;
        reset <= '0';
        
        -- IDLE -> RUN
        start <= '1';
        wait for CLK_PERIOD;
        start <= '0';
        wait for CLK_PERIOD;
        assert current_state = RUN report "Transición IDLE->RUN falló" severity error;
        
        -- RUN -> DONE
        finish <= '1';
        wait for CLK_PERIOD;
        finish <= '0';
        wait for CLK_PERIOD;
        assert current_state = DONE report "Transición RUN->DONE falló" severity error;
        
        -- Test reset desde RUN
        start <= '1';
        wait for 2 * CLK_PERIOD;
        reset <= '1';
        wait for CLK_PERIOD;
        assert current_state = IDLE report "Reset desde RUN falló" severity error;
        reset <= '0';
        
        report "Todos los tests de FSM pasaron";
        wait;
    end process;
end architecture;
```

---

## Nivel 7: Procedimientos en Testbench

### Respuesta 7.1

```vhdl
procedure apply_reset(
    signal reset : out std_logic;
    signal clk : in std_logic;
    constant num_cycles : positive := 2
) is
begin
    reset <= '1';
    for i in 1 to num_cycles loop
        wait until rising_edge(clk);
    end loop;
    reset <= '0';
end procedure;

-- Uso:
apply_reset(reset, clk, 5);
```

### Respuesta 7.2

```vhdl
procedure send_uart_byte(
    signal tx : out std_logic;
    constant byte_val : std_logic_vector(7 downto 0);
    constant baud_period : time := 104.17 us  -- 9600 baud
) is
begin
    -- Start bit
    tx <= '0';
    wait for baud_period;
    
    -- Data bits (LSB first)
    for i in 0 to 7 loop
        tx <= byte_val(i);
        wait for baud_period;
    end loop;
    
    -- Stop bit
    tx <= '1';
    wait for baud_period;
end procedure;
```

---

## Nivel 8: Análisis de Síntesis

### Respuesta 8.1

Problema: `next_state` no tiene valor default en IDLE cuando `input='0'`.

```vhdl
process(state, input)
begin
    -- Agregar defaults
    next_state <= state;  -- ¡Agregar!
    output <= '0';
    
    case state is
        when IDLE =>
            if input = '1' then
                next_state <= RUN;
            end if;
        when RUN =>
            output <= '1';
            next_state <= IDLE;
        when others =>
            next_state <= IDLE;  -- ¡Agregar!
    end case;
end process;
```

### Respuesta 8.2

Recursos:
- 8 flip-flops para `counter`
- 16 flip-flops para `product`
- 1 sumador de 8 bits (counter + 1)
- 1 multiplicador 8x8 (o DSP block)

### Respuesta 8.3

```vhdl
-- Multiplicar por 5 = 4 + 1 = (shift left 2) + original
y <= (a & "00") + ("00" & a);  -- a*4 + a = a*5
-- Evita multiplicador, usa solo shift y sumador
```

---

## Nivel 9: Simulación Avanzada

### Respuesta 9.1

```vhdl
architecture sim of tb is
    shared variable test_count : integer := 0;
    shared variable error_count : integer := 0;
begin
    -- ... DUT ...
    
    CHECKER: process
    begin
        wait until valid_out = '1';
        test_count := test_count + 1;
        
        if actual /= expected then
            error_count := error_count + 1;
            report "Test " & integer'image(test_count) & " FALLÓ";
        end if;
    end process;
    
    FINAL: process
    begin
        wait for 1 ms;  -- Tiempo total de simulación
        
        report "==== REPORTE FINAL ====";
        report "Tests ejecutados: " & integer'image(test_count);
        report "Errores: " & integer'image(error_count);
        
        if error_count = 0 then
            report "*** TODOS LOS TESTS PASARON ***" severity note;
        else
            report "*** HAY ERRORES ***" severity error;
        end if;
        
        std.env.stop;  -- VHDL-2008
    end process;
end architecture;
```

### Respuesta 9.2

```vhdl
TIMEOUT: process
begin
    wait for 10 ms;  -- Timeout
    report "TIMEOUT: Simulación excedió tiempo límite" severity failure;
end process;
```

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para ejercicios de síntesis y simulación
NOTA: Pueden existir soluciones alternativas válidas
-->
