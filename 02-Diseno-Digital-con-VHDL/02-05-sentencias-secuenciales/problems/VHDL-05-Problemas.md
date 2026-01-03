<!--
::METADATA::
type: problem
topic_id: vhdl-05-sentencias-secuenciales
file_id: problemas-secuenciales
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [ejercicios, VHDL, process, secuencial]
search_keywords: "ejercicios, problemas, process, secuencial"
-->

> 🏠 **Navegación:** [← Métodos](../methods/VHDL-05-Metodos-Secuenciales.md) | [Respuestas →](../solutions/VHDL-05-Respuestas.md)

---

# Problemas: Sentencias Secuenciales

## Nivel 1: Process Básico

### Problema 1.1
¿Cuál es la diferencia entre sentencias concurrentes y secuenciales en VHDL?

### Problema 1.2
Identificar qué señales deben ir en la lista de sensibilidad:
```vhdl
process(_______)
begin
    if sel = '1' then
        y <= a and b;
    else
        y <= c or d;
    end if;
end process;
```

### Problema 1.3
¿Por qué este process infiere un latch?
```vhdl
process(en, data)
begin
    if en = '1' then
        output <= data;
    end if;
end process;
```

---

## Nivel 2: Variables vs Señales

### Problema 2.1
¿Cuál es el valor final de `y` y `z`?
```vhdl
signal a, b : std_logic := '0';
signal y, z : std_logic;

process(clk)
    variable v : std_logic := '0';
begin
    if rising_edge(clk) then
        v := '1';
        y <= v;  -- ¿Valor?
        
        a <= '1';
        z <= a;  -- ¿Valor?
    end if;
end process;
```

### Problema 2.2
Convertir este código usando variables en lugar de señales intermedias:
```vhdl
signal temp1, temp2 : std_logic;
...
temp1 <= a and b;
temp2 <= temp1 or c;
y <= temp2 and d;
```

### Problema 2.3
¿Cuándo es preferible usar variables sobre señales?

---

## Nivel 3: if-then-else

### Problema 3.1
Implementar un multiplexor 4:1 usando `if-then-else`.

### Problema 3.2
Implementar un codificador de prioridad 4:2 usando `if-then-else`.

### Problema 3.3
¿Qué circuito infiere este código?
```vhdl
process(clk)
begin
    if rising_edge(clk) then
        if load = '1' then
            q <= d;
        elsif shift = '1' then
            q <= q(6 downto 0) & serial_in;
        end if;
    end if;
end process;
```

---

## Nivel 4: case

### Problema 4.1
Implementar un decodificador 3:8 usando `case`.

### Problema 4.2
Implementar una ALU de 8 bits con operaciones:
- "000": ADD
- "001": SUB
- "010": AND
- "011": OR
- "100": XOR
- "101": NOT A
- "110": Shift left
- "111": Shift right

### Problema 4.3
¿Por qué es necesario `when others` en un `case`?

### Problema 4.4
Corregir este código:
```vhdl
process(sel)
begin
    case sel is
        when "00" => y <= a;
        when "01" => y <= b;
        when "10" => y <= c;
    end case;
end process;
```

---

## Nivel 5: Bucles

### Problema 5.1
Usar un `for loop` para contar los bits '1' en un vector de 8 bits.

### Problema 5.2
Usar un `for loop` para invertir el orden de los bits en un vector.

### Problema 5.3
¿Por qué este bucle NO es sintetizable?
```vhdl
process(start)
    variable i : integer := 0;
begin
    while data(i) /= '1' loop
        i := i + 1;
    end loop;
    position <= i;
end process;
```

### Problema 5.4
Implementar un comparador de igualdad usando `for loop` y `exit`.

---

## Nivel 6: Flip-Flops y Registros

### Problema 6.1
Implementar un flip-flop D con:
- Reset asíncrono activo alto
- Enable síncrono

### Problema 6.2
Implementar un flip-flop T (toggle).

### Problema 6.3
Implementar un registro de 8 bits con carga paralela y clear síncrono.

### Problema 6.4
¿Cuál es la diferencia entre reset síncrono y asíncrono en términos de síntesis?

---

## Nivel 7: Contadores

### Problema 7.1
Implementar un contador ascendente de 8 bits con reset y enable.

### Problema 7.2
Implementar un contador descendente de 4 bits con carga paralela.

### Problema 7.3
Implementar un contador módulo 10 (BCD) con salida de overflow.

### Problema 7.4
Implementar un contador up/down con señal de dirección.

---

## Nivel 8: Registros de Desplazamiento

### Problema 8.1
Implementar un registro de desplazamiento de 8 bits con entrada serial.

### Problema 8.2
Implementar un registro con:
- Carga paralela
- Desplazamiento izquierda/derecha
- Hold (mantener valor)

### Problema 8.3
Implementar un LFSR (Linear Feedback Shift Register) de 4 bits.

---

## Nivel 9: Combinacional en Process

### Problema 9.1
Convertir este código concurrente a un process:
```vhdl
y <= d0 when sel = "00" else
     d1 when sel = "01" else
     d2 when sel = "10" else
     d3;
```

### Problema 9.2
Identificar el problema en este process combinacional:
```vhdl
process(a, b, sel)
begin
    if sel = '1' then
        y <= a;
        z <= b;
    else
        y <= b;
        -- z no asignado aquí
    end if;
end process;
```

### Problema 9.3
Diseñar un sumador/restador de 8 bits en un process:
- add_sub = '0': suma
- add_sub = '1': resta

---

## Nivel 10: Integración

### Problema 10.1
Diseñar un divisor de frecuencia que genere un pulso cada N ciclos de reloj (N configurable por genérico).

### Problema 10.2
Diseñar un debouncer para un botón con:
- Contador de estabilidad
- Salida registrada

### Problema 10.3
Diseñar un generador de PWM con:
- Período configurable
- Duty cycle de 8 bits
- Salida PWM

---

<!-- IA_CONTEXT
PROPÓSITO: Ejercicios sobre sentencias secuenciales VHDL
RESPUESTAS: Ver archivo solutions/VHDL-05-Respuestas.md
HERRAMIENTAS: ModelSim, GHDL, Quartus, Vivado
-->
