<!--
::METADATA::
type: detailed_solution
topic_id: vhdl-01-introduccion
problem_id: 1.3
file_id: solucion-problema-1-3
status: complete
audience: student
last_updated: 2026-01-03
difficulty: 1
tags: [solucion, VHDL, identificadores, sintaxis]
-->

> 🏠 **Navegación:** [← Problema 1.2](./VHDL-01-Sol-Problema-1.2.md) | [Problema 2.1 →](./VHDL-01-Sol-Problema-2.1.md)

---

# Solución Detallada: Problema 1.3

## Enunciado
Identificar los errores en los siguientes identificadores:
```vhdl
signal 1_contador : integer;
signal valor__doble : std_logic;
signal salida_ : std_logic;
signal mi-senal : std_logic;
signal Contador_8bits : integer;
```

---

## Reglas de Identificadores en VHDL

### Reglas Obligatorias

| Regla | Descripción |
|-------|-------------|
| R1 | Debe comenzar con una **letra** (a-z, A-Z) |
| R2 | Solo puede contener letras, dígitos y guion bajo |
| R3 | **No** puede terminar con guion bajo |
| R4 | **No** puede tener dos guiones bajos consecutivos |
| R5 | **No** es sensible a mayúsculas/minúsculas |
| R6 | **No** puede ser palabra reservada |

---

## Análisis de Cada Identificador

### 1. `1_contador`

```vhdl
signal 1_contador : integer;  -- ❌ ERROR
```

| Análisis | Resultado |
|----------|-----------|
| Comienza con | `1` (dígito) |
| Regla violada | **R1**: Debe comenzar con letra |
| Solución | `contador_1` o `cnt_1` |

```vhdl
signal contador_1 : integer;  -- ✅ CORRECTO
```

---

### 2. `valor__doble`

```vhdl
signal valor__doble : std_logic;  -- ❌ ERROR
```

| Análisis | Resultado |
|----------|-----------|
| Problema | Dos guiones bajos consecutivos `__` |
| Regla violada | **R4**: No puede tener `__` |
| Solución | `valor_doble` |

```vhdl
signal valor_doble : std_logic;  -- ✅ CORRECTO
```

---

### 3. `salida_`

```vhdl
signal salida_ : std_logic;  -- ❌ ERROR
```

| Análisis | Resultado |
|----------|-----------|
| Problema | Termina con guion bajo |
| Regla violada | **R3**: No puede terminar con `_` |
| Solución | `salida` o `salida_s` |

```vhdl
signal salida : std_logic;  -- ✅ CORRECTO
```

---

### 4. `mi-senal`

```vhdl
signal mi-senal : std_logic;  -- ❌ ERROR
```

| Análisis | Resultado |
|----------|-----------|
| Problema | Contiene guion `-` (operador resta) |
| Regla violada | **R2**: Solo letras, dígitos y `_` |
| Interpretación | VHDL ve: `mi - senal` (operación) |
| Solución | `mi_senal` |

```vhdl
signal mi_senal : std_logic;  -- ✅ CORRECTO
```

---

### 5. `Contador_8bits`

```vhdl
signal Contador_8bits : integer;  -- ✅ CORRECTO
```

| Análisis | Resultado |
|----------|-----------|
| Comienza con | `C` (letra) ✓ |
| Contenido | Letras, dígitos, un `_` ✓ |
| No termina con | `_` ✓ |
| No tiene | `__` ✓ |
| Resultado | **VÁLIDO** |

---

## Resumen de Respuestas

| Identificador | Estado | Error | Corrección |
|---------------|:------:|-------|------------|
| `1_contador` | ❌ | Comienza con dígito | `contador_1` |
| `valor__doble` | ❌ | Doble guion bajo | `valor_doble` |
| `salida_` | ❌ | Termina con `_` | `salida` |
| `mi-senal` | ❌ | Guion (operador) | `mi_senal` |
| `Contador_8bits` | ✅ | Ninguno | - |

---

## Ejemplos Adicionales de Identificadores

### Válidos ✅

```vhdl
signal clk : std_logic;
signal reset_n : std_logic;
signal data_in_8b : std_logic_vector(7 downto 0);
signal FSM_state : integer;
signal counter256 : integer;
```

### Inválidos ❌

```vhdl
signal 8bit_data : ...;     -- Comienza con número
signal data__bus : ...;     -- Doble guion bajo
signal _start : ...;        -- Comienza con guion bajo
signal end : ...;           -- Palabra reservada
signal clock- : ...;        -- Termina con guion
```

---

## Palabras Reservadas (No usar como identificadores)

| Categoría | Palabras |
|-----------|----------|
| Estructurales | `entity`, `architecture`, `component`, `port`, `generic` |
| Tipos | `signal`, `variable`, `constant`, `type`, `subtype` |
| Control | `if`, `then`, `else`, `elsif`, `case`, `when` |
| Bucles | `for`, `while`, `loop`, `next`, `exit` |
| Otros | `begin`, `end`, `is`, `of`, `all`, `and`, `or`, `not` |

---

## Conceptos Clave

1. **Consistencia**: VHDL no distingue mayúsculas/minúsculas (`Contador` = `contador`)
2. **Legibilidad**: Usar nombres descriptivos (`data_valid` vs `dv`)
3. **Convenciones**: Sufijos comunes: `_n` (activo bajo), `_i` (entrada), `_o` (salida)
4. **Guion bajo**: Separador, no decoración

---

## Convenciones de Nombrado Recomendadas

| Tipo | Convención | Ejemplo |
|------|------------|---------|
| Señales | snake_case | `data_in`, `clk_100mhz` |
| Constantes | MAYÚSCULAS | `WIDTH`, `RESET_VALUE` |
| Genéricos | PascalCase o MAYÚSCULAS | `DataWidth`, `BUS_WIDTH` |
| Entidades | snake_case | `uart_tx`, `fifo_buffer` |
| Activo bajo | sufijo `_n` | `reset_n`, `chip_sel_n` |

---

> 💡 **Tip:** Usar un estilo consistente mejora la legibilidad. Muchos equipos adoptan guías como la de OpenCores o Xilinx.
