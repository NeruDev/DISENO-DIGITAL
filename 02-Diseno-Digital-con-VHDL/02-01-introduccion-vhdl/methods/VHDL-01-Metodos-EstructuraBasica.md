<!--
::METADATA::
type: method
topic_id: vhdl-01-introduccion
file_id: metodos-estructura-basica
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [VHDL, estructura, plantilla, metodologia]
search_keywords: "estructura VHDL, plantilla, metodología diseño"
-->

> 🏠 **Navegación:** [← Teoría](../theory/VHDL-01-Teoria-IntroduccionVHDL.md) | [Problemas →](../problems/VHDL-01-Problemas.md)

---

# Métodos: Estructura Básica de VHDL

## Método 1: Plantilla Básica de Archivo VHDL

### Estructura Estándar

```vhdl
--------------------------------------------------------------------------------
-- Archivo: nombre_modulo.vhd
-- Autor: [Tu nombre]
-- Fecha: [Fecha]
-- Descripción: [Breve descripción del módulo]
--------------------------------------------------------------------------------

-- 1. DECLARACIÓN DE BIBLIOTECAS
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

-- 2. DECLARACIÓN DE ENTIDAD
entity nombre_modulo is
    generic (
        -- Parámetros genéricos (opcionales)
        PARAM1 : integer := 8
    );
    port (
        -- Entradas
        clk     : in  std_logic;
        reset   : in  std_logic;
        entrada : in  std_logic_vector(7 downto 0);
        
        -- Salidas
        salida  : out std_logic_vector(7 downto 0)
    );
end entity nombre_modulo;

-- 3. DECLARACIÓN DE ARQUITECTURA
architecture behavioral of nombre_modulo is
    
    -- Declaración de señales internas
    signal senal_interna : std_logic;
    
    -- Declaración de constantes
    constant VALOR_MAX : integer := 255;
    
begin
    
    -- Implementación del comportamiento
    
end architecture behavioral;
```

---

## Método 2: Declarar Puertos Correctamente

### Tipos de Puertos

| Modo | Descripción | Uso |
|------|-------------|-----|
| `in` | Solo lectura | Entradas |
| `out` | Solo escritura | Salidas |
| `inout` | Lectura y escritura | Bidireccional |
| `buffer` | Salida legible internamente | Poco usado |

### Reglas

```vhdl
port (
    -- Entradas primero (convención)
    clk    : in  std_logic;                      -- Reloj
    rst_n  : in  std_logic;                      -- Reset activo bajo
    enable : in  std_logic;                      -- Enable
    data_in: in  std_logic_vector(7 downto 0);   -- Bus de datos
    
    -- Salidas después
    data_out : out std_logic_vector(7 downto 0);
    valid    : out std_logic;
    
    -- Bidireccional al final
    data_io  : inout std_logic_vector(7 downto 0)  -- Sin coma al final
);
```

### Convenciones de Nombres

| Sufijo | Significado |
|--------|-------------|
| `_n` | Activo bajo (negado) |
| `_i` | Input |
| `_o` | Output |
| `_io` | Bidireccional |
| `_clk` | Señal de reloj |
| `_rst` | Reset |
| `_en` | Enable |

---

## Método 3: Usar std_logic vs bit

### Comparación

| Característica | `bit` | `std_logic` |
|----------------|-------|-------------|
| Valores | '0', '1' | 9 valores |
| Alta impedancia | No | 'Z' |
| Don't care | No | '-' |
| Síntesis | Limitada | Completa |
| Recomendado | No | **Sí** |

### Ejemplo

```vhdl
-- NO recomendado
signal a : bit;
signal bus1 : bit_vector(7 downto 0);

-- RECOMENDADO
signal a : std_logic;
signal bus1 : std_logic_vector(7 downto 0);
```

---

## Método 4: Asignación de Señales

### Asignación Concurrente (fuera de process)

```vhdl
architecture ejemplo of modulo is
begin
    -- Asignación simple
    Y <= A and B;
    
    -- Asignación condicional (when-else)
    Y <= '1' when A = '1' else
         '0' when B = '1' else
         'Z';
    
    -- Asignación selectiva (with-select)
    with sel select
        Y <= A when "00",
             B when "01",
             C when "10",
             D when others;
end architecture;
```

### Asignación Secuencial (dentro de process)

```vhdl
process(clk)
begin
    if rising_edge(clk) then
        Q <= D;  -- Flip-flop D
    end if;
end process;
```

---

## Método 5: Crear Testbench Básico

### Estructura de Testbench

```vhdl
--------------------------------------------------------------------------------
-- Testbench para: nombre_modulo
--------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_nombre_modulo is
    -- El testbench no tiene puertos
end entity tb_nombre_modulo;

architecture sim of tb_nombre_modulo is

    -- Componente a probar
    component nombre_modulo is
        port (
            clk    : in  std_logic;
            reset  : in  std_logic;
            entrada: in  std_logic;
            salida : out std_logic
        );
    end component;
    
    -- Señales de estímulo
    signal clk_tb    : std_logic := '0';
    signal reset_tb  : std_logic := '1';
    signal entrada_tb: std_logic := '0';
    signal salida_tb : std_logic;
    
    -- Constante de período de reloj
    constant CLK_PERIOD : time := 10 ns;

begin

    -- Instanciación del DUT (Device Under Test)
    DUT: nombre_modulo
        port map (
            clk     => clk_tb,
            reset   => reset_tb,
            entrada => entrada_tb,
            salida  => salida_tb
        );
    
    -- Generación de reloj
    clk_process: process
    begin
        clk_tb <= '0';
        wait for CLK_PERIOD / 2;
        clk_tb <= '1';
        wait for CLK_PERIOD / 2;
    end process;
    
    -- Proceso de estímulos
    stim_process: process
    begin
        -- Reset inicial
        reset_tb <= '1';
        wait for 100 ns;
        reset_tb <= '0';
        
        -- Aplicar estímulos
        entrada_tb <= '1';
        wait for 50 ns;
        entrada_tb <= '0';
        wait for 50 ns;
        
        -- Fin de simulación
        report "Simulación completada" severity note;
        wait;
    end process;

end architecture sim;
```

---

## Método 6: Instanciación de Componentes

### Declaración e Instanciación

```vhdl
architecture structural of top_module is

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
    
    -- Señales internas
    signal count_sig : std_logic_vector(7 downto 0);
    
begin

    -- Instanciación con port map posicional (no recomendado)
    inst1: contador
        generic map (8)
        port map (clk, reset, enable, count_sig);
    
    -- Instanciación con port map nominal (RECOMENDADO)
    inst2: contador
        generic map (
            WIDTH => 8
        )
        port map (
            clk    => clk,
            reset  => reset,
            enable => enable,
            count  => count_sig
        );

end architecture;
```

---

## Método 7: Genéricos para Diseños Parametrizables

### Definición de Genéricos

```vhdl
entity registro is
    generic (
        WIDTH : integer := 8;        -- Ancho del registro
        RESET_VALUE : std_logic_vector := x"00"  -- Valor inicial
    );
    port (
        clk   : in  std_logic;
        reset : in  std_logic;
        d     : in  std_logic_vector(WIDTH-1 downto 0);
        q     : out std_logic_vector(WIDTH-1 downto 0)
    );
end entity;
```

### Uso de Genéricos

```vhdl
-- Registro de 8 bits
reg8: registro
    generic map (WIDTH => 8, RESET_VALUE => x"00")
    port map (...);

-- Registro de 16 bits
reg16: registro
    generic map (WIDTH => 16, RESET_VALUE => x"0000")
    port map (...);
```

---

## Método 8: Organización de Proyectos

### Estructura de Carpetas

```
proyecto/
├── src/
│   ├── top_module.vhd
│   ├── submodulo1.vhd
│   └── submodulo2.vhd
├── tb/
│   ├── tb_top_module.vhd
│   └── tb_submodulo1.vhd
├── sim/
│   └── wave.do
├── syn/
│   └── constraints.sdc
└── doc/
    └── especificacion.pdf
```

### Convenciones de Nombres de Archivos

- Un archivo por entidad
- Nombre del archivo = nombre de la entidad
- Extensión `.vhd` o `.vhdl`
- Testbenches con prefijo `tb_`

---

## Método 9: Síntesis vs Simulación

### Código Sintetizable

```vhdl
-- ✓ Sintetizable
process(clk)
begin
    if rising_edge(clk) then
        if reset = '1' then
            q <= (others => '0');
        else
            q <= d;
        end if;
    end if;
end process;
```

### Código Solo para Simulación

```vhdl
-- ✗ NO sintetizable (solo simulación)
wait for 10 ns;
report "Valor = " & integer'image(to_integer(unsigned(dato)));
assert (salida = esperado) report "Error!" severity error;

-- Variables de tipo file, text
-- Asignaciones con 'after'
salida <= '1' after 5 ns;
```

---

## Método 10: Checklist de Código VHDL

### Antes de Sintetizar

- [ ] Todas las señales tienen valor por defecto o se inicializan
- [ ] No hay latches no intencionales
- [ ] Todas las ramas de if/case están cubiertas
- [ ] Los procesos tienen lista de sensibilidad completa
- [ ] Los tipos coinciden (no hay conversiones implícitas)
- [ ] No hay warnings en la compilación

### Estilo de Código

- [ ] Indentación consistente (2 o 4 espacios)
- [ ] Comentarios significativos
- [ ] Nombres descriptivos
- [ ] Una entidad por archivo
- [ ] Genéricos para valores parametrizables

---

<!-- IA_CONTEXT
USO: Referencia para estructura básica de proyectos VHDL
NIVEL: Básico (1/3)
HERRAMIENTAS: Quartus, Vivado, ModelSim, GHDL
-->
