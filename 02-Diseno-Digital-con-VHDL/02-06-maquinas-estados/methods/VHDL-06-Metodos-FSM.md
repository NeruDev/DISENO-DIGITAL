<!--
::METADATA::
type: method
topic_id: vhdl-06-maquinas-estados
file_id: metodos-fsm
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [VHDL, metodologia, FSM, máquina de estados]
search_keywords: "metodología FSM, máquina de estados, diseño"
-->

> 🏠 **Navegación:** [← Teoría](../theory/VHDL-06-Teoria-FSM.md) | [Problemas →](../problems/VHDL-06-Problemas.md)

---

# Métodos: Máquinas de Estados

## Método 1: Diseño Sistemático de FSM

### Paso 1: Diagrama de Estados

1. Identificar estados necesarios
2. Definir transiciones (condiciones)
3. Definir salidas (Moore o Mealy)

### Paso 2: Tabla de Estados

| Estado | Entradas | Próximo Estado | Salidas |
|--------|----------|----------------|---------|
| IDLE | start=0 | IDLE | out=0 |
| IDLE | start=1 | RUN | out=0 |
| RUN | done=0 | RUN | out=1 |
| RUN | done=1 | DONE | out=1 |
| DONE | - | IDLE | out=0 |

### Paso 3: Codificar en VHDL

```vhdl
type state_type is (IDLE, RUN, DONE);
```

---

## Método 2: Plantilla de Dos Procesos (Recomendada)

```vhdl
architecture rtl of fsm is
    type state_type is (ST1, ST2, ST3);
    signal current_state, next_state : state_type;
begin

    -- Registro de estado
    STATE_REG: process(clk, reset)
    begin
        if reset = '1' then
            current_state <= ST1;
        elsif rising_edge(clk) then
            current_state <= next_state;
        end if;
    end process;

    -- Lógica combinacional
    COMB: process(current_state, input1, input2)
    begin
        -- Defaults
        next_state <= current_state;
        output1 <= '0';
        output2 <= '0';
        
        case current_state is
            when ST1 =>
                -- Transiciones y salidas
            when ST2 =>
                -- ...
            when others =>
                next_state <= ST1;
        end case;
    end process;

end architecture;
```

---

## Método 3: Valores por Defecto

### Evitar Latches con Defaults

```vhdl
COMB: process(current_state, inputs)
begin
    -- SIEMPRE definir valores por defecto primero
    next_state <= current_state;  -- Mantener estado
    output1 <= '0';
    output2 <= '0';
    ready <= '0';
    
    -- Después las condiciones específicas
    case current_state is
        when IDLE =>
            ready <= '1';  -- Sobrescribe default
            if start = '1' then
                next_state <= RUN;
            end if;
        -- ...
    end case;
end process;
```

---

## Método 4: Salidas Registradas

### Eliminar Glitches

```vhdl
-- Opción 1: Registrar en proceso secuencial
STATE_REG: process(clk, reset)
begin
    if reset = '1' then
        current_state <= IDLE;
        output_reg <= '0';
    elsif rising_edge(clk) then
        current_state <= next_state;
        output_reg <= output_comb;  -- Registrar
    end if;
end process;

-- Opción 2: Calcular salida del próximo estado
case current_state is
    when IDLE =>
        if start = '1' then
            next_state <= RUN;
            output_next <= '1';  -- Salida anticipada
        end if;
    -- ...
```

---

## Método 5: FSM con Temporizadores

### Contador Integrado

```vhdl
signal counter : unsigned(7 downto 0);

process(clk, reset)
begin
    if reset = '1' then
        state <= IDLE;
        counter <= (others => '0');
    elsif rising_edge(clk) then
        case state is
            when WAIT =>
                if counter = TIMEOUT then
                    state <= NEXT_STATE;
                    counter <= (others => '0');
                else
                    counter <= counter + 1;
                end if;
            when others =>
                counter <= (others => '0');
                -- ...
        end case;
    end if;
end process;
```

---

## Método 6: FSM Jerárquicas

### Estado con Sub-FSM

```vhdl
type main_state is (MAIN_IDLE, MAIN_PROCESS, MAIN_DONE);
type sub_state is (SUB_START, SUB_WORK, SUB_END);

signal main_st : main_state;
signal sub_st : sub_state;

process(clk, reset)
begin
    if reset = '1' then
        main_st <= MAIN_IDLE;
        sub_st <= SUB_START;
    elsif rising_edge(clk) then
        case main_st is
            when MAIN_PROCESS =>
                -- Sub-FSM activa
                case sub_st is
                    when SUB_START =>
                        sub_st <= SUB_WORK;
                    when SUB_WORK =>
                        if work_done = '1' then
                            sub_st <= SUB_END;
                        end if;
                    when SUB_END =>
                        sub_st <= SUB_START;
                        main_st <= MAIN_DONE;
                end case;
            when others =>
                -- ...
        end case;
    end if;
end process;
```

---

## Método 7: Detección de Flancos

### Para Entradas Asíncronas

```vhdl
signal input_d1, input_d2 : std_logic;
signal input_rising : std_logic;

-- Sincronizador
process(clk)
begin
    if rising_edge(clk) then
        input_d1 <= async_input;
        input_d2 <= input_d1;
    end if;
end process;

-- Detector de flanco
input_rising <= input_d1 and not input_d2;

-- Usar en FSM
if input_rising = '1' then
    next_state <= TRIGGERED;
end if;
```

---

## Método 8: FSM con Handshake

### Protocolo Request-Acknowledge

```vhdl
type state_type is (IDLE, WAIT_ACK, PROCESS, SEND_DONE);

process(clk, reset)
begin
    if reset = '1' then
        state <= IDLE;
        req <= '0';
    elsif rising_edge(clk) then
        case state is
            when IDLE =>
                if start = '1' then
                    req <= '1';
                    state <= WAIT_ACK;
                end if;
            when WAIT_ACK =>
                if ack = '1' then
                    req <= '0';
                    state <= PROCESS;
                end if;
            when PROCESS =>
                -- Procesar datos
                state <= SEND_DONE;
            when SEND_DONE =>
                if ack = '0' then  -- Esperar que ack baje
                    state <= IDLE;
                end if;
        end case;
    end if;
end process;
```

---

## Método 9: Verificar FSM Segura

### Checklist de Seguridad

- [ ] `when others` en todos los `case`
- [ ] Estado inicial definido en reset
- [ ] No hay estados inalcanzables
- [ ] Todos los estados tienen salida
- [ ] Considerar codificación segura para críticos

### Pruebas Recomendadas

1. Reset desde cada estado
2. Secuencia completa de operación
3. Entradas inesperadas
4. Timeout si aplica

---

## Método 10: Debug de FSM

### Señales de Debug

```vhdl
-- Exponer estado para debug
debug_state <= std_logic_vector(to_unsigned(state_type'pos(current_state), 4));

-- Contador de transiciones
process(clk)
begin
    if rising_edge(clk) then
        if current_state /= next_state then
            transition_count <= transition_count + 1;
        end if;
    end if;
end process;

-- Detección de estado ilegal
illegal_state <= '1' when current_state = ILLEGAL else '0';
```

### Report en Simulación

```vhdl
process(current_state)
begin
    report "Estado: " & state_type'image(current_state);
end process;
```

---

## Método 11: Checklist General

### Antes de Síntesis

- [ ] Tipo enumerado para estados
- [ ] Reset inicializa a estado válido
- [ ] Lista de sensibilidad completa (proceso combinacional)
- [ ] Valores por defecto para evitar latches
- [ ] `when others` en todos los case
- [ ] Salidas asignadas en todos los estados
- [ ] Transiciones cubren todas las condiciones

### Errores Comunes

| Error | Síntoma | Solución |
|-------|---------|----------|
| Latch inferido | Warning síntesis | Agregar defaults |
| Estado inaccesible | FSM incompleta | Revisar transiciones |
| Glitches en salida | Comportamiento erróneo | Registrar salidas |
| Reset no funciona | Estado no cambia | Verificar prioridad |

---

<!-- IA_CONTEXT
USO: Métodos prácticos para diseño de FSM en VHDL
NIVEL: Intermedio (2/3)
HERRAMIENTAS: Quartus, Vivado, ModelSim
-->
