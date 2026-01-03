# 🔧 Aplicación: Testbench Completo con Auto-verificación

```
::METADATA::
tipo: aplicacion
tema: VHDL-07-sintesis-simulacion
dificultad: avanzada
objetivo: Crear testbench profesional con auto-verificación y cobertura
::END::
```

## 📋 Descripción del Proyecto

Desarrollar un testbench completo para verificar un multiplicador de 8 bits, incluyendo generación automática de estímulos, auto-verificación y reportes de cobertura.

## 🎯 Objetivos de Aprendizaje

- Crear testbenches auto-verificables
- Implementar generación de estímulos aleatorios
- Usar assert para verificación automática
- Generar reportes de simulación
- Medir cobertura funcional

## 📝 DUT: Multiplicador de 8 bits

### Entidad del DUT

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity multiplicador_8bit is
    port (
        clk     : in  std_logic;
        rst     : in  std_logic;
        start   : in  std_logic;
        a, b    : in  std_logic_vector(7 downto 0);
        producto: out std_logic_vector(15 downto 0);
        done    : out std_logic
    );
end entity multiplicador_8bit;

architecture rtl of multiplicador_8bit is
    type estado_t is (IDLE, CALC, FIN);
    signal estado : estado_t := IDLE;
    signal acc    : unsigned(15 downto 0);
    signal mult   : unsigned(7 downto 0);
    signal cnt    : integer range 0 to 8;
begin
    process(clk, rst)
    begin
        if rst = '1' then
            estado <= IDLE;
            acc <= (others => '0');
            done <= '0';
        elsif rising_edge(clk) then
            done <= '0';
            case estado is
                when IDLE =>
                    if start = '1' then
                        acc <= (others => '0');
                        mult <= unsigned(b);
                        cnt <= 0;
                        estado <= CALC;
                    end if;
                when CALC =>
                    if mult(0) = '1' then
                        acc <= acc + (unsigned(a) & x"00") srl (8 - cnt);
                    end if;
                    mult <= '0' & mult(7 downto 1);
                    cnt <= cnt + 1;
                    if cnt = 7 then
                        estado <= FIN;
                    end if;
                when FIN =>
                    done <= '1';
                    estado <= IDLE;
            end case;
        end if;
    end process;
    
    producto <= std_logic_vector(acc);
end architecture rtl;
```

## 🧪 Testbench Completo

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use IEEE.MATH_REAL.ALL;  -- Para generación aleatoria
use STD.TEXTIO.ALL;

entity multiplicador_8bit_tb is
end entity multiplicador_8bit_tb;

architecture tb of multiplicador_8bit_tb is
    -- Constantes
    constant CLK_PERIOD : time := 10 ns;
    constant NUM_TESTS  : integer := 100;
    
    -- Señales DUT
    signal clk_tb      : std_logic := '0';
    signal rst_tb      : std_logic := '1';
    signal start_tb    : std_logic := '0';
    signal a_tb, b_tb  : std_logic_vector(7 downto 0) := (others => '0');
    signal prod_tb     : std_logic_vector(15 downto 0);
    signal done_tb     : std_logic;
    
    -- Contadores de verificación
    signal test_count  : integer := 0;
    signal pass_count  : integer := 0;
    signal fail_count  : integer := 0;
    
    -- Flag de fin de simulación
    signal sim_done    : boolean := false;
    
    -- Función para generar número aleatorio
    impure function random_byte return std_logic_vector is
        variable seed1, seed2 : positive := 1;
        variable rand : real;
        variable result : integer;
    begin
        uniform(seed1, seed2, rand);
        result := integer(rand * 255.0);
        return std_logic_vector(to_unsigned(result, 8));
    end function;
    
begin
    -- Instancia DUT
    DUT: entity work.multiplicador_8bit
        port map (
            clk      => clk_tb,
            rst      => rst_tb,
            start    => start_tb,
            a        => a_tb,
            b        => b_tb,
            producto => prod_tb,
            done     => done_tb
        );
    
    -- Generador de reloj
    CLK_GEN: process
    begin
        while not sim_done loop
            clk_tb <= '0';
            wait for CLK_PERIOD/2;
            clk_tb <= '1';
            wait for CLK_PERIOD/2;
        end loop;
        wait;
    end process CLK_GEN;
    
    -- Proceso de estímulos y verificación
    STIM_PROC: process
        variable expected : integer;
        variable actual   : integer;
        variable v_a, v_b : integer;
        variable l : line;
        
        -- Procedimiento para ejecutar un test
        procedure run_test(a_val, b_val : integer) is
        begin
            a_tb <= std_logic_vector(to_unsigned(a_val, 8));
            b_tb <= std_logic_vector(to_unsigned(b_val, 8));
            
            wait until rising_edge(clk_tb);
            start_tb <= '1';
            wait until rising_edge(clk_tb);
            start_tb <= '0';
            
            -- Esperar resultado
            wait until done_tb = '1';
            wait until rising_edge(clk_tb);
            
            -- Calcular valores
            expected := a_val * b_val;
            actual := to_integer(unsigned(prod_tb));
            test_count <= test_count + 1;
            
            -- Verificar resultado
            if actual = expected then
                pass_count <= pass_count + 1;
            else
                fail_count <= fail_count + 1;
                -- Reportar error
                write(l, string'("ERROR: "));
                write(l, a_val);
                write(l, string'(" * "));
                write(l, b_val);
                write(l, string'(" = "));
                write(l, actual);
                write(l, string'(" (esperado: "));
                write(l, expected);
                write(l, string'(")"));
                writeline(output, l);
            end if;
        end procedure;
        
    begin
        -- Reset inicial
        rst_tb <= '1';
        wait for 100 ns;
        rst_tb <= '0';
        wait for 50 ns;
        
        -- ========== CASOS LÍMITE ==========
        report "=== Iniciando tests de casos límite ===" severity note;
        
        -- Test 0 * 0
        run_test(0, 0);
        
        -- Test 0 * X
        run_test(0, 128);
        
        -- Test X * 0
        run_test(200, 0);
        
        -- Test 1 * 1
        run_test(1, 1);
        
        -- Test 255 * 1
        run_test(255, 1);
        
        -- Test 1 * 255
        run_test(1, 255);
        
        -- Test 255 * 255 (máximo)
        run_test(255, 255);
        
        -- ========== CASOS CONOCIDOS ==========
        report "=== Iniciando tests de casos conocidos ===" severity note;
        
        run_test(10, 10);    -- 100
        run_test(12, 12);    -- 144
        run_test(16, 16);    -- 256
        run_test(100, 100);  -- 10000
        
        -- ========== TESTS ALEATORIOS ==========
        report "=== Iniciando tests aleatorios ===" severity note;
        
        for i in 1 to NUM_TESTS loop
            v_a := to_integer(unsigned(random_byte));
            v_b := to_integer(unsigned(random_byte));
            run_test(v_a, v_b);
        end loop;
        
        -- ========== REPORTE FINAL ==========
        wait for 100 ns;
        
        report "============================================" severity note;
        report "           REPORTE DE SIMULACIÓN            " severity note;
        report "============================================" severity note;
        report "Total de tests: " & integer'image(test_count) severity note;
        report "Tests pasados:  " & integer'image(pass_count) severity note;
        report "Tests fallidos: " & integer'image(fail_count) severity note;
        
        if fail_count = 0 then
            report ">>> TODOS LOS TESTS PASARON <<<" severity note;
        else
            report ">>> HAY ERRORES EN EL DISEÑO <<<" severity error;
        end if;
        report "============================================" severity note;
        
        sim_done <= true;
        wait;
    end process STIM_PROC;
    
    -- Monitor de timeout
    TIMEOUT: process
    begin
        wait for 1 ms;
        if not sim_done then
            report "TIMEOUT: Simulación excedió tiempo máximo" severity failure;
        end if;
        wait;
    end process TIMEOUT;
    
end architecture tb;
```

## 📊 Estructura del Testbench

```
┌──────────────────────────────────────────────────┐
│                  TESTBENCH                       │
├──────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────┐             │
│  │ CLK_GEN     │    │ TIMEOUT     │             │
│  │ (Reloj)     │    │ (Watchdog)  │             │
│  └─────────────┘    └─────────────┘             │
│                                                  │
│  ┌──────────────────────────────────────────┐   │
│  │             STIM_PROC                    │   │
│  │  ┌────────────┐  ┌────────────────────┐  │   │
│  │  │ Casos      │  │ Verificación       │  │   │
│  │  │ Límite     │  │ Automática         │  │   │
│  │  └────────────┘  └────────────────────┘  │   │
│  │  ┌────────────┐  ┌────────────────────┐  │   │
│  │  │ Casos      │  │ Generación         │  │   │
│  │  │ Conocidos  │  │ Aleatoria          │  │   │
│  │  └────────────┘  └────────────────────┘  │   │
│  └──────────────────────────────────────────┘   │
│                       │                          │
│                       v                          │
│              ┌──────────────┐                    │
│              │     DUT      │                    │
│              │ Multiplicador│                    │
│              └──────────────┘                    │
└──────────────────────────────────────────────────┘
```

## 📋 Checklist de Verificación

- [x] Casos límite (0, 1, 255)
- [x] Casos conocidos (verificación manual)
- [x] Tests aleatorios (cobertura amplia)
- [x] Auto-verificación con assert
- [x] Reporte de resultados
- [x] Timeout de seguridad
- [x] Conteo de pass/fail

## 🔗 Referencias

- [VHDL-07-Teoria-SintesisSimulacion.md](../theory/VHDL-07-Teoria-SintesisSimulacion.md)
- [VHDL-07-Metodos-Verificacion.md](../methods/VHDL-07-Metodos-Verificacion.md)
