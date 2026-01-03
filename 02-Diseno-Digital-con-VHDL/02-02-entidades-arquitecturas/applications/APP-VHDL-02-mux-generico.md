# 🔧 Aplicación: Multiplexor Genérico en VHDL

```
::METADATA::
tipo: aplicacion
tema: VHDL-02-entidades-arquitecturas
dificultad: intermedia
objetivo: Diseño parametrizable con generics
::END::
```

## 📋 Descripción del Proyecto

Implementar un multiplexor configurable usando generics para definir el ancho de datos.

## 🎯 Objetivos de Aprendizaje

- Usar generics para diseños parametrizables
- Definir puertos con tamaño variable
- Instanciar componentes con configuración

## 📝 Código VHDL

### MUX 4:1 Genérico

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux4to1_generic is
    generic (
        WIDTH : positive := 8  -- Ancho de datos configurable
    );
    port (
        sel   : in  std_logic_vector(1 downto 0);
        in0   : in  std_logic_vector(WIDTH-1 downto 0);
        in1   : in  std_logic_vector(WIDTH-1 downto 0);
        in2   : in  std_logic_vector(WIDTH-1 downto 0);
        in3   : in  std_logic_vector(WIDTH-1 downto 0);
        output: out std_logic_vector(WIDTH-1 downto 0)
    );
end entity mux4to1_generic;

architecture dataflow of mux4to1_generic is
begin
    with sel select
        output <= in0 when "00",
                  in1 when "01",
                  in2 when "10",
                  in3 when "11",
                  (others => 'X') when others;
end architecture dataflow;
```

### Uso del Componente

```vhdl
-- Instancia MUX de 8 bits (valor por defecto)
mux_8bit: entity work.mux4to1_generic
    port map (
        sel    => select_signal,
        in0    => data_a,
        in1    => data_b,
        in2    => data_c,
        in3    => data_d,
        output => result
    );

-- Instancia MUX de 16 bits
mux_16bit: entity work.mux4to1_generic
    generic map (WIDTH => 16)
    port map (
        sel    => select_signal,
        in0    => data_a_wide,
        in1    => data_b_wide,
        in2    => data_c_wide,
        in3    => data_d_wide,
        output => result_wide
    );
```

## 🧪 Testbench

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux4to1_tb is
end entity mux4to1_tb;

architecture sim of mux4to1_tb is
    constant TB_WIDTH : positive := 4;
    
    signal sel_tb  : std_logic_vector(1 downto 0);
    signal in0_tb  : std_logic_vector(TB_WIDTH-1 downto 0) := "0001";
    signal in1_tb  : std_logic_vector(TB_WIDTH-1 downto 0) := "0010";
    signal in2_tb  : std_logic_vector(TB_WIDTH-1 downto 0) := "0100";
    signal in3_tb  : std_logic_vector(TB_WIDTH-1 downto 0) := "1000";
    signal out_tb  : std_logic_vector(TB_WIDTH-1 downto 0);
begin
    DUT: entity work.mux4to1_generic
        generic map (WIDTH => TB_WIDTH)
        port map (
            sel    => sel_tb,
            in0    => in0_tb,
            in1    => in1_tb,
            in2    => in2_tb,
            in3    => in3_tb,
            output => out_tb
        );
    
    stim_proc: process
    begin
        sel_tb <= "00"; wait for 10 ns;  -- Espera in0 = 0001
        assert out_tb = "0001" report "Error sel=00" severity error;
        
        sel_tb <= "01"; wait for 10 ns;  -- Espera in1 = 0010
        assert out_tb = "0010" report "Error sel=01" severity error;
        
        sel_tb <= "10"; wait for 10 ns;  -- Espera in2 = 0100
        assert out_tb = "0100" report "Error sel=10" severity error;
        
        sel_tb <= "11"; wait for 10 ns;  -- Espera in3 = 1000
        assert out_tb = "1000" report "Error sel=11" severity error;
        
        report "Simulación completada exitosamente!";
        wait;
    end process;
end architecture sim;
```

## 📐 Arquitectura Alternativa (Estructural)

```vhdl
architecture structural of mux4to1_generic is
    -- Usando generate para crear lógica bit a bit
begin
    gen_mux: for i in 0 to WIDTH-1 generate
        output(i) <= (in0(i) and not sel(1) and not sel(0)) or
                     (in1(i) and not sel(1) and     sel(0)) or
                     (in2(i) and     sel(1) and not sel(0)) or
                     (in3(i) and     sel(1) and     sel(0));
    end generate;
end architecture structural;
```

## ✅ Criterios de Éxito

- [ ] Funciona para cualquier WIDTH > 0
- [ ] Síntesis eficiente (LUTs mínimas)
- [ ] Testbench self-checking pasa
- [ ] Documentación clara de generics

## 📚 Recursos Relacionados

- [VHDL-02-Intro.md](../VHDL-02-Intro.md)
- [GLOSSARY: generic](../../../GLOSSARY/README.md#generic)
- [GLOSSARY: mux](../../../GLOSSARY/README.md#mux)

---

> 💡 **Tip**: Los generics permiten reutilizar código para diferentes anchos de datos
