<!--
::METADATA::
type: problem
topic_id: vhdl-04-sentencias-concurrentes
file_id: problemas-concurrentes
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [ejercicios, VHDL, concurrente, when-else, with-select]
search_keywords: "ejercicios, problemas, sentencias concurrentes"
-->

> 🏠 **Navegación:** [← Métodos](../methods/VHDL-04-Metodos-Concurrentes.md) | [Respuestas →](../solutions/VHDL-04-Respuestas.md)

---

# Problemas: Sentencias Concurrentes

## Nivel 1: Asignación Simple

### Problema 1.1
Escribir asignaciones concurrentes para:
- Y = A AND B
- Z = NOT(C OR D)
- W = (A XOR B) AND C

### Problema 1.2
¿Por qué el orden de las siguientes sentencias no importa?
```vhdl
y <= a and b;
z <= c or d;
w <= y xor z;
```

### Problema 1.3
Escribir la asignación para concatenar dos nibbles en un byte:
```vhdl
signal nibble_hi, nibble_lo : std_logic_vector(3 downto 0);
signal byte_out : std_logic_vector(7 downto 0);
```

---

## Nivel 2: when-else

### Problema 2.1
Implementar un multiplexor 2:1 usando `when-else`:
- Entradas: a, b (1 bit cada uno)
- Selector: sel (1 bit)
- Salida: y

### Problema 2.2
Implementar un multiplexor 4:1 de 8 bits usando `when-else`:
- Entradas: d0, d1, d2, d3 (8 bits cada uno)
- Selector: sel (2 bits)
- Salida: y (8 bits)

### Problema 2.3
¿Qué problema tiene este código?
```vhdl
y <= a when sel = "00" else
     b when sel = "01" else
     c when sel = "10";
```

### Problema 2.4
Implementar un comparador de magnitud (8 bits) que indique si A > B, A = B, o A < B.

---

## Nivel 3: with-select

### Problema 3.1
Implementar el mismo multiplexor 4:1 del problema 2.2 usando `with-select`.

### Problema 3.2
Implementar un decodificador BCD a 7 segmentos (ánodo común) usando `with-select`.

### Problema 3.3
Implementar una ALU simple de 4 bits con operaciones:
- "00": A + B
- "01": A - B
- "10": A AND B
- "11": A OR B

### Problema 3.4
¿Cuándo es preferible usar `with-select` sobre `when-else`?

---

## Nivel 4: Comparación

### Problema 4.1
Convertir de `when-else` a `with-select`:
```vhdl
output <= "00" when input = '0' else
          "01" when input = '1' else
          "11";
```

### Problema 4.2
Convertir de `with-select` a `when-else`:
```vhdl
with sel select
    y <= a when "00",
         b when "01",
         c when "10",
         d when others;
```

### Problema 4.3
Implementar un codificador de prioridad 4:2. ¿`when-else` o `with-select`?

---

## Nivel 5: for-generate

### Problema 5.1
Usar `for-generate` para crear 8 inversores:
```vhdl
signal input, output : std_logic_vector(7 downto 0);
```

### Problema 5.2
Crear un sumador ripple-carry de 4 bits usando `for-generate` e instancias de full_adder.

### Problema 5.3
Crear un registro de desplazamiento de 8 bits usando `for-generate`.

### Problema 5.4
¿Qué error tiene este código?
```vhdl
GEN: for i in 0 to 7 generate
    output(i) <= input(i+1);  -- Desplazamiento
end generate;
```

---

## Nivel 6: if-generate

### Problema 6.1
Usar `if-generate` para incluir un contador de debug solo si `DEBUG = true`.

### Problema 6.2
Implementar un módulo que pueda configurarse para:
- Si `WIDTH = 8`: usar un sumador de 8 bits
- Si `WIDTH = 16`: usar un sumador de 16 bits

### Problema 6.3
¿Por qué las condiciones en `if-generate` deben ser constantes?

---

## Nivel 7: Combinaciones

### Problema 7.1
Diseñar un barrel shifter de 8 bits que pueda:
- Desplazar 0, 1, 2, o 3 posiciones a la izquierda
- Selector de 2 bits

### Problema 7.2
Diseñar un circuito detector de paridad para un byte.

### Problema 7.3
Implementar un multiplexor 8:1 jerárquicamente usando:
- Un nivel de cuatro mux 2:1
- Un segundo nivel de dos mux 2:1
- Un tercer nivel de un mux 2:1

---

## Nivel 8: Tristate y Buses

### Problema 8.1
Implementar un buffer tristate de 8 bits con:
- data_in: entrada de 8 bits
- oe: output enable
- data_out: salida tristate

### Problema 8.2
Diseñar un bus compartido donde 4 dispositivos pueden escribir:
```vhdl
signal device_data : array (0 to 3) of std_logic_vector(7 downto 0);
signal device_en   : std_logic_vector(3 downto 0);
signal bus         : std_logic_vector(7 downto 0);
```

### Problema 8.3
¿Por qué no se pueden tener múltiples drivers sin usar 'Z'?

---

## Nivel 9: Optimización

### Problema 9.1
Simplificar este código manteniendo la funcionalidad:
```vhdl
y <= '1' when a = '1' and b = '0' else
     '1' when a = '0' and b = '1' else
     '0' when a = '0' and b = '0' else
     '0';
```

### Problema 9.2
¿Qué circuito infiere este código?
```vhdl
with sel select
    y <= a when "000",
         a when "001",
         b when "010",
         b when "011",
         c when others;
```

### Problema 9.3
Reescribir usando menos líneas el código del problema 9.2.

---

## Nivel 10: Diseño Completo

### Problema 10.1
Diseñar una unidad de control de semáforo con:
- Estados: VERDE, AMARILLO, ROJO (codificados en 2 bits)
- Salidas: luz_verde, luz_amarilla, luz_roja
- Temporizadores para cada estado

### Problema 10.2
Diseñar un controlador de display 7 segmentos multiplexado para 4 dígitos:
- Entrada: 16 bits (4 dígitos BCD)
- Salidas: segmentos (7 bits), ánodo activo (4 bits)
- Usar contador para multiplexar

### Problema 10.3
Diseñar un router de paquetes simple:
- 4 puertos de entrada (8 bits cada uno)
- 4 puertos de salida (8 bits cada uno)
- Selector de destino (2 bits por puerto)
- Usar `for-generate` para los 4 canales

---

<!-- IA_CONTEXT
PROPÓSITO: Ejercicios sobre sentencias concurrentes VHDL
RESPUESTAS: Ver archivo solutions/VHDL-04-Respuestas.md
HERRAMIENTAS: ModelSim, GHDL, Quartus, Vivado
-->
