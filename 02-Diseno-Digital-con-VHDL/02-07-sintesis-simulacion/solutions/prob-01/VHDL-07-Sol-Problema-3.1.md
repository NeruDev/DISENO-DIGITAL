<!--
::METADATA::
type: detailed_solution
topic_id: vhdl-07-sintesis-simulacion
problem_id: 3.1
file_id: solucion-problema-3-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 3
tags: [solucion, VHDL, testbench, simulacion, verificacion]
-->

> 🏠 **Navegación:** [← Índice](./README.md) | [Problema 3.2 →](./VHDL-07-Sol-Problema-3.2.md)

---

# Solución Detallada: Problema 3.1

## Enunciado
Crear un testbench completo para verificar un sumador de 4 bits con acarreo de entrada y salida.

---

## Paso 1: Diseño Bajo Prueba (DUT)

### Interfaz del Sumador

```
         ┌─────────────────────┐
 A[3:0] ─┤                     ├─ SUM[3:0]
 B[3:0] ─┤   ADDER 4-BIT      │
 Cin ────┤                     ├─ Cout
         └─────────────────────┘
```

### Código del Sumador

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity adder_4bit is
    port (
        A    : in  std_logic_vector(3 downto 0);
        B    : in  std_logic_vector(3 downto 0);
        Cin  : in  std_logic;
        SUM  : out std_logic_vector(3 downto 0);
        Cout : out std_logic
    );
end entity adder_4bit;

architecture behavioral of adder_4bit is
    signal temp : unsigned(4 downto 0);  -- 5 bits para acarreo
begin
    temp <= ('0' & unsigned(A)) + unsigned(B) + ("0000" & Cin);
    SUM  <= std_logic_vector(temp(3 downto 0));
    Cout <= temp(4);
end architecture behavioral;
```

---

## Paso 2: Estructura del Testbench

### Arquitectura General

```
┌─────────────────────────────────────────────────────────┐
│                      TESTBENCH                          │
│  ┌──────────────┐                                       │
│  │  GENERADOR   │──► A, B, Cin                          │
│  │  DE ESTIM.   │                                       │
│  └──────────────┘         ┌───────────────┐             │
│                           │               │             │
│           A, B, Cin ─────►│     DUT       ├────► SUM    │
│                           │  adder_4bit   │             │
│                           │               ├────► Cout   │
│                           └───────────────┘             │
│  ┌──────────────┐                                       │
│  │   CHECKER    │◄── SUM, Cout                          │
│  │  (Asserts)   │                                       │
│  └──────────────┘                                       │
└─────────────────────────────────────────────────────────┘
```

---

## Paso 3: Testbench Completo

```vhdl
--------------------------------------------------------------------------------
-- Archivo: tb_adder_4bit.vhd
-- Descripción: Testbench exhaustivo para sumador de 4 bits
-- Metodología: Self-checking con modelo de referencia
--------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity tb_adder_4bit is
    -- Entidad vacía (característica de testbenches)
end entity tb_adder_4bit;

architecture test of tb_adder_4bit is

    ---------------------------------------------------------------------------
    -- CONSTANTES
    ---------------------------------------------------------------------------
    constant CLK_PERIOD : time := 10 ns;
    constant N_BITS     : integer := 4;
    
    ---------------------------------------------------------------------------
    -- SEÑALES DE ESTÍMULO
    ---------------------------------------------------------------------------
    signal A, B     : std_logic_vector(N_BITS-1 downto 0) := (others => '0');
    signal Cin      : std_logic := '0';
    
    ---------------------------------------------------------------------------
    -- SEÑALES DE RESPUESTA
    ---------------------------------------------------------------------------
    signal SUM      : std_logic_vector(N_BITS-1 downto 0);
    signal Cout     : std_logic;
    
    ---------------------------------------------------------------------------
    -- SEÑALES DE VERIFICACIÓN
    ---------------------------------------------------------------------------
    signal expected_sum  : std_logic_vector(N_BITS-1 downto 0);
    signal expected_cout : std_logic;
    signal test_count    : integer := 0;
    signal error_count   : integer := 0;
    signal clk           : std_logic := '0';
    
begin

    ---------------------------------------------------------------------------
    -- DUT INSTANTIATION
    ---------------------------------------------------------------------------
    DUT: entity work.adder_4bit
        port map (
            A    => A,
            B    => B,
            Cin  => Cin,
            SUM  => SUM,
            Cout => Cout
        );
    
    ---------------------------------------------------------------------------
    -- CLOCK GENERATION
    ---------------------------------------------------------------------------
    clk <= not clk after CLK_PERIOD/2;
    
    ---------------------------------------------------------------------------
    -- MODELO DE REFERENCIA (para verificación)
    ---------------------------------------------------------------------------
    reference_model: process(A, B, Cin)
        variable temp : unsigned(N_BITS downto 0);
    begin
        temp := ('0' & unsigned(A)) + unsigned(B) + ("0000" & Cin);
        expected_sum  <= std_logic_vector(temp(N_BITS-1 downto 0));
        expected_cout <= temp(N_BITS);
    end process;
    
    ---------------------------------------------------------------------------
    -- PROCESO DE ESTÍMULOS
    ---------------------------------------------------------------------------
    stimulus: process
        -- Procedimiento para un caso de prueba
        procedure test_case(
            constant a_val  : in integer;
            constant b_val  : in integer;
            constant cin_val: in std_logic;
            constant desc   : in string
        ) is
        begin
            A   <= std_logic_vector(to_unsigned(a_val, N_BITS));
            B   <= std_logic_vector(to_unsigned(b_val, N_BITS));
            Cin <= cin_val;
            wait for CLK_PERIOD;
            
            test_count <= test_count + 1;
            
            -- Verificación automática
            if SUM /= expected_sum or Cout /= expected_cout then
                error_count <= error_count + 1;
                report "ERROR: " & desc & 
                       " | A=" & integer'image(a_val) &
                       " B=" & integer'image(b_val) &
                       " Cin=" & std_logic'image(cin_val) &
                       " | Got SUM=" & integer'image(to_integer(unsigned(SUM))) &
                       " Cout=" & std_logic'image(Cout) &
                       " | Expected SUM=" & integer'image(to_integer(unsigned(expected_sum))) &
                       " Cout=" & std_logic'image(expected_cout)
                severity error;
            else
                report "PASS: " & desc severity note;
            end if;
        end procedure;
        
    begin
        report "========== INICIO DE SIMULACIÓN ==========" severity note;
        
        -------------------------------------------------------------------
        -- CASOS BÁSICOS
        -------------------------------------------------------------------
        report "--- Casos Básicos ---" severity note;
        test_case(0, 0, '0', "0+0+0");
        test_case(0, 0, '1', "0+0+1");
        test_case(1, 1, '0', "1+1+0");
        test_case(1, 1, '1', "1+1+1");
        
        -------------------------------------------------------------------
        -- CASOS LÍMITE
        -------------------------------------------------------------------
        report "--- Casos Límite ---" severity note;
        test_case(15, 0, '0',  "MAX+0");
        test_case(0, 15, '0',  "0+MAX");
        test_case(15, 15, '0', "MAX+MAX sin Cin");
        test_case(15, 15, '1', "MAX+MAX con Cin (overflow)");
        test_case(15, 1, '0',  "MAX+1 (overflow)");
        
        -------------------------------------------------------------------
        -- CASOS DE ACARREO
        -------------------------------------------------------------------
        report "--- Casos de Acarreo ---" severity note;
        test_case(8, 8, '0',  "8+8 (acarreo interno)");
        test_case(9, 7, '0',  "9+7 (acarreo)");
        test_case(7, 9, '1',  "7+9+1 (acarreo con Cin)");
        
        -------------------------------------------------------------------
        -- VERIFICACIÓN EXHAUSTIVA (opcional - 512 casos)
        -------------------------------------------------------------------
        report "--- Verificación Exhaustiva ---" severity note;
        for a_int in 0 to 15 loop
            for b_int in 0 to 15 loop
                for cin_int in 0 to 1 loop
                    A   <= std_logic_vector(to_unsigned(a_int, N_BITS));
                    B   <= std_logic_vector(to_unsigned(b_int, N_BITS));
                    Cin <= std_logic(to_unsigned(cin_int, 1)(0));
                    wait for CLK_PERIOD;
                    
                    test_count <= test_count + 1;
                    
                    if SUM /= expected_sum or Cout /= expected_cout then
                        error_count <= error_count + 1;
                    end if;
                end loop;
            end loop;
        end loop;
        
        -------------------------------------------------------------------
        -- REPORTE FINAL
        -------------------------------------------------------------------
        wait for CLK_PERIOD;
        report "========================================" severity note;
        report "SIMULACIÓN COMPLETADA" severity note;
        report "Total de pruebas: " & integer'image(test_count) severity note;
        report "Errores encontrados: " & integer'image(error_count) severity note;
        
        if error_count = 0 then
            report "RESULTADO: *** TODOS LOS TESTS PASARON ***" severity note;
        else
            report "RESULTADO: *** HAY ERRORES ***" severity failure;
        end if;
        report "========================================" severity note;
        
        wait;  -- Detener simulación
    end process stimulus;
    
end architecture test;
```

---

## Paso 4: Técnicas Avanzadas de Testbench

### 4.1 Lectura desde Archivo

```vhdl
use STD.TEXTIO.ALL;

process
    file test_vectors : text open read_mode is "vectors.txt";
    variable line_data : line;
    variable a_int, b_int, expected : integer;
begin
    while not endfile(test_vectors) loop
        readline(test_vectors, line_data);
        read(line_data, a_int);
        read(line_data, b_int);
        read(line_data, expected);
        
        A <= std_logic_vector(to_unsigned(a_int, 4));
        B <= std_logic_vector(to_unsigned(b_int, 4));
        wait for 10 ns;
        
        assert to_integer(unsigned(SUM)) = expected
            report "Mismatch!" severity error;
    end loop;
    wait;
end process;
```

### 4.2 Cobertura de Código (Conceptual)

```vhdl
-- Señales de cobertura
signal tested_zero_plus_zero : boolean := false;
signal tested_max_overflow   : boolean := false;
signal tested_all_bits       : std_logic_vector(15 downto 0) := (others => '0');

-- Tracking en el testbench
if a_int = 0 and b_int = 0 then
    tested_zero_plus_zero <= true;
end if;

-- Reporte de cobertura
report "Cobertura de casos críticos:" severity note;
report "  Zero+Zero: " & boolean'image(tested_zero_plus_zero) severity note;
```

---

## Paso 5: Resumen de Buenas Prácticas

| Práctica | Descripción |
|----------|-------------|
| Self-checking | Incluir verificación automática con asserts |
| Modelo de referencia | Calcular valor esperado independientemente |
| Casos límite | Probar valores extremos (0, MAX, overflow) |
| Procedure/Function | Encapsular casos repetitivos |
| Reporting | Mensajes claros de PASS/FAIL |
| Contadores | Llevar cuenta de tests y errores |

---

## Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| Entidad vacía | Testbenches no tienen puertos |
| `assert` | Verificación con mensaje de error |
| `severity` | note, warning, error, failure |
| `wait for` | Avanza el tiempo de simulación |
| `wait;` | Detiene el proceso indefinidamente |

---

## Checklist de Testbench

- [x] Entidad vacía
- [x] Instanciación del DUT
- [x] Generación de clock
- [x] Modelo de referencia
- [x] Casos básicos
- [x] Casos límite
- [x] Verificación automática
- [x] Reporte final

---

> 💡 **Tip:** Un buen testbench es más valioso que el diseño mismo. Invierte tiempo en crear verificación exhaustiva y reutilizable.
