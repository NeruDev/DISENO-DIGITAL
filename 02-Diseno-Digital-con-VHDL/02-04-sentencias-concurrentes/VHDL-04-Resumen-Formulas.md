<!--
::METADATA::
type: reference
topic_id: vhdl-04-sentencias-concurrentes
file_id: resumen-concurrentes
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [cheatsheet, VHDL, concurrente]
search_keywords: "resumen, sentencias concurrentes, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./02-04-Intro.md)

---

# 📋 Cheatsheet: Sentencias Concurrentes

## Concepto Clave

**Todas las sentencias concurrentes se ejecutan simultáneamente**

```vhdl
-- Estas líneas operan AL MISMO TIEMPO
a <= b and c;
d <= e or f;
g <= not h;
```

---

## Asignación Simple

```vhdl
signal <= expresion;

y <= a and b;
z <= not(c or d);
w <= (a xor b) and c;
```

---

## when-else (Condicional)

```vhdl
signal <= valor1 when cond1 else
          valor2 when cond2 else
          valor_default;
```

**Ejemplo: MUX 4:1**
```vhdl
y <= d0 when sel = "00" else
     d1 when sel = "01" else
     d2 when sel = "10" else
     d3;
```

**Características:**
- Evaluación con **prioridad**
- Primera condición verdadera gana
- Siempre incluir `else` final

---

## with-select (Selectiva)

```vhdl
with selector select
    signal <= val1 when opc1,
              val2 when opc2,
              val_default when others;
```

**Ejemplo: MUX 4:1**
```vhdl
with sel select
    y <= d0 when "00",
         d1 when "01",
         d2 when "10",
         d3 when others;
```

**Características:**
- Sin prioridad (mutuamente exclusivo)
- Siempre incluir `when others`
- Múltiples opciones: `when "00" | "01"`

---

## Cuándo Usar Cada Uno

| Situación | Usar |
|-----------|------|
| MUX puro | `with-select` |
| Prioridad requerida | `when-else` |
| Decodificador | `with-select` |
| Codificador prioridad | `when-else` |

---

## for-generate

```vhdl
LABEL: for i in rango generate
    -- Sentencias concurrentes
end generate;
```

**Ejemplo: 8 inversores**
```vhdl
GEN: for i in 0 to 7 generate
    y(i) <= not x(i);
end generate;
```

---

## if-generate

```vhdl
LABEL: if condicion_constante generate
    -- Sentencias concurrentes
end generate;
```

**Ejemplo: Debug opcional**
```vhdl
GEN_DBG: if DEBUG generate
    -- Lógica de debug
end generate;
```

---

## Instanciación de Componentes

```vhdl
INST: entity work.modulo(arch)
    generic map (PARAM => valor)
    port map (
        puerto1 => señal1,
        puerto2 => señal2
    );
```

---

## Tristate Buffer

```vhdl
data_out <= data_in when oe = '1' else (others => 'Z');
```

---

## Errores Comunes

| Error | Consecuencia | Solución |
|-------|--------------|----------|
| Sin `else` | Latch | Agregar else |
| Sin `when others` | Latch | Agregar default |
| Múltiples drivers | Conflicto | Un driver por señal |
| Índice fuera de rango | Error | Verificar límites |

---

## Operadores Lógicos

```vhdl
y <= a and b;
y <= a or b;
y <= a xor b;
y <= a nand b;
y <= a nor b;
y <= not a;
```

---

## Concatenación

```vhdl
word <= byte_hi & byte_lo;
extended <= "0000" & nibble;
```

---

## Comparaciones

```vhdl
eq <= '1' when a = b else '0';
gt <= '1' when unsigned(a) > unsigned(b) else '0';
```

---

## Regla de Oro

⚠️ **Siempre cubrir todos los casos para evitar latches**

```vhdl
-- ✓ Correcto
y <= a when sel = '1' else b;

-- ✗ Incorrecto (latch)
y <= a when sel = '1';
```

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante desarrollo VHDL
-->
