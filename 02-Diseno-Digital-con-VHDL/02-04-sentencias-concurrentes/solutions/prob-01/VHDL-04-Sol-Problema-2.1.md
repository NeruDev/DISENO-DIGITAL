<!--
::METADATA::
type: detailed_solution
topic_id: vhdl-04-sentencias-concurrentes
problem_id: 2.1
file_id: solucion-problema-2-1
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 2
tags: [solucion, VHDL, when-else, with-select, MUX]
-->

> 🏠 **Navegación:** [← Índice](./README.md) | [Problema 2.2 →](./VHDL-04-Sol-Problema-2.2.md)

---

# Solución Detallada: Problema 2.1

## Enunciado
Implementar un multiplexor 4:1 de 8 bits usando:
- a) Sentencia `when-else`
- b) Sentencia `with-select`

Comparar ambas implementaciones.

---

## Paso 1: Interfaz del Multiplexor

```
           ┌─────────────────┐
  D0 ──────┤                 │
  D1 ──────┤     MUX 4:1     ├────── Y
  D2 ──────┤     8 bits      │
  D3 ──────┤                 │
           └───────┬─────────┘
                   │
              SEL[1:0]
```

| Puerto | Tipo | Descripción |
|--------|------|-------------|
| D0-D3 | in std_logic_vector(7:0) | Entradas de datos |
| SEL | in std_logic_vector(1:0) | Selección |
| Y | out std_logic_vector(7:0) | Salida |

---

## Paso 2: Solución con `when-else`

### Características de `when-else`
- Asignación condicional **priorizada**
- Las condiciones se evalúan en orden
- Primera condición verdadera gana
- Similar a `if-elsif-else`

### Código VHDL

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux_4to1_when is
    port (
        D0, D1, D2, D3 : in  std_logic_vector(7 downto 0);
        SEL            : in  std_logic_vector(1 downto 0);
        Y              : out std_logic_vector(7 downto 0)
    );
end entity mux_4to1_when;

architecture when_else of mux_4to1_when is
begin
    Y <= D0 when SEL = "00" else
         D1 when SEL = "01" else
         D2 when SEL = "10" else
         D3 when SEL = "11" else
         (others => 'X');  -- Manejo de metavalores
end architecture when_else;
```

### Diagrama de Prioridad

```
SEL="00"? ─► Sí ─► Y = D0
    │
    No
    │
    ▼
SEL="01"? ─► Sí ─► Y = D1
    │
    No
    │
    ▼
SEL="10"? ─► Sí ─► Y = D2
    │
    No
    │
    ▼
SEL="11"? ─► Sí ─► Y = D3
    │
    No
    │
    ▼
Y = "XXXXXXXX"
```

---

## Paso 3: Solución con `with-select`

### Características de `with-select`
- Asignación basada en **selección paralela**
- Todas las opciones son mutuamente exclusivas
- No hay prioridad implícita
- Similar a `case` pero concurrente

### Código VHDL

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux_4to1_select is
    port (
        D0, D1, D2, D3 : in  std_logic_vector(7 downto 0);
        SEL            : in  std_logic_vector(1 downto 0);
        Y              : out std_logic_vector(7 downto 0)
    );
end entity mux_4to1_select;

architecture with_select of mux_4to1_select is
begin
    with SEL select
        Y <= D0 when "00",
             D1 when "01",
             D2 when "10",
             D3 when "11",
             (others => 'X') when others;
end architecture with_select;
```

### Diagrama de Selección Paralela

```
           ┌──► "00" → Y = D0
           │
           ├──► "01" → Y = D1
SEL ───────┤
           ├──► "10" → Y = D2
           │
           ├──► "11" → Y = D3
           │
           └──► others → Y = "X...X"
```

---

## Paso 4: Comparación

| Aspecto | `when-else` | `with-select` |
|---------|:-----------:|:-------------:|
| Evaluación | Priorizada (secuencial) | Paralela |
| Condiciones | Cualquier expresión | Solo igualdad |
| Síntesis | Puede generar cascada | Genera MUX directo |
| `others` | Opcional (último `else`) | Requerido |
| Legibilidad | Mejor para rangos | Mejor para valores discretos |
| Velocidad | Similar (optimizado) | Similar (optimizado) |

### Cuándo usar cada uno

| Escenario | Recomendado |
|-----------|-------------|
| Selección por valor discreto | `with-select` |
| Condiciones con rangos | `when-else` |
| Prioridades explícitas | `when-else` |
| Decodificador simple | `with-select` |
| Lógica de comparación compleja | `when-else` |

---

## Paso 5: Ejemplos Avanzados

### `when-else` con rangos (Priority Encoder)

```vhdl
-- Encoder de prioridad
Y <= "11" when REQ(3) = '1' else  -- Mayor prioridad
     "10" when REQ(2) = '1' else
     "01" when REQ(1) = '1' else
     "00" when REQ(0) = '1' else
     "00";

VALID <= '1' when REQ /= "0000" else '0';
```

### `with-select` con múltiples valores

```vhdl
-- Decodificador 7 segmentos
with DIGIT select
    SEGMENTS <= "1111110" when "0000",  -- 0
                "0110000" when "0001",  -- 1
                "1101101" when "0010",  -- 2
                "1111001" when "0011",  -- 3
                "0110011" when "0100",  -- 4
                "1011011" when "0101",  -- 5
                "1011111" when "0110",  -- 6
                "1110000" when "0111",  -- 7
                "1111111" when "1000",  -- 8
                "1111011" when "1001",  -- 9
                "0000000" when others;
```

### `with-select` con rangos (alternativa menos común)

```vhdl
-- Usando '|' para múltiples valores
with OPCODE select
    ALU_OP <= "00" when "0000" | "0001",  -- ADD o SUB
              "01" when "0010" | "0011",  -- AND o OR
              "10" when "0100",           -- NOT
              "11" when others;
```

---

## Testbench

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity tb_mux_4to1 is
end entity;

architecture test of tb_mux_4to1 is
    signal D0, D1, D2, D3, Y_when, Y_select : std_logic_vector(7 downto 0);
    signal SEL : std_logic_vector(1 downto 0);
begin
    -- DUT when-else
    DUT1: entity work.mux_4to1_when
        port map (D0, D1, D2, D3, SEL, Y_when);
    
    -- DUT with-select
    DUT2: entity work.mux_4to1_select
        port map (D0, D1, D2, D3, SEL, Y_select);
    
    process
    begin
        -- Valores de prueba
        D0 <= x"AA";
        D1 <= x"BB";
        D2 <= x"CC";
        D3 <= x"DD";
        
        -- Test cada selección
        for i in 0 to 3 loop
            SEL <= std_logic_vector(to_unsigned(i, 2));
            wait for 10 ns;
            
            -- Verificar que ambos dan el mismo resultado
            assert Y_when = Y_select
                report "Diferencia entre when-else y with-select para SEL=" 
                       & integer'image(i)
                severity error;
        end loop;
        
        report "Test completado" severity note;
        wait;
    end process;
end architecture;
```

---

## Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| Concurrente | Ambas sentencias se ejecutan en paralelo |
| `others` | Manejo obligatorio en `with-select` |
| Metavalores | `'X'`, `'U'`, `'Z'` para simulación |
| Síntesis | Ambos generan lógica similar |

---

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| Falta `others` | `with-select` incompleto | Agregar `when others` |
| Condiciones solapadas | `when-else` ambiguo | Ordenar por prioridad |
| Latch inferido | Falta caso por defecto | Cubrir todos los casos |
| Tipo incompatible | Comparar tipos distintos | Usar conversión |

---

> 💡 **Tip:** Las herramientas de síntesis modernas optimizan ambas estructuras de manera similar, así que elige la que sea más legible para tu caso.
