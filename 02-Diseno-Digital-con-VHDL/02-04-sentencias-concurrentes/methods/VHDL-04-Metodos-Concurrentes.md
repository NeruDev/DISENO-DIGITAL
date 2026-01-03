<!--
::METADATA::
type: method
topic_id: vhdl-04-sentencias-concurrentes
file_id: metodos-concurrentes
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [VHDL, metodologia, concurrente, combinacional]
search_keywords: "metodología sentencias concurrentes"
-->

> 🏠 **Navegación:** [← Teoría](../theory/VHDL-04-Teoria-Concurrentes.md) | [Problemas →](../problems/VHDL-04-Problemas.md)

---

# Métodos: Sentencias Concurrentes

## Método 1: Elegir entre `when-else` y `with-select`

### Criterio de Decisión

| Situación | Usar |
|-----------|------|
| Selector con opciones mutuamente exclusivas | `with-select` |
| Condiciones con prioridad | `when-else` |
| Multiplexor puro | `with-select` |
| Codificador de prioridad | `when-else` |

### Ejemplo: MUX (usar `with-select`)

```vhdl
-- ✓ Mejor para MUX
with sel select
    y <= a when "00",
         b when "01",
         c when "10",
         d when others;
```

### Ejemplo: Prioridad (usar `when-else`)

```vhdl
-- ✓ Mejor para prioridad
grant <= "001" when req(0) = '1' else
         "010" when req(1) = '1' else
         "100" when req(2) = '1' else
         "000";
```

---

## Método 2: Implementar Lógica Combinacional

### Decodificador 2 a 4

```vhdl
-- Con with-select
with sel select
    y <= "0001" when "00",
         "0010" when "01",
         "0100" when "10",
         "1000" when others;
```

### Codificador 4 a 2 (con prioridad)

```vhdl
-- Con when-else (prioridad: bit 3 > bit 2 > bit 1 > bit 0)
code <= "11" when input(3) = '1' else
        "10" when input(2) = '1' else
        "01" when input(1) = '1' else
        "00";

valid <= '1' when input /= "0000" else '0';
```

---

## Método 3: Evitar Latches

### ✗ Incorrecto: Latch Inferido

```vhdl
-- PELIGRO: No cubre todos los casos
y <= a when sel = '1';  -- ¿Qué pasa cuando sel = '0'?
```

### ✓ Correcto: Siempre Especificar Default

```vhdl
-- Siempre incluir else o when others
y <= a when sel = '1' else '0';

with sel select
    y <= a when "00",
         b when "01",
         c when others;  -- SIEMPRE incluir
```

---

## Método 4: Generate para Estructuras Repetitivas

### Ripple Carry Adder

```vhdl
architecture structural of adder_n is
    signal carry : std_logic_vector(N downto 0);
begin
    carry(0) <= cin;
    
    GEN_FA: for i in 0 to N-1 generate
        FA_i: entity work.full_adder
            port map (
                a    => a(i),
                b    => b(i),
                cin  => carry(i),
                sum  => sum(i),
                cout => carry(i+1)
            );
    end generate;
    
    cout <= carry(N);
end architecture;
```

### Banco de Inversores

```vhdl
GEN_INV: for i in data'range generate
    data_inv(i) <= not data(i);
end generate;
```

---

## Método 5: Configuración con `if-generate`

### Debug Habilitado

```vhdl
architecture rtl of modulo is
    constant DEBUG : boolean := true;
begin
    GEN_DEBUG: if DEBUG generate
        signal debug_count : unsigned(31 downto 0);
    begin
        process(clk)
        begin
            if rising_edge(clk) then
                debug_count <= debug_count + 1;
            end if;
        end process;
    end generate;
    
    -- Lógica normal aquí...
end architecture;
```

### Selección de Implementación

```vhdl
GEN_FAST: if USE_FAST_MULT generate
    -- Multiplicador rápido (más área)
    result <= a * b;
end generate;

GEN_SLOW: if not USE_FAST_MULT generate
    -- Multiplicador secuencial (menos área)
    -- ... implementación iterativa ...
end generate;
```

---

## Método 6: Combinar Operadores

### Reducir Código

```vhdl
-- En lugar de múltiples líneas
y(0) <= a(0) and enable;
y(1) <= a(1) and enable;
y(2) <= a(2) and enable;
...

-- Usar operación vectorial (si enable es vector)
y <= a and enable_vector;

-- O usar generate
GEN: for i in a'range generate
    y(i) <= a(i) and enable;
end generate;
```

---

## Método 7: Tabla de Verdad a VHDL

### Paso 1: Identificar Entradas y Salidas

```
Entradas: A, B, C
Salidas: Y
```

### Paso 2: Escribir Tabla

| A | B | C | Y |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| ... | ... | ... | ... |

### Paso 3: Convertir a VHDL

```vhdl
-- Opción 1: with-select
with (a & b & c) select
    y <= '0' when "000",
         '1' when "001",
         '1' when "010",
         ...
         '0' when others;

-- Opción 2: Expresión booleana simplificada
y <= (not a and c) or (not a and b) or ...;
```

---

## Método 8: Tristate Buffers

### Buffer Bidireccional

```vhdl
-- Señales
signal data_out : std_logic_vector(7 downto 0);
signal data_in  : std_logic_vector(7 downto 0);
signal oe       : std_logic;

-- Puerto bidireccional
port (data_io : inOut std_logic_vector(7 downto 0));

-- Lógica (sentencias concurrentes)
data_io <= data_out when oe = '1' else (others => 'Z');
data_in <= data_io;
```

---

## Método 9: Prioridad de Operadores

### Orden de Evaluación

| Prioridad | Operadores |
|-----------|------------|
| Alta | `**`, `abs`, `not` |
| | `*`, `/`, `mod`, `rem` |
| | `+`, `-` (unario) |
| | `+`, `-`, `&` |
| | `sll`, `srl`, `sla`, `sra`, `rol`, `ror` |
| | `=`, `/=`, `<`, `<=`, `>`, `>=` |
| | `and`, `or`, `nand`, `nor`, `xor`, `xnor` |
| Baja | |

### Usar Paréntesis

```vhdl
-- Mejor con paréntesis explícitos
y <= (a and b) or (c and d);  -- Claro
y <= a and b or c and d;       -- Ambiguo
```

---

## Método 10: Checklist de Sentencias Concurrentes

### Antes de Síntesis

- [ ] ¿Todas las señales tienen asignación?
- [ ] ¿`with-select` tiene `when others`?
- [ ] ¿`when-else` tiene `else` final?
- [ ] ¿Los rangos de `for-generate` son correctos?
- [ ] ¿Las condiciones de `if-generate` son constantes?
- [ ] ¿No hay múltiples drivers para una señal?

### Errores Comunes

| Error | Solución |
|-------|----------|
| Sin `when others` | Agregar case default |
| Sin `else` final | Agregar valor default |
| Múltiples drivers | Una sola asignación por señal |
| Latch inferido | Cubrir todos los casos |

---

<!-- IA_CONTEXT
USO: Métodos prácticos para sentencias concurrentes
NIVEL: Intermedio (2/3)
HERRAMIENTAS: Quartus, Vivado, ModelSim
-->
