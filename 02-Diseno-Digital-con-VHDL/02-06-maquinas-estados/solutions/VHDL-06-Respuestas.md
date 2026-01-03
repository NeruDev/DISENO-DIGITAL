<!--
::METADATA::
type: solution
topic_id: vhdl-06-maquinas-estados
file_id: respuestas-fsm
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [respuestas, soluciones, VHDL, FSM]
search_keywords: "respuestas, soluciones, FSM, máquina de estados"
-->

> 🏠 **Navegación:** [← Problemas](../problems/VHDL-06-Problemas.md)

---

# Respuestas: Máquinas de Estados

## Nivel 1: Conceptos Básicos

### Respuesta 1.1

**Moore:** Las salidas dependen SOLO del estado actual.
- Salida = f(Estado)
- Más estable, sincronizada con el reloj

**Mealy:** Las salidas dependen del estado actual Y las entradas.
- Salida = f(Estado, Entradas)
- Respuesta más rápida, potencialmente con glitches

### Respuesta 1.2

Es una máquina **Mealy** porque en el estado IDLE la salida depende de la entrada (`if btn='1' then output='1'`).

### Respuesta 1.3

Ventajas de tipos enumerados:
- Código más legible y mantenible
- El compilador detecta errores
- El sintetizador optimiza la codificación
- La simulación muestra nombres de estados

---

## Nivel 2: Estructura Básica

### Respuesta 2.1

```vhdl
type state_type is (RESET, INIT, RUN, PAUSE, STOP);
signal current_state, next_state : state_type;
```

### Respuesta 2.2

```vhdl
STATE_REG: process(clk, reset)
begin
    if reset = '1' then
        current_state <= RESET;  -- o el estado inicial apropiado
    elsif rising_edge(clk) then
        current_state <= next_state;
    end if;
end process;
```

### Respuesta 2.3

**Problemas:**
1. Lista de sensibilidad incompleta - falta `start`
2. No hay valor por defecto para `next_state` en IDLE cuando `start='0'`

**Solución:**
```vhdl
COMB: process(current_state, start)
begin
    next_state <= current_state;  -- Valor por defecto
    case current_state is
        when IDLE =>
            if start = '1' then
                next_state <= RUN;
            end if;
        when RUN =>
            next_state <= DONE;
        when others =>
            next_state <= IDLE;
    end case;
end process;
```

---

## Nivel 3: Diseño de FSM Simple

### Respuesta 3.1: Detector de "101"

```vhdl
architecture rtl of seq_detector is
    type state_type is (S0, S1, S10, S101);
    signal state : state_type;
begin
    process(clk, reset)
    begin
        if reset = '1' then
            state <= S0;
        elsif rising_edge(clk) then
            case state is
                when S0 =>
                    if din = '1' then state <= S1;
                    else state <= S0; end if;
                when S1 =>
                    if din = '0' then state <= S10;
                    else state <= S1; end if;
                when S10 =>
                    if din = '1' then state <= S101;
                    else state <= S0; end if;
                when S101 =>
                    if din = '1' then state <= S1;
                    else state <= S10; end if;
                when others => state <= S0;
            end case;
        end if;
    end process;
    
    detected <= '1' when state = S101 else '0';
end architecture;
```

### Respuesta 3.2: Control de Puerta

```vhdl
type state_type is (CERRADA, ABRIENDO, ABIERTA, CERRANDO);
signal state : state_type;

process(clk, reset)
begin
    if reset = '1' then
        state <= CERRADA;
    elsif rising_edge(clk) then
        case state is
            when CERRADA =>
                if boton = '1' then state <= ABRIENDO; end if;
            when ABRIENDO =>
                if sensor_abierta = '1' then state <= ABIERTA; end if;
            when ABIERTA =>
                if boton = '1' then state <= CERRANDO; end if;
            when CERRANDO =>
                if sensor_cerrada = '1' then state <= CERRADA; end if;
            when others => state <= CERRADA;
        end case;
    end if;
end process;

motor_abrir <= '1' when state = ABRIENDO else '0';
motor_cerrar <= '1' when state = CERRANDO else '0';
```

---

## Nivel 4: Dos Procesos

### Respuesta 4.1

```vhdl
architecture two_proc of fsm is
    type state_type is (IDLE, RUN);
    signal current_state, next_state : state_type;
begin
    -- Proceso secuencial
    SEQ: process(clk, reset)
    begin
        if reset = '1' then
            current_state <= IDLE;
        elsif rising_edge(clk) then
            current_state <= next_state;
        end if;
    end process;
    
    -- Proceso combinacional
    COMB: process(current_state, start, stop)
    begin
        next_state <= current_state;
        output <= '0';
        
        case current_state is
            when IDLE =>
                if start = '1' then
                    next_state <= RUN;
                end if;
            when RUN =>
                output <= '1';
                if stop = '1' then
                    next_state <= IDLE;
                end if;
            when others =>
                next_state <= IDLE;
        end case;
    end process;
end architecture;
```

### Respuesta 4.2

**Ventajas:**
- Separación clara de lógica secuencial y combinacional
- Más fácil de depurar
- Más fácil de modificar
- El sintetizador puede optimizar mejor

### Respuesta 4.3

Los valores por defecto evitan latches. Sin ellos, si algún camino no asigna una señal, se infiere un latch para mantener el valor anterior.

---

## Nivel 5: Moore vs Mealy

### Respuesta 5.1

**Moore (2 estados):**
```vhdl
type state_type is (LOW, HIGH);
signal state : state_type;

process(clk, reset)
begin
    if reset = '1' then
        state <= LOW;
    elsif rising_edge(clk) then
        case state is
            when LOW  => if input = '1' then state <= HIGH; end if;
            when HIGH => if input = '0' then state <= LOW; end if;
        end case;
    end if;
end process;

-- Salida: detecta transición LOW->HIGH
edge_detected <= '1' when state = LOW and input = '1' else '0';
-- Nota: esto es en realidad Mealy porque depende de input
```

**Mealy (1 estado interno):**
```vhdl
signal input_prev : std_logic;

process(clk, reset)
begin
    if reset = '1' then
        input_prev <= '0';
    elsif rising_edge(clk) then
        input_prev <= input;
    end if;
end process;

edge_detected <= '1' when input = '1' and input_prev = '0' else '0';
```

### Respuesta 5.2

Mealy tiene menos estados porque puede reaccionar inmediatamente a las entradas sin necesitar estados intermedios.

### Respuesta 5.3

Moore es preferible cuando:
- Se necesitan salidas sin glitches
- Timing crítico (salidas sincronizadas)
- Mayor claridad en el diseño
- Sistemas safety-critical

---

## Nivel 6: FSM con Temporizadores

### Respuesta 6.1

```vhdl
type state_type is (ST_VERDE, ST_AMARILLO, ST_ROJO);
signal state : state_type;
signal counter : integer range 0 to 35;

process(clk, reset)
begin
    if reset = '1' then
        state <= ST_ROJO;
        counter <= 0;
    elsif rising_edge(clk) then
        counter <= counter + 1;
        case state is
            when ST_VERDE =>
                if counter = 29 then
                    state <= ST_AMARILLO;
                    counter <= 0;
                end if;
            when ST_AMARILLO =>
                if counter = 4 then
                    state <= ST_ROJO;
                    counter <= 0;
                end if;
            when ST_ROJO =>
                if counter = 34 then
                    state <= ST_VERDE;
                    counter <= 0;
                end if;
            when others =>
                state <= ST_ROJO;
                counter <= 0;
        end case;
    end if;
end process;

verde <= '1' when state = ST_VERDE else '0';
amarillo <= '1' when state = ST_AMARILLO else '0';
rojo <= '1' when state = ST_ROJO else '0';
```

---

## Nivel 7: FSM Seguras

### Respuesta 7.1

`when others` es importante porque:
- std_logic tiene 9 valores posibles, no solo '0' y '1'
- Previene estados indefinidos
- El sintetizador puede añadir estados para optimización
- Permite recuperación de errores

### Respuesta 7.2

**One-hot:** Cada estado usa un flip-flop dedicado; solo uno está activo.

**Ventajas:**
- Decodificación simple (un bit)
- Transiciones rápidas
- Fácil detección de errores
- Menor lógica combinacional

**Desventajas:**
- Usa más flip-flops
- No eficiente para muchos estados

### Respuesta 7.3

```vhdl
-- Detectar si más de un bit está activo (para one-hot)
signal illegal_state : std_logic;
signal state_vector : std_logic_vector(3 downto 0);

state_vector <= "0001" when state = S0 else
                "0010" when state = S1 else
                "0100" when state = S2 else
                "1000" when state = S3 else
                "0000";

-- Para detección general
illegal_state <= '1' when state'valid = false else '0';
```

---

## Nivel 9: FSM Complejas

### Respuesta 9.1: UART TX (simplificado)

```vhdl
type state_type is (IDLE, START_BIT, DATA_BITS, STOP_BIT);
signal state : state_type;
signal bit_counter : integer range 0 to 7;
signal shift_reg : std_logic_vector(7 downto 0);

process(clk, reset)
begin
    if reset = '1' then
        state <= IDLE;
        tx <= '1';
        busy <= '0';
    elsif rising_edge(clk) then
        case state is
            when IDLE =>
                tx <= '1';
                busy <= '0';
                if send = '1' then
                    shift_reg <= data_in;
                    state <= START_BIT;
                    busy <= '1';
                end if;
            when START_BIT =>
                tx <= '0';
                bit_counter <= 0;
                state <= DATA_BITS;
            when DATA_BITS =>
                tx <= shift_reg(0);
                shift_reg <= '0' & shift_reg(7 downto 1);
                if bit_counter = 7 then
                    state <= STOP_BIT;
                else
                    bit_counter <= bit_counter + 1;
                end if;
            when STOP_BIT =>
                tx <= '1';
                state <= IDLE;
            when others =>
                state <= IDLE;
        end case;
    end if;
end process;
```

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para ejercicios de FSM
NOTA: Pueden existir soluciones alternativas válidas
-->
