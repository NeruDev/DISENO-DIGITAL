<!--
::METADATA::
type: reference
topic_id: vhdl-03-tipos-datos
file_id: resumen-tipos-datos
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [cheatsheet, VHDL, tipos, conversiones]
search_keywords: "resumen, tipos datos, conversiones, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./02-03-Intro.md)

---

# 📋 Cheatsheet: Tipos de Datos VHDL

## Bibliotecas Necesarias

```vhdl
library ieee;
use ieee.std_logic_1164.all;  -- std_logic
use ieee.numeric_std.all;      -- unsigned, signed
```

---

## std_logic (9 valores)

| Valor | Significado | Sint. |
|-------|-------------|-------|
| `'0'` | Cero fuerte | ✓ |
| `'1'` | Uno fuerte | ✓ |
| `'Z'` | Alta impedancia | ✓ |
| `'L'` | Cero débil | ✓ |
| `'H'` | Uno débil | ✓ |
| `'-'` | Don't care | ✓ |
| `'U'` | No inicializado | ✗ |
| `'X'` | Desconocido | ✗ |
| `'W'` | Débil desconocido | ✗ |

---

## Declaraciones Comunes

```vhdl
signal clk  : std_logic;
signal data : std_logic_vector(7 downto 0);
signal cnt  : unsigned(7 downto 0);
signal val  : signed(15 downto 0);
signal idx  : integer range 0 to 255;
```

---

## Rangos de Valores

| Tipo (8 bits) | Rango |
|---------------|-------|
| `unsigned(7 downto 0)` | 0 a 255 |
| `signed(7 downto 0)` | -128 a +127 |

---

## Conversiones

```
std_logic_vector ←→ unsigned ←→ integer
       ↕
     signed ←————————————→ integer
```

### Tabla de Conversiones

| De → A | Función |
|--------|---------|
| slv → unsigned | `unsigned(slv)` |
| slv → signed | `signed(slv)` |
| unsigned → slv | `std_logic_vector(uns)` |
| signed → slv | `std_logic_vector(sgn)` |
| int → unsigned | `to_unsigned(int, bits)` |
| int → signed | `to_signed(int, bits)` |
| unsigned → int | `to_integer(uns)` |
| signed → int | `to_integer(sgn)` |

### Ejemplo Completo

```vhdl
-- Integer a std_logic_vector
slv <= std_logic_vector(to_unsigned(100, 8));

-- std_logic_vector a Integer
int_val <= to_integer(unsigned(slv));
```

---

## Asignaciones de Vectores

```vhdl
data <= "10110011";         -- Binario
data <= x"B3";              -- Hexadecimal
data <= (others => '0');    -- Todos ceros
data <= (7 => '1', others => '0');  -- Solo bit 7
```

---

## Slicing (Extracción)

```vhdl
signal word : std_logic_vector(15 downto 0);

msb     <= word(15);           -- 1 bit
hi_byte <= word(15 downto 8);  -- 8 bits
lo_byte <= word(7 downto 0);   -- 8 bits
```

---

## Concatenación

```vhdl
word <= hi_byte & lo_byte;
extended <= "0000" & nibble;
```

---

## Tipos Enumerados

```vhdl
type state_t is (IDLE, RUN, STOP);
signal state : state_t := IDLE;
```

---

## Arrays

```vhdl
-- Definir tipo
type mem_t is array (0 to 255) of std_logic_vector(7 downto 0);

-- Declarar y usar
signal mem : mem_t;
mem(0) <= x"FF";
dato <= mem(addr);
```

---

## Records

```vhdl
type bus_t is record
    addr : std_logic_vector(15 downto 0);
    data : std_logic_vector(7 downto 0);
    wr   : std_logic;
end record;

signal bus : bus_t;
bus.addr <= x"1234";
```

---

## Atributos Útiles

| Atributo | Para `x(7 downto 0)` |
|----------|----------------------|
| `x'left` | 7 |
| `x'right` | 0 |
| `x'high` | 7 |
| `x'low` | 0 |
| `x'length` | 8 |
| `x'range` | `7 downto 0` |

---

## Resize (Cambiar Tamaño)

```vhdl
-- Extender (zero-extend para unsigned)
u16 <= resize(u8, 16);

-- Truncar
u8 <= resize(u16, 8);
```

---

## ❌ Evitar

```vhdl
-- NO usar estas bibliotecas
use ieee.std_logic_unsigned.all;
use ieee.std_logic_arith.all;
```

## ✓ Usar

```vhdl
use ieee.numeric_std.all;
```

---

## Errores Comunes

| Error | Solución |
|-------|----------|
| `slv + 1` | `unsigned(slv) + 1` |
| `int` a `slv` | `std_logic_vector(to_unsigned(int, n))` |
| Tamaños no coinciden | Verificar 'length |

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante desarrollo VHDL
-->
