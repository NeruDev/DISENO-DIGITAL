# 🔧 Aplicación: Decodificador 7-Segmentos en VHDL

```
::METADATA::
tipo: aplicacion
tema: VHDL-01-introduccion-vhdl
dificultad: basica
objetivo: Primer proyecto VHDL funcional
::END::
```

## 📋 Descripción del Proyecto

Implementar un decodificador BCD a 7-segmentos como primer proyecto VHDL completo.

## 🎯 Objetivos de Aprendizaje

- Crear entidad y arquitectura básica
- Usar asignaciones concurrentes
- Compilar y simular diseño
- Verificar funcionamiento con testbench

## 📝 Código VHDL

### Entidad

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity bcd_7seg is
    port (
        bcd : in  std_logic_vector(3 downto 0);  -- Entrada BCD
        seg : out std_logic_vector(6 downto 0)   -- Salida 7-seg (a-g)
    );
end entity bcd_7seg;
```

### Arquitectura (with-select)

```vhdl
architecture behavioral of bcd_7seg is
begin
    -- Segmentos activos en BAJO (ánodo común)
    -- seg = "abcdefg"
    with bcd select
        seg <= "0000001" when "0000",  -- 0
               "1001111" when "0001",  -- 1
               "0010010" when "0010",  -- 2
               "0000110" when "0011",  -- 3
               "1001100" when "0100",  -- 4
               "0100100" when "0101",  -- 5
               "0100000" when "0110",  -- 6
               "0001111" when "0111",  -- 7
               "0000000" when "1000",  -- 8
               "0000100" when "1001",  -- 9
               "1111111" when others;  -- Apagado
end architecture behavioral;
```

## 🧪 Testbench

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity bcd_7seg_tb is
end entity bcd_7seg_tb;

architecture sim of bcd_7seg_tb is
    signal bcd_test : std_logic_vector(3 downto 0);
    signal seg_test : std_logic_vector(6 downto 0);
begin
    -- Instancia del DUT
    DUT: entity work.bcd_7seg
        port map (
            bcd => bcd_test,
            seg => seg_test
        );
    
    -- Proceso de estímulos
    stim_proc: process
    begin
        -- Probar todos los dígitos 0-9
        for i in 0 to 9 loop
            bcd_test <= std_logic_vector(to_unsigned(i, 4));
            wait for 10 ns;
        end loop;
        
        -- Probar valores inválidos
        bcd_test <= "1010";  -- 10 (inválido)
        wait for 10 ns;
        
        bcd_test <= "1111";  -- 15 (inválido)
        wait for 10 ns;
        
        wait;  -- Fin de simulación
    end process;
end architecture sim;
```

## 📊 Tabla de Resultados Esperados

| BCD | Decimal | seg (abcdefg) | Display |
|:---:|:-------:|:-------------:|:-------:|
| 0000 | 0 | 0000001 | 0 |
| 0001 | 1 | 1001111 | 1 |
| 0010 | 2 | 0010010 | 2 |
| 0011 | 3 | 0000110 | 3 |
| 0100 | 4 | 1001100 | 4 |
| 0101 | 5 | 0100100 | 5 |
| 0110 | 6 | 0100000 | 6 |
| 0111 | 7 | 0001111 | 7 |
| 1000 | 8 | 0000000 | 8 |
| 1001 | 9 | 0000100 | 9 |

## 📐 Representación del Display

```
       a
     ━━━━━
    ┃     ┃
  f ┃     ┃ b
    ┃  g  ┃
     ━━━━━
    ┃     ┃
  e ┃     ┃ c
    ┃     ┃
     ━━━━━
       d
```

## ✅ Criterios de Éxito

- [ ] Síntesis sin errores ni warnings
- [ ] Simulación muestra patrones correctos
- [ ] Manejo de entradas inválidas (> 9)
- [ ] Código documentado

## 📚 Recursos Relacionados

- [VHDL-01-Intro.md](../VHDL-01-Intro.md)
- [VHDL-02 Entidades](../../02-02-entidades-arquitecturas/)
- [GLOSSARY: vhdl](../../../GLOSSARY/README.md#vhdl)

---

> 💡 **Tip**: Para cátodo común, invertir los bits de seg
