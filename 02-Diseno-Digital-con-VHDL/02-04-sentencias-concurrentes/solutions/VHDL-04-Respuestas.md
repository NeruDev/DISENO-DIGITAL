<!--
::METADATA::
type: solution
topic_id: vhdl-04-sentencias-concurrentes
file_id: respuestas-concurrentes
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [respuestas, soluciones, VHDL, concurrente]
search_keywords: "respuestas, soluciones, sentencias concurrentes"
-->

> 🏠 **Navegación:** [← Problemas](../problems/VHDL-04-Problemas.md)

---

# Respuestas: Sentencias Concurrentes

## Nivel 1: Asignación Simple

### Respuesta 1.1

```vhdl
Y <= A and B;
Z <= not(C or D);
W <= (A xor B) and C;
```

### Respuesta 1.2

El orden no importa porque son **sentencias concurrentes**. En hardware, las tres operaciones ocurren simultáneamente. VHDL modela este comportamiento: todas las asignaciones se evalúan en el mismo "instante" de tiempo de simulación.

### Respuesta 1.3

```vhdl
byte_out <= nibble_hi & nibble_lo;
```

---

## Nivel 2: when-else

### Respuesta 2.1

```vhdl
y <= a when sel = '0' else b;
```

### Respuesta 2.2

```vhdl
y <= d0 when sel = "00" else
     d1 when sel = "01" else
     d2 when sel = "10" else
     d3;
```

### Respuesta 2.3

**Problema:** Falta el caso `sel = "11"`. Esto puede inferir un **latch** no deseado.

**Solución:**
```vhdl
y <= a when sel = "00" else
     b when sel = "01" else
     c when sel = "10" else
     d;  -- Agregar caso default
```

### Respuesta 2.4

```vhdl
signal A, B : std_logic_vector(7 downto 0);
signal gt, eq, lt : std_logic;

gt <= '1' when unsigned(A) > unsigned(B) else '0';
eq <= '1' when A = B else '0';
lt <= '1' when unsigned(A) < unsigned(B) else '0';
```

---

## Nivel 3: with-select

### Respuesta 3.1

```vhdl
with sel select
    y <= d0 when "00",
         d1 when "01",
         d2 when "10",
         d3 when others;
```

### Respuesta 3.2

```vhdl
-- BCD a 7 segmentos (ánodo común: '0' = encendido)
with bcd select
    segments <= "0000001" when "0000",  -- 0
                "1001111" when "0001",  -- 1
                "0010010" when "0010",  -- 2
                "0000110" when "0011",  -- 3
                "1001100" when "0100",  -- 4
                "0100100" when "0101",  -- 5
                "0100000" when "0110",  -- 6
                "0001111" when "0111",  -- 7
                "0000000" when "1000",  -- 8
                "0000100" when "1001",  -- 9
                "1111111" when others;  -- Apagado
```

### Respuesta 3.3

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity alu_4bit is
    port (
        A, B   : in  std_logic_vector(3 downto 0);
        op     : in  std_logic_vector(1 downto 0);
        result : out std_logic_vector(3 downto 0)
    );
end entity;

architecture dataflow of alu_4bit is
    signal a_uns, b_uns : unsigned(3 downto 0);
begin
    a_uns <= unsigned(A);
    b_uns <= unsigned(B);
    
    with op select
        result <= std_logic_vector(a_uns + b_uns) when "00",
                  std_logic_vector(a_uns - b_uns) when "01",
                  A and B when "10",
                  A or B when others;
end architecture;
```

### Respuesta 3.4

`with-select` es preferible cuando:
- El selector tiene opciones mutuamente exclusivas
- Se implementa un multiplexor puro
- No hay prioridad entre opciones

---

## Nivel 4: Comparación

### Respuesta 4.1

```vhdl
with input select
    output <= "00" when '0',
              "01" when '1',
              "11" when others;
```

### Respuesta 4.2

```vhdl
y <= a when sel = "00" else
     b when sel = "01" else
     c when sel = "10" else
     d;
```

### Respuesta 4.3

Usar **`when-else`** porque hay prioridad (el bit más significativo activo tiene precedencia):

```vhdl
code <= "11" when input(3) = '1' else
        "10" when input(2) = '1' else
        "01" when input(1) = '1' else
        "00";
valid <= '1' when input /= "0000" else '0';
```

---

## Nivel 5: for-generate

### Respuesta 5.1

```vhdl
GEN_INV: for i in 0 to 7 generate
    output(i) <= not input(i);
end generate;
```

### Respuesta 5.2

```vhdl
architecture structural of adder_4bit is
    signal carry : std_logic_vector(4 downto 0);
begin
    carry(0) <= cin;
    
    GEN_FA: for i in 0 to 3 generate
        FA_i: entity work.full_adder
            port map (
                a    => a(i),
                b    => b(i),
                cin  => carry(i),
                sum  => sum(i),
                cout => carry(i+1)
            );
    end generate;
    
    cout <= carry(4);
end architecture;
```

### Respuesta 5.3

```vhdl
-- Registro de desplazamiento a la derecha
GEN_SR: for i in 0 to 6 generate
    process(clk)
    begin
        if rising_edge(clk) then
            q(i) <= q(i+1);
        end if;
    end process;
end generate;

-- Bit de entrada
process(clk)
begin
    if rising_edge(clk) then
        q(7) <= serial_in;
    end if;
end process;
```

### Respuesta 5.4

**Error:** `input(i+1)` para `i=7` accede a `input(8)`, que está fuera de rango.

**Solución:**
```vhdl
GEN: for i in 0 to 6 generate
    output(i) <= input(i+1);
end generate;
output(7) <= '0';  -- Bit más significativo
```

---

## Nivel 6: if-generate

### Respuesta 6.1

```vhdl
architecture rtl of modulo is
    constant DEBUG : boolean := true;
begin
    GEN_DEBUG: if DEBUG generate
        signal debug_cnt : unsigned(31 downto 0) := (others => '0');
    begin
        process(clk)
        begin
            if rising_edge(clk) then
                debug_cnt <= debug_cnt + 1;
            end if;
        end process;
    end generate;
end architecture;
```

### Respuesta 6.2

```vhdl
entity adder_configurable is
    generic (WIDTH : integer := 8);
    port (
        a, b : in  std_logic_vector(WIDTH-1 downto 0);
        sum  : out std_logic_vector(WIDTH-1 downto 0)
    );
end entity;

architecture rtl of adder_configurable is
begin
    GEN_8: if WIDTH = 8 generate
        sum <= std_logic_vector(unsigned(a) + unsigned(b));
    end generate;
    
    GEN_16: if WIDTH = 16 generate
        sum <= std_logic_vector(unsigned(a) + unsigned(b));
    end generate;
end architecture;
```

### Respuesta 6.3

Las condiciones deben ser **constantes** (evaluables en tiempo de compilación) porque `if-generate` determina qué hardware se sintetiza. El hardware generado es fijo, no cambia en tiempo de ejecución.

---

## Nivel 7: Combinaciones

### Respuesta 7.1

```vhdl
entity barrel_shifter is
    port (
        data_in  : in  std_logic_vector(7 downto 0);
        shift    : in  std_logic_vector(1 downto 0);
        data_out : out std_logic_vector(7 downto 0)
    );
end entity;

architecture dataflow of barrel_shifter is
begin
    with shift select
        data_out <= data_in                              when "00",
                    data_in(6 downto 0) & '0'           when "01",
                    data_in(5 downto 0) & "00"          when "10",
                    data_in(4 downto 0) & "000"         when others;
end architecture;
```

### Respuesta 7.2

```vhdl
-- Paridad par: '1' si número impar de unos
parity <= data(7) xor data(6) xor data(5) xor data(4) xor
          data(3) xor data(2) xor data(1) xor data(0);

-- O con VHDL-2008:
parity <= xor data;
```

---

## Nivel 8: Tristate

### Respuesta 8.1

```vhdl
data_out <= data_in when oe = '1' else (others => 'Z');
```

### Respuesta 8.2

```vhdl
bus <= device_data(0) when device_en(0) = '1' else
       device_data(1) when device_en(1) = '1' else
       device_data(2) when device_en(2) = '1' else
       device_data(3) when device_en(3) = '1' else
       (others => 'Z');
```

### Respuesta 8.3

Sin 'Z', múltiples drivers pueden generar conflictos ('X' en simulación). En hardware real, esto causa cortocircuitos y daños. La alta impedancia 'Z' permite que solo un driver controle el bus.

---

## Nivel 9: Optimización

### Respuesta 9.1

```vhdl
-- Simplificado: es un XOR
y <= a xor b;
```

### Respuesta 9.2

El código infiere un **MUX 2:1** efectivo (no 8:1) porque:
- "000" y "001" → a
- "010" y "011" → b
- resto → c

### Respuesta 9.3

```vhdl
with sel(2 downto 1) select
    y <= a when "00",
         b when "01",
         c when others;
```

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para ejercicios de sentencias concurrentes
NOTA: Pueden existir soluciones alternativas válidas
-->
