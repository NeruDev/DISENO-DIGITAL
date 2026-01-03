# Soluciones Detalladas: Síntesis y Simulación (VHDL-07)

```
::METADATA::
tipo: indice-soluciones
tema: vhdl-07-sintesis-simulacion
actualizado: 2026-01-03
::END::
```

## Estructura de Niveles de Solución

| Nivel | Archivo | Contenido |
|-------|---------|-----------|
| 1️⃣ | [`VHDL-07-Respuestas.md`](../VHDL-07-Respuestas.md) | Solo respuestas finales |
| 2️⃣ | Esta carpeta `prob-01/` | Soluciones paso a paso |
| 3️⃣ | Secciones "Conceptos Clave" | Explicación profunda del método |

---

## Índice de Soluciones Detalladas

### Nivel 1: Conceptos de Síntesis ⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 1.1 | RTL vs Behavioral | [VHDL-07-Sol-Problema-1.1.md](VHDL-07-Sol-Problema-1.1.md) | ⭐⭐ |
| 1.2 | Código sintetizable | [VHDL-07-Sol-Problema-1.2.md](VHDL-07-Sol-Problema-1.2.md) | ⭐⭐ |
| 1.3 | Inferencia de hardware | [VHDL-07-Sol-Problema-1.3.md](VHDL-07-Sol-Problema-1.3.md) | ⭐⭐ |

### Nivel 2: Testbenches ⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 2.1 | Testbench básico | [VHDL-07-Sol-Problema-2.1.md](VHDL-07-Sol-Problema-2.1.md) | ⭐⭐ |
| 2.2 | Generación de estímulos | [VHDL-07-Sol-Problema-2.2.md](VHDL-07-Sol-Problema-2.2.md) | ⭐⭐ |
| 2.3 | Aserciones y verificación | [VHDL-07-Sol-Problema-2.3.md](VHDL-07-Sol-Problema-2.3.md) | ⭐⭐ |

### Nivel 3: Timing y Constraints ⭐⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 3.1 | Setup y Hold time | [VHDL-07-Sol-Problema-3.1.md](VHDL-07-Sol-Problema-3.1.md) | ⭐⭐⭐ |
| 3.2 | Clock constraints | [VHDL-07-Sol-Problema-3.2.md](VHDL-07-Sol-Problema-3.2.md) | ⭐⭐⭐ |
| 3.3 | Timing closure | [VHDL-07-Sol-Problema-3.3.md](VHDL-07-Sol-Problema-3.3.md) | ⭐⭐⭐ |

### Nivel 4: Optimización ⭐⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 4.1 | Área vs Velocidad | [VHDL-07-Sol-Problema-4.1.md](VHDL-07-Sol-Problema-4.1.md) | ⭐⭐⭐ |
| 4.2 | Resource sharing | [VHDL-07-Sol-Problema-4.2.md](VHDL-07-Sol-Problema-4.2.md) | ⭐⭐⭐ |
| 4.3 | Pipelining | [VHDL-07-Sol-Problema-4.3.md](VHDL-07-Sol-Problema-4.3.md) | ⭐⭐⭐ |

---

## Flujo de Diseño VHDL

```
    ┌─────────────┐
    │ Especific.  │
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐     ┌─────────────┐
    │ Diseño VHDL │────►│ Simulación  │──── ¿OK? ──┐
    │    (RTL)    │     │ Funcional   │            │
    └──────┬──────┘     └─────────────┘            │No
           │                                       │
           │Sí                                     ▼
           ▼                              ┌────────────┐
    ┌─────────────┐                       │  Corregir  │
    │  Síntesis   │                       └────────────┘
    │   (Netlist) │
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐     ┌─────────────┐
    │ Place & Route────►│ Simulación  │
    │             │     │  Timing     │
    └──────┬──────┘     └─────────────┘
           │
           ▼
    ┌─────────────┐
    │  Bitstream  │
    │   (FPGA)    │
    └─────────────┘
```

---

## Plantilla de Testbench

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity tb_modulo is
    -- Testbench no tiene puertos
end entity tb_modulo;

architecture test of tb_modulo is
    -- Constantes
    constant CLK_PERIOD : time := 10 ns;
    
    -- Señales de estímulo
    signal clk     : std_logic := '0';
    signal reset   : std_logic := '1';
    signal entrada : std_logic_vector(7 downto 0);
    
    -- Señales de salida
    signal salida  : std_logic_vector(7 downto 0);
    
begin
    -- Instancia del DUT (Device Under Test)
    DUT: entity work.modulo
        port map (
            clk     => clk,
            reset   => reset,
            entrada => entrada,
            salida  => salida
        );
    
    -- Generación de reloj
    clk <= not clk after CLK_PERIOD/2;
    
    -- Proceso de estímulos
    stim_proc: process
    begin
        -- Reset inicial
        reset <= '1';
        entrada <= (others => '0');
        wait for CLK_PERIOD * 5;
        
        -- Quitar reset
        reset <= '0';
        wait for CLK_PERIOD;
        
        -- Aplicar estímulos
        entrada <= x"AA";
        wait for CLK_PERIOD * 10;
        
        entrada <= x"55";
        wait for CLK_PERIOD * 10;
        
        -- Verificar resultados
        assert salida = x"FF" 
            report "Error: salida incorrecta" 
            severity error;
        
        -- Fin de simulación
        report "Simulación completada" severity note;
        wait;
    end process;
    
end architecture test;
```

---

## Código Sintetizable vs No Sintetizable

### ✅ Sintetizable

```vhdl
-- Registros
process(clk)
begin
    if rising_edge(clk) then
        reg <= data;
    end if;
end process;

-- Lógica combinacional
output <= a and b;

-- MUX
y <= a when sel = '1' else b;

-- Instanciación
U1: entity work.component port map(...);
```

### ❌ No Sintetizable (Solo simulación)

```vhdl
-- Wait con tiempo específico
wait for 10 ns;

-- After (delays)
y <= x after 5 ns;

-- File I/O
file f : text open read_mode is "data.txt";

-- Assert con report
assert a = b report "Error" severity error;

-- Inicialización de señales (algunas herramientas)
signal x : std_logic := '1';
```

---

## Inferencia de Hardware

| Código VHDL | Hardware Inferido |
|-------------|-------------------|
| `if rising_edge(clk)` | Flip-flop |
| `if clk'event and clk='1'` | Flip-flop |
| Proceso sin clk | Lógica combinacional |
| `case` / `with select` | MUX / Decoder |
| `+`, `-` | Sumador/Restador |
| `*` | Multiplicador |
| `sll`, `srl` | Shifter |

---

## Navegación

| ⬅️ Respuestas | 🏠 Intro | ➡️ Problemas |
|:-------------:|:--------:|:------------:|
| [VHDL-07-Respuestas.md](../VHDL-07-Respuestas.md) | [VHDL-07-Intro.md](../../VHDL-07-Intro.md) | [VHDL-07-Problemas.md](../../problems/VHDL-07-Problemas.md) |
