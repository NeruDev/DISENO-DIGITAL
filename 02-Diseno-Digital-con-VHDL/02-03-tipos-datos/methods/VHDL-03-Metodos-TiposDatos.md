<!--
::METADATA::
type: method
topic_id: vhdl-03-tipos-datos
file_id: metodos-tipos-datos
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [VHDL, metodologia, conversiones, tipos]
search_keywords: "metodología tipos, conversiones VHDL"
-->

> 🏠 **Navegación:** [← Teoría](../theory/VHDL-03-Teoria-TiposDatos.md) | [Problemas →](../problems/VHDL-03-Problemas.md)

---

# Métodos: Tipos de Datos

## Método 1: Selección del Tipo Correcto

### Decisión de Tipo

| Necesidad | Tipo Recomendado |
|-----------|------------------|
| Señal de control simple | `std_logic` |
| Bus de datos sin aritmética | `std_logic_vector` |
| Contador/aritmética sin signo | `unsigned` |
| Aritmética con signo | `signed` |
| Índices de bucle | `integer range ...` |
| Estados de FSM | Tipo enumerado |
| Estructura compleja | `record` |
| Memoria/tabla | `array` |

### Ejemplo de Selección

```vhdl
-- ✗ Incorrecto: aritmética con std_logic_vector
signal cnt : std_logic_vector(7 downto 0);
cnt <= cnt + 1;  -- ERROR sin numeric_std

-- ✓ Correcto: usar unsigned para contadores
signal cnt : unsigned(7 downto 0);
cnt <= cnt + 1;  -- OK
```

---

## Método 2: Conversiones Seguras

### Cadena de Conversión

```vhdl
-- Integer → std_logic_vector
slv <= std_logic_vector(to_unsigned(int_val, slv'length));

-- std_logic_vector → Integer
int_val <= to_integer(unsigned(slv));

-- signed ←→ unsigned (cuidado con el signo)
uns <= unsigned(sgn);  -- Interpreta bits directamente
sgn <= signed(uns);    -- Interpreta bits directamente
```

### Función Auxiliar Segura

```vhdl
-- Conversión segura integer → slv
function int_to_slv(val : integer; width : positive) 
    return std_logic_vector is
begin
    return std_logic_vector(to_unsigned(val, width));
end function;

-- Uso
data <= int_to_slv(100, 8);  -- Convierte 100 a 8 bits
```

---

## Método 3: Evitar Bibliotecas Obsoletas

### ✗ NO Usar

```vhdl
-- EVITAR: bibliotecas no estándar
use ieee.std_logic_unsigned.all;  -- NO
use ieee.std_logic_arith.all;     -- NO
```

### ✓ Usar

```vhdl
-- CORRECTO: biblioteca estándar
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
```

### Razones

- `numeric_std` es el estándar IEEE
- `std_logic_arith` tiene conflictos
- Mejora portabilidad

---

## Método 4: Inicialización de Vectores

### Agregados (Aggregates)

```vhdl
-- Todos ceros
signal data : std_logic_vector(7 downto 0) := (others => '0');

-- Todos unos
signal ones : std_logic_vector(7 downto 0) := (others => '1');

-- Un bit específico
signal one_hot : std_logic_vector(7 downto 0) := (3 => '1', others => '0');

-- Múltiples bits específicos
signal pattern : std_logic_vector(7 downto 0) := (7|5|3|1 => '1', others => '0');
```

### Literales

```vhdl
data <= "10110011";           -- Binario
data <= x"B3";                -- Hexadecimal
data <= o"263";               -- Octal
addr <= 16x"FFFF";            -- Hex con tamaño (VHDL-2008)
```

---

## Método 5: Extensión de Signo

### Para unsigned (zero extend)

```vhdl
signal u8  : unsigned(7 downto 0);
signal u16 : unsigned(15 downto 0);

-- Método 1: resize
u16 <= resize(u8, 16);

-- Método 2: concatenación con ceros
u16 <= x"00" & u8;
```

### Para signed (sign extend)

```vhdl
signal s8  : signed(7 downto 0);
signal s16 : signed(15 downto 0);

-- Método 1: resize (mantiene signo automáticamente)
s16 <= resize(s8, 16);

-- Método 2: replicar bit de signo
s16 <= (15 downto 8 => s8(7)) & s8;
```

---

## Método 6: Truncamiento Seguro

### Truncar unsigned

```vhdl
signal u16 : unsigned(15 downto 0);
signal u8  : unsigned(7 downto 0);

-- Tomar bits bajos
u8 <= u16(7 downto 0);

-- Con resize
u8 <= resize(u16, 8);  -- Advertencia si hay pérdida
```

### Detectar Overflow

```vhdl
-- Verificar si hay pérdida de datos
if u16(15 downto 8) /= x"00" then
    overflow <= '1';
else
    overflow <= '0';
    u8 <= u16(7 downto 0);
end if;
```

---

## Método 7: Definir Tipos en Package

### Crear Package

```vhdl
-- tipos_pkg.vhd
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

package tipos_pkg is
    -- Constantes
    constant DATA_WIDTH : integer := 32;
    constant ADDR_WIDTH : integer := 16;
    
    -- Subtipos
    subtype data_t is std_logic_vector(DATA_WIDTH-1 downto 0);
    subtype addr_t is std_logic_vector(ADDR_WIDTH-1 downto 0);
    
    -- Arrays
    type data_array_t is array (natural range <>) of data_t;
    
    -- Records
    type bus_t is record
        addr  : addr_t;
        data  : data_t;
        valid : std_logic;
    end record;
end package;
```

### Usar Package

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use work.tipos_pkg.all;

entity mi_modulo is
    port (
        bus_in  : in  bus_t;
        bus_out : out bus_t
    );
end entity;
```

---

## Método 8: Comparaciones Correctas

### Comparar std_logic_vector

```vhdl
-- Comparación directa
if slv = "00000000" then ...
if slv = x"00" then ...

-- Comparar con constante
constant ZERO : std_logic_vector(7 downto 0) := (others => '0');
if slv = ZERO then ...
```

### Comparar con Don't Care

```vhdl
-- Usar std_match para comparar con '-'
if std_match(slv, "1---0000") then
    -- Match si bit 7 = '1' y bits 3-0 = "0000"
end if;
```

---

## Método 9: Records para Interfaces

### Definir Interface Completa

```vhdl
type axi_stream_m is record
    tdata  : std_logic_vector(31 downto 0);
    tvalid : std_logic;
    tlast  : std_logic;
end record;

type axi_stream_s is record
    tready : std_logic;
end record;

-- En entidad
port (
    m_axis : out axi_stream_m;  -- Master to Slave
    s_axis : in  axi_stream_s   -- Slave to Master
);
```

### Asignar Records

```vhdl
-- Asignación por campo
m_axis.tdata  <= data;
m_axis.tvalid <= valid;
m_axis.tlast  <= last;

-- Asignación completa
m_axis <= (tdata => data, tvalid => valid, tlast => last);
```

---

## Método 10: Checklist de Tipos

### Antes de Síntesis

- [ ] ¿Usé `numeric_std` (no `std_logic_arith`)?
- [ ] ¿Los contadores usan `unsigned`?
- [ ] ¿Las conversiones son explícitas?
- [ ] ¿Los rangos de integer están definidos?
- [ ] ¿Los tipos enumerados para FSM?
- [ ] ¿Los arrays tienen límites definidos?

### Errores Comunes

| Error | Solución |
|-------|----------|
| `+` con std_logic_vector | Convertir a unsigned |
| Asignar integer a slv | Usar to_unsigned + conversión |
| Mezclar signed/unsigned | Conversión explícita |
| Array sin límites | Definir rango al declarar |

---

<!-- IA_CONTEXT
USO: Métodos prácticos para tipos de datos VHDL
NIVEL: Intermedio (2/3)
HERRAMIENTAS: Quartus, Vivado, ModelSim
-->
