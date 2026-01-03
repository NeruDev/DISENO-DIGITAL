<!--
::METADATA::
type: theory
topic_id: vhdl-06-maquinas-estados
file_id: teoria-fsm
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [VHDL, FSM, Moore, Mealy, máquina de estados]
search_keywords: "FSM, máquina de estados, Moore, Mealy, state machine"
-->

> 🏠 **Navegación:** [← Volver al Índice](../02-06-Intro.md) | [Métodos →](../methods/VHDL-06-Metodos-FSM.md)

---

# Máquinas de Estados en VHDL

## 1. Introducción a FSM

### 1.1 ¿Qué es una FSM?

Una **Finite State Machine** (FSM) es un modelo computacional con:
- Número finito de **estados**
- **Transiciones** entre estados basadas en entradas
- **Salidas** que dependen del estado (y opcionalmente de entradas)

### 1.2 Componentes de una FSM

```
┌─────────────────────────────────────────────────┐
│                    FSM                          │
│  ┌──────────┐      ┌──────────┐     ┌───────┐ │
│  │  Lógica  │      │ Registro │     │Lógica │ │
│  │  Próximo │─────▶│   de     │────▶│Salida │──▶ Salidas
│  │  Estado  │      │  Estado  │     │       │ │
│  └──────────┘      └──────────┘     └───────┘ │
│       ▲                  │                     │
│       │                  │                     │
│  Entradas ◀──────────────┘                    │
└─────────────────────────────────────────────────┘
```

---

## 2. Tipos de FSM

### 2.1 Máquina de Moore

Las **salidas** dependen **solo** del estado actual.

```
Salidas = f(Estado_actual)
```

```
┌───────┐        ┌───────┐
│ IDLE  │───────▶│ WAIT  │
│ out=0 │   start│ out=0 │
└───────┘        └───┬───┘
    ▲                │ done
    │                ▼
    │            ┌───────┐
    └────────────│ DONE  │
         reset   │ out=1 │
                 └───────┘
```

### 2.2 Máquina de Mealy

Las **salidas** dependen del estado actual **y** las entradas.

```
Salidas = f(Estado_actual, Entradas)
```

```
┌───────┐  start/out=0  ┌───────┐
│ IDLE  │──────────────▶│ WAIT  │
└───────┘               └───┬───┘
    ▲                       │ done/out=1
    │                       ▼
    └───────────────────────┘
           reset/out=0
```

### 2.3 Comparación Moore vs Mealy

| Característica | Moore | Mealy |
|----------------|-------|-------|
| Salidas dependen de | Solo estado | Estado + entradas |
| Número de estados | Más estados | Menos estados |
| Timing de salidas | Sincronizado | Puede ser asíncrono |
| Complejidad | Más simple | Más eficiente |
| Latencia | 1 ciclo más | Respuesta inmediata |

---

## 3. Representación de Estados

### 3.1 Tipo Enumerado (Recomendado)

```vhdl
type state_type is (IDLE, START, RUN, STOP, DONE);
signal current_state, next_state : state_type;
```

### 3.2 Codificación de Estados

El sintetizador elige la codificación, o se puede especificar:

| Codificación | Descripción | Estados (4) |
|--------------|-------------|-------------|
| Binary | Código binario | 00, 01, 10, 11 |
| One-Hot | Un bit por estado | 0001, 0010, 0100, 1000 |
| Gray | Solo 1 bit cambia | 00, 01, 11, 10 |

### 3.3 Atributos de Codificación

```vhdl
type state_type is (S0, S1, S2, S3);
attribute enum_encoding : string;
attribute enum_encoding of state_type : type is "one-hot";
-- o "gray", "sequential", "johnson"
```

---

## 4. Arquitectura de FSM: Un Proceso

### 4.1 Estructura

```vhdl
architecture one_process of fsm is
    type state_type is (IDLE, RUN, DONE);
    signal state : state_type := IDLE;
begin
    process(clk, reset)
    begin
        if reset = '1' then
            state <= IDLE;
            output <= '0';
        elsif rising_edge(clk) then
            case state is
                when IDLE =>
                    output <= '0';
                    if start = '1' then
                        state <= RUN;
                    end if;
                when RUN =>
                    output <= '1';
                    if done = '1' then
                        state <= DONE;
                    end if;
                when DONE =>
                    output <= '0';
                    state <= IDLE;
                when others =>
                    state <= IDLE;
            end case;
        end if;
    end process;
end architecture;
```

### 4.2 Características

- **Un solo process** maneja todo
- Más compacto
- Salidas registradas (sin glitches)
- Puede ser más difícil de leer

---

## 5. Arquitectura de FSM: Dos Procesos

### 5.1 Estructura

```vhdl
architecture two_process of fsm is
    type state_type is (IDLE, RUN, DONE);
    signal current_state, next_state : state_type;
begin

    -- Proceso secuencial: registro de estado
    SEQ: process(clk, reset)
    begin
        if reset = '1' then
            current_state <= IDLE;
        elsif rising_edge(clk) then
            current_state <= next_state;
        end if;
    end process;

    -- Proceso combinacional: lógica de transición y salidas
    COMB: process(current_state, start, done)
    begin
        -- Valores por defecto
        next_state <= current_state;
        output <= '0';
        
        case current_state is
            when IDLE =>
                if start = '1' then
                    next_state <= RUN;
                end if;
            when RUN =>
                output <= '1';
                if done = '1' then
                    next_state <= DONE;
                end if;
            when DONE =>
                next_state <= IDLE;
            when others =>
                next_state <= IDLE;
        end case;
    end process;
end architecture;
```

### 5.2 Características

- Separación clara de funciones
- Más fácil de depurar
- Salidas combinacionales (pueden tener glitches)
- Estilo preferido en industria

---

## 6. Arquitectura de FSM: Tres Procesos

### 6.1 Estructura

```vhdl
architecture three_process of fsm is
    type state_type is (IDLE, RUN, DONE);
    signal current_state, next_state : state_type;
begin

    -- Proceso 1: Registro de estado
    STATE_REG: process(clk, reset)
    begin
        if reset = '1' then
            current_state <= IDLE;
        elsif rising_edge(clk) then
            current_state <= next_state;
        end if;
    end process;

    -- Proceso 2: Lógica de próximo estado
    NEXT_STATE_LOGIC: process(current_state, start, done)
    begin
        next_state <= current_state;  -- Default
        case current_state is
            when IDLE =>
                if start = '1' then
                    next_state <= RUN;
                end if;
            when RUN =>
                if done = '1' then
                    next_state <= DONE;
                end if;
            when DONE =>
                next_state <= IDLE;
            when others =>
                next_state <= IDLE;
        end case;
    end process;

    -- Proceso 3: Lógica de salidas
    OUTPUT_LOGIC: process(current_state)  -- Moore
    begin
        case current_state is
            when IDLE => output <= '0';
            when RUN  => output <= '1';
            when DONE => output <= '0';
            when others => output <= '0';
        end case;
    end process;
end architecture;
```

### 6.2 Características

- Máxima modularidad
- Fácil de mantener y modificar
- Clara separación de responsabilidades
- Útil para FSM complejas

---

## 7. Mealy vs Moore en VHDL

### 7.1 Moore: Salidas Solo de Estado

```vhdl
-- Salidas dependen SOLO del estado
OUTPUT_MOORE: process(current_state)
begin
    case current_state is
        when IDLE => output <= '0';
        when RUN  => output <= '1';
        when DONE => output <= '0';
    end case;
end process;
```

### 7.2 Mealy: Salidas de Estado y Entradas

```vhdl
-- Salidas dependen del estado Y las entradas
OUTPUT_MEALY: process(current_state, input)
begin
    case current_state is
        when IDLE =>
            if input = '1' then
                output <= '1';  -- Transición anticipada
            else
                output <= '0';
            end if;
        when RUN =>
            output <= '1';
        when DONE =>
            output <= '0';
    end case;
end process;
```

---

## 8. FSM Seguras

### 8.1 Problema: Estados Ilegales

Si el registro de estado se corrompe (ruido, radiación), puede ir a un estado no definido.

### 8.2 Solución: `when others`

```vhdl
case current_state is
    when IDLE => ...
    when RUN  => ...
    when DONE => ...
    when others =>
        next_state <= IDLE;  -- Recuperación
        error_flag <= '1';
end case;
```

### 8.3 Codificación One-Hot Segura

```vhdl
-- Detectar estado inválido
if current_state'length /= 1 then
    -- Estado corrupto (más de un bit activo)
    error <= '1';
end if;
```

### 8.4 Atributo `safe_state`

Algunos sintetizadores soportan:

```vhdl
attribute syn_encoding : string;
attribute syn_encoding of state : type is "safe, one-hot";
```

---

## 9. Salidas Registradas

### 9.1 ¿Por Qué Registrar Salidas?

- Elimina glitches
- Mejora timing
- Sincroniza con el reloj

### 9.2 Implementación

```vhdl
-- Salidas registradas en proceso secuencial
process(clk, reset)
begin
    if reset = '1' then
        current_state <= IDLE;
        output_reg <= '0';
    elsif rising_edge(clk) then
        current_state <= next_state;
        output_reg <= output_next;  -- Registrar salida
    end if;
end process;
```

---

## 10. Ejemplo Completo: Controlador de Semáforo

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity traffic_light is
    port (
        clk   : in  std_logic;
        reset : in  std_logic;
        red   : out std_logic;
        yellow: out std_logic;
        green : out std_logic
    );
end entity;

architecture moore of traffic_light is
    type state_type is (ST_RED, ST_RED_YELLOW, ST_GREEN, ST_YELLOW);
    signal state : state_type := ST_RED;
    signal counter : integer range 0 to 100;
begin

    process(clk, reset)
    begin
        if reset = '1' then
            state <= ST_RED;
            counter <= 0;
        elsif rising_edge(clk) then
            counter <= counter + 1;
            
            case state is
                when ST_RED =>
                    if counter = 50 then
                        state <= ST_RED_YELLOW;
                        counter <= 0;
                    end if;
                when ST_RED_YELLOW =>
                    if counter = 10 then
                        state <= ST_GREEN;
                        counter <= 0;
                    end if;
                when ST_GREEN =>
                    if counter = 50 then
                        state <= ST_YELLOW;
                        counter <= 0;
                    end if;
                when ST_YELLOW =>
                    if counter = 10 then
                        state <= ST_RED;
                        counter <= 0;
                    end if;
                when others =>
                    state <= ST_RED;
            end case;
        end if;
    end process;

    -- Salidas Moore
    red    <= '1' when state = ST_RED or state = ST_RED_YELLOW else '0';
    yellow <= '1' when state = ST_YELLOW or state = ST_RED_YELLOW else '0';
    green  <= '1' when state = ST_GREEN else '0';

end architecture;
```

---

## Referencias

- IEEE Std 1076-2008
- Ashenden, P.J. (2008). *The Designer's Guide to VHDL*
- Xilinx UG901 - Vivado Design Suite User Guide: Synthesis

---

<!-- IA_CONTEXT
NIVEL: Intermedio (2/3)
PREREQUISITOS: 02-01 a 02-05
CONEXIONES: Fundamental para diseño de controladores
ERRORES_COMUNES: Olvidar when others, latches en salidas, lista de sensibilidad incompleta
-->
