<!--
::METADATA::
type: method
topic_id: vhdl-02-entidades-arquitecturas
file_id: metodos-entidades-arq
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [VHDL, metodologia, diseño, jerarquia]
search_keywords: "metodología VHDL, diseño jerárquico, entidad arquitectura"
-->

> 🏠 **Navegación:** [← Teoría](../theory/VHDL-02-Teoria-EntidadesArquitecturas.md) | [Problemas →](../problems/VHDL-02-Problemas.md)

---

# Métodos: Entidades y Arquitecturas

## Método 1: Diseño Top-Down

### Procedimiento

1. **Definir interfaz del top-level**
2. **Identificar bloques funcionales**
3. **Definir interfaces de cada bloque**
4. **Implementar cada bloque**
5. **Integrar y verificar**

### Ejemplo: Sistema de Comunicación

```
┌─────────────────────────────────────────────┐
│              top_sistema                     │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐     │
│  │ rx_uart │──│ procesa │──│ tx_uart │     │
│  └─────────┘  └─────────┘  └─────────┘     │
└─────────────────────────────────────────────┘
```

**Paso 1: Top-level entity**
```vhdl
entity top_sistema is
    port (
        clk     : in  std_logic;
        reset   : in  std_logic;
        rx      : in  std_logic;
        tx      : out std_logic
    );
end entity;
```

**Paso 2-4: Definir e implementar bloques**
```vhdl
-- rx_uart, procesador, tx_uart como entidades separadas
```

---

## Método 2: Crear Módulos Parametrizables

### Usando Genéricos

```vhdl
entity registro_n is
    generic (
        WIDTH : integer := 8
    );
    port (
        clk   : in  std_logic;
        rst   : in  std_logic;
        en    : in  std_logic;
        d     : in  std_logic_vector(WIDTH-1 downto 0);
        q     : out std_logic_vector(WIDTH-1 downto 0)
    );
end entity;

architecture rtl of registro_n is
begin
    process(clk, rst)
    begin
        if rst = '1' then
            q <= (others => '0');
        elsif rising_edge(clk) then
            if en = '1' then
                q <= d;
            end if;
        end if;
    end process;
end architecture;
```

### Instanciación con Diferentes Parámetros

```vhdl
-- Registro de 8 bits
REG8: entity work.registro_n
    generic map (WIDTH => 8)
    port map (clk => clk, rst => rst, en => en8, d => d8, q => q8);

-- Registro de 16 bits
REG16: entity work.registro_n
    generic map (WIDTH => 16)
    port map (clk => clk, rst => rst, en => en16, d => d16, q => q16);

-- Registro de 32 bits
REG32: entity work.registro_n
    generic map (WIDTH => 32)
    port map (clk => clk, rst => rst, en => en32, d => d32, q => q32);
```

---

## Método 3: Encapsulamiento de Señales de Salida

### Problema: No se puede leer una señal `out`

```vhdl
-- ✗ ERROR: No se puede leer salida
port (q : out std_logic);
...
q <= not q;  -- ERROR!
```

### Solución: Señal Interna

```vhdl
entity contador is
    port (
        clk   : in  std_logic;
        reset : in  std_logic;
        q     : out std_logic_vector(3 downto 0)
    );
end entity;

architecture rtl of contador is
    signal q_interno : std_logic_vector(3 downto 0);  -- Señal interna
begin
    process(clk, reset)
    begin
        if reset = '1' then
            q_interno <= (others => '0');
        elsif rising_edge(clk) then
            q_interno <= std_logic_vector(unsigned(q_interno) + 1);
        end if;
    end process;
    
    q <= q_interno;  -- Asignar a la salida
end architecture;
```

---

## Método 4: Instanciación de Componentes

### Método Tradicional (Con declaración)

```vhdl
architecture structural of top is
    -- 1. Declarar componente
    component half_adder is
        port (
            a, b : in  std_logic;
            s, c : out std_logic
        );
    end component;
    
    signal s1, c1, c2 : std_logic;
begin
    -- 2. Instanciar con nombre
    HA1: half_adder
        port map (a => A, b => B, s => s1, c => c1);
    
    HA2: half_adder
        port map (a => s1, b => Cin, s => Sum, c => c2);
    
    Cout <= c1 or c2;
end architecture;
```

### Método Directo (VHDL-93+)

```vhdl
architecture structural of top is
    signal s1, c1, c2 : std_logic;
begin
    -- Instanciar directamente sin declarar componente
    HA1: entity work.half_adder(behavioral)
        port map (a => A, b => B, s => s1, c => c1);
    
    HA2: entity work.half_adder(behavioral)
        port map (a => s1, b => Cin, s => Sum, c => c2);
end architecture;
```

---

## Método 5: Port Map Posicional vs Nominal

### Posicional (No recomendado)

```vhdl
-- Los puertos se conectan por orden
INST: componente port map (clk, rst, data_in, data_out);
```

### Nominal (Recomendado)

```vhdl
-- Los puertos se conectan por nombre
INST: componente port map (
    clk      => system_clk,
    rst      => system_rst,
    data_in  => input_data,
    data_out => output_data
);
```

### Ventajas del Método Nominal

- ✓ Más claro y legible
- ✓ Orden no importa
- ✓ Detecta errores de conexión
- ✓ Facilita mantenimiento

---

## Método 6: Uso de `open` para Puertos no Conectados

```vhdl
entity modulo is
    port (
        clk     : in  std_logic;
        data_in : in  std_logic_vector(7 downto 0);
        data_out: out std_logic_vector(7 downto 0);
        status  : out std_logic  -- No siempre se usa
    );
end entity;

-- Instanciación sin conectar status
INST: entity work.modulo
    port map (
        clk      => clk,
        data_in  => datos,
        data_out => resultado,
        status   => open  -- Puerto no conectado
    );
```

**Nota:** Solo puertos `out` pueden dejarse `open`.

---

## Método 7: Generate para Instanciación Múltiple

### For-Generate

```vhdl
architecture structural of banco_registros is
    component registro is
        port (clk, rst, en : in std_logic;
              d : in std_logic_vector(7 downto 0);
              q : out std_logic_vector(7 downto 0));
    end component;
    
    type reg_array is array (0 to 7) of std_logic_vector(7 downto 0);
    signal d_array, q_array : reg_array;
    signal en_array : std_logic_vector(7 downto 0);
begin
    -- Generar 8 registros
    GEN_REGS: for i in 0 to 7 generate
        REG_I: registro
            port map (
                clk => clk,
                rst => rst,
                en  => en_array(i),
                d   => d_array(i),
                q   => q_array(i)
            );
    end generate;
end architecture;
```

### If-Generate (Condicional)

```vhdl
architecture rtl of modulo is
begin
    -- Generar pipeline solo si está habilitado
    GEN_PIPE: if USE_PIPELINE = true generate
        -- Registros de pipeline
        process(clk)
        begin
            if rising_edge(clk) then
                stage1 <= input;
                stage2 <= stage1;
                output <= stage2;
            end if;
        end process;
    end generate;
    
    GEN_NO_PIPE: if USE_PIPELINE = false generate
        output <= input;  -- Sin pipeline
    end generate;
end architecture;
```

---

## Método 8: Organización de Archivos

### Un Archivo por Entidad

```
proyecto/
├── src/
│   ├── top_module.vhd      -- entity + architecture
│   ├── uart_rx.vhd
│   ├── uart_tx.vhd
│   ├── fifo.vhd
│   └── contador.vhd
```

### Convenciones de Nombres

| Elemento | Convención |
|----------|------------|
| Archivo | `nombre_modulo.vhd` |
| Entidad | `nombre_modulo` |
| Arquitectura | `behavioral`, `rtl`, `structural` |
| Señales | `snake_case` minúsculas |
| Constantes | `UPPER_CASE` |
| Genéricos | `UPPER_CASE` |

---

## Método 9: Verificar Puertos con Constantes

### Forzar Valores en Testbench

```vhdl
-- Entrada no usada a '0'
INST: entity work.modulo
    port map (
        clk      => clk,
        enable   => '1',          -- Siempre habilitado
        reset    => '0',          -- Nunca reset
        data_in  => input_data,
        data_out => open
    );
```

---

## Método 10: Checklist de Diseño

### Antes de Síntesis

- [ ] Todos los puertos declarados correctamente (in/out/inout)
- [ ] Genéricos tienen valores por defecto razonables
- [ ] Señales internas declaradas e inicializadas si es necesario
- [ ] Todas las señales asignadas (sin latches no intencionales)
- [ ] Port map usa nombres (no posicional)
- [ ] Componentes declarados coinciden con entidades
- [ ] Arquitectura coincide con entidad referenciada

### Estilo

- [ ] Un archivo por entidad
- [ ] Nombres descriptivos
- [ ] Comentarios en interfaces
- [ ] Indentación consistente

---

<!-- IA_CONTEXT
USO: Métodos prácticos para diseño con entidades y arquitecturas
NIVEL: Básico (1/3)
HERRAMIENTAS: Quartus, Vivado, ModelSim
-->
