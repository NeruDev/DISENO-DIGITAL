<!--
::METADATA::
type: theory
topic_id: vhdl-01-introduccion
file_id: teoria-introduccion-vhdl
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [VHDL, HDL, introduccion, historia, sintaxis]
search_keywords: "VHDL, HDL, lenguaje descripción hardware, introducción"
-->

> 🏠 **Navegación:** [← Volver al Índice](../02-01-Intro.md) | [Métodos →](../methods/VHDL-01-Metodos-EstructuraBasica.md)

---

# Introducción a VHDL

## 1. ¿Qué es VHDL?

**VHDL** = VHSIC Hardware Description Language
**VHSIC** = Very High Speed Integrated Circuit

### 1.1 Definición

VHDL es un **lenguaje de descripción de hardware** (HDL) que permite:
- Describir el comportamiento de circuitos digitales
- Modelar sistemas a diferentes niveles de abstracción
- Simular diseños antes de implementarlos
- Sintetizar hardware real en FPGAs o ASICs

### 1.2 Historia

| Año | Evento |
|-----|--------|
| 1981 | Iniciado por DoD (Departamento de Defensa USA) |
| 1987 | Estandarizado IEEE 1076-1987 |
| 1993 | Actualización IEEE 1076-1993 |
| 2000 | IEEE 1076-2000 |
| 2008 | IEEE 1076-2008 (VHDL-2008) |
| 2019 | IEEE 1076-2019 |

---

## 2. Características de VHDL

### 2.1 Ventajas

- ✅ **Independiente de tecnología:** El mismo código puede sintetizarse en diferentes FPGAs
- ✅ **Documentación implícita:** El código describe el hardware
- ✅ **Simulación:** Verificar antes de fabricar
- ✅ **Reutilización:** Componentes pueden usarse en múltiples proyectos
- ✅ **Portabilidad:** Código estándar IEEE

### 2.2 Características del Lenguaje

- **Fuertemente tipado:** Requiere declaración explícita de tipos
- **No sensible a mayúsculas:** `Signal` = `SIGNAL` = `signal`
- **Concurrente:** Las sentencias se ejecutan en paralelo (como el hardware)
- **Secuencial:** También permite descripción secuencial dentro de procesos

---

## 3. Niveles de Abstracción

### 3.1 Jerarquía de Descripción

```
┌─────────────────────────────────────┐
│         Nivel de Sistema            │  ← Algoritmos, comportamiento
├─────────────────────────────────────┤
│     Nivel de Transferencia          │  ← RTL (Register Transfer Level)
│        de Registros                 │
├─────────────────────────────────────┤
│        Nivel de Compuertas          │  ← Lógica combinacional/secuencial
├─────────────────────────────────────┤
│        Nivel de Switch              │  ← Transistores (no sintetizable)
└─────────────────────────────────────┘
```

### 3.2 Descripción RTL

El nivel más común para síntesis:
- Registros (flip-flops)
- Lógica combinacional entre registros
- Transferencias de datos controladas por reloj

---

## 4. Flujo de Diseño

### 4.1 Proceso Típico

```
┌──────────────┐
│ Especifica-  │
│    ción      │
└──────┬───────┘
       ▼
┌──────────────┐
│   Código     │  ← VHDL
│    VHDL      │
└──────┬───────┘
       ▼
┌──────────────┐
│  Simulación  │  ← ModelSim, GHDL
│   funcional  │
└──────┬───────┘
       ▼
┌──────────────┐
│   Síntesis   │  ← Quartus, Vivado, ISE
└──────┬───────┘
       ▼
┌──────────────┐
│ Place & Route│
└──────┬───────┘
       ▼
┌──────────────┐
│  Simulación  │
│   temporal   │
└──────┬───────┘
       ▼
┌──────────────┐
│  Programar   │  ← FPGA
│    FPGA      │
└──────────────┘
```

### 4.2 Herramientas

| Herramienta | Uso |
|-------------|-----|
| Quartus Prime | FPGAs Intel/Altera |
| Vivado | FPGAs Xilinx |
| ModelSim | Simulación |
| GHDL | Simulación (open source) |
| GTKWave | Visor de formas de onda |

---

## 5. Estructura Básica de VHDL

### 5.1 Unidades de Diseño

```vhdl
-- 1. LIBRARY: Importar bibliotecas
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- 2. ENTITY: Interfaz externa (puertos)
entity nombre_entidad is
    port (
        -- declaración de puertos
    );
end entity nombre_entidad;

-- 3. ARCHITECTURE: Implementación interna
architecture nombre_arq of nombre_entidad is
    -- declaraciones
begin
    -- implementación
end architecture nombre_arq;
```

### 5.2 Ejemplo Completo: Compuerta AND

```vhdl
-- Bibliotecas
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Entidad
entity compuerta_and is
    port (
        A : in  std_logic;
        B : in  std_logic;
        Y : out std_logic
    );
end entity compuerta_and;

-- Arquitectura
architecture behavioral of compuerta_and is
begin
    Y <= A and B;
end architecture behavioral;
```

---

## 6. Bibliotecas Estándar

### 6.1 IEEE.STD_LOGIC_1164

Define el tipo `std_logic` con 9 valores posibles:

| Valor | Significado |
|-------|-------------|
| 'U' | Uninitialized (no inicializado) |
| 'X' | Forcing Unknown (desconocido fuerte) |
| '0' | Forcing 0 (cero fuerte) |
| '1' | Forcing 1 (uno fuerte) |
| 'Z' | High Impedance (alta impedancia) |
| 'W' | Weak Unknown (desconocido débil) |
| 'L' | Weak 0 (cero débil) |
| 'H' | Weak 1 (uno débil) |
| '-' | Don't Care |

**En síntesis típicamente se usan:** '0', '1', 'Z', '-'

### 6.2 IEEE.NUMERIC_STD

Proporciona tipos para aritmética:
- `unsigned`: Vector sin signo
- `signed`: Vector con signo (complemento a 2)
- Operaciones: +, -, *, comparaciones

### 6.3 Declaración de Bibliotecas

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;    -- std_logic, std_logic_vector
use IEEE.NUMERIC_STD.ALL;        -- unsigned, signed, aritmética
```

---

## 7. Identificadores y Comentarios

### 7.1 Reglas para Identificadores

- Deben comenzar con letra
- Pueden contener letras, números y guión bajo
- No pueden terminar con guión bajo
- No pueden tener dos guiones bajos consecutivos
- No sensibles a mayúsculas/minúsculas

```vhdl
-- Válidos
signal contador : integer;
signal Dato_Entrada : std_logic;
signal CLK_100MHz : std_logic;

-- Inválidos
signal 1contador : integer;     -- comienza con número
signal dato__salida : std_logic; -- doble guión bajo
signal valor_ : std_logic;      -- termina con guión bajo
```

### 7.2 Comentarios

```vhdl
-- Esto es un comentario de línea

/* 
   Esto es un comentario
   de múltiples líneas (VHDL-2008)
*/
```

---

## 8. Palabras Reservadas

```
abs, access, after, alias, all, and, architecture, array,
assert, attribute, begin, block, body, buffer, bus, case,
component, configuration, constant, disconnect, downto,
else, elsif, end, entity, exit, file, for, function,
generate, generic, group, guarded, if, impure, in, inertial,
inout, is, label, library, linkage, literal, loop, map,
mod, nand, new, next, nor, not, null, of, on, open, or,
others, out, package, port, postponed, procedure, process,
protected, pure, range, record, register, reject, rem,
report, return, rol, ror, select, severity, signal, shared,
sla, sll, sra, srl, subtype, then, to, transport, type,
unaffected, units, until, use, variable, wait, when, while,
with, xnor, xor
```

---

## 9. Operadores

### 9.1 Operadores Lógicos

```vhdl
and, or, nand, nor, xor, xnor, not
```

### 9.2 Operadores Relacionales

```vhdl
=    -- igual
/=   -- diferente
<    -- menor que
<=   -- menor o igual
>    -- mayor que
>=   -- mayor o igual
```

### 9.3 Operadores Aritméticos

```vhdl
+    -- suma
-    -- resta
*    -- multiplicación
/    -- división
mod  -- módulo
rem  -- residuo
**   -- exponenciación
abs  -- valor absoluto
```

### 9.4 Operadores de Desplazamiento (VHDL-93+)

```vhdl
sll  -- shift left logical
srl  -- shift right logical
sla  -- shift left arithmetic
sra  -- shift right arithmetic
rol  -- rotate left
ror  -- rotate right
```

### 9.5 Operador de Concatenación

```vhdl
&    -- concatenación
-- Ejemplo: "01" & "10" = "0110"
```

---

## 10. VHDL vs Verilog

| Aspecto | VHDL | Verilog |
|---------|------|---------|
| Origen | DoD/IEEE | Industria |
| Tipado | Fuerte | Débil |
| Sintaxis | Verbose (Ada-like) | Concisa (C-like) |
| Case | Insensible | Sensible |
| Uso | Europa, militar | USA, industria |
| Estándar | IEEE 1076 | IEEE 1364 |

---

## Referencias

- IEEE Std 1076-2008, "IEEE Standard VHDL Language Reference Manual"
- Ashenden, P. J. (2008). *The Designer's Guide to VHDL*. Morgan Kaufmann.
- Pedroni, V. A. (2010). *Circuit Design with VHDL*. MIT Press.

---

<!-- IA_CONTEXT
NIVEL: Básico (1/3)
PREREQUISITOS: Conocimientos básicos de diseño digital
CONEXIONES: Base para todos los temas de VHDL
ERRORES_COMUNES: Confundir asignación <=/:=, olvidar bibliotecas, no entender concurrencia
-->
