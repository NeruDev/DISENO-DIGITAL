<!--
::METADATA::
type: reference
topic_id: vhdl-06-maquinas-estados
file_id: resumen-fsm
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [cheatsheet, VHDL, FSM]
search_keywords: "resumen, FSM, máquina de estados, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./02-06-Intro.md)

---

# 📋 Cheatsheet: Máquinas de Estados

## Moore vs Mealy

| Moore | Mealy |
|-------|-------|
| Salida = f(Estado) | Salida = f(Estado, Entradas) |
| Más estados | Menos estados |
| Sin glitches | Respuesta rápida |

---

## Declaración de Estados

```vhdl
type state_type is (IDLE, RUN, DONE);
signal current_state, next_state : state_type;
```

---

## Plantilla: Dos Procesos

```vhdl
-- Registro de estado
SEQ: process(clk, reset)
begin
    if reset = '1' then
        current_state <= IDLE;
    elsif rising_edge(clk) then
        current_state <= next_state;
    end if;
end process;

-- Lógica combinacional
COMB: process(current_state, input1, input2)
begin
    -- DEFAULTS PRIMERO
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
        when others =>
            next_state <= IDLE;
    end case;
end process;
```

---

## Plantilla: Un Proceso

```vhdl
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
                    state <= IDLE;
                end if;
            when others =>
                state <= IDLE;
        end case;
    end if;
end process;
```

---

## Reglas Críticas

### ⚠️ Siempre incluir:
- `when others` en case
- Valores por defecto al inicio
- Reset a estado válido

### Lista de Sensibilidad
```vhdl
-- Secuencial
process(clk, reset)  -- Solo clk y reset async

-- Combinacional  
process(current_state, input1, input2)  -- TODAS las entradas
```

---

## Codificación de Estados

| Tipo | S0 | S1 | S2 | S3 |
|------|----|----|----|----|
| Binary | 00 | 01 | 10 | 11 |
| One-Hot | 0001 | 0010 | 0100 | 1000 |
| Gray | 00 | 01 | 11 | 10 |

---

## Salidas Moore

```vhdl
-- Asignación concurrente (fuera de process)
output <= '1' when current_state = RUN else '0';

-- O en process de salidas
case current_state is
    when IDLE => output <= '0';
    when RUN  => output <= '1';
    when DONE => output <= '0';
end case;
```

---

## Salidas Mealy

```vhdl
case current_state is
    when IDLE =>
        if input = '1' then
            output <= '1';  -- Depende de entrada
        else
            output <= '0';
        end if;
    when RUN =>
        output <= '1';
end case;
```

---

## FSM con Temporizador

```vhdl
signal counter : integer range 0 to MAX;

when WAIT =>
    if counter = TIMEOUT then
        state <= NEXT;
        counter <= 0;
    else
        counter <= counter + 1;
    end if;
```

---

## Salidas Registradas

```vhdl
-- En proceso secuencial
elsif rising_edge(clk) then
    current_state <= next_state;
    output_reg <= output_comb;  -- Registrar
end if;
```

---

## Errores Comunes

| Error | Consecuencia |
|-------|--------------|
| Sin `when others` | Síntesis incompleta |
| Sin defaults | Latch inferido |
| Lista incompleta | Simulación errónea |
| Sin reset | Estado indefinido |

---

## FSM Segura

```vhdl
when others =>
    next_state <= IDLE;  -- Recuperación
    error_flag <= '1';   -- Señalización
```

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante diseño de FSM
-->
