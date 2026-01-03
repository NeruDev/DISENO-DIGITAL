<!--
::METADATA::
type: solution
topic_id: vhdl-02-entidades-arquitecturas
file_id: respuestas-entidades-arq
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [respuestas, soluciones, VHDL, entidad, arquitectura]
search_keywords: "respuestas, soluciones, entity, architecture"
-->

> 🏠 **Navegación:** [← Problemas](../problems/VHDL-02-Problemas.md)

---

# Respuestas: Entidades y Arquitecturas

## Nivel 1: Declaración de Entidades

### Respuesta 1.1

```vhdl
entity nand3 is
    port (
        a : in  std_logic;
        b : in  std_logic;
        c : in  std_logic;
        y : out std_logic
    );
end entity nand3;
```

### Respuesta 1.2

```vhdl
entity mux4to1 is
    port (
        d0  : in  std_logic_vector(7 downto 0);
        d1  : in  std_logic_vector(7 downto 0);
        d2  : in  std_logic_vector(7 downto 0);
        d3  : in  std_logic_vector(7 downto 0);
        sel : in  std_logic_vector(1 downto 0);
        y   : out std_logic_vector(7 downto 0)
    );
end entity mux4to1;
```

### Respuesta 1.3

```vhdl
entity mi_modulo is                                    -- Faltaba 'is'
    port (                                             -- Faltaba '('
        clk      : in  std_logic;                      -- Faltaba ';'
        data_in  : in  std_logic_vector(7 downto 0);   -- 'to' → 'downto'
        data_out : out std_logic_vector(7 downto 0);   -- ',' → ';'
        status   : out std_logic                       -- 'buffer' → 'out', sin ';'
    );                                                 -- Faltaba ');'
end entity mi_modulo;                                  -- Faltaba 'mi_modulo'
```

---

## Nivel 2: Arquitecturas Básicas

### Respuesta 2.1

```vhdl
architecture dataflow of xor_gate is
begin
    y <= a xor b;
end architecture dataflow;
```

### Respuesta 2.2

```vhdl
entity tristate_buffer is
    port (
        data_in : in  std_logic_vector(7 downto 0);
        oe      : in  std_logic;
        data_out: out std_logic_vector(7 downto 0)
    );
end entity;

architecture behavioral of tristate_buffer is
begin
    data_out <= data_in when oe = '1' else (others => 'Z');
end architecture;
```

### Respuesta 2.3

```vhdl
entity comparador4 is
    port (
        a  : in  std_logic_vector(3 downto 0);
        b  : in  std_logic_vector(3 downto 0);
        eq : out std_logic
    );
end entity;

architecture dataflow of comparador4 is
begin
    eq <= '1' when a = b else '0';
end architecture;
```

---

## Nivel 3: Genéricos

### Respuesta 3.1

```vhdl
entity registro_gen is
    generic (
        WIDTH     : integer := 8;
        RESET_VAL : std_logic_vector := x"00"
    );
    port (
        clk   : in  std_logic;
        reset : in  std_logic;
        en    : in  std_logic;
        d     : in  std_logic_vector(WIDTH-1 downto 0);
        q     : out std_logic_vector(WIDTH-1 downto 0)
    );
end entity;

architecture rtl of registro_gen is
begin
    process(clk, reset)
    begin
        if reset = '1' then
            q <= RESET_VAL(WIDTH-1 downto 0);
        elsif rising_edge(clk) then
            if en = '1' then
                q <= d;
            end if;
        end if;
    end process;
end architecture;
```

### Respuesta 3.2

```vhdl
entity contador is
    generic (
        WIDTH : integer := 8
    );
    port (
        clk   : in  std_logic;
        reset : in  std_logic;
        q     : out std_logic_vector(WIDTH-1 downto 0)
    );
end entity;
```

### Respuesta 3.3

```vhdl
-- a) 4 bits
CNT4: entity work.contador
    generic map (WIDTH => 4)
    port map (clk => clk, reset => rst, q => count4);

-- b) 12 bits
CNT12: entity work.contador
    generic map (WIDTH => 12)
    port map (clk => clk, reset => rst, q => count12);

-- c) 16 bits (nota: valor inicial requiere modificar entidad)
CNT16: entity work.contador
    generic map (WIDTH => 16)
    port map (clk => clk, reset => rst, q => count16);
```

---

## Nivel 4: Señales Internas

### Respuesta 4.1

**Error:** No se puede leer un puerto `out` dentro del módulo.

**Solución:**
```vhdl
architecture good of contador is
    signal q_int : std_logic_vector(3 downto 0);
begin
    process(clk)
    begin
        if rising_edge(clk) then
            q_int <= std_logic_vector(unsigned(q_int) + 1);
        end if;
    end process;
    
    q <= q_int;  -- Asignar señal interna a salida
end architecture;
```

### Respuesta 4.2

```vhdl
architecture rtl of modulo is
    -- Contador de 8 bits
    signal counter : unsigned(7 downto 0);
    
    -- Flag de overflow
    signal overflow : std_logic;
    
    -- Registro temporal de 16 bits
    signal temp_reg : std_logic_vector(15 downto 0);
    
    -- Estado de máquina (4 valores)
    type state_type is (IDLE, INIT, RUN, DONE);
    signal state : state_type;
begin
    ...
end architecture;
```

### Respuesta 4.3

| Señal | Variable |
|-------|----------|
| Se declara en arquitectura | Se declara en process |
| Se actualiza al final del delta | Se actualiza inmediatamente |
| Representa cables/registros | Almacenamiento temporal |

```vhdl
-- Señal
signal contador_sig : integer;
proceso: process(clk)
begin
    contador_sig <= contador_sig + 1;  -- Valor anterior en esta línea
end process;

-- Variable
process(clk)
    variable contador_var : integer;
begin
    contador_var := contador_var + 1;  -- Valor nuevo inmediatamente
end process;
```

---

## Nivel 5: Componentes

### Respuesta 5.1

```vhdl
architecture structural of adder2bit is
    component full_adder is
        port (a, b, cin : in std_logic; sum, cout : out std_logic);
    end component;
    
    signal c1 : std_logic;
begin
    FA0: full_adder port map (
        a => a(0), b => b(0), cin => cin,
        sum => sum(0), cout => c1
    );
    
    FA1: full_adder port map (
        a => a(1), b => b(1), cin => c1,
        sum => sum(1), cout => cout
    );
end architecture;
```

### Respuesta 5.2

```vhdl
REG1: entity work.registro(rtl)
    port map (
        clk   => clk,
        reset => reset,
        d     => data_in,
        q     => data_out
    );
```

### Respuesta 5.3

**Posicional:** Conexiones por orden de declaración
**Nominal:** Conexiones por nombre con `=>`

Se recomienda **nominal** porque:
- Más legible
- Orden no importa
- Detecta errores fácilmente

---

## Nivel 6: Estilos de Arquitectura

### Respuesta 6.1

```vhdl
-- a) Behavioral
architecture behavioral of mux2to1 is
begin
    process(sel, a, b)
    begin
        if sel = '0' then
            y <= a;
        else
            y <= b;
        end if;
    end process;
end architecture;

-- b) Dataflow
architecture dataflow of mux2to1 is
begin
    y <= a when sel = '0' else b;
end architecture;

-- c) Structural
architecture structural of mux2to1 is
    signal sel_n, and_a, and_b : std_logic;
begin
    sel_n <= not sel;
    and_a <= a and sel_n;
    and_b <= b and sel;
    y <= and_a or and_b;
end architecture;
```

### Respuesta 6.2

- a) Máquina de estados → **Behavioral**
- b) Sumador aritmético → **Dataflow o RTL**
- c) Conectar módulos → **Structural**
- d) Lógica combinacional simple → **Dataflow**

### Respuesta 6.3

```vhdl
architecture dataflow of decoder2to4 is
begin
    y(0) <= en and (not sel(1)) and (not sel(0));
    y(1) <= en and (not sel(1)) and sel(0);
    y(2) <= en and sel(1) and (not sel(0));
    y(3) <= en and sel(1) and sel(0);
end architecture;
```

---

## Nivel 7: Generate

### Respuesta 7.1

```vhdl
architecture structural of reg8 is
    component dff is
        port (clk, d : in std_logic; q : out std_logic);
    end component;
begin
    GEN_FF: for i in 0 to 7 generate
        FF_I: dff port map (clk => clk, d => d(i), q => q(i));
    end generate;
end architecture;
```

### Respuesta 7.2

```vhdl
architecture rtl of modulo is
    signal cycle_count : unsigned(31 downto 0);
begin
    GEN_DEBUG: if DEBUG = true generate
        process(clk)
        begin
            if rising_edge(clk) then
                cycle_count <= cycle_count + 1;
            end if;
        end process;
    end generate;
end architecture;
```

### Respuesta 7.3

```vhdl
architecture structural of adder_n is
    signal carry : std_logic_vector(N downto 0);
begin
    carry(0) <= cin;
    
    GEN_ADDERS: for i in 0 to N-1 generate
        FA_I: entity work.full_adder
            port map (
                a    => a(i),
                b    => b(i),
                cin  => carry(i),
                sum  => sum(i),
                cout => carry(i+1)
            );
    end generate;
    
    cout <= carry(N);
end architecture;
```

---

## Nivel 9: Constantes y Alias

### Respuesta 9.1

```vhdl
constant DATA_WIDTH : integer := 32;
constant CLK_FREQ   : integer := 100_000_000;  -- 100 MHz
constant CLK_PERIOD : time := 1 sec / CLK_FREQ; -- 10 ns
constant ZERO_32    : std_logic_vector(31 downto 0) := (others => '0');
```

### Respuesta 9.2

```vhdl
signal instruction : std_logic_vector(15 downto 0);

alias opcode : std_logic_vector(3 downto 0) is instruction(15 downto 12);
alias rd     : std_logic_vector(3 downto 0) is instruction(11 downto 8);
alias rs1    : std_logic_vector(3 downto 0) is instruction(7 downto 4);
alias rs2    : std_logic_vector(3 downto 0) is instruction(3 downto 0);
```

### Respuesta 9.3

- **Constantes:** Valores fijos en tiempo de compilación, conocidos
- **Genéricos:** Valores configurables al instanciar, permiten reutilización

Usar constantes para valores que nunca cambian, genéricos para hacer módulos parametrizables.

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para ejercicios de entidades y arquitecturas
NOTA: Pueden existir soluciones alternativas válidas
-->
