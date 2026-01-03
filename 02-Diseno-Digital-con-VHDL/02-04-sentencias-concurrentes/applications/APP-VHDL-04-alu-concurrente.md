# 🔧 Aplicación: ALU con Sentencias Concurrentes VHDL

```
::METADATA::
tipo: aplicacion
tema: VHDL-04-sentencias-concurrentes
dificultad: intermedia
objetivo: Implementar ALU usando solo sentencias concurrentes
::END::
```

## 📋 Descripción del Proyecto

Diseñar una ALU de 8 bits usando exclusivamente sentencias concurrentes VHDL (when-else, with-select, generate).

## 🎯 Objetivos de Aprendizaje

- Dominar asignación condicional `when-else`
- Usar asignación selectiva `with-select`
- Implementar lógica combinacional pura
- Generar estructuras repetitivas con `generate`

## 📝 Código VHDL

### Entidad

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity alu_concurrente is
    generic (
        WIDTH : integer := 8
    );
    port (
        A, B    : in  std_logic_vector(WIDTH-1 downto 0);
        op_sel  : in  std_logic_vector(2 downto 0);
        result  : out std_logic_vector(WIDTH-1 downto 0);
        zero    : out std_logic;
        carry   : out std_logic;
        overflow: out std_logic
    );
end entity alu_concurrente;
```

### Arquitectura Concurrente

```vhdl
architecture dataflow of alu_concurrente is
    -- Señales internas para operaciones
    signal sum_result  : std_logic_vector(WIDTH downto 0);
    signal sub_result  : std_logic_vector(WIDTH downto 0);
    signal and_result  : std_logic_vector(WIDTH-1 downto 0);
    signal or_result   : std_logic_vector(WIDTH-1 downto 0);
    signal xor_result  : std_logic_vector(WIDTH-1 downto 0);
    signal not_result  : std_logic_vector(WIDTH-1 downto 0);
    signal shl_result  : std_logic_vector(WIDTH-1 downto 0);
    signal shr_result  : std_logic_vector(WIDTH-1 downto 0);
    
    signal alu_out     : std_logic_vector(WIDTH-1 downto 0);
    signal carry_int   : std_logic;
    
begin
    -- Operaciones aritméticas con extensión para carry
    sum_result <= std_logic_vector(unsigned('0' & A) + unsigned('0' & B));
    sub_result <= std_logic_vector(unsigned('0' & A) - unsigned('0' & B));
    
    -- Operaciones lógicas bit a bit (usando generate implícito)
    and_result <= A and B;
    or_result  <= A or B;
    xor_result <= A xor B;
    not_result <= not A;
    
    -- Desplazamientos
    shl_result <= A(WIDTH-2 downto 0) & '0';
    shr_result <= '0' & A(WIDTH-1 downto 1);
    
    -- Multiplexor de operación con WITH-SELECT
    with op_sel select
        alu_out <= sum_result(WIDTH-1 downto 0) when "000",  -- ADD
                   sub_result(WIDTH-1 downto 0) when "001",  -- SUB
                   and_result                   when "010",  -- AND
                   or_result                    when "011",  -- OR
                   xor_result                   when "100",  -- XOR
                   not_result                   when "101",  -- NOT A
                   shl_result                   when "110",  -- SHL
                   shr_result                   when "111",  -- SHR
                   (others => '0')              when others;
    
    -- Carry con WHEN-ELSE
    carry_int <= sum_result(WIDTH) when op_sel = "000" else
                 sub_result(WIDTH) when op_sel = "001" else
                 A(WIDTH-1)        when op_sel = "110" else
                 A(0)              when op_sel = "111" else
                 '0';
    
    -- Flag Zero: detecta si resultado es cero
    zero <= '1' when alu_out = (alu_out'range => '0') else '0';
    
    -- Flag Overflow (para suma/resta con signo)
    overflow <= (A(WIDTH-1) xnor B(WIDTH-1)) and 
                (A(WIDTH-1) xor alu_out(WIDTH-1)) 
                when op_sel = "000" else
                (A(WIDTH-1) xor B(WIDTH-1)) and 
                (A(WIDTH-1) xor alu_out(WIDTH-1)) 
                when op_sel = "001" else
                '0';
    
    -- Salidas
    result <= alu_out;
    carry  <= carry_int;
    
end architecture dataflow;
```

## 🧪 Testbench

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity alu_concurrente_tb is
end entity alu_concurrente_tb;

architecture sim of alu_concurrente_tb is
    signal A_tb, B_tb : std_logic_vector(7 downto 0);
    signal op_tb      : std_logic_vector(2 downto 0);
    signal result_tb  : std_logic_vector(7 downto 0);
    signal zero_tb, carry_tb, ovf_tb : std_logic;
begin
    DUT: entity work.alu_concurrente
        port map (
            A => A_tb, B => B_tb, op_sel => op_tb,
            result => result_tb, zero => zero_tb,
            carry => carry_tb, overflow => ovf_tb
        );
    
    stim: process
    begin
        -- Test ADD
        A_tb <= x"25"; B_tb <= x"13"; op_tb <= "000";
        wait for 10 ns;
        assert result_tb = x"38" report "ADD failed" severity error;
        
        -- Test SUB
        op_tb <= "001";
        wait for 10 ns;
        assert result_tb = x"12" report "SUB failed" severity error;
        
        -- Test AND
        A_tb <= x"F0"; B_tb <= x"0F"; op_tb <= "010";
        wait for 10 ns;
        assert result_tb = x"00" report "AND failed" severity error;
        
        -- Test OR
        op_tb <= "011";
        wait for 10 ns;
        assert result_tb = x"FF" report "OR failed" severity error;
        
        -- Test Zero flag
        A_tb <= x"00"; B_tb <= x"00"; op_tb <= "000";
        wait for 10 ns;
        assert zero_tb = '1' report "Zero flag failed" severity error;
        
        -- Test Carry
        A_tb <= x"FF"; B_tb <= x"01"; op_tb <= "000";
        wait for 10 ns;
        assert carry_tb = '1' report "Carry flag failed" severity error;
        
        wait;
    end process;
end architecture sim;
```

## 📊 Operaciones de la ALU

| op_sel | Operación | Descripción |
|--------|-----------|-------------|
| 000 | ADD | A + B |
| 001 | SUB | A - B |
| 010 | AND | A AND B |
| 011 | OR | A OR B |
| 100 | XOR | A XOR B |
| 101 | NOT | NOT A |
| 110 | SHL | A << 1 |
| 111 | SHR | A >> 1 |

## 🔗 Referencias

- [VHDL-04-Teoria-SentenciasConcurrentes.md](../theory/VHDL-04-Teoria-SentenciasConcurrentes.md)
