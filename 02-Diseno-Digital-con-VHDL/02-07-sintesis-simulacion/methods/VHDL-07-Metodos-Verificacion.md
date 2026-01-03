<!--
::METADATA::
type: method
topic_id: vhdl-07-sintesis-simulacion
file_id: metodos-verificacion
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [VHDL, metodología, testbench, verificación, síntesis]
search_keywords: "metodología testbench, verificación, síntesis"
-->

> 🏠 **Navegación:** [← Teoría](../theory/VHDL-07-Teoria-SintesisSimulacion.md) | [Problemas →](../problems/VHDL-07-Problemas.md)

---

# Métodos: Síntesis y Verificación

## Método 1: Plantilla de Testbench Básico

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_design is
end entity;

architecture sim of tb_design is
    -- Constantes
    constant CLK_PERIOD : time := 10 ns;
    
    -- Señales
    signal clk   : std_logic := '0';
    signal reset : std_logic := '1';
    signal done  : boolean := false;
    
    -- Señales específicas del DUT
    signal input1, input2 : std_logic;
    signal output1 : std_logic;
    
begin
    -- DUT
    UUT: entity work.my_design
        port map (
            clk => clk,
            reset => reset,
            input1 => input1,
            input2 => input2,
            output1 => output1
        );
    
    -- Reloj (se detiene con 'done')
    clk <= not clk after CLK_PERIOD/2 when not done else '0';
    
    -- Estímulos
    STIM: process
    begin
        -- Reset
        reset <= '1';
        input1 <= '0';
        input2 <= '0';
        wait for 5 * CLK_PERIOD;
        reset <= '0';
        
        -- Test 1
        input1 <= '1';
        wait for CLK_PERIOD;
        assert output1 = '1' report "Test 1 falló" severity error;
        
        -- Test 2
        input1 <= '0';
        input2 <= '1';
        wait for CLK_PERIOD;
        
        -- Finalizar
        done <= true;
        report "Simulación completada";
        wait;
    end process;
    
end architecture;
```

---

## Método 2: Procedimientos Reutilizables

```vhdl
architecture sim of tb is
    -- Procedimiento para esperar ciclos
    procedure wait_cycles(signal clk : std_logic; n : positive) is
    begin
        for i in 1 to n loop
            wait until rising_edge(clk);
        end loop;
    end procedure;
    
    -- Procedimiento para enviar byte
    procedure send_byte(
        signal data : out std_logic_vector(7 downto 0);
        signal valid : out std_logic;
        constant byte_val : std_logic_vector(7 downto 0)
    ) is
    begin
        data <= byte_val;
        valid <= '1';
        wait for CLK_PERIOD;
        valid <= '0';
    end procedure;
    
    -- Procedimiento para verificar
    procedure check_output(
        signal actual : std_logic_vector(7 downto 0);
        constant expected : std_logic_vector(7 downto 0);
        constant test_name : string
    ) is
    begin
        assert actual = expected
            report test_name & ": esperado " & 
                   to_hstring(expected) & " obtenido " & 
                   to_hstring(actual)
            severity error;
    end procedure;
begin
    -- Uso:
    STIM: process
    begin
        wait_cycles(clk, 5);
        send_byte(data_in, valid_in, x"A5");
        wait_cycles(clk, 10);
        check_output(data_out, x"5A", "Test inversión");
        wait;
    end process;
end architecture;
```

---

## Método 3: Verificación Automática con Vectores

```vhdl
type test_vector is record
    input_a : std_logic_vector(3 downto 0);
    input_b : std_logic_vector(3 downto 0);
    expected : std_logic_vector(4 downto 0);
end record;

type test_array is array (natural range <>) of test_vector;

constant TESTS : test_array := (
    (x"0", x"0", "00000"),
    (x"1", x"1", "00010"),
    (x"F", x"1", "10000"),
    (x"A", x"5", "01111")
);

STIM: process
begin
    wait for 100 ns;  -- Reset
    
    for i in TESTS'range loop
        a <= TESTS(i).input_a;
        b <= TESTS(i).input_b;
        wait for CLK_PERIOD;
        
        assert result = TESTS(i).expected
            report "Test " & integer'image(i) & " falló"
            severity error;
    end loop;
    
    report "Todos los tests pasaron";
    wait;
end process;
```

---

## Método 4: Lectura de Archivos de Test

```vhdl
use std.textio.all;
use ieee.std_logic_textio.all;

STIM: process
    file test_file : text open read_mode is "test_vectors.txt";
    variable l : line;
    variable input_val : std_logic_vector(7 downto 0);
    variable expected_val : std_logic_vector(7 downto 0);
    variable test_num : integer := 0;
begin
    wait for 100 ns;  -- Reset
    
    while not endfile(test_file) loop
        readline(test_file, l);
        
        -- Saltar comentarios
        if l'length > 0 and l(1) /= '#' then
            hread(l, input_val);  -- Leer hex
            hread(l, expected_val);
            
            data_in <= input_val;
            wait for CLK_PERIOD;
            
            assert data_out = expected_val
                report "Test " & integer'image(test_num) & " falló"
                severity error;
            
            test_num := test_num + 1;
        end if;
    end loop;
    
    report "Ejecutados " & integer'image(test_num) & " tests";
    wait;
end process;
```

**Archivo test_vectors.txt:**
```
# input expected
00 00
55 AA
A5 5A
FF 00
```

---

## Método 5: Código Sintetizable - Checklist

### Antes de Síntesis

```vhdl
-- ✅ Usar bibliotecas estándar
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;  -- Preferir sobre std_logic_arith

-- ✅ Evitar inicialización de señales (para ASIC)
signal counter : unsigned(7 downto 0);  -- Sin := "00000000"

-- ✅ Un solo reloj por proceso
process(clk)
begin
    if rising_edge(clk) then
        -- Toda la lógica síncrona aquí
    end if;
end process;

-- ✅ Reset completo
process(clk, reset)
begin
    if reset = '1' then
        q <= (others => '0');  -- Inicializar TODO
    elsif rising_edge(clk) then
        q <= d;
    end if;
end process;
```

---

## Método 6: Evitar Latches

```vhdl
-- ❌ Genera latch
process(sel, a, b)
begin
    if sel = '1' then
        y <= a;
    end if;  -- ¿Qué pasa cuando sel='0'?
end process;

-- ✅ Sin latch
process(sel, a, b)
begin
    y <= b;  -- Default primero
    if sel = '1' then
        y <= a;
    end if;
end process;

-- ✅ Alternativa: else explícito
process(sel, a, b)
begin
    if sel = '1' then
        y <= a;
    else
        y <= b;
    end if;
end process;
```

---

## Método 7: Separar Lógica Combinacional y Secuencial

```vhdl
-- Proceso secuencial (simple)
SEQ: process(clk, reset)
begin
    if reset = '1' then
        state <= IDLE;
        data_reg <= (others => '0');
    elsif rising_edge(clk) then
        state <= next_state;
        data_reg <= next_data;
    end if;
end process;

-- Proceso combinacional (toda la lógica)
COMB: process(state, input, data_reg)
begin
    -- Defaults
    next_state <= state;
    next_data <= data_reg;
    output <= '0';
    
    -- Lógica
    case state is
        when IDLE =>
            if input = '1' then
                next_state <= RUN;
                next_data <= input_data;
            end if;
        when RUN =>
            output <= '1';
            next_state <= IDLE;
    end case;
end process;
```

---

## Método 8: Verificar Warnings de Síntesis

### Warnings Críticos

| Warning | Causa | Solución |
|---------|-------|----------|
| "Latch inferred" | if sin else | Agregar default |
| "Signal not in sensitivity list" | Lista incompleta | Agregar señal |
| "Combinational loop" | Feedback | Rediseñar |
| "Multi-driven net" | Múltiples drivers | Usar tri-state o MUX |

### Script de Verificación

```tcl
# En Vivado TCL
set warnings [get_msg_config -severity {WARNING} -count]
if {$warnings > 0} {
    puts "ATENCIÓN: $warnings warnings de síntesis"
}
```

---

## Método 9: Testbench Auto-verificante

```vhdl
architecture sim of tb is
    signal error_count : integer := 0;
    signal test_count : integer := 0;
begin
    -- ... DUT y estímulos ...
    
    CHECKER: process
    begin
        wait until rising_edge(clk);
        
        if valid_out = '1' then
            test_count <= test_count + 1;
            
            if data_out /= expected then
                error_count <= error_count + 1;
                report "ERROR en test " & integer'image(test_count);
            end if;
        end if;
    end process;
    
    -- Reporte final
    REPORT_FINAL: process
    begin
        wait until done = '1';
        
        report "============================";
        report "Tests ejecutados: " & integer'image(test_count);
        report "Errores: " & integer'image(error_count);
        
        if error_count = 0 then
            report "TODOS LOS TESTS PASARON" severity note;
        else
            report "TESTS FALLARON" severity error;
        end if;
        
        wait;
    end process;
end architecture;
```

---

## Método 10: Simulación Post-Síntesis

### Flujo de Trabajo

1. **Síntesis:** Generar netlist
2. **Exportar:** Netlist + SDF (timing)
3. **Simular:** Usar mismo testbench con netlist

```vhdl
-- En testbench post-síntesis
-- Instanciar netlist en lugar de RTL
UUT: entity work.my_design_netlist
    port map (...);

-- Cargar timing (específico de herramienta)
-- ModelSim: vsim -sdfmax /UUT=timing.sdf ...
```

### Verificar Timing

```vhdl
-- Verificar setup time
process(clk)
    variable last_data_change : time := 0 ns;
begin
    if data'event then
        last_data_change := now;
    end if;
    
    if rising_edge(clk) then
        assert (now - last_data_change) >= SETUP_TIME
            report "Setup time violation"
            severity error;
    end if;
end process;
```

---

## Método 11: Depuración Sistemática

### Agregar Señales de Debug

```vhdl
-- En RTL (antes de síntesis)
attribute mark_debug : string;
attribute mark_debug of state : signal is "true";
attribute mark_debug of counter : signal is "true";

-- Alternativa: sacar a puertos de debug
debug_state <= std_logic_vector(to_unsigned(
    state_type'pos(current_state), 4));
```

### ChipScope / ILA (Xilinx)

```vhdl
-- Instantiar ILA
component ila_0
    port (
        clk : in std_logic;
        probe0 : in std_logic_vector(7 downto 0);
        probe1 : in std_logic_vector(3 downto 0)
    );
end component;

DEBUG: ila_0 port map (
    clk => clk,
    probe0 => data_bus,
    probe1 => state_debug
);
```

---

<!-- IA_CONTEXT
USO: Métodos prácticos para síntesis y verificación VHDL
NIVEL: Intermedio (2/3)
HERRAMIENTAS: ModelSim, Vivado, Quartus, GHDL
-->
