<!--
::METADATA::
type: problem
topic_id: vhdl-01-introduccion
file_id: problemas-introduccion-vhdl
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [ejercicios, VHDL, introduccion, sintaxis]
search_keywords: "ejercicios, problemas, VHDL, introducción"
-->

> 🏠 **Navegación:** [← Métodos](../methods/VHDL-01-Metodos-EstructuraBasica.md) | [Respuestas →](../solutions/VHDL-01-Respuestas.md)

---

# Problemas: Introducción a VHDL

## Nivel 1: Conceptos Básicos

### Problema 1.1
Responder:
- a) ¿Qué significan las siglas VHDL y VHSIC?
- b) ¿Cuál es el estándar IEEE actual de VHDL?
- c) Mencionar 3 ventajas de usar VHDL

### Problema 1.2
Indicar si las siguientes afirmaciones son verdaderas o falsas:
- a) VHDL es sensible a mayúsculas/minúsculas
- b) Las sentencias en VHDL se ejecutan en paralelo por defecto
- c) VHDL es un lenguaje de programación como C
- d) std_logic puede tener más de 2 valores

### Problema 1.3
Identificar los errores en los siguientes identificadores:
```vhdl
signal 1_contador : integer;
signal valor__doble : std_logic;
signal salida_ : std_logic;
signal mi-senal : std_logic;
signal Contador_8bits : integer;
```

---

## Nivel 2: Tipos de Datos Básicos

### Problema 2.1
Para el tipo `std_logic`, indicar qué representa cada valor:
- a) '0' y '1'
- b) 'Z'
- c) 'U'
- d) '-'
- e) 'X'

### Problema 2.2
Declarar las siguientes señales:
- a) Un bit de enable
- b) Un bus de datos de 8 bits
- c) Una señal de reloj
- d) Un contador de 4 bits
- e) Un flag de error

### Problema 2.3
¿Cuál es la diferencia entre `std_logic_vector(7 downto 0)` y `std_logic_vector(0 to 7)`? ¿Cuál se usa más comúnmente?

---

## Nivel 3: Estructura de Archivos

### Problema 3.1
Ordenar correctamente las siguientes secciones de un archivo VHDL:
- [ ] architecture
- [ ] port
- [ ] library
- [ ] entity
- [ ] use

### Problema 3.2
Completar el código para una compuerta OR de 2 entradas:

```vhdl
library ______;
use IEEE.____________.ALL;

entity compuerta_or is
    ______ (
        A : __ std_logic;
        B : __ std_logic;
        Y : ___ std_logic
    );
end entity _________;

architecture _________ of compuerta_or is
begin
    Y <= _________;
end architecture;
```

### Problema 3.3
Identificar y corregir los errores en el siguiente código:

```vhdl
library IEEE
use IEEE.STD_LOGIC_1164.ALL

entity mi_modulo
    port (
        entrada in std_logic;
        salida out std_logic,
    )
end mi_modulo

architecture behavioral of mi_modulo
begin
    salida = entrada
end behavioral
```

---

## Nivel 4: Operadores

### Problema 4.1
Evaluar las siguientes expresiones:
- a) `'1' and '0'`
- b) `'1' or '0'`
- c) `'1' xor '1'`
- d) `not '0'`
- e) `'1' nand '1'`

### Problema 4.2
¿Cuál es el resultado de?
```vhdl
signal A : std_logic_vector(3 downto 0) := "1010";
signal B : std_logic_vector(3 downto 0) := "1100";
signal C : std_logic_vector(3 downto 0);

C <= A and B;   -- ¿Resultado?
C <= A or B;    -- ¿Resultado?
C <= A xor B;   -- ¿Resultado?
C <= not A;     -- ¿Resultado?
```

### Problema 4.3
Escribir la expresión VHDL para:
- a) F = A·B + C
- b) F = (A + B)·(C + D)
- c) F = A ⊕ B ⊕ C
- d) F = NOT(A·B)

---

## Nivel 5: Asignación de Señales

### Problema 5.1
Escribir el código VHDL para un multiplexor 4:1 usando:
- a) Sentencia `when-else`
- b) Sentencia `with-select`

### Problema 5.2
Implementar un decodificador 2:4 con enable usando asignación concurrente.

### Problema 5.3
¿Cuál es la diferencia entre estas dos asignaciones?
```vhdl
-- Asignación 1
Y <= A and B;

-- Asignación 2
process(A, B)
begin
    Y <= A and B;
end process;
```

---

## Nivel 6: Bibliotecas

### Problema 6.1
¿Qué biblioteca(s) necesitas incluir para usar?
- a) `std_logic`
- b) `unsigned`
- c) `integer`
- d) `signed`

### Problema 6.2
Escribir las declaraciones de biblioteca para:
- a) Un módulo que usa solo lógica combinacional básica
- b) Un módulo que hace operaciones aritméticas con vectores
- c) Un módulo que usa std_logic y aritmética

### Problema 6.3
¿Por qué no se recomienda usar `IEEE.STD_LOGIC_ARITH` y `IEEE.STD_LOGIC_UNSIGNED`?

---

## Nivel 7: Entidad y Arquitectura

### Problema 7.1
Diseñar la entidad para:
- a) Un flip-flop D con reset asíncrono
- b) Un registro de 8 bits con load y clear
- c) Un sumador de 4 bits con carry in y carry out

### Problema 7.2
Un módulo tiene:
- 2 entradas de 8 bits (A, B)
- 1 entrada de control de 3 bits (op)
- 1 salida de 8 bits (result)
- 1 salida de flags de 4 bits (flags)

Escribir la declaración de entidad completa.

### Problema 7.3
¿Cuál es la diferencia entre `out` y `buffer` en la declaración de puertos? ¿Cuál se recomienda usar?

---

## Nivel 8: Componentes

### Problema 8.1
Dado un componente `half_adder` con puertos (a, b : in; sum, carry : out), escribir:
- a) La declaración del componente
- b) La instanciación para crear un sumador completo

### Problema 8.2
Crear un módulo que instancie 4 flip-flops D para formar un registro de 4 bits.

### Problema 8.3
¿Cuál es la diferencia entre instanciación con port map posicional y nominal? Dar ejemplo de cada una.

---

## Nivel 9: Testbench Básico

### Problema 9.1
Escribir un testbench para una compuerta AND de 2 entradas que pruebe todas las combinaciones posibles.

### Problema 9.2
Para un flip-flop D, escribir un testbench que:
- a) Genere un reloj de 100 MHz
- b) Aplique reset por 50 ns
- c) Cambie la entrada D varias veces
- d) Verifique la salida Q

### Problema 9.3
¿Por qué un testbench no tiene puertos en su entidad?

---

## Nivel 10: Integración

### Problema 10.1
Diseñar completamente (entidad + arquitectura) un módulo que implemente:
$$Y = A \cdot B + \overline{C} \cdot D$$

### Problema 10.2
Diseñar un comparador de 4 bits con salidas:
- EQ (igual)
- GT (mayor que)
- LT (menor que)

### Problema 10.3
Crear un proyecto completo con:
- Módulo: decodificador BCD a 7 segmentos
- Testbench que pruebe los dígitos 0-9

---

<!-- IA_CONTEXT
PROPÓSITO: Ejercicios introductorios de VHDL
RESPUESTAS: Ver archivo solutions/VHDL-01-Respuestas.md
HERRAMIENTAS: ModelSim, GHDL, Quartus, Vivado
-->
