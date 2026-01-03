<!--
::METADATA::
type: theory
topic_id: vhdl-02-entidades-arquitecturas
file_id: teoria-entidades-arquitecturas
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [VHDL, entity, architecture, component, generics, port]
search_keywords: "entidad, arquitectura, entity, architecture, VHDL"
-->

> 🏠 **Navegación:** [← Volver al Índice](../02-02-Intro.md) | [Métodos →](../methods/VHDL-02-Metodos-EntidadesArq.md)

---

# Entidades y Arquitecturas en VHDL

## 1. Concepto de Entidad

### 1.1 Definición

La **entidad** (entity) define la **interfaz externa** de un módulo de hardware:
- Nombre del módulo
- Puertos de entrada/salida
- Parámetros genéricos (opcionales)

Es la "caja negra" que describe cómo se conecta el módulo con el exterior.

### 1.2 Analogía

```
┌─────────────────────────────┐
│        ENTITY               │
│  (Interfaz/Puertos)         │
│                             │
│   ┌─────────────────────┐   │
│   │    ARCHITECTURE     │   │
│   │  (Implementación)   │   │
│   └─────────────────────┘   │
│                             │
└─────────────────────────────┘
```

---

## 2. Sintaxis de Entity

### 2.1 Estructura Completa

```vhdl
entity nombre_entidad is
    generic (
        -- Parámetros configurables
        PARAM1 : tipo := valor_default;
        PARAM2 : tipo := valor_default
    );
    port (
        -- Declaración de puertos
        puerto1 : modo tipo;
        puerto2 : modo tipo
    );
end entity nombre_entidad;
```

### 2.2 Ejemplo Básico

```vhdl
entity sumador is
    port (
        A    : in  std_logic_vector(7 downto 0);
        B    : in  std_logic_vector(7 downto 0);
        Cin  : in  std_logic;
        Sum  : out std_logic_vector(7 downto 0);
        Cout : out std_logic
    );
end entity sumador;
```

---

## 3. Puertos (Port)

### 3.1 Modos de Puerto

| Modo | Dirección | Descripción |
|------|-----------|-------------|
| `in` | Entrada | Solo lectura dentro del módulo |
| `out` | Salida | Solo escritura, no legible internamente |
| `inOut` | Bidireccional | Lectura y escritura |
| `buffer` | Salida | Salida legible internamente (obsoleto) |

### 3.2 Ejemplos de Cada Modo

```vhdl
port (
    -- Entradas típicas
    clk      : in  std_logic;                       -- Reloj
    reset_n  : in  std_logic;                       -- Reset activo bajo
    data_in  : in  std_logic_vector(7 downto 0);    -- Bus de datos
    enable   : in  std_logic;                       -- Habilitación
    
    -- Salidas típicas
    data_out : out std_logic_vector(7 downto 0);   -- Datos de salida
    valid    : out std_logic;                       -- Dato válido
    ready    : out std_logic;                       -- Listo para recibir
    
    -- Bidireccional (para buses externos)
    data_io  : inOut std_logic_vector(7 downto 0)  -- Bus bidireccional
);
```

### 3.3 Puerto `inOut`

Se usa para buses bidireccionales (ej: conexión a memoria externa):

```vhdl
-- Control de buffer tri-state
process(oe, data_internal)
begin
    if oe = '1' then
        data_io <= data_internal;  -- Salida activa
    else
        data_io <= (others => 'Z'); -- Alta impedancia
    end if;
end process;

-- Lectura del bus
data_read <= data_io;
```

---

## 4. Genéricos (Generic)

### 4.1 Propósito

Los **genéricos** permiten crear módulos **parametrizables**:
- Ancho de buses configurable
- Valores constantes modificables
- Reutilización de código

### 4.2 Sintaxis

```vhdl
entity registro is
    generic (
        WIDTH      : integer := 8;           -- Ancho del registro
        RESET_VAL  : std_logic_vector := x"00"  -- Valor de reset
    );
    port (
        clk   : in  std_logic;
        reset : in  std_logic;
        d     : in  std_logic_vector(WIDTH-1 downto 0);
        q     : out std_logic_vector(WIDTH-1 downto 0)
    );
end entity registro;
```

### 4.3 Tipos de Genéricos Comunes

```vhdl
generic (
    -- Enteros
    DATA_WIDTH : integer := 8;
    ADDR_WIDTH : integer := 16;
    
    -- Naturales (solo positivos)
    DEPTH : natural := 256;
    
    -- Booleanos
    USE_RESET : boolean := true;
    
    -- Tiempo (solo simulación)
    CLK_PERIOD : time := 10 ns;
    
    -- Vectores
    INIT_VALUE : std_logic_vector(7 downto 0) := x"00"
);
```

---

## 5. Concepto de Arquitectura

### 5.1 Definición

La **arquitectura** (architecture) define la **implementación interna** de una entidad:
- Lógica del circuito
- Conexiones internas
- Comportamiento

### 5.2 Relación Entidad-Arquitectura

- Una entidad puede tener **múltiples arquitecturas**
- Cada arquitectura ofrece una implementación diferente
- Al instanciar se especifica cuál usar

```vhdl
-- Una entidad, múltiples arquitecturas
entity contador is
    port (...);
end entity;

architecture behavioral of contador is ...
architecture structural of contador is ...
architecture rtl of contador is ...
```

---

## 6. Sintaxis de Architecture

### 6.1 Estructura Completa

```vhdl
architecture nombre_arquitectura of nombre_entidad is
    
    -- ZONA DECLARATIVA (antes de begin)
    -- Señales internas
    signal senal1 : tipo;
    
    -- Constantes
    constant CONST1 : tipo := valor;
    
    -- Tipos definidos por usuario
    type estado_type is (IDLE, RUN, STOP);
    
    -- Componentes
    component otro_modulo is
        port (...);
    end component;
    
begin
    
    -- ZONA DE SENTENCIAS (después de begin)
    -- Asignaciones concurrentes
    -- Instanciaciones de componentes
    -- Procesos
    
end architecture nombre_arquitectura;
```

### 6.2 Ejemplo Completo

```vhdl
architecture behavioral of sumador is
    -- Señal interna para el resultado extendido
    signal suma_temp : std_logic_vector(8 downto 0);
begin
    -- Suma con extensión de bit
    suma_temp <= ('0' & A) + ('0' & B) + ("00000000" & Cin);
    
    -- Asignación de salidas
    Sum  <= suma_temp(7 downto 0);
    Cout <= suma_temp(8);
end architecture behavioral;
```

---

## 7. Estilos de Arquitectura

### 7.1 Behavioral (Comportamental)

Describe **qué hace** el circuito, no cómo está construido.

```vhdl
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
```

### 7.2 Dataflow (Flujo de Datos)

Describe las **transferencias de datos** usando asignaciones concurrentes.

```vhdl
architecture dataflow of mux2to1 is
begin
    y <= a when sel = '0' else b;
end architecture;
```

### 7.3 Structural (Estructural)

Describe la **interconexión de componentes**.

```vhdl
architecture structural of mux2to1 is
    signal sel_n, and1_out, and2_out : std_logic;
begin
    -- NOT gate
    sel_n <= not sel;
    
    -- AND gates
    and1_out <= a and sel_n;
    and2_out <= b and sel;
    
    -- OR gate
    y <= and1_out or and2_out;
end architecture;
```

### 7.4 RTL (Register Transfer Level)

Combinación de comportamental y dataflow, enfocado en registros y lógica combinacional.

```vhdl
architecture rtl of registro is
begin
    process(clk, reset)
    begin
        if reset = '1' then
            q <= (others => '0');
        elsif rising_edge(clk) then
            q <= d;
        end if;
    end process;
end architecture;
```

---

## 8. Señales Internas

### 8.1 Declaración

```vhdl
architecture ejemplo of modulo is
    -- Señales simples
    signal flag : std_logic;
    signal contador : unsigned(7 downto 0);
    
    -- Señales con valor inicial (solo simulación)
    signal estado : std_logic := '0';
    
    -- Múltiples señales del mismo tipo
    signal a, b, c : std_logic;
begin
    ...
end architecture;
```

### 8.2 Señales vs Variables

| Característica | Señal | Variable |
|----------------|-------|----------|
| Alcance | Arquitectura completa | Solo dentro de process |
| Actualización | Al final del delta cycle | Inmediata |
| Síntesis | Cables/registros | Almacenamiento temporal |
| Declaración | Antes de `begin` | Dentro de `process` |

---

## 9. Componentes

### 9.1 Declaración de Componente

```vhdl
architecture structural of top is
    -- Declaración del componente
    component contador is
        generic (
            WIDTH : integer := 8
        );
        port (
            clk    : in  std_logic;
            reset  : in  std_logic;
            enable : in  std_logic;
            count  : out std_logic_vector(WIDTH-1 downto 0)
        );
    end component;
    
    signal count_out : std_logic_vector(7 downto 0);
begin
    -- Instanciación
    CNT1: contador
        generic map (WIDTH => 8)
        port map (
            clk    => clk,
            reset  => reset,
            enable => en,
            count  => count_out
        );
end architecture;
```

### 9.2 Instanciación Directa (VHDL-93)

Sin declarar componente explícitamente:

```vhdl
CNT1: entity work.contador(behavioral)
    generic map (WIDTH => 8)
    port map (
        clk    => clk,
        reset  => reset,
        enable => en,
        count  => count_out
    );
```

---

## 10. Constantes y Alias

### 10.1 Constantes

```vhdl
architecture ejemplo of modulo is
    constant ZERO_8  : std_logic_vector(7 downto 0) := (others => '0');
    constant MAX_VAL : integer := 255;
    constant CLK_DIV : integer := 50_000_000;  -- Separador legible
begin
    ...
end architecture;
```

### 10.2 Alias

Proporciona nombre alternativo a parte de una señal:

```vhdl
signal instruction : std_logic_vector(31 downto 0);

-- Alias para campos de la instrucción
alias opcode  : std_logic_vector(5 downto 0) is instruction(31 downto 26);
alias rs      : std_logic_vector(4 downto 0) is instruction(25 downto 21);
alias rt      : std_logic_vector(4 downto 0) is instruction(20 downto 16);
alias rd      : std_logic_vector(4 downto 0) is instruction(15 downto 11);
alias imm     : std_logic_vector(15 downto 0) is instruction(15 downto 0);
```

---

## 11. Múltiples Arquitecturas

### 11.1 Ejemplo

```vhdl
-- Entidad común
entity filtro is
    port (
        clk    : in  std_logic;
        x      : in  std_logic_vector(15 downto 0);
        y      : out std_logic_vector(15 downto 0)
    );
end entity;

-- Arquitectura 1: FIR
architecture fir of filtro is
begin
    -- Implementación FIR
end architecture;

-- Arquitectura 2: IIR
architecture iir of filtro is
begin
    -- Implementación IIR
end architecture;

-- Al instanciar:
FILT1: entity work.filtro(fir) port map (...);
FILT2: entity work.filtro(iir) port map (...);
```

---

## Referencias

- IEEE Std 1076-2008, "IEEE Standard VHDL Language Reference Manual"
- Ashenden, P. J. (2008). *The Designer's Guide to VHDL*. Morgan Kaufmann.

---

<!-- IA_CONTEXT
NIVEL: Básico (1/3)
PREREQUISITOS: 02-01 Introducción VHDL
CONEXIONES: Fundamento para todos los diseños VHDL
ERRORES_COMUNES: Confundir in/out, olvidar declarar componentes, no especificar genéricos
-->
