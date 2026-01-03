<!--
::METADATA::
type: theory
topic_id: vhdl-07-sintesis-simulacion
file_id: teoria-sintesis-simulacion
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [VHDL, síntesis, simulación, testbench, verificación]
search_keywords: "síntesis, simulación, testbench, timing, verificación"
-->

> 🏠 **Navegación:** [← Volver al Índice](../02-07-Intro.md) | [Métodos →](../methods/VHDL-07-Metodos-Verificacion.md)

---

# Síntesis y Simulación en VHDL

## 1. Flujo de Diseño Digital

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ Especificación│───▶│  Diseño RTL  │───▶│  Simulación  │
│  del Sistema │    │    (VHDL)    │    │  Funcional   │
└──────────────┘    └──────────────┘    └──────┬───────┘
                                               │
        ┌──────────────────────────────────────┘
        ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Síntesis   │───▶│ Place & Route│───▶│  Simulación  │
│              │    │              │    │   Timing     │
└──────────────┘    └──────────────┘    └──────┬───────┘
                                               │
                                               ▼
                                        ┌──────────────┐
                                        │ Programación │
                                        │    FPGA      │
                                        └──────────────┘
```

---

## 2. Síntesis

### 2.1 ¿Qué es la Síntesis?

La **síntesis** traduce código VHDL RTL a una lista de compuertas (netlist).

```
VHDL RTL → Síntesis → Netlist (compuertas) → Mapeo → FPGA/ASIC
```

### 2.2 Subconjunto Sintetizable

**NO todo VHDL es sintetizable:**

| Sintetizable ✅ | No Sintetizable ❌ |
|-----------------|-------------------|
| Tipos estándar | `real`, `file` |
| `if`, `case`, `for` | `wait for 10 ns` |
| Operaciones aritméticas | División por variable |
| Arrays de tamaño fijo | Arrays dinámicos |
| Registros síncronos | Variables compartidas |

### 2.3 Reglas de Código Sintetizable

#### Procesos Síncronos

```vhdl
-- ✅ Sintetizable: flip-flop
process(clk)
begin
    if rising_edge(clk) then
        q <= d;
    end if;
end process;

-- ❌ No sintetizable: múltiples relojes
process(clk1, clk2)
begin
    if rising_edge(clk1) then
        q1 <= d;
    elsif rising_edge(clk2) then
        q2 <= d;
    end if;
end process;
```

#### Reset Asíncrono

```vhdl
-- ✅ Sintetizable: reset async, luego flanco
process(clk, reset)
begin
    if reset = '1' then
        q <= '0';
    elsif rising_edge(clk) then
        q <= d;
    end if;
end process;
```

### 2.4 Inferencia de Hardware

| Código VHDL | Hardware Inferido |
|-------------|-------------------|
| `if rising_edge(clk)` | Flip-flop |
| `when-else` | Multiplexor |
| `+`, `-` | Sumador/Restador |
| `*` | Multiplicador |
| `case` | Decodificador/MUX |
| `for generate` | Lógica replicada |

---

## 3. Simulación Funcional

### 3.1 Propósito

Verificar que el diseño funciona **lógicamente** correcto, sin considerar retardos.

### 3.2 Estructura de un Testbench

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_dut is
    -- Entidad vacía para testbench
end entity;

architecture sim of tb_dut is
    -- Señales de prueba
    signal clk : std_logic := '0';
    signal reset : std_logic := '1';
    signal input : std_logic := '0';
    signal output : std_logic;
    
    -- Constantes
    constant CLK_PERIOD : time := 10 ns;
begin
    -- Instancia del DUT (Design Under Test)
    DUT: entity work.my_design
        port map (
            clk => clk,
            reset => reset,
            input => input,
            output => output
        );
    
    -- Generador de reloj
    clk <= not clk after CLK_PERIOD / 2;
    
    -- Proceso de estímulos
    STIM: process
    begin
        -- Reset inicial
        reset <= '1';
        wait for 20 ns;
        reset <= '0';
        
        -- Caso de prueba 1
        input <= '1';
        wait for 10 ns;
        assert output = '1' report "Error: output debe ser 1" severity error;
        
        -- Caso de prueba 2
        input <= '0';
        wait for 10 ns;
        assert output = '0' report "Error: output debe ser 0" severity error;
        
        -- Fin de simulación
        report "Simulación completada exitosamente";
        wait;  -- Detener el proceso
    end process;
end architecture;
```

---

## 4. Generadores de Estímulos

### 4.1 Reloj

```vhdl
constant CLK_PERIOD : time := 10 ns;

-- Opción 1: Asignación concurrente
clk <= not clk after CLK_PERIOD / 2;

-- Opción 2: Proceso dedicado
CLK_GEN: process
begin
    clk <= '0';
    wait for CLK_PERIOD / 2;
    clk <= '1';
    wait for CLK_PERIOD / 2;
end process;
```

### 4.2 Reset

```vhdl
RESET_GEN: process
begin
    reset <= '1';
    wait for 100 ns;
    reset <= '0';
    wait;  -- Proceso termina aquí
end process;
```

### 4.3 Datos de Prueba

```vhdl
-- Secuencia de datos
STIM: process
begin
    data <= x"00";
    wait for 10 ns;
    data <= x"55";
    wait for 10 ns;
    data <= x"AA";
    wait for 10 ns;
    data <= x"FF";
    wait;
end process;

-- Datos desde archivo
process
    file test_file : text open read_mode is "test_vectors.txt";
    variable line_buf : line;
    variable data_val : std_logic_vector(7 downto 0);
begin
    while not endfile(test_file) loop
        readline(test_file, line_buf);
        read(line_buf, data_val);
        data <= data_val;
        wait for 10 ns;
    end loop;
    wait;
end process;
```

---

## 5. Verificación: Assert

### 5.1 Sintaxis

```vhdl
assert condición
    report "mensaje"
    severity nivel;
```

**Niveles de severidad:**
- `note` - Informativo
- `warning` - Advertencia
- `error` - Error (continúa)
- `failure` - Fallo (puede detener)

### 5.2 Ejemplos

```vhdl
-- Verificar resultado
assert output = expected
    report "Salida incorrecta: esperado=" & 
           std_logic'image(expected) & 
           " obtenido=" & 
           std_logic'image(output)
    severity error;

-- Verificar timing
assert (now - last_edge) >= SETUP_TIME
    report "Violación de setup time"
    severity error;

-- Verificar rango
assert unsigned(data) < 256
    report "Datos fuera de rango"
    severity failure;
```

---

## 6. Simulación Temporal (Post-Síntesis)

### 6.1 Propósito

Verificar que el diseño funciona con **retardos reales** después de place & route.

### 6.2 Modelos de Retardo

```vhdl
-- Retardo inercial (por defecto)
y <= a and b after 5 ns;  -- Pulsos < 5ns se filtran

-- Retardo de transporte
y <= transport a and b after 5 ns;  -- Todos los pulsos pasan
```

### 6.3 SDF Back-annotation

El archivo SDF (Standard Delay Format) contiene retardos reales:

```vhdl
-- En testbench para simulación post-layout
library work;
use work.my_design_post_route;  -- Netlist con timing

-- Cargar SDF
-- (varía según herramienta de simulación)
```

---

## 7. Cobertura de Código

### 7.1 Tipos de Cobertura

| Tipo | Descripción |
|------|-------------|
| Statement | ¿Se ejecutó cada línea? |
| Branch | ¿Se evaluó cada rama if/case? |
| Condition | ¿Se probaron todas las combinaciones? |
| FSM | ¿Se visitaron todos los estados/transiciones? |
| Toggle | ¿Cambiaron todas las señales 0→1 y 1→0? |

### 7.2 Verificación de Estados FSM

```vhdl
-- Verificar transición de estados
process(clk)
begin
    if rising_edge(clk) then
        case current_state is
            when IDLE =>
                assert next_state = IDLE or next_state = RUN
                    report "Transición ilegal desde IDLE"
                    severity error;
            when RUN =>
                -- ...
        end case;
    end if;
end process;
```

---

## 8. Buenas Prácticas de Testbench

### 8.1 Estructura Recomendada

```vhdl
architecture tb of testbench is
    -- 1. Constantes
    constant CLK_PERIOD : time := 10 ns;
    
    -- 2. Señales
    signal clk, reset : std_logic;
    
    -- 3. Procedimientos de utilidad
    procedure wait_cycles(n : integer) is
    begin
        for i in 1 to n loop
            wait until rising_edge(clk);
        end loop;
    end procedure;
    
begin
    -- 4. Instanciación DUT
    
    -- 5. Generadores (clk, reset)
    
    -- 6. Proceso de estímulos
    
    -- 7. Proceso de verificación (checker)
end architecture;
```

### 8.2 Separar Estímulos y Verificación

```vhdl
-- Proceso de estímulos
STIMULUS: process
begin
    -- Generar entradas
    data_in <= x"A5";
    start <= '1';
    wait for CLK_PERIOD;
    start <= '0';
    wait for 10 * CLK_PERIOD;
    -- ...
end process;

-- Proceso de verificación
CHECKER: process
begin
    wait until done = '1';
    assert data_out = EXPECTED_RESULT
        report "Resultado incorrecto"
        severity error;
end process;
```

---

## 9. Herramientas

### 9.1 Simuladores

| Herramienta | Tipo | Notas |
|-------------|------|-------|
| ModelSim | Comercial | Industria estándar |
| GHDL | Open Source | Solo VHDL |
| Vivado Simulator | Comercial | Integrado Xilinx |
| QuestaSim | Comercial | Verificación avanzada |

### 9.2 Sintetizadores

| Herramienta | Vendedor | Target |
|-------------|----------|--------|
| Vivado | Xilinx | FPGA Xilinx |
| Quartus Prime | Intel | FPGA Intel/Altera |
| Synplify | Synopsys | Múltiples |
| Design Compiler | Synopsys | ASIC |

---

## 10. Warnings Comunes de Síntesis

| Warning | Significado | Acción |
|---------|-------------|--------|
| Latch inferred | Latch no intencional | Agregar else/default |
| Multi-driven net | Múltiples drivers | Revisar arquitectura |
| Unused signal | Señal sin uso | Eliminar o verificar |
| Combinational loop | Retroalimentación | Corregir diseño |
| Clock not on dedicated | Reloj en pin normal | Usar pin de reloj |

---

## Referencias

- IEEE Std 1076-2008 (VHDL)
- Xilinx UG901 - Vivado Design Suite User Guide: Synthesis
- Intel Quartus Prime Handbook
- Ashenden, P.J. (2008). *The Designer's Guide to VHDL*

---

<!-- IA_CONTEXT
NIVEL: Intermedio (2/3)
PREREQUISITOS: 02-01 a 02-06
CONEXIONES: Cierra el ciclo de diseño VHDL
ERRORES_COMUNES: Código no sintetizable, testbench incompleto, ignorar warnings
-->
