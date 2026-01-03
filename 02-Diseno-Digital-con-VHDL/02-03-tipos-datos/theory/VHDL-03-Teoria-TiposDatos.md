<!--
::METADATA::
type: theory
topic_id: vhdl-03-tipos-datos
file_id: teoria-tipos-datos
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [VHDL, tipos, std_logic, vector, unsigned, signed, array, record]
search_keywords: "tipos de datos, std_logic, std_logic_vector, unsigned, signed"
-->

> 🏠 **Navegación:** [← Volver al Índice](../02-03-Intro.md) | [Métodos →](../methods/VHDL-03-Metodos-TiposDatos.md)

---

# Tipos de Datos en VHDL

## 1. Sistema de Tipos en VHDL

### 1.1 Características

VHDL es un lenguaje **fuertemente tipado**:
- Cada objeto tiene un tipo definido
- No hay conversión implícita entre tipos
- Errores de tipo detectados en compilación

### 1.2 Categorías de Tipos

```
┌─────────────────────────────────────────────────┐
│               TIPOS VHDL                        │
├─────────────────────────────────────────────────┤
│ Escalares    │ bit, boolean, integer, real,    │
│              │ character, enumeration          │
├──────────────┼──────────────────────────────────┤
│ Compuestos   │ array, record                   │
├──────────────┼──────────────────────────────────┤
│ Acceso       │ punteros (no sintetizables)     │
├──────────────┼──────────────────────────────────┤
│ Archivo      │ file (no sintetizables)         │
└─────────────────────────────────────────────────┘
```

---

## 2. Tipo `std_logic`

### 2.1 El Tipo Más Importante

`std_logic` es el tipo estándar para señales digitales. Pertenece a la biblioteca IEEE.

```vhdl
library ieee;
use ieee.std_logic_1164.all;
```

### 2.2 Los 9 Valores de `std_logic`

| Valor | Significado | Sintetizable |
|-------|-------------|--------------|
| `'U'` | No inicializado | Solo simulación |
| `'X'` | Desconocido fuerte | Solo simulación |
| `'0'` | Cero fuerte | ✓ |
| `'1'` | Uno fuerte | ✓ |
| `'Z'` | Alta impedancia | ✓ |
| `'W'` | Desconocido débil | Solo simulación |
| `'L'` | Cero débil (pull-down) | ✓ |
| `'H'` | Uno débil (pull-up) | ✓ |
| `'-'` | Don't care | ✓ |

### 2.3 Uso en Diseño

```vhdl
signal clk     : std_logic;           -- Reloj
signal reset   : std_logic := '0';    -- Con valor inicial
signal bus_en  : std_logic;           -- Control
signal data_io : std_logic;           -- Puede ser 'Z'
```

### 2.4 Tabla de Resolución

Cuando múltiples drivers manejan una señal:

```
  U  X  0  1  Z  W  L  H  -
U U  U  U  U  U  U  U  U  U
X U  X  X  X  X  X  X  X  X
0 U  X  0  X  0  0  0  0  X
1 U  X  X  1  1  1  1  1  X
Z U  X  0  1  Z  W  L  H  X
W U  X  0  1  W  W  W  W  X
L U  X  0  1  L  W  L  W  X
H U  X  0  1  H  W  W  H  X
- U  X  X  X  X  X  X  X  X
```

---

## 3. Tipo `std_logic_vector`

### 3.1 Definición

Array de `std_logic`. Representa buses de datos.

```vhdl
signal byte_data  : std_logic_vector(7 downto 0);   -- 8 bits, MSB=7
signal address    : std_logic_vector(15 downto 0);  -- 16 bits
signal nibble     : std_logic_vector(3 downto 0);   -- 4 bits
```

### 3.2 `downto` vs `to`

| Dirección | MSB | LSB | Uso |
|-----------|-----|-----|-----|
| `(7 downto 0)` | Índice 7 | Índice 0 | **Estándar** |
| `(0 to 7)` | Índice 0 | Índice 7 | Evitar |

### 3.3 Operaciones

```vhdl
-- Acceso a bit individual
bit_5 <= data(5);

-- Acceso a rango (slice)
msb_nibble <= data(7 downto 4);
lsb_nibble <= data(3 downto 0);

-- Concatenación
byte <= nibble_hi & nibble_lo;

-- Asignación completa
data <= "10110011";          -- Binario
data <= x"B3";               -- Hexadecimal
data <= (others => '0');     -- Todos ceros
data <= (7 => '1', others => '0');  -- Solo bit 7
```

---

## 4. Tipos `unsigned` y `signed`

### 4.1 Biblioteca

```vhdl
library ieee;
use ieee.numeric_std.all;
```

### 4.2 Diferencias

| Tipo | Rango (8 bits) | Uso |
|------|----------------|-----|
| `unsigned` | 0 a 255 | Números sin signo |
| `signed` | -128 a +127 | Números con signo (complemento a 2) |

### 4.3 Declaración

```vhdl
signal contador  : unsigned(7 downto 0);
signal offset    : signed(7 downto 0);
signal resultado : signed(15 downto 0);
```

### 4.4 Operaciones Aritméticas

```vhdl
-- Suma y resta
resultado <= a + b;
resultado <= a - 1;

-- Incremento/Decremento
contador <= contador + 1;

-- Multiplicación
producto <= a * b;

-- Comparaciones
if a > b then ...
if contador = 0 then ...

-- Resize (cambiar tamaño)
resultado_16 <= resize(operando_8, 16);
```

---

## 5. Conversiones de Tipos

### 5.1 Diagrama de Conversiones

```
        std_logic_vector
            ↑    ↓
    unsigned ←→ signed
        ↑         ↑
      integer  integer
```

### 5.2 Funciones de Conversión

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- std_logic_vector ←→ unsigned
signal slv : std_logic_vector(7 downto 0);
signal uns : unsigned(7 downto 0);

uns <= unsigned(slv);           -- slv → unsigned
slv <= std_logic_vector(uns);   -- unsigned → slv

-- std_logic_vector ←→ signed
signal sgn : signed(7 downto 0);

sgn <= signed(slv);             -- slv → signed
slv <= std_logic_vector(sgn);   -- signed → slv

-- integer ←→ unsigned/signed
signal int_val : integer;

uns <= to_unsigned(int_val, 8);     -- integer → unsigned
sgn <= to_signed(int_val, 8);       -- integer → signed
int_val <= to_integer(uns);          -- unsigned → integer
int_val <= to_integer(sgn);          -- signed → integer
```

### 5.3 Tabla Resumen

| De | A | Función |
|----|---|---------|
| `std_logic_vector` | `unsigned` | `unsigned(slv)` |
| `std_logic_vector` | `signed` | `signed(slv)` |
| `unsigned` | `std_logic_vector` | `std_logic_vector(uns)` |
| `signed` | `std_logic_vector` | `std_logic_vector(sgn)` |
| `integer` | `unsigned` | `to_unsigned(int, bits)` |
| `integer` | `signed` | `to_signed(int, bits)` |
| `unsigned` | `integer` | `to_integer(uns)` |
| `signed` | `integer` | `to_integer(sgn)` |

---

## 6. Tipos Enteros

### 6.1 Integer

```vhdl
signal contador : integer;                    -- Rango completo
signal indice   : integer range 0 to 255;     -- Rango restringido
signal direccion: integer range 0 to 1023;
```

### 6.2 Natural y Positive

```vhdl
signal nat_val : natural;   -- 0 a INTEGER'HIGH
signal pos_val : positive;  -- 1 a INTEGER'HIGH
```

### 6.3 Rango de Integer

- Mínimo: `INTEGER'LOW` = -(2^31 - 1)
- Máximo: `INTEGER'HIGH` = 2^31 - 1

**Recomendación:** Siempre especificar rango para síntesis.

---

## 7. Tipos Booleanos y Enumerados

### 7.1 Boolean

```vhdl
signal flag : boolean := false;

if flag then      -- No necesita "= true"
if not flag then  -- Negación
```

### 7.2 Tipos Enumerados

```vhdl
-- Definición de tipo
type estado_t is (IDLE, INICIO, PROCESO, FIN);
signal estado : estado_t := IDLE;

-- Uso
case estado is
    when IDLE    => ...
    when INICIO  => ...
    when PROCESO => ...
    when FIN     => ...
end case;
```

### 7.3 Enumerados para FSM

```vhdl
type fsm_state is (
    ST_RESET,
    ST_WAIT,
    ST_READ,
    ST_WRITE,
    ST_DONE
);
signal current_state, next_state : fsm_state;
```

---

## 8. Arrays

### 8.1 Arrays Unidimensionales

```vhdl
-- Tipo array definido por usuario
type byte_array is array (0 to 255) of std_logic_vector(7 downto 0);
signal memoria : byte_array;

-- Acceso
memoria(0) <= x"FF";
dato <= memoria(indice);
```

### 8.2 Arrays Bidimensionales

```vhdl
-- Matriz 4x4 de 8 bits
type matriz_t is array (0 to 3, 0 to 3) of std_logic_vector(7 downto 0);
signal matriz : matriz_t;

-- Acceso
matriz(0, 0) <= x"00";
matriz(fila, columna) <= dato;
```

### 8.3 Arrays sin Límites (Unconstrained)

```vhdl
type slv_array is array (natural range <>) of std_logic_vector(7 downto 0);

-- Al usar, se define el rango
signal mem : slv_array(0 to 15);
```

---

## 9. Records

### 9.1 Definición

```vhdl
type instruccion_t is record
    opcode : std_logic_vector(3 downto 0);
    rs     : std_logic_vector(3 downto 0);
    rt     : std_logic_vector(3 downto 0);
    rd     : std_logic_vector(3 downto 0);
end record;

signal instr : instruccion_t;
```

### 9.2 Acceso a Campos

```vhdl
-- Acceso individual
instr.opcode <= "0001";
codigo <= instr.opcode;

-- Asignación completa
instr <= (opcode => "0001", rs => "0010", rt => "0011", rd => "0100");
```

### 9.3 Records para Interfaces

```vhdl
-- Bus AXI simplificado
type axi_lite_t is record
    addr    : std_logic_vector(31 downto 0);
    data    : std_logic_vector(31 downto 0);
    valid   : std_logic;
    ready   : std_logic;
end record;

signal master : axi_lite_t;
signal slave  : axi_lite_t;
```

---

## 10. Atributos de Tipos

### 10.1 Atributos de Vectores

| Atributo | Significado | Ejemplo (`x(7 downto 0)`) |
|----------|-------------|---------------------------|
| `'left` | Índice izquierdo | 7 |
| `'right` | Índice derecho | 0 |
| `'high` | Índice mayor | 7 |
| `'low` | Índice menor | 0 |
| `'length` | Número de elementos | 8 |
| `'range` | Rango completo | `7 downto 0` |

### 10.2 Uso

```vhdl
for i in data'range loop
    ...
end loop;

constant SIZE : integer := data'length;
```

### 10.3 Atributos de Enumerados

```vhdl
type color is (ROJO, VERDE, AZUL);

color'pos(VERDE)    -- Retorna 1
color'val(2)        -- Retorna AZUL
color'succ(ROJO)    -- Retorna VERDE
color'pred(AZUL)    -- Retorna VERDE
```

---

## Referencias

- IEEE Std 1076-2008
- IEEE Std 1164-1993 (std_logic_1164)
- IEEE Std 1076.3-1997 (numeric_std)

---

<!-- IA_CONTEXT
NIVEL: Intermedio (2/3)
PREREQUISITOS: 02-01, 02-02
CONEXIONES: Fundamental para todo diseño VHDL
ERRORES_COMUNES: Conversiones incorrectas, usar std_logic_arith en lugar de numeric_std
-->
