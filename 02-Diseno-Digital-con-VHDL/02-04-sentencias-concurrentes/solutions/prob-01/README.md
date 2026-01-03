# Soluciones Detalladas: Sentencias Concurrentes (VHDL-04)

```
::METADATA::
tipo: indice-soluciones
tema: vhdl-04-sentencias-concurrentes
actualizado: 2026-01-03
::END::
```

## Estructura de Niveles de Solución

| Nivel | Archivo | Contenido |
|-------|---------|-----------|
| 1️⃣ | [`VHDL-04-Respuestas.md`](../VHDL-04-Respuestas.md) | Solo respuestas finales |
| 2️⃣ | Esta carpeta `prob-01/` | Soluciones paso a paso |
| 3️⃣ | Secciones "Conceptos Clave" | Explicación profunda del método |

---

## Índice de Soluciones Detalladas

### Nivel 1: Asignaciones Simples ⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 1.1 | Asignación simple | [VHDL-04-Sol-Problema-1.1.md](VHDL-04-Sol-Problema-1.1.md) | ⭐ |
| 1.2 | Operadores lógicos | [VHDL-04-Sol-Problema-1.2.md](VHDL-04-Sol-Problema-1.2.md) | ⭐ |

### Nivel 2: Asignación Condicional ⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 2.1 | WHEN-ELSE | [VHDL-04-Sol-Problema-2.1.md](VHDL-04-Sol-Problema-2.1.md) | ⭐⭐ |
| 2.2 | WITH-SELECT | [VHDL-04-Sol-Problema-2.2.md](VHDL-04-Sol-Problema-2.2.md) | ⭐⭐ |
| 2.3 | Comparación WHEN vs WITH | [VHDL-04-Sol-Problema-2.3.md](VHDL-04-Sol-Problema-2.3.md) | ⭐⭐ |

### Nivel 3: Instanciación de Componentes ⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 3.1 | Component declaration | [VHDL-04-Sol-Problema-3.1.md](VHDL-04-Sol-Problema-3.1.md) | ⭐⭐ |
| 3.2 | Port map posicional | [VHDL-04-Sol-Problema-3.2.md](VHDL-04-Sol-Problema-3.2.md) | ⭐⭐ |
| 3.3 | Port map nombrado | [VHDL-04-Sol-Problema-3.3.md](VHDL-04-Sol-Problema-3.3.md) | ⭐⭐ |

### Nivel 4: Generate ⭐⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 4.1 | FOR-GENERATE | [VHDL-04-Sol-Problema-4.1.md](VHDL-04-Sol-Problema-4.1.md) | ⭐⭐⭐ |
| 4.2 | IF-GENERATE | [VHDL-04-Sol-Problema-4.2.md](VHDL-04-Sol-Problema-4.2.md) | ⭐⭐⭐ |
| 4.3 | Estructuras repetitivas | [VHDL-04-Sol-Problema-4.3.md](VHDL-04-Sol-Problema-4.3.md) | ⭐⭐⭐ |

---

## Referencia de Sentencias Concurrentes

### Tipos de Sentencias

| Sentencia | Uso | Ejemplo |
|-----------|-----|---------|
| Asignación simple | Conexiones directas | `Y <= A and B;` |
| `when-else` | Prioridad implícita | `Y <= A when sel='1' else B;` |
| `with-select` | Selección por valor | `with sel select Y <= ...` |
| `component` | Instanciación | `U1: comp port map(...);` |
| `generate` | Estructuras repetidas | `gen: for i in 0 to N-1 generate` |

### Comparación WHEN-ELSE vs WITH-SELECT

| Característica | WHEN-ELSE | WITH-SELECT |
|----------------|-----------|-------------|
| Prioridad | Sí (implícita) | No |
| Múltiples señales | ✅ | ❌ |
| Claridad | Condiciones | Selector único |
| Síntesis | MUX con prioridad | MUX paralelo |
| Casos exhaustivos | Último `else` | `when others` |

---

## Plantillas

### WHEN-ELSE

```vhdl
output <= valor1 when condicion1 else
          valor2 when condicion2 else
          valor3 when condicion3 else
          valor_default;
```

### WITH-SELECT

```vhdl
with selector select
    output <= valor1 when "00",
              valor2 when "01",
              valor3 when "10",
              valor4 when others;
```

### Instanciación de Componente

```vhdl
-- Declaración (en architecture, antes de begin)
component nombre_componente is
    port (
        entrada : in  std_logic;
        salida  : out std_logic
    );
end component;

-- Instanciación (después de begin)
U1: nombre_componente
    port map (
        entrada => mi_entrada,
        salida  => mi_salida
    );
```

### FOR-GENERATE

```vhdl
gen_label: for i in 0 to N-1 generate
    -- Sentencias concurrentes aquí
    signal_array(i) <= input_array(i) and enable;
end generate gen_label;
```

---

## Navegación

| ⬅️ Respuestas | 🏠 Intro | ➡️ Problemas |
|:-------------:|:--------:|:------------:|
| [VHDL-04-Respuestas.md](../VHDL-04-Respuestas.md) | [VHDL-04-Intro.md](../../VHDL-04-Intro.md) | [VHDL-04-Problemas.md](../../problems/VHDL-04-Problemas.md) |
