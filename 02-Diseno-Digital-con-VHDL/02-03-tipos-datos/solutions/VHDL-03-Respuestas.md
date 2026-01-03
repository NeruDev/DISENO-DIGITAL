<!--
::METADATA::
type: solution
topic_id: vhdl-03-tipos-datos
file_id: respuestas-tipos-datos
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [respuestas, soluciones, VHDL, tipos]
search_keywords: "respuestas, soluciones, tipos datos VHDL"
-->

> 🏠 **Navegación:** [← Problemas](../problems/VHDL-03-Problemas.md)

---

# Respuestas: Tipos de Datos

## Nivel 1: std_logic Básico

### Respuesta 1.1

Los 9 valores de `std_logic`:

| Valor | Significado | Sintetizable |
|-------|-------------|--------------|
| `'U'` | No inicializado | No |
| `'X'` | Desconocido fuerte | No |
| `'0'` | Cero fuerte | **Sí** |
| `'1'` | Uno fuerte | **Sí** |
| `'Z'` | Alta impedancia | **Sí** |
| `'W'` | Desconocido débil | No |
| `'L'` | Cero débil | **Sí** |
| `'H'` | Uno débil | **Sí** |
| `'-'` | Don't care | **Sí** |

### Respuesta 1.2

`'0' and 'Z'` = `'0'`

Según la tabla de resolución, '0' "gana" porque es un driver fuerte.

### Respuesta 1.3

```vhdl
signal clk      : std_logic;                       -- Reloj
signal reset_n  : std_logic;                       -- Reset activo bajo
signal data_io  : std_logic_vector(7 downto 0);   -- Bus bidireccional
signal enable   : std_logic;                       -- Habilitación
```

---

## Nivel 2: std_logic_vector

### Respuesta 2.1

```vhdl
signal data     : std_logic_vector(15 downto 0);  -- Bus datos 16 bits
signal address  : std_logic_vector(31 downto 0);  -- Bus direcciones 32 bits
signal registro : std_logic_vector(3 downto 0);   -- Registro 4 bits
```

### Respuesta 2.2

```vhdl
signal data : std_logic_vector(15 downto 0);

-- Nibble más significativo (bits 15-12)
msb_nibble <= data(15 downto 12);

-- Bits 7 a 4
mid_bits <= data(7 downto 4);

-- Bit menos significativo
lsb <= data(0);
```

### Respuesta 2.3

| `(7 downto 0)` | `(0 to 7)` |
|----------------|------------|
| MSB en índice 7 | MSB en índice 0 |
| Estándar en la industria | Poco común |
| Más natural para aritmética | Puede causar confusión |

**Siempre usar `downto`** para consistencia.

### Respuesta 2.4

```vhdl
signal byte : std_logic_vector(7 downto 0);

-- a) Binario
byte <= "10110011";

-- b) Hexadecimal
byte <= x"A5";

-- c) Todos unos
byte <= (others => '1');

-- d) Solo bit 5
byte <= (5 => '1', others => '0');
```

---

## Nivel 3: unsigned y signed

### Respuesta 3.1

```vhdl
signal contador : unsigned(7 downto 0);           -- Contador sin signo
signal valor    : signed(15 downto 0);            -- Con signo 16 bits
signal offset   : signed(7 downto 0);             -- -128 a +127
```

### Respuesta 3.2

| Tipo | Rango |
|------|-------|
| `unsigned(7 downto 0)` | 0 a 255 |
| `signed(7 downto 0)` | -128 a +127 |
| `unsigned(15 downto 0)` | 0 a 65535 |
| `signed(15 downto 0)` | -32768 a +32767 |

### Respuesta 3.3

```vhdl
process(clk)
begin
    if rising_edge(clk) then
        contador <= contador + 1;  -- Incremento
    end if;
end process;
```

### Respuesta 3.4

`std_logic_vector` no tiene operador `+` definido.

**Solución:** Usar `unsigned` o convertir:
```vhdl
cnt <= std_logic_vector(unsigned(cnt) + 1);
```

---

## Nivel 4: Conversiones

### Respuesta 4.1

```vhdl
-- slv a unsigned
uns <= unsigned(slv);

-- unsigned a slv
slv <= std_logic_vector(uns);

-- integer a unsigned (8 bits)
uns <= to_unsigned(int_val, 8);

-- unsigned a integer
int_val <= to_integer(uns);
```

### Respuesta 4.2

```vhdl
slv <= std_logic_vector(to_unsigned(200, 8));
-- Resultado: "11001000" = 0xC8
```

### Respuesta 4.3

```vhdl
int_val <= to_integer(unsigned(slv));
```

### Respuesta 4.4

```vhdl
library ieee;
use ieee.numeric_std.all;
```

---

## Nivel 5: Integer y Rangos

### Respuesta 5.1

```vhdl
signal byte_val : integer range 0 to 255;
```

### Respuesta 5.2

Sin rango especificado, el sintetizador podría inferir 32 bits para el integer.
Con rango, se usan solo los bits necesarios (ej: 8 bits para 0-255).

### Respuesta 5.3

| `natural` | `positive` |
|-----------|------------|
| 0 a INTEGER'HIGH | 1 a INTEGER'HIGH |
| Incluye el cero | **No** incluye el cero |

### Respuesta 5.4

**Mejor: Opción B o C**

- Opción A: Usa 32 bits, desperdicio
- Opción B: Usa 10 bits exactos
- Opción C: También usa 10 bits, más portable

Para hardware, B o C son equivalentes. C es preferible para operaciones aritméticas.

---

## Nivel 6: Tipos Enumerados

### Respuesta 6.1

```vhdl
type estado_t is (IDLE, READ, WRITE, DONE);
```

### Respuesta 6.2

```vhdl
signal estado : estado_t := IDLE;
```

### Respuesta 6.3

```vhdl
process(clk)
begin
    if rising_edge(clk) then
        case estado is
            when IDLE =>
                if start = '1' then
                    estado <= READ;
                end if;
            when READ =>
                estado <= WRITE;
            when WRITE =>
                estado <= DONE;
            when DONE =>
                estado <= IDLE;
        end case;
    end if;
end process;
```

### Respuesta 6.4

**Ventajas de enumerados:**
- Código más legible
- Errores detectados en compilación
- Síntesis optimiza codificación automáticamente
- Simulación muestra nombres, no bits

---

## Nivel 7: Arrays

### Respuesta 7.1

```vhdl
type rom_type is array (0 to 255) of std_logic_vector(7 downto 0);
signal rom : rom_type;
```

### Respuesta 7.2

```vhdl
type small_array is array (0 to 3) of std_logic_vector(7 downto 0);
signal data : small_array := (
    0 => x"01",
    1 => x"02", 
    2 => x"04",
    3 => x"08"
);
```

### Respuesta 7.3

```vhdl
type matriz_4x4 is array (0 to 3, 0 to 3) of std_logic_vector(7 downto 0);
signal matriz : matriz_4x4;
```

### Respuesta 7.4

```vhdl
valor <= matriz(2, 3);
-- o para asignar:
matriz(2, 3) <= x"FF";
```

---

## Nivel 8: Records

### Respuesta 8.1

```vhdl
type pixel_t is record
    r : std_logic_vector(7 downto 0);
    g : std_logic_vector(7 downto 0);
    b : std_logic_vector(7 downto 0);
end record;
```

### Respuesta 8.2

```vhdl
signal pixel : pixel_t;

-- Asignación por campo
pixel.r <= x"FF";
pixel.g <= x"00";
pixel.b <= x"80";
```

### Respuesta 8.3

```vhdl
type bus_t is record
    address      : std_logic_vector(15 downto 0);
    data         : std_logic_vector(7 downto 0);
    write_enable : std_logic;
    chip_select  : std_logic;
end record;
```

### Respuesta 8.4

```vhdl
signal bus_sig : bus_t;

bus_sig <= (
    address      => x"1234",
    data         => x"AB",
    write_enable => '1',
    chip_select  => '1'
);
```

---

## Nivel 9: Atributos

### Respuesta 9.1

Para `data : std_logic_vector(15 downto 0)`:

| Atributo | Valor |
|----------|-------|
| `data'left` | 15 |
| `data'right` | 0 |
| `data'high` | 15 |
| `data'low` | 0 |
| `data'length` | 16 |

### Respuesta 9.2

```vhdl
for i in data'range loop
    -- Procesar data(i)
    bit_i <= data(i);
end loop;

-- O equivalente:
for i in data'low to data'high loop
    bit_i <= data(i);
end loop;
```

### Respuesta 9.3

`color'pos(BLUE)` = 2

(RED=0, GREEN=1, BLUE=2, YELLOW=3)

---

## Nivel 10: Integración

### Respuesta 10.1

```vhdl
entity alu_8bit is
    port (
        a, b   : in  std_logic_vector(7 downto 0);
        op     : in  std_logic_vector(1 downto 0);
        result : out std_logic_vector(7 downto 0)
    );
end entity;

architecture rtl of alu_8bit is
    signal a_uns, b_uns, res_uns : unsigned(7 downto 0);
begin
    -- Conversión entrada
    a_uns <= unsigned(a);
    b_uns <= unsigned(b);
    
    -- Operación
    with op select res_uns <=
        a_uns + b_uns when "00",
        a_uns - b_uns when "01",
        a_uns and b_uns when "10",
        a_uns or b_uns when others;
    
    -- Conversión salida
    result <= std_logic_vector(res_uns);
end architecture;
```

### Respuesta 10.2

```vhdl
package bus_pkg is
    constant BUS_WIDTH : integer := 16;
    constant DATA_WIDTH : integer := 8;
    
    subtype addr_t is std_logic_vector(BUS_WIDTH-1 downto 0);
    subtype data_t is std_logic_vector(DATA_WIDTH-1 downto 0);
    
    type mem_array_t is array (natural range <>) of data_t;
    
    type bus_interface_t is record
        addr   : addr_t;
        data   : data_t;
        wr     : std_logic;
        rd     : std_logic;
        cs     : std_logic;
    end record;
end package;
```

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para ejercicios de tipos de datos
NOTA: Pueden existir soluciones alternativas válidas
-->
