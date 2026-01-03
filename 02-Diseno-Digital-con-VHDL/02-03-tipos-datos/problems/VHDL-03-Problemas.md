<!--
::METADATA::
type: problem
topic_id: vhdl-03-tipos-datos
file_id: problemas-tipos-datos
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [ejercicios, VHDL, tipos, conversiones]
search_keywords: "ejercicios, problemas, tipos datos VHDL"
-->

> 🏠 **Navegación:** [← Métodos](../methods/VHDL-03-Metodos-TiposDatos.md) | [Respuestas →](../solutions/VHDL-03-Respuestas.md)

---

# Problemas: Tipos de Datos

## Nivel 1: std_logic Básico

### Problema 1.1
¿Cuáles son los 9 valores posibles de `std_logic`? ¿Cuáles son sintetizables?

### Problema 1.2
¿Qué resultado da `'0' and 'Z'` según la tabla de resolución?

### Problema 1.3
Declarar señales para:
- Una señal de reloj
- Un reset activo bajo
- Un bus bidireccional de 8 bits
- Una señal de habilitación

---

## Nivel 2: std_logic_vector

### Problema 2.1
Escribir las declaraciones para:
- Un bus de datos de 16 bits
- Un bus de direcciones de 32 bits
- Un registro de 4 bits

### Problema 2.2
Dado `signal data : std_logic_vector(15 downto 0)`:
- Extraer el nibble más significativo
- Extraer los bits 7 a 4
- Extraer el bit menos significativo

### Problema 2.3
¿Cuál es la diferencia entre `(7 downto 0)` y `(0 to 7)`?

### Problema 2.4
Escribir las asignaciones para:
```vhdl
signal byte : std_logic_vector(7 downto 0);
```
- a) Valor binario 10110011
- b) Valor hexadecimal A5
- c) Todos los bits a '1'
- d) Solo el bit 5 a '1', resto '0'

---

## Nivel 3: unsigned y signed

### Problema 3.1
Declarar:
- Un contador de 8 bits sin signo
- Un valor con signo de 16 bits
- Un offset que puede ser negativo (-128 a +127)

### Problema 3.2
¿Qué rango de valores pueden tener?
- `unsigned(7 downto 0)`
- `signed(7 downto 0)`
- `unsigned(15 downto 0)`
- `signed(15 downto 0)`

### Problema 3.3
Escribir el código para incrementar un contador unsigned:
```vhdl
signal contador : unsigned(7 downto 0);
```

### Problema 3.4
¿Por qué este código da error?
```vhdl
signal cnt : std_logic_vector(7 downto 0);
cnt <= cnt + 1;
```

---

## Nivel 4: Conversiones

### Problema 4.1
Completar las conversiones:
```vhdl
signal slv : std_logic_vector(7 downto 0);
signal uns : unsigned(7 downto 0);
signal sgn : signed(7 downto 0);
signal int_val : integer;

-- slv a unsigned
uns <= ________(slv);

-- unsigned a slv
slv <= ____________(uns);

-- integer a unsigned (8 bits)
uns <= ____________(int_val, 8);

-- unsigned a integer
int_val <= ____________(uns);
```

### Problema 4.2
Convertir el valor integer 200 a `std_logic_vector(7 downto 0)`.

### Problema 4.3
Convertir `std_logic_vector(7 downto 0)` a integer.

### Problema 4.4
¿Qué biblioteca debe importarse para usar `to_unsigned`, `to_signed`, `to_integer`?

---

## Nivel 5: Integer y Rangos

### Problema 5.1
Declarar un integer que solo puede valer de 0 a 255.

### Problema 5.2
¿Por qué se recomienda especificar el rango de un integer para síntesis?

### Problema 5.3
¿Cuál es la diferencia entre `natural` y `positive`?

### Problema 5.4
Un contador necesita contar de 0 a 999. ¿Qué declaración es mejor?
```vhdl
-- Opción A
signal cnt : integer;

-- Opción B
signal cnt : integer range 0 to 999;

-- Opción C
signal cnt : unsigned(9 downto 0);
```

---

## Nivel 6: Tipos Enumerados

### Problema 6.1
Definir un tipo enumerado para una máquina de estados con: IDLE, READ, WRITE, DONE.

### Problema 6.2
Declarar una señal del tipo creado en 6.1 con valor inicial IDLE.

### Problema 6.3
Escribir un case usando el tipo enumerado:
```vhdl
type estado_t is (IDLE, READ, WRITE, DONE);
signal estado : estado_t;
```

### Problema 6.4
¿Qué ventajas tienen los tipos enumerados sobre usar `std_logic_vector` para estados?

---

## Nivel 7: Arrays

### Problema 7.1
Definir un tipo array para una memoria ROM de 256 posiciones de 8 bits.

### Problema 7.2
Inicializar un array pequeño (4 elementos) con valores específicos.

### Problema 7.3
Declarar una matriz 2D de 4x4 elementos de 8 bits.

### Problema 7.4
Acceder al elemento [2][3] de la matriz del problema 7.3.

---

## Nivel 8: Records

### Problema 8.1
Definir un record para representar un píxel con campos R, G, B de 8 bits cada uno.

### Problema 8.2
Declarar una señal del tipo pixel y asignar valores a cada campo.

### Problema 8.3
Crear un record para un bus simple con:
- address: 16 bits
- data: 8 bits
- write_enable: 1 bit
- chip_select: 1 bit

### Problema 8.4
Hacer asignación completa (aggregate) al record del problema 8.3.

---

## Nivel 9: Atributos

### Problema 9.1
Dado `signal data : std_logic_vector(15 downto 0)`, ¿cuál es el valor de?
- `data'left`
- `data'right`
- `data'high`
- `data'low`
- `data'length`

### Problema 9.2
Escribir un bucle que itere sobre todos los bits de un vector usando atributos.

### Problema 9.3
Dado el tipo:
```vhdl
type color is (RED, GREEN, BLUE, YELLOW);
```
¿Cuál es el valor de `color'pos(BLUE)`?

---

## Nivel 10: Integración

### Problema 10.1
Diseñar una ALU de 8 bits que:
- Use `unsigned` para operaciones
- Tenga entradas A, B como `std_logic_vector`
- Salida como `std_logic_vector`
- Incluya las conversiones necesarias

### Problema 10.2
Crear un package con:
- Constante de ancho de bus
- Subtipo para el bus
- Tipo array para memoria
- Record para interfaz de bus

### Problema 10.3
Implementar una memoria RAM usando:
- Tipo array para almacenamiento
- Record para la interfaz
- Conversiones apropiadas

---

<!-- IA_CONTEXT
PROPÓSITO: Ejercicios sobre tipos de datos VHDL
RESPUESTAS: Ver archivo solutions/VHDL-03-Respuestas.md
HERRAMIENTAS: ModelSim, GHDL, Quartus, Vivado
-->
