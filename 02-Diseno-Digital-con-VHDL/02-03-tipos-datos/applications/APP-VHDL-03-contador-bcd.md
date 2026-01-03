# 🔧 Aplicación: Contador BCD con Tipos de Datos VHDL

```
::METADATA::
tipo: aplicacion
tema: VHDL-03-tipos-datos
dificultad: intermedia
objetivo: Uso práctico de tipos de datos en contador BCD
::END::
```

## 📋 Descripción del Proyecto

Implementar un contador BCD de 2 dígitos (00-99) demostrando el uso de diferentes tipos de datos VHDL.

## 🎯 Objetivos de Aprendizaje

- Usar tipos `integer`, `unsigned` y `std_logic_vector`
- Implementar conversiones entre tipos
- Manejar rangos y restricciones de tipos
- Crear tipos enumerados para estados

## 📝 Código VHDL

### Entidad

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity contador_bcd_2dig is
    port (
        clk     : in  std_logic;
        rst     : in  std_logic;
        enable  : in  std_logic;
        unidades: out std_logic_vector(3 downto 0);
        decenas : out std_logic_vector(3 downto 0);
        carry   : out std_logic
    );
end entity contador_bcd_2dig;
```

### Arquitectura con Tipos Diversos

```vhdl
architecture behavioral of contador_bcd_2dig is
    -- Tipo enumerado para estados
    type estado_t is (IDLE, CUENTA, OVERFLOW);
    signal estado : estado_t := IDLE;
    
    -- Uso de integer con rango restringido
    signal cnt_uni : integer range 0 to 9 := 0;
    signal cnt_dec : integer range 0 to 9 := 0;
    
    -- Señales internas unsigned para operaciones
    signal uni_unsigned : unsigned(3 downto 0);
    signal dec_unsigned : unsigned(3 downto 0);
    
begin
    -- Proceso de conteo
    process(clk, rst)
    begin
        if rst = '1' then
            cnt_uni <= 0;
            cnt_dec <= 0;
            estado <= IDLE;
        elsif rising_edge(clk) then
            case estado is
                when IDLE =>
                    if enable = '1' then
                        estado <= CUENTA;
                    end if;
                    
                when CUENTA =>
                    if enable = '0' then
                        estado <= IDLE;
                    else
                        if cnt_uni = 9 then
                            cnt_uni <= 0;
                            if cnt_dec = 9 then
                                cnt_dec <= 0;
                                estado <= OVERFLOW;
                            else
                                cnt_dec <= cnt_dec + 1;
                            end if;
                        else
                            cnt_uni <= cnt_uni + 1;
                        end if;
                    end if;
                    
                when OVERFLOW =>
                    estado <= CUENTA;
            end case;
        end if;
    end process;
    
    -- Conversiones: integer -> unsigned -> std_logic_vector
    uni_unsigned <= to_unsigned(cnt_uni, 4);
    dec_unsigned <= to_unsigned(cnt_dec, 4);
    
    unidades <= std_logic_vector(uni_unsigned);
    decenas  <= std_logic_vector(dec_unsigned);
    
    carry <= '1' when estado = OVERFLOW else '0';
    
end architecture behavioral;
```

## 🧪 Testbench

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity contador_bcd_2dig_tb is
end entity contador_bcd_2dig_tb;

architecture sim of contador_bcd_2dig_tb is
    signal clk_tb     : std_logic := '0';
    signal rst_tb     : std_logic := '1';
    signal enable_tb  : std_logic := '0';
    signal uni_tb     : std_logic_vector(3 downto 0);
    signal dec_tb     : std_logic_vector(3 downto 0);
    signal carry_tb   : std_logic;
    
    constant CLK_PERIOD : time := 10 ns;
begin
    -- Instancia DUT
    DUT: entity work.contador_bcd_2dig
        port map (
            clk      => clk_tb,
            rst      => rst_tb,
            enable   => enable_tb,
            unidades => uni_tb,
            decenas  => dec_tb,
            carry    => carry_tb
        );
    
    -- Generador de reloj
    clk_tb <= not clk_tb after CLK_PERIOD/2;
    
    -- Estímulos
    stim_proc: process
    begin
        wait for 20 ns;
        rst_tb <= '0';
        wait for 20 ns;
        
        enable_tb <= '1';
        -- Contar hasta overflow (100 ciclos)
        wait for 110 * CLK_PERIOD;
        
        enable_tb <= '0';
        wait for 30 ns;
        
        wait;
    end process;
end architecture sim;
```

## 📊 Tipos de Datos Utilizados

| Tipo | Uso | Ventaja |
|------|-----|---------|
| `integer range` | Contadores internos | Síntesis eficiente, auto-límite |
| `unsigned` | Operaciones aritméticas | Soporte de operadores +/- |
| `std_logic_vector` | Puertos de salida | Compatibilidad universal |
| `type enum` | Máquina de estados | Código legible y seguro |

## 🔗 Referencias

- [VHDL-03-Teoria-TiposDatos.md](../theory/VHDL-03-Teoria-TiposDatos.md)
- [VHDL-03-Metodos-TiposDatos.md](../methods/VHDL-03-Metodos-TiposDatos.md)
