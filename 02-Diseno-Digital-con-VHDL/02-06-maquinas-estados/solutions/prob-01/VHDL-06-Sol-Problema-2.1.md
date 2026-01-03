<!--
::METADATA::
type: detailed_solution
topic_id: vhdl-06-maquinas-estados
problem_id: 2.1
file_id: solucion-problema-2-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 3
tags: [solucion, VHDL, FSM, Moore, detector]
-->

> 🏠 **Navegación:** [← Índice](./README.md) | [Problema 2.2 →](./VHDL-06-Sol-Problema-2.2.md)

---

# Solución Detallada: Problema 2.1

## Enunciado
Diseñar una máquina de estados Moore que detecte la secuencia "101" en una entrada serial.

---

## Paso 1: Análisis del Problema

### Especificaciones
| Parámetro | Valor |
|-----------|-------|
| Tipo de FSM | Moore |
| Secuencia a detectar | "101" |
| Solapamiento | Sí (permite detectar 10101 como 2 secuencias) |
| Salida | '1' cuando se detecta, '0' en otro caso |

### Interfaz

| Puerto | Dirección | Descripción |
|--------|:---------:|-------------|
| clk | in | Reloj |
| reset | in | Reset asíncrono |
| x | in | Entrada serial (1 bit) |
| detected | out | Salida de detección |

---

## Paso 2: Diagrama de Estados

```
                    0
            ┌───────────────┐
            │               │
            ▼               │
        ┌───────┐    1    ┌─┴─────┐    0    ┌───────┐
  ──────┤  S0   ├────────►│  S1   ├────────►│  S10  │
 reset  │ OUT=0 │         │ OUT=0 │         │ OUT=0 │
        └───┬───┘         └───┬───┘         └───┬───┘
            │                 │                 │
            │0                │0                │1
            │                 │                 │
            └─────────────────┘                 │
                                               │
                                               ▼
                                          ┌───────┐
                               ┌──────────┤ S101  │
                               │          │ OUT=1 │
                               │          └───┬───┘
                               │              │
                               │              │0
                               │              ▼
                               │          ┌───────┐
                               └──────────┤  S10  │
                                   1      │ OUT=0 │
                                          └───────┘
```

### Tabla de Transición

| Estado Actual | x=0 | x=1 | Salida |
|:-------------:|:---:|:---:|:------:|
| S0 (inicio) | S0 | S1 | 0 |
| S1 (got "1") | S10 | S1 | 0 |
| S10 (got "10") | S0 | S101 | 0 |
| S101 (got "101") | S10 | S1 | **1** |

---

## Paso 3: Código VHDL

```vhdl
--------------------------------------------------------------------------------
-- Archivo: detector_101.vhd
-- Descripción: Detector de secuencia "101" - FSM Moore
-- Autor: [Estudiante]
-- Fecha: 2026-01-03
--------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity detector_101 is
    port (
        clk      : in  std_logic;
        reset    : in  std_logic;
        x        : in  std_logic;
        detected : out std_logic
    );
end entity detector_101;

architecture moore_fsm of detector_101 is
    -- Definición de estados
    type state_type is (S0, S1, S10, S101);
    signal current_state, next_state : state_type;
    
begin
    ---------------------------------------------------------------------------
    -- Proceso 1: Registro de estado (secuencial)
    ---------------------------------------------------------------------------
    state_register: process(clk, reset)
    begin
        if reset = '1' then
            current_state <= S0;
        elsif rising_edge(clk) then
            current_state <= next_state;
        end if;
    end process state_register;
    
    ---------------------------------------------------------------------------
    -- Proceso 2: Lógica de siguiente estado (combinacional)
    ---------------------------------------------------------------------------
    next_state_logic: process(current_state, x)
    begin
        case current_state is
            when S0 =>
                if x = '1' then
                    next_state <= S1;
                else
                    next_state <= S0;
                end if;
                
            when S1 =>
                if x = '0' then
                    next_state <= S10;
                else
                    next_state <= S1;  -- Mantenerse (111... esperando 0)
                end if;
                
            when S10 =>
                if x = '1' then
                    next_state <= S101;  -- ¡Secuencia detectada!
                else
                    next_state <= S0;    -- Reiniciar
                end if;
                
            when S101 =>
                if x = '0' then
                    next_state <= S10;   -- Solapamiento: "101" -> "10"
                else
                    next_state <= S1;    -- "1011" -> reiniciar con "1"
                end if;
                
            when others =>
                next_state <= S0;
        end case;
    end process next_state_logic;
    
    ---------------------------------------------------------------------------
    -- Proceso 3: Lógica de salida Moore (solo depende del estado)
    ---------------------------------------------------------------------------
    output_logic: process(current_state)
    begin
        case current_state is
            when S101   => detected <= '1';
            when others => detected <= '0';
        end case;
    end process output_logic;
    
end architecture moore_fsm;
```

---

## Paso 4: Alternativa - Un Solo Proceso

```vhdl
architecture single_process of detector_101 is
    type state_type is (S0, S1, S10, S101);
    signal state : state_type;
begin
    fsm: process(clk, reset)
    begin
        if reset = '1' then
            state <= S0;
            detected <= '0';
        elsif rising_edge(clk) then
            -- Valores por defecto
            detected <= '0';
            
            case state is
                when S0 =>
                    if x = '1' then state <= S1;
                    else state <= S0;
                    end if;
                    
                when S1 =>
                    if x = '0' then state <= S10;
                    else state <= S1;
                    end if;
                    
                when S10 =>
                    if x = '1' then
                        state <= S101;
                        detected <= '1';  -- Salida registrada
                    else
                        state <= S0;
                    end if;
                    
                when S101 =>
                    if x = '0' then state <= S10;
                    else state <= S1;
                    end if;
                    
                when others =>
                    state <= S0;
            end case;
        end if;
    end process;
end architecture;
```

> ⚠️ **Nota:** En esta versión, la salida está registrada (retardo de 1 ciclo).

---

## Paso 5: Testbench

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_detector_101 is
end entity;

architecture test of tb_detector_101 is
    constant CLK_PERIOD : time := 10 ns;
    signal clk, reset, x, detected : std_logic;
begin
    -- DUT
    DUT: entity work.detector_101
        port map (clk, reset, x, detected);
    
    -- Clock generation
    clk <= not clk after CLK_PERIOD/2 when now < 500 ns else '0';
    
    -- Test sequence
    process
    begin
        -- Reset
        reset <= '1'; x <= '0';
        wait for CLK_PERIOD * 2;
        reset <= '0';
        
        -- Secuencia: 0 1 0 1 0 1 1 0 1
        --            - - - D - D - - D
        -- D = detected
        
        x <= '0'; wait for CLK_PERIOD;  -- S0 -> S0
        x <= '1'; wait for CLK_PERIOD;  -- S0 -> S1
        x <= '0'; wait for CLK_PERIOD;  -- S1 -> S10
        x <= '1'; wait for CLK_PERIOD;  -- S10 -> S101 (detect!)
        
        assert detected = '1' 
            report "Error: Primera detección fallida" 
            severity error;
        
        x <= '0'; wait for CLK_PERIOD;  -- S101 -> S10 (solapamiento)
        x <= '1'; wait for CLK_PERIOD;  -- S10 -> S101 (detect!)
        
        assert detected = '1' 
            report "Error: Segunda detección (solapamiento) fallida" 
            severity error;
        
        x <= '1'; wait for CLK_PERIOD;  -- S101 -> S1
        x <= '0'; wait for CLK_PERIOD;  -- S1 -> S10
        x <= '1'; wait for CLK_PERIOD;  -- S10 -> S101 (detect!)
        
        assert detected = '1' 
            report "Error: Tercera detección fallida" 
            severity error;
        
        wait for CLK_PERIOD * 5;
        report "Test completado exitosamente" severity note;
        wait;
    end process;
end architecture;
```

---

## Verificación

### Secuencia de Prueba: `010101101`

| Ciclo | x | Estado | Siguiente | detected |
|:-----:|:-:|:------:|:---------:|:--------:|
| 0 | 0 | S0 | S0 | 0 |
| 1 | 1 | S0 | S1 | 0 |
| 2 | 0 | S1 | S10 | 0 |
| 3 | 1 | S10 | S101 | **1** ✓ |
| 4 | 0 | S101 | S10 | 0 |
| 5 | 1 | S10 | S101 | **1** ✓ |
| 6 | 1 | S101 | S1 | 0 |
| 7 | 0 | S1 | S10 | 0 |
| 8 | 1 | S10 | S101 | **1** ✓ |

Detecta 3 veces "101" (con solapamiento).

---

## Conceptos Clave

| Concepto | Aplicación |
|----------|------------|
| FSM Moore | Salida solo depende del estado |
| Solapamiento | El estado S101 vuelve a S10 o S1 |
| 2 procesos | Separación registro/combinacional |
| `type` enumerado | Define estados legibles |

---

> 💡 **Tip:** El solapamiento se logra porque desde S101, no volvemos a S0 sino a estados intermedios que aprovechan los bits ya recibidos.
