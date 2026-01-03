# 🔧 Aplicación: Transmisor UART con Sentencias Secuenciales

```
::METADATA::
tipo: aplicacion
tema: VHDL-05-sentencias-secuenciales
dificultad: avanzada
objetivo: Implementar UART TX usando procesos y sentencias secuenciales
::END::
```

## 📋 Descripción del Proyecto

Diseñar un transmisor UART (Universal Asynchronous Receiver/Transmitter) usando sentencias secuenciales: process, if-then-else, case, loop.

## 🎯 Objetivos de Aprendizaje

- Implementar máquinas de estado con `case`
- Usar contadores dentro de procesos
- Manejar señales de control con `if-then-else`
- Sincronizar con `wait` y flancos de reloj

## 📝 Especificaciones

| Parámetro | Valor |
|-----------|-------|
| Baud Rate | 9600 bps (configurable) |
| Datos | 8 bits |
| Paridad | Ninguna |
| Stop bits | 1 |
| Reloj | 50 MHz |

## 📝 Código VHDL

### Entidad

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity uart_tx is
    generic (
        CLK_FREQ  : integer := 50_000_000;  -- 50 MHz
        BAUD_RATE : integer := 9600
    );
    port (
        clk      : in  std_logic;
        rst      : in  std_logic;
        tx_start : in  std_logic;
        tx_data  : in  std_logic_vector(7 downto 0);
        tx_out   : out std_logic;
        tx_busy  : out std_logic;
        tx_done  : out std_logic
    );
end entity uart_tx;
```

### Arquitectura con Proceso Secuencial

```vhdl
architecture behavioral of uart_tx is
    -- Constantes calculadas
    constant CLKS_PER_BIT : integer := CLK_FREQ / BAUD_RATE;
    
    -- Tipo enumerado para estados
    type tx_state_t is (IDLE, START_BIT, DATA_BITS, STOP_BIT, CLEANUP);
    signal state : tx_state_t := IDLE;
    
    -- Señales internas
    signal clk_count : integer range 0 to CLKS_PER_BIT-1 := 0;
    signal bit_index : integer range 0 to 7 := 0;
    signal tx_data_reg : std_logic_vector(7 downto 0) := (others => '0');
    signal tx_out_reg : std_logic := '1';
    
begin
    -- Proceso principal de transmisión
    TX_PROC: process(clk, rst)
    begin
        if rst = '1' then
            state <= IDLE;
            tx_out_reg <= '1';  -- Línea en alto (idle)
            tx_busy <= '0';
            tx_done <= '0';
            clk_count <= 0;
            bit_index <= 0;
            
        elsif rising_edge(clk) then
            tx_done <= '0';  -- Default: pulso de un ciclo
            
            case state is
                -- Estado IDLE: esperando datos
                when IDLE =>
                    tx_out_reg <= '1';
                    tx_busy <= '0';
                    clk_count <= 0;
                    bit_index <= 0;
                    
                    if tx_start = '1' then
                        tx_data_reg <= tx_data;  -- Capturar datos
                        tx_busy <= '1';
                        state <= START_BIT;
                    end if;
                
                -- Bit de START (bajo)
                when START_BIT =>
                    tx_out_reg <= '0';
                    
                    if clk_count < CLKS_PER_BIT - 1 then
                        clk_count <= clk_count + 1;
                    else
                        clk_count <= 0;
                        state <= DATA_BITS;
                    end if;
                
                -- Transmitir 8 bits de datos
                when DATA_BITS =>
                    tx_out_reg <= tx_data_reg(bit_index);
                    
                    if clk_count < CLKS_PER_BIT - 1 then
                        clk_count <= clk_count + 1;
                    else
                        clk_count <= 0;
                        
                        if bit_index < 7 then
                            bit_index <= bit_index + 1;
                        else
                            bit_index <= 0;
                            state <= STOP_BIT;
                        end if;
                    end if;
                
                -- Bit de STOP (alto)
                when STOP_BIT =>
                    tx_out_reg <= '1';
                    
                    if clk_count < CLKS_PER_BIT - 1 then
                        clk_count <= clk_count + 1;
                    else
                        clk_count <= 0;
                        tx_done <= '1';
                        state <= CLEANUP;
                    end if;
                
                -- Limpieza antes de volver a IDLE
                when CLEANUP =>
                    tx_busy <= '0';
                    state <= IDLE;
                    
                when others =>
                    state <= IDLE;
            end case;
        end if;
    end process TX_PROC;
    
    tx_out <= tx_out_reg;
    
end architecture behavioral;
```

## 🧪 Testbench

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity uart_tx_tb is
end entity uart_tx_tb;

architecture sim of uart_tx_tb is
    constant CLK_PERIOD : time := 20 ns;  -- 50 MHz
    
    signal clk_tb      : std_logic := '0';
    signal rst_tb      : std_logic := '1';
    signal tx_start_tb : std_logic := '0';
    signal tx_data_tb  : std_logic_vector(7 downto 0) := x"00";
    signal tx_out_tb   : std_logic;
    signal tx_busy_tb  : std_logic;
    signal tx_done_tb  : std_logic;
begin
    -- DUT con baud rate alto para simulación rápida
    DUT: entity work.uart_tx
        generic map (
            CLK_FREQ  => 50_000_000,
            BAUD_RATE => 5_000_000  -- Rápido para simulación
        )
        port map (
            clk      => clk_tb,
            rst      => rst_tb,
            tx_start => tx_start_tb,
            tx_data  => tx_data_tb,
            tx_out   => tx_out_tb,
            tx_busy  => tx_busy_tb,
            tx_done  => tx_done_tb
        );
    
    -- Generador de reloj
    clk_tb <= not clk_tb after CLK_PERIOD/2;
    
    -- Estímulos
    stim: process
    begin
        wait for 100 ns;
        rst_tb <= '0';
        wait for 50 ns;
        
        -- Transmitir 'A' (0x41)
        tx_data_tb <= x"41";
        tx_start_tb <= '1';
        wait for CLK_PERIOD;
        tx_start_tb <= '0';
        
        -- Esperar fin de transmisión
        wait until tx_done_tb = '1';
        wait for 200 ns;
        
        -- Transmitir 'B' (0x42)
        tx_data_tb <= x"42";
        tx_start_tb <= '1';
        wait for CLK_PERIOD;
        tx_start_tb <= '0';
        
        wait until tx_done_tb = '1';
        wait for 100 ns;
        
        wait;
    end process;
end architecture sim;
```

## 📊 Diagrama de Estados

```
      tx_start=1
IDLE ──────────────> START_BIT
  ^                      │
  │                      │ 1 bit time
  │                      v
CLEANUP <── STOP_BIT <── DATA_BITS
               │              │
               │ 1 bit time   │ 8 bits
               └──────────────┘
```

## 🔢 Cálculo de Tiempos

Para **9600 baud** @ **50 MHz**:

$$T_{bit} = \frac{1}{9600} = 104.17 \mu s$$

$$CLKS\_PER\_BIT = \frac{50,000,000}{9600} = 5208$$

## 🔗 Referencias

- [VHDL-05-Teoria-SentenciasSecuenciales.md](../theory/VHDL-05-Teoria-SentenciasSecuenciales.md)
