<!--
::METADATA::
type: reference
topic_id: vhdl-01-introduccion
file_id: resumen-formulas-intro-vhdl
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [cheatsheet, VHDL, referencia, sintaxis]
search_keywords: "resumen, fórmulas, VHDL, cheatsheet, referencia rápida"
-->

> 🏠 **Navegación:** [← Volver al Índice](./02-01-Intro.md)

---

# 📋 Cheatsheet: Introducción a VHDL

## Estructura Básica

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity nombre is
    port (
        entrada : in  std_logic;
        salida  : out std_logic
    );
end entity;

architecture behavioral of nombre is
begin
    -- implementación
end architecture;
```

---

## Bibliotecas Esenciales

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;  -- std_logic
use IEEE.NUMERIC_STD.ALL;      -- unsigned, signed
```

⚠️ **NO usar:** `STD_LOGIC_ARITH`, `STD_LOGIC_UNSIGNED`

---

## Tipos de Datos Comunes

| Tipo | Uso |
|------|-----|
| `std_logic` | 1 bit |
| `std_logic_vector(n downto 0)` | n+1 bits |
| `unsigned(n downto 0)` | Aritmética sin signo |
| `signed(n downto 0)` | Aritmética con signo |
| `integer` | Números enteros |
| `boolean` | true/false |

---

## Valores de std_logic

| Valor | Significado |
|-------|-------------|
| '0' | Cero fuerte |
| '1' | Uno fuerte |
| 'Z' | Alta impedancia |
| '-' | Don't care |
| 'U' | No inicializado |
| 'X' | Desconocido |

---

## Modos de Puerto

| Modo | Descripción |
|------|-------------|
| `in` | Entrada (solo lectura) |
| `out` | Salida (solo escritura) |
| `inout` | Bidireccional |
| `buffer` | Salida legible (evitar) |

---

## Operadores

### Lógicos
```vhdl
and, or, nand, nor, xor, xnor, not
```

### Relacionales
```vhdl
=  /=  <  <=  >  >=
```

### Aritméticos
```vhdl
+  -  *  /  mod  rem  **  abs
```

### Concatenación
```vhdl
&    -- "01" & "10" = "0110"
```

---

## Asignación de Señales

### Concurrente
```vhdl
Y <= A and B;
```

### Condicional (when-else)
```vhdl
Y <= A when sel = '1' else B;
```

### Selectiva (with-select)
```vhdl
with sel select
    Y <= A when "00",
         B when "01",
         C when others;
```

---

## Declaraciones

### Señales
```vhdl
signal nombre : tipo := valor_inicial;
```

### Constantes
```vhdl
constant NOMBRE : tipo := valor;
```

### Variables (solo en process)
```vhdl
variable nombre : tipo := valor_inicial;
```

---

## Literales

```vhdl
'1'           -- std_logic
"1010"        -- std_logic_vector
x"A5"         -- hexadecimal
b"1010_0101"  -- binario con separador
o"127"        -- octal
```

---

## Conversiones

```vhdl
-- std_logic_vector ↔ unsigned
unsigned(slv)
std_logic_vector(uns)

-- unsigned/signed ↔ integer
to_integer(uns)
to_unsigned(int, width)
to_signed(int, width)
```

---

## Plantilla Testbench

```vhdl
entity tb_nombre is
end entity;

architecture sim of tb_nombre is
    signal clk : std_logic := '0';
    constant PERIOD : time := 10 ns;
begin
    DUT: entity work.nombre
        port map (...);
    
    clk <= not clk after PERIOD/2;
    
    process
    begin
        -- estímulos
        wait;
    end process;
end architecture;
```

---

## Reglas de Nombres

✓ Comenzar con letra
✓ Letras, números, guión bajo
✗ No terminar en `_`
✗ No doble `__`
✗ No guión medio `-`

---

## Comentarios

```vhdl
-- Comentario de línea

/* Comentario
   multilínea (VHDL-2008) */
```

---

## Errores Comunes

| Error | Corrección |
|-------|------------|
| `=` para asignar | Usar `<=` |
| Olvidar `;` | Agregar al final |
| Olvidar `is` | `entity nombre is` |
| Tipos incompatibles | Convertir explícitamente |

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante desarrollo VHDL
-->
