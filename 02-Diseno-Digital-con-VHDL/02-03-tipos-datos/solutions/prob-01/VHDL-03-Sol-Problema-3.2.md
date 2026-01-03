<!--
::METADATA::
type: detailed_solution
topic_id: vhdl-03-tipos-datos
problem_id: 3.2
file_id: solucion-problema-3-2
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 2
tags: [solucion, VHDL, tipos, conversion]
-->

> 🏠 **Navegación:** [← Problema 3.1](./VHDL-03-Sol-Problema-3.1.md) | [Problema 3.3 →](./VHDL-03-Sol-Problema-3.3.md)

---

# Solución Detallada: Problema 3.2

## Enunciado
Realizar las siguientes conversiones de tipos:
- a) `std_logic_vector` a `integer`
- b) `integer` a `std_logic_vector`
- c) `unsigned` a `signed`
- d) Suma de `std_logic_vector` como unsigned

---

## Bibliotecas Requeridas

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
```

> ⚠️ **Importante:** Usar `NUMERIC_STD`, NO usar `STD_LOGIC_ARITH` (obsoleta).

---

## a) std_logic_vector → integer

### Problema
```vhdl
signal slv : std_logic_vector(7 downto 0) := "10101010";
signal int_val : integer;
```

### Solución (Paso a Paso)

```vhdl
-- Paso 1: Convertir a unsigned
-- Paso 2: Convertir a integer

int_val <= to_integer(unsigned(slv));
```

### Explicación

| Paso | Operación | Resultado |
|------|-----------|-----------|
| Inicial | `"10101010"` | std_logic_vector |
| 1 | `unsigned("10101010")` | unsigned(170) |
| 2 | `to_integer(170)` | integer 170 |

### Para Números con Signo

```vhdl
-- Si el valor es con signo (complemento a 2):
int_val <= to_integer(signed(slv));
-- "10101010" = -86 (como signed)
```

---

## b) integer → std_logic_vector

### Problema
```vhdl
signal int_val : integer := 170;
signal slv : std_logic_vector(7 downto 0);
```

### Solución (Paso a Paso)

```vhdl
-- Paso 1: Convertir integer a unsigned (especificar bits)
-- Paso 2: Convertir unsigned a std_logic_vector

slv <= std_logic_vector(to_unsigned(int_val, 8));
```

### Explicación

| Paso | Operación | Resultado |
|------|-----------|-----------|
| Inicial | `170` | integer |
| 1 | `to_unsigned(170, 8)` | unsigned "10101010" |
| 2 | `std_logic_vector(...)` | slv "10101010" |

### Para Números Negativos

```vhdl
signal int_neg : integer := -86;
signal slv_signed : std_logic_vector(7 downto 0);

slv_signed <= std_logic_vector(to_signed(int_neg, 8));
-- Resultado: "10101010" (complemento a 2 de -86)
```

---

## c) unsigned → signed

### Problema
```vhdl
signal u_val : unsigned(7 downto 0) := "01111111";  -- 127
signal s_val : signed(7 downto 0);
```

### Solución

```vhdl
-- Conversión directa (reinterpretación de bits)
s_val <= signed(u_val);
```

### Análisis

| unsigned | bits | signed (interpretación) |
|:--------:|------|:-----------------------:|
| 127 | "01111111" | +127 |
| 128 | "10000000" | -128 |
| 255 | "11111111" | -1 |

> ⚠️ **Cuidado:** La conversión NO cambia los bits, solo su interpretación.

### Conversión con Extensión de Signo

```vhdl
-- Si necesitas extender de 8 a 16 bits:
signal u8 : unsigned(7 downto 0) := "10000000";  -- 128
signal s16 : signed(15 downto 0);

-- Extensión con ceros (unsigned)
s16 <= signed(resize(u8, 16));  -- 0x0080 = +128

-- Si quisieras extensión de signo:
-- Primero convertir a signed, luego resize
```

---

## d) Suma de std_logic_vector como unsigned

### Problema
```vhdl
signal a, b : std_logic_vector(7 downto 0);
signal sum  : std_logic_vector(7 downto 0);
signal sum_extended : std_logic_vector(8 downto 0);  -- Con carry
```

### Solución

```vhdl
-- Suma sin carry (puede overflow)
sum <= std_logic_vector(unsigned(a) + unsigned(b));

-- Suma con carry (9 bits)
sum_extended <= std_logic_vector(
    resize(unsigned(a), 9) + resize(unsigned(b), 9)
);
-- O equivalente:
sum_extended <= std_logic_vector(('0' & unsigned(a)) + ('0' & unsigned(b)));
```

### Ejemplo Numérico

```vhdl
a <= "11110000";  -- 240
b <= "00010001";  -- 17
-- 240 + 17 = 257

sum <= ...;           -- "00000001" (overflow: 257 mod 256 = 1)
sum_extended <= ...;  -- "100000001" (257 en 9 bits)
```

---

## Resumen de Conversiones

```vhdl
architecture examples of conversions is
    signal slv : std_logic_vector(7 downto 0);
    signal u   : unsigned(7 downto 0);
    signal s   : signed(7 downto 0);
    signal i   : integer;
begin
    -- std_logic_vector ↔ unsigned
    u   <= unsigned(slv);
    slv <= std_logic_vector(u);
    
    -- std_logic_vector ↔ signed  
    s   <= signed(slv);
    slv <= std_logic_vector(s);
    
    -- unsigned ↔ integer
    i <= to_integer(u);
    u <= to_unsigned(i, 8);
    
    -- signed ↔ integer
    i <= to_integer(s);
    s <= to_signed(i, 8);
    
    -- unsigned ↔ signed (mismo ancho)
    s <= signed(u);
    u <= unsigned(s);
end architecture;
```

---

## Diagrama de Conversión Visual

```
                    std_logic_vector
                          │
              ┌───────────┴───────────┐
              │                       │
         unsigned()              signed()
              │                       │
              ▼                       ▼
          unsigned                 signed
              │                       │
      to_integer()            to_integer()
              │                       │
              └───────────┬───────────┘
                          │
                          ▼
                       integer
                          │
              ┌───────────┴───────────┐
              │                       │
    to_unsigned(i,n)          to_signed(i,n)
              │                       │
              ▼                       ▼
          unsigned                 signed
              │                       │
    std_logic_vector()    std_logic_vector()
              │                       │
              └───────────┬───────────┘
                          │
                          ▼
                  std_logic_vector
```

---

## Errores Comunes

| Error | Problema | Solución |
|-------|----------|----------|
| `slv + slv` | No hay operador + para slv | Convertir a unsigned |
| `to_unsigned(i)` | Falta especificar bits | `to_unsigned(i, N)` |
| Mezclar signed/unsigned | Resultado impredecible | Conversión explícita |
| Usar STD_LOGIC_ARITH | Biblioteca obsoleta | Usar NUMERIC_STD |

---

## Conceptos Clave

1. **std_logic_vector**: Solo bits, sin semántica numérica
2. **unsigned/signed**: Tipos con aritmética definida
3. **Conversión de tipo**: NO cambia bits, cambia interpretación
4. **to_integer/to_unsigned**: Funciones de conversión (sí cambian representación)

---

> 💡 **Tip:** Siempre especifica el número de bits en `to_unsigned()` y `to_signed()`. El compilador no puede inferirlo del contexto.
