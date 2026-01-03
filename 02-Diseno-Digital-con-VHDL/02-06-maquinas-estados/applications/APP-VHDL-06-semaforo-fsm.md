# 🔧 Aplicación: Controlador de Semáforo con FSM

```
::METADATA::
tipo: aplicacion
tema: VHDL-06-maquinas-estados
dificultad: intermedia
objetivo: Implementar controlador de semáforo con FSM Moore y Mealy
::END::
```

## 📋 Descripción del Proyecto

Diseñar un controlador de semáforo de intersección usando máquinas de estados finitos (FSM) tipo Moore, con extensión Mealy para detección de peatones.

## 🎯 Objetivos de Aprendizaje

- Diseñar FSM tipo Moore de múltiples estados
- Implementar temporización con contadores
- Añadir entradas Mealy para eventos
- Codificar estados de forma segura

## 📝 Especificaciones

### Secuencia de Semáforo

| Estado | Luz Principal | Luz Secundaria | Duración |
|--------|---------------|----------------|----------|
| S0_VERDE_NS | Verde N-S | Rojo E-O | 30s |
| S1_AMARILLO_NS | Amarillo N-S | Rojo E-O | 5s |
| S2_VERDE_EO | Rojo N-S | Verde E-O | 25s |
| S3_AMARILLO_EO | Rojo N-S | Amarillo E-O | 5s |
| S4_PEATON | Rojo ambos | Peatón activo | 15s |

## 📝 Código VHDL

### Entidad

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity semaforo_fsm is
    generic (
        CLK_FREQ : integer := 50_000_000  -- 50 MHz
    );
    port (
        clk         : in  std_logic;
        rst         : in  std_logic;
        btn_peaton  : in  std_logic;  -- Solicitud de cruce peatonal
        sensor_auto : in  std_logic;  -- Sensor de vehículo
        -- Salidas Norte-Sur
        luz_ns      : out std_logic_vector(2 downto 0);  -- RYG
        -- Salidas Este-Oeste
        luz_eo      : out std_logic_vector(2 downto 0);  -- RYG
        -- Peatón
        luz_peaton  : out std_logic;
        -- Debug
        estado_dbg  : out std_logic_vector(2 downto 0)
    );
end entity semaforo_fsm;
```

### Arquitectura FSM Moore

```vhdl
architecture fsm of semaforo_fsm is
    -- Definición de estados (codificación one-hot para seguridad)
    type estado_t is (S0_VERDE_NS, S1_AMARILLO_NS, 
                      S2_VERDE_EO, S3_AMARILLO_EO, S4_PEATON);
    
    attribute syn_encoding : string;
    attribute syn_encoding of estado_t : type is "one-hot";
    
    signal estado_actual, estado_siguiente : estado_t := S0_VERDE_NS;
    
    -- Constantes de tiempo (en ciclos de 1 segundo)
    constant T_VERDE_NS   : integer := 30;
    constant T_AMARILLO   : integer := 5;
    constant T_VERDE_EO   : integer := 25;
    constant T_PEATON     : integer := 15;
    
    -- Divisor para generar pulsos de 1 Hz
    signal contador_1hz   : integer range 0 to CLK_FREQ-1 := 0;
    signal pulso_1hz      : std_logic := '0';
    
    -- Contador de tiempo en estado
    signal tiempo_estado  : integer range 0 to 31 := 0;
    
    -- Registro de solicitud peatón
    signal peaton_pending : std_logic := '0';
    
begin
    -- Divisor de frecuencia: genera pulso cada 1 segundo
    DIV_1HZ: process(clk, rst)
    begin
        if rst = '1' then
            contador_1hz <= 0;
            pulso_1hz <= '0';
        elsif rising_edge(clk) then
            pulso_1hz <= '0';
            if contador_1hz = CLK_FREQ - 1 then
                contador_1hz <= 0;
                pulso_1hz <= '1';
            else
                contador_1hz <= contador_1hz + 1;
            end if;
        end if;
    end process DIV_1HZ;
    
    -- Registro de solicitud peatón (Mealy: respuesta inmediata)
    REG_PEATON: process(clk, rst)
    begin
        if rst = '1' then
            peaton_pending <= '0';
        elsif rising_edge(clk) then
            if btn_peaton = '1' then
                peaton_pending <= '1';
            elsif estado_actual = S4_PEATON then
                peaton_pending <= '0';
            end if;
        end if;
    end process REG_PEATON;
    
    -- Registro de estado
    REG_ESTADO: process(clk, rst)
    begin
        if rst = '1' then
            estado_actual <= S0_VERDE_NS;
            tiempo_estado <= 0;
        elsif rising_edge(clk) then
            if pulso_1hz = '1' then
                if estado_actual /= estado_siguiente then
                    estado_actual <= estado_siguiente;
                    tiempo_estado <= 0;
                else
                    tiempo_estado <= tiempo_estado + 1;
                end if;
            end if;
        end if;
    end process REG_ESTADO;
    
    -- Lógica de transición (Moore con extensión Mealy)
    TRANS: process(estado_actual, tiempo_estado, peaton_pending, sensor_auto)
    begin
        estado_siguiente <= estado_actual;  -- Default: mantener
        
        case estado_actual is
            when S0_VERDE_NS =>
                if tiempo_estado >= T_VERDE_NS - 1 then
                    estado_siguiente <= S1_AMARILLO_NS;
                -- Mealy: si hay peatón y no hay autos, cambiar antes
                elsif peaton_pending = '1' and sensor_auto = '0' 
                      and tiempo_estado >= 10 then
                    estado_siguiente <= S1_AMARILLO_NS;
                end if;
                
            when S1_AMARILLO_NS =>
                if tiempo_estado >= T_AMARILLO - 1 then
                    if peaton_pending = '1' then
                        estado_siguiente <= S4_PEATON;
                    else
                        estado_siguiente <= S2_VERDE_EO;
                    end if;
                end if;
                
            when S2_VERDE_EO =>
                if tiempo_estado >= T_VERDE_EO - 1 then
                    estado_siguiente <= S3_AMARILLO_EO;
                elsif peaton_pending = '1' and tiempo_estado >= 10 then
                    estado_siguiente <= S3_AMARILLO_EO;
                end if;
                
            when S3_AMARILLO_EO =>
                if tiempo_estado >= T_AMARILLO - 1 then
                    if peaton_pending = '1' then
                        estado_siguiente <= S4_PEATON;
                    else
                        estado_siguiente <= S0_VERDE_NS;
                    end if;
                end if;
                
            when S4_PEATON =>
                if tiempo_estado >= T_PEATON - 1 then
                    estado_siguiente <= S0_VERDE_NS;
                end if;
                
            when others =>
                estado_siguiente <= S0_VERDE_NS;
        end case;
    end process TRANS;
    
    -- Lógica de salida (Moore: solo depende del estado)
    SALIDAS: process(estado_actual)
    begin
        -- Defaults
        luz_ns <= "100";      -- Rojo
        luz_eo <= "100";      -- Rojo
        luz_peaton <= '0';
        
        case estado_actual is
            when S0_VERDE_NS =>
                luz_ns <= "001";  -- Verde
                luz_eo <= "100";  -- Rojo
                
            when S1_AMARILLO_NS =>
                luz_ns <= "010";  -- Amarillo
                luz_eo <= "100";  -- Rojo
                
            when S2_VERDE_EO =>
                luz_ns <= "100";  -- Rojo
                luz_eo <= "001";  -- Verde
                
            when S3_AMARILLO_EO =>
                luz_ns <= "100";  -- Rojo
                luz_eo <= "010";  -- Amarillo
                
            when S4_PEATON =>
                luz_ns <= "100";  -- Rojo
                luz_eo <= "100";  -- Rojo
                luz_peaton <= '1';
                
            when others =>
                luz_ns <= "100";
                luz_eo <= "100";
        end case;
    end process SALIDAS;
    
    -- Salida de debug
    with estado_actual select
        estado_dbg <= "000" when S0_VERDE_NS,
                      "001" when S1_AMARILLO_NS,
                      "010" when S2_VERDE_EO,
                      "011" when S3_AMARILLO_EO,
                      "100" when S4_PEATON,
                      "111" when others;
    
end architecture fsm;
```

## 📊 Diagrama de Estados

```
                    ┌─────────────────────────────────────┐
                    │                                     │
                    v          t≥30s                      │
              ┌──────────┐  ────────>  ┌──────────────┐   │
     RST ───> │ VERDE_NS │             │ AMARILLO_NS  │   │
              └──────────┘             └──────────────┘   │
                    ^                        │           │
                    │                        │ t≥5s     │
                    │                        v           │
              ┌──────────┐             ┌──────────────┐   │
              │  PEATON  │ <────────── │  VERDE_EO   │   │
              └──────────┘  btn_peaton └──────────────┘   │
                    │                        │           │
                    │ t≥15s                  │ t≥25s    │
                    │                        v           │
                    │                 ┌──────────────┐   │
                    └───────────────> │ AMARILLO_EO  │───┘
                                      └──────────────┘
```

## 🔗 Referencias

- [VHDL-06-Teoria-FSM.md](../theory/VHDL-06-Teoria-FSM.md)
- [VHDL-06-Metodos-FSM.md](../methods/VHDL-06-Metodos-FSM.md)
