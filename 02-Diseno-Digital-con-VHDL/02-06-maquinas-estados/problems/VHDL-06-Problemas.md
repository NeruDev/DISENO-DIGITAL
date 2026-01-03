<!--
::METADATA::
type: problem
topic_id: vhdl-06-maquinas-estados
file_id: problemas-fsm
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [ejercicios, VHDL, FSM, máquina de estados]
search_keywords: "ejercicios, problemas, FSM, máquina de estados"
-->

> 🏠 **Navegación:** [← Métodos](../methods/VHDL-06-Metodos-FSM.md) | [Respuestas →](../solutions/VHDL-06-Respuestas.md)

---

# Problemas: Máquinas de Estados

## Nivel 1: Conceptos Básicos

### Problema 1.1
¿Cuál es la diferencia entre una máquina de Moore y una de Mealy?

### Problema 1.2
Identificar si esta FSM es Moore o Mealy:
```
Estado IDLE: if btn='1' then output='1', goto RUN
Estado RUN:  output='0', if done='1' then goto IDLE
```

### Problema 1.3
¿Por qué se recomienda usar tipos enumerados para los estados en lugar de std_logic_vector?

---

## Nivel 2: Estructura Básica

### Problema 2.1
Completar la declaración de tipo y señales para una FSM con estados: RESET, INIT, RUN, PAUSE, STOP.

### Problema 2.2
Escribir el proceso de registro de estado con reset asíncrono.

### Problema 2.3
¿Qué problema tiene este código?
```vhdl
COMB: process(current_state)  -- Lista de sensibilidad
begin
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

### Problema 3.1
Diseñar una FSM para un detector de secuencia "101":
- Entrada: din (1 bit)
- Salida: detected (1 bit, '1' cuando se detecta "101")
- Estados: S0 (inicial), S1, S10, S101

### Problema 3.2
Diseñar una FSM para control de puerta:
- Entradas: sensor_abierta, sensor_cerrada, boton
- Salidas: motor_abrir, motor_cerrar
- Estados: CERRADA, ABRIENDO, ABIERTA, CERRANDO

### Problema 3.3
Diseñar una FSM de Moore para un dispensador de productos:
- Entradas: moneda, seleccion
- Salidas: dispensar, devolver_cambio
- Estados: ESPERA, SELECCION, DISPENSANDO, CAMBIO

---

## Nivel 4: Dos Procesos

### Problema 4.1
Convertir esta FSM de un proceso a dos procesos:
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
                if stop = '1' then
                    state <= IDLE;
                end if;
            when others =>
                state <= IDLE;
        end case;
    end if;
end process;
```

### Problema 4.2
¿Cuáles son las ventajas del estilo de dos procesos?

### Problema 4.3
En el estilo de dos procesos, ¿por qué es importante incluir valores por defecto?

---

## Nivel 5: Moore vs Mealy

### Problema 5.1
Implementar un detector de flanco de subida:
- a) Como máquina de Moore
- b) Como máquina de Mealy

### Problema 5.2
¿Cuál tiene menos estados? ¿Por qué?

### Problema 5.3
¿Cuándo es preferible usar Moore sobre Mealy?

---

## Nivel 6: FSM con Temporizadores

### Problema 6.1
Diseñar una FSM para un semáforo con tiempos:
- VERDE: 30 ciclos
- AMARILLO: 5 ciclos
- ROJO: 35 ciclos

### Problema 6.2
Modificar la FSM anterior para incluir un modo de emergencia (amarillo parpadeante).

### Problema 6.3
Diseñar una FSM para un botón con debounce (10 ciclos de estabilidad).

---

## Nivel 7: FSM Seguras

### Problema 7.1
¿Por qué es importante incluir `when others` en el case de una FSM?

### Problema 7.2
¿Qué es la codificación "one-hot" y cuáles son sus ventajas?

### Problema 7.3
Agregar detección de estado ilegal a esta FSM:
```vhdl
type state_type is (S0, S1, S2, S3);
```

---

## Nivel 8: FSM con Handshake

### Problema 8.1
Diseñar una FSM que implemente un protocolo request-acknowledge:
- Señales: req_out, ack_in, data_ready
- La FSM genera req, espera ack, procesa datos

### Problema 8.2
Diseñar una FSM maestra y una esclava que se comuniquen mediante handshake.

### Problema 8.3
¿Qué problemas pueden ocurrir si no se sincronizan las señales de handshake entre dominios de reloj diferentes?

---

## Nivel 9: FSM Complejas

### Problema 9.1
Diseñar una FSM para un controlador de UART TX simplificado:
- Estados: IDLE, START_BIT, DATA (8 bits), STOP_BIT
- Entrada: data_in (8 bits), send
- Salida: tx, busy

### Problema 9.2
Diseñar una FSM para un controlador de memoria:
- Estados: IDLE, READ_START, READ_WAIT, READ_DONE, WRITE_START, WRITE_WAIT, WRITE_DONE
- Señales: rd, wr, addr, data_in, data_out, ready, busy

### Problema 9.3
Diseñar una FSM para un árbitro de bus de 3 maestros.

---

## Nivel 10: Integración

### Problema 10.1
Diseñar una FSM completa para una lavadora:
- Modos: WASH, RINSE, SPIN
- Cada modo tiene múltiples pasos
- Incluir temporizadores y sensores

### Problema 10.2
Diseñar un controlador de elevador de 4 pisos con:
- Botones de llamada por piso
- Sensores de posición
- Indicadores de piso y dirección

### Problema 10.3
Diseñar un controlador de teclado PS/2:
- Recibir datos seriales
- Detectar teclas presionadas y liberadas
- Generar código de escaneo

---

<!-- IA_CONTEXT
PROPÓSITO: Ejercicios sobre máquinas de estados VHDL
RESPUESTAS: Ver archivo solutions/VHDL-06-Respuestas.md
HERRAMIENTAS: ModelSim, GHDL, Quartus, Vivado
-->
