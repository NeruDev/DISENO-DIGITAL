<!--
::METADATA::
type: theory
topic_id: vhdl-04-sentencias-concurrentes
file_id: teoria-sentencias-concurrentes
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [VHDL, concurrente, when-else, with-select, generate]
search_keywords: "sentencias concurrentes, when else, with select, generate"
-->

> 🏠 **Navegación:** [← Volver al Índice](../02-04-Intro.md) | [Métodos →](../methods/VHDL-04-Metodos-Concurrentes.md)

---

# Sentencias Concurrentes en VHDL

## 1. Concepto de Concurrencia

### 1.1 ¿Qué es Concurrente?

En VHDL, las sentencias **concurrentes** se ejecutan **simultáneamente**, no en orden secuencial.

```vhdl
architecture ejemplo of modulo is
begin
    -- Estas tres líneas se ejecutan AL MISMO TIEMPO
    a <= b and c;
    d <= e or f;
    g <= not h;
end architecture;
```

### 1.2 Hardware vs Software

| Software | Hardware (VHDL) |
|----------|-----------------|
| Instrucciones secuenciales | Sentencias concurrentes |
| Una a la vez | Todas simultáneas |
| Orden importa | Orden no importa |

### 1.3 Analogía

```
┌────────────────────────────────────────────────┐
│              CIRCUITO REAL                     │
│                                                │
│   ┌───┐        ┌───┐        ┌───┐             │
│ b─┤AND├─a    e─┤OR ├─d    h─┤NOT├─g           │
│ c─┤   │      f─┤   │        └───┘             │
│   └───┘        └───┘                          │
│                                                │
│  Todas las compuertas operan simultáneamente  │
└────────────────────────────────────────────────┘
```

---

## 2. Asignación Simple de Señales

### 2.1 Sintaxis

```vhdl
signal_destino <= expresion;
```

### 2.2 Ejemplos

```vhdl
-- Asignaciones lógicas
y <= a and b;
z <= (a or b) and (c xor d);
inv <= not entrada;

-- Asignaciones aritméticas (con numeric_std)
suma <= a + b;
diff <= unsigned(a) - unsigned(b);

-- Concatenación
palabra <= byte_alto & byte_bajo;

-- Constante
cero <= '0';
bus_cero <= (others => '0');
```

---

## 3. Asignación Condicional: `when-else`

### 3.1 Sintaxis

```vhdl
signal <= valor1 when condicion1 else
          valor2 when condicion2 else
          valor3 when condicion3 else
          valor_default;
```

### 3.2 Ejemplo: Multiplexor 4:1

```vhdl
y <= d0 when sel = "00" else
     d1 when sel = "01" else
     d2 when sel = "10" else
     d3;
```

### 3.3 Equivalencia con Hardware

```
sel  ┬──┐
d0 ──┼──┼──┐
d1 ──┼──┼──┼──┐
d2 ──┼──┼──┼──┼──┬── y
d3 ──┴──┴──┴──┴──┘
      MUX 4:1
```

### 3.4 Prioridad en `when-else`

Las condiciones se evalúan **en orden**. La primera verdadera gana.

```vhdl
-- a tiene mayor prioridad que b
output <= x when a = '1' else
          y when b = '1' else
          z;
```

---

## 4. Asignación Selectiva: `with-select`

### 4.1 Sintaxis

```vhdl
with selector select
    signal <= valor1 when opcion1,
              valor2 when opcion2,
              valor3 when opcion3,
              valor_default when others;
```

### 4.2 Ejemplo: Multiplexor 4:1

```vhdl
with sel select
    y <= d0 when "00",
         d1 when "01",
         d2 when "10",
         d3 when others;
```

### 4.3 `when-else` vs `with-select`

| `when-else` | `with-select` |
|-------------|---------------|
| Condiciones cualquiera | Basado en un selector |
| Con prioridad | Sin prioridad (mutuamente exclusivo) |
| Más flexible | Más claro para MUX |
| Puede generar cadena de MUX | Genera MUX directo |

### 4.4 Múltiples Opciones

```vhdl
with opcode select
    alu_out <= a + b when "000" | "001",  -- OR de opciones
               a - b when "010",
               a and b when "011",
               a or b when "100",
               (others => '0') when others;
```

---

## 5. Instanciación de Componentes

### 5.1 Es una Sentencia Concurrente

```vhdl
architecture structural of top is
begin
    -- Cada instancia opera concurrentemente
    U1: and_gate port map (a => in1, b => in2, y => sig1);
    U2: or_gate port map (a => sig1, b => in3, y => sig2);
    U3: not_gate port map (a => sig2, y => output);
end architecture;
```

### 5.2 Orden No Importa

```vhdl
-- Estas dos arquitecturas son EQUIVALENTES
architecture v1 of top is
begin
    U1: and_gate port map (...);
    U2: or_gate port map (...);
end architecture;

architecture v2 of top is
begin
    U2: or_gate port map (...);   -- Orden invertido
    U1: and_gate port map (...);  -- pero mismo resultado
end architecture;
```

---

## 6. Generate: `for-generate`

### 6.1 Sintaxis

```vhdl
etiqueta: for variable in rango generate
    -- Sentencias concurrentes
end generate etiqueta;
```

### 6.2 Ejemplo: Banco de Registros

```vhdl
architecture structural of reg_bank is
begin
    GEN_REGS: for i in 0 to 7 generate
        REG_I: entity work.registro
            port map (
                clk => clk,
                d   => d_bus(i),
                q   => q_bus(i)
            );
    end generate GEN_REGS;
end architecture;
```

### 6.3 Uso con Señales Indexadas

```vhdl
GEN_INV: for i in 0 to 7 generate
    q(i) <= not d(i);  -- 8 inversores en paralelo
end generate;
```

---

## 7. Generate: `if-generate`

### 7.1 Sintaxis

```vhdl
etiqueta: if condicion generate
    -- Sentencias concurrentes
end generate etiqueta;
```

### 7.2 Ejemplo: Opciones de Diseño

```vhdl
architecture configurable of modulo is
begin
    GEN_PIPE: if USE_PIPELINE generate
        -- Versión con pipeline
        stage1 <= input;
        stage2 <= stage1;
        output <= stage2;
    end generate;
    
    GEN_NO_PIPE: if not USE_PIPELINE generate
        -- Versión sin pipeline
        output <= input;
    end generate;
end architecture;
```

### 7.3 VHDL-2008: `else generate`

```vhdl
GEN: if CONDITION generate
    -- Si verdadero
else generate
    -- Si falso
end generate;
```

---

## 8. Operadores Concurrentes

### 8.1 Operadores Lógicos

```vhdl
-- Operadores bit a bit
y <= a and b;
y <= a or b;
y <= a xor b;
y <= a nand b;
y <= a nor b;
y <= a xnor b;
y <= not a;
```

### 8.2 Reducción (VHDL-2008)

```vhdl
-- Operadores de reducción
any_bit  <= or data;     -- OR de todos los bits
all_bits <= and data;    -- AND de todos los bits
parity   <= xor data;    -- Paridad
```

### 8.3 Operadores de Comparación

```vhdl
eq <= '1' when a = b else '0';
gt <= '1' when unsigned(a) > unsigned(b) else '0';
lt <= '1' when signed(a) < signed(b) else '0';
```

---

## 9. Asignación con Retardo

### 9.1 Retardos en Simulación

```vhdl
-- Retardo inercial (por defecto)
y <= a after 10 ns;

-- Retardo de transporte
y <= transport a after 10 ns;
```

### 9.2 Solo para Simulación

Los retardos `after` son **ignorados en síntesis**. Solo sirven para modelar comportamiento temporal en simulación.

---

## 10. Procesos como Sentencias Concurrentes

### 10.1 Proceso es Concurrente

Un `process` es una sentencia concurrente que contiene sentencias secuenciales.

```vhdl
architecture mixed of modulo is
begin
    -- Sentencia concurrente simple
    y <= a and b;
    
    -- Proceso: concurrente externamente, secuencial internamente
    process(clk)
    begin
        if rising_edge(clk) then
            q <= d;
        end if;
    end process;
    
    -- Otra sentencia concurrente
    z <= c or d;
end architecture;
```

### 10.2 Múltiples Procesos

```vhdl
architecture multi of top is
begin
    -- Estos procesos se ejecutan concurrentemente
    PROC_A: process(clk) ...
    PROC_B: process(clk) ...
    PROC_C: process(clk) ...
end architecture;
```

---

## 11. Resumen de Sentencias Concurrentes

| Sentencia | Uso Principal |
|-----------|---------------|
| `<=` simple | Asignaciones directas |
| `when-else` | Lógica condicional con prioridad |
| `with-select` | Multiplexores, decodificadores |
| `for-generate` | Estructuras repetitivas |
| `if-generate` | Configuración condicional |
| Instanciación | Diseño jerárquico |
| `process` | Lógica secuencial/registro |

---

## Referencias

- IEEE Std 1076-2008
- Ashenden, P.J. (2008). *The Designer's Guide to VHDL*

---

<!-- IA_CONTEXT
NIVEL: Intermedio (2/3)
PREREQUISITOS: 02-01, 02-02, 02-03
CONEXIONES: Fundamental para describir lógica combinacional
ERRORES_COMUNES: Olvidar "when others", confundir when-else con with-select
-->
