<!--
::METADATA::
type: solution
topic_id: vhdl-01-introduccion
file_id: respuestas-introduccion-vhdl
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [respuestas, soluciones, VHDL]
search_keywords: "respuestas, soluciones, VHDL, introducción"
-->

> 🏠 **Navegación:** [← Problemas](../problems/VHDL-01-Problemas.md)

---

# Respuestas: Introducción a VHDL

## Nivel 1: Conceptos Básicos

### Respuestas 1.1

**a)** VHDL = VHSIC Hardware Description Language
    VHSIC = Very High Speed Integrated Circuit

**b)** IEEE 1076-2019 (la más reciente), aunque IEEE 1076-2008 es muy usada

**c)** Ventajas:
- Independencia de tecnología
- Simulación antes de fabricar
- Documentación implícita
- Reutilización de componentes
- Estándar internacional

### Respuestas 1.2

- a) **FALSO** - VHDL NO es sensible a mayúsculas
- b) **VERDADERO** - Las sentencias fuera de process son concurrentes
- c) **FALSO** - Es un HDL, describe hardware, no es secuencial como C
- d) **VERDADERO** - std_logic tiene 9 valores posibles

### Respuestas 1.3

```vhdl
signal 1_contador : integer;      -- ERROR: comienza con número
signal valor__doble : std_logic;  -- ERROR: doble guión bajo
signal salida_ : std_logic;       -- ERROR: termina con guión bajo
signal mi-senal : std_logic;      -- ERROR: guión medio (no permitido)
signal Contador_8bits : integer;  -- CORRECTO
```

---

## Nivel 2: Tipos de Datos Básicos

### Respuestas 2.1

- a) '0' y '1': Cero y uno fuertes (valores lógicos normales)
- b) 'Z': Alta impedancia (tri-state)
- c) 'U': No inicializado (uninitialized)
- d) '-': Don't care (indiferente)
- e) 'X': Desconocido fuerte (conflicto o indeterminado)

### Respuestas 2.2

```vhdl
signal enable     : std_logic;                      -- a) Bit de enable
signal data_bus   : std_logic_vector(7 downto 0);   -- b) Bus 8 bits
signal clk        : std_logic;                      -- c) Reloj
signal counter    : std_logic_vector(3 downto 0);   -- d) Contador 4 bits
signal error_flag : std_logic;                      -- e) Flag de error
```

### Respuestas 2.3

- `(7 downto 0)`: Bit 7 es MSB, bit 0 es LSB (convención big-endian)
- `(0 to 7)`: Bit 0 es MSB, bit 7 es LSB (convención little-endian)

**Se usa más comúnmente `downto`** porque coincide con la convención de buses de datos donde el bit más significativo tiene índice mayor.

---

## Nivel 3: Estructura de Archivos

### Respuestas 3.1

Orden correcto:
1. library
2. use
3. entity
4. port
5. architecture

### Respuestas 3.2

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity compuerta_or is
    port (
        A : in  std_logic;
        B : in  std_logic;
        Y : out std_logic
    );
end entity compuerta_or;

architecture behavioral of compuerta_or is
begin
    Y <= A or B;
end architecture behavioral;
```

### Respuestas 3.3

```vhdl
library IEEE;                           -- Faltaba ;
use IEEE.STD_LOGIC_1164.ALL;           -- Faltaba ;

entity mi_modulo is                     -- Faltaba 'is'
    port (
        entrada : in  std_logic;        -- Faltaba :
        salida  : out std_logic         -- Cambiado , por nada (última línea)
    );                                  -- Faltaba ;
end entity mi_modulo;                   -- Agregado entity

architecture behavioral of mi_modulo is -- Faltaba 'is'
begin
    salida <= entrada;                  -- Cambiado = por <=
end architecture behavioral;            -- Agregado architecture
```

---

## Nivel 4: Operadores

### Respuestas 4.1

- a) `'1' and '0'` = **'0'**
- b) `'1' or '0'` = **'1'**
- c) `'1' xor '1'` = **'0'**
- d) `not '0'` = **'1'**
- e) `'1' nand '1'` = **'0'**

### Respuestas 4.2

```vhdl
A = "1010", B = "1100"

C <= A and B;   -- "1000"
C <= A or B;    -- "1110"
C <= A xor B;   -- "0110"
C <= not A;     -- "0101"
```

### Respuestas 4.3

```vhdl
-- a) F = A·B + C
F <= (A and B) or C;

-- b) F = (A + B)·(C + D)
F <= (A or B) and (C or D);

-- c) F = A ⊕ B ⊕ C
F <= A xor B xor C;

-- d) F = NOT(A·B)
F <= not (A and B);
-- o también:
F <= A nand B;
```

---

## Nivel 5: Asignación de Señales

### Respuestas 5.1

**a) Con when-else:**
```vhdl
Y <= D0 when sel = "00" else
     D1 when sel = "01" else
     D2 when sel = "10" else
     D3;
```

**b) Con with-select:**
```vhdl
with sel select
    Y <= D0 when "00",
         D1 when "01",
         D2 when "10",
         D3 when others;
```

### Respuestas 5.2

```vhdl
-- Decodificador 2:4 con enable
Y(0) <= enable and (not A(1)) and (not A(0));
Y(1) <= enable and (not A(1)) and A(0);
Y(2) <= enable and A(1) and (not A(0));
Y(3) <= enable and A(1) and A(0);
```

### Respuestas 5.3

**Funcionalmente son equivalentes.** Ambas crean lógica combinacional.

La diferencia está en el estilo:
- Primera: asignación concurrente directa
- Segunda: dentro de proceso (más típico para lógica secuencial)

Para combinacional simple, la primera es preferida por claridad.

---

## Nivel 6: Bibliotecas

### Respuestas 6.1

- a) `std_logic` → `IEEE.STD_LOGIC_1164`
- b) `unsigned` → `IEEE.NUMERIC_STD`
- c) `integer` → No necesita biblioteca (tipo primitivo)
- d) `signed` → `IEEE.NUMERIC_STD`

### Respuestas 6.2

```vhdl
-- a) Lógica combinacional básica
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- b) Operaciones aritméticas con vectores
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

-- c) std_logic y aritmética
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
```

### Respuestas 6.3

`STD_LOGIC_ARITH` y `STD_LOGIC_UNSIGNED` son bibliotecas de Synopsys, **no son estándar IEEE**. Pueden causar conflictos y no son portables.

**Usar siempre `NUMERIC_STD`** que es el estándar IEEE.

---

## Nivel 7: Entidad y Arquitectura

### Respuestas 7.1

```vhdl
-- a) Flip-flop D con reset asíncrono
entity ff_d is
    port (
        clk   : in  std_logic;
        rst   : in  std_logic;
        d     : in  std_logic;
        q     : out std_logic
    );
end entity;

-- b) Registro 8 bits con load y clear
entity registro8 is
    port (
        clk   : in  std_logic;
        clear : in  std_logic;
        load  : in  std_logic;
        d     : in  std_logic_vector(7 downto 0);
        q     : out std_logic_vector(7 downto 0)
    );
end entity;

-- c) Sumador 4 bits
entity adder4 is
    port (
        a     : in  std_logic_vector(3 downto 0);
        b     : in  std_logic_vector(3 downto 0);
        cin   : in  std_logic;
        sum   : out std_logic_vector(3 downto 0);
        cout  : out std_logic
    );
end entity;
```

### Respuestas 7.2

```vhdl
entity alu is
    port (
        A      : in  std_logic_vector(7 downto 0);
        B      : in  std_logic_vector(7 downto 0);
        op     : in  std_logic_vector(2 downto 0);
        result : out std_logic_vector(7 downto 0);
        flags  : out std_logic_vector(3 downto 0)
    );
end entity alu;
```

### Respuestas 7.3

- `out`: Solo escritura desde dentro del módulo
- `buffer`: Salida que puede leerse internamente

**Se recomienda `out`** y usar una señal interna si se necesita leer el valor:
```vhdl
signal q_internal : std_logic;
...
q <= q_internal;  -- Asignar a salida
-- Usar q_internal dentro del módulo
```

---

## Nivel 8: Componentes

### Respuestas 8.1

```vhdl
-- a) Declaración
component half_adder is
    port (
        a, b     : in  std_logic;
        sum, carry : out std_logic
    );
end component;

-- b) Sumador completo con 2 half adders
signal s1, c1, c2 : std_logic;

HA1: half_adder port map (
    a => A, b => B, sum => s1, carry => c1
);
HA2: half_adder port map (
    a => s1, b => Cin, sum => Sum, carry => c2
);
Cout <= c1 or c2;
```

### Respuestas 8.3

```vhdl
-- Posicional (por orden)
inst1: componente port map (clk, reset, data_in, data_out);

-- Nominal (por nombre) - RECOMENDADO
inst2: componente port map (
    clk      => clk,
    reset    => reset,
    data_in  => data_in,
    data_out => data_out
);
```

Nominal es más claro y menos propenso a errores.

---

## Nivel 9: Testbench Básico

### Respuestas 9.1

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_and_gate is
end entity;

architecture sim of tb_and_gate is
    signal A, B, Y : std_logic;
begin
    DUT: entity work.and_gate port map (A, B, Y);
    
    process
    begin
        A <= '0'; B <= '0'; wait for 10 ns;  -- Y = 0
        A <= '0'; B <= '1'; wait for 10 ns;  -- Y = 0
        A <= '1'; B <= '0'; wait for 10 ns;  -- Y = 0
        A <= '1'; B <= '1'; wait for 10 ns;  -- Y = 1
        wait;
    end process;
end architecture;
```

### Respuestas 9.3

Un testbench no tiene puertos porque no se conecta a nada externo. Es el nivel más alto de la jerarquía de simulación y genera sus propios estímulos internamente.

---

## Nivel 10: Integración

### Respuestas 10.1

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity funcion_logica is
    port (
        A, B, C, D : in  std_logic;
        Y          : out std_logic
    );
end entity;

architecture behavioral of funcion_logica is
begin
    Y <= (A and B) or ((not C) and D);
end architecture;
```

### Respuestas 10.2

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity comparador4 is
    port (
        A, B : in  std_logic_vector(3 downto 0);
        EQ   : out std_logic;
        GT   : out std_logic;
        LT   : out std_logic
    );
end entity;

architecture behavioral of comparador4 is
begin
    EQ <= '1' when A = B else '0';
    GT <= '1' when unsigned(A) > unsigned(B) else '0';
    LT <= '1' when unsigned(A) < unsigned(B) else '0';
end architecture;
```

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para ejercicios introductorios de VHDL
NOTA: Pueden existir soluciones alternativas válidas
-->
