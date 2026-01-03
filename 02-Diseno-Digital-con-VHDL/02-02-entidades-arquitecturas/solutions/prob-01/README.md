# Soluciones Detalladas: Entidades y Arquitecturas (VHDL-02)

```
::METADATA::
tipo: indice-soluciones
tema: vhdl-02-entidades-arquitecturas
actualizado: 2026-01-03
::END::
```

## Estructura de Niveles de Solución

| Nivel | Archivo | Contenido |
|-------|---------|-----------|
| 1️⃣ | [`VHDL-02-Respuestas.md`](../VHDL-02-Respuestas.md) | Solo respuestas finales |
| 2️⃣ | Esta carpeta `prob-01/` | Soluciones paso a paso |
| 3️⃣ | Secciones "Conceptos Clave" | Explicación profunda del método |

---

## Índice de Soluciones Detalladas

### Nivel 1: Declaración de Entidades ⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 1.1 | Entidad NAND 3 entradas | [VHDL-02-Sol-Problema-1.1.md](VHDL-02-Sol-Problema-1.1.md) | ⭐⭐ |
| 1.2 | Entidad MUX 4:1 8 bits | [VHDL-02-Sol-Problema-1.2.md](VHDL-02-Sol-Problema-1.2.md) | ⭐⭐ |
| 1.3 | Corrección de errores | [VHDL-02-Sol-Problema-1.3.md](VHDL-02-Sol-Problema-1.3.md) | ⭐⭐ |

### Nivel 2: Arquitecturas Básicas ⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 2.1 | Arquitectura XOR | [VHDL-02-Sol-Problema-2.1.md](VHDL-02-Sol-Problema-2.1.md) | ⭐⭐ |
| 2.2 | Buffer tri-state | [VHDL-02-Sol-Problema-2.2.md](VHDL-02-Sol-Problema-2.2.md) | ⭐⭐ |
| 2.3 | Comparador dataflow | [VHDL-02-Sol-Problema-2.3.md](VHDL-02-Sol-Problema-2.3.md) | ⭐⭐ |

### Nivel 3: Genéricos ⭐⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 3.1 | Registro parametrizable | [VHDL-02-Sol-Problema-3.1.md](VHDL-02-Sol-Problema-3.1.md) | ⭐⭐⭐ |
| 3.2 | Contador genérico | [VHDL-02-Sol-Problema-3.2.md](VHDL-02-Sol-Problema-3.2.md) | ⭐⭐⭐ |
| 3.3 | Instanciación con genéricos | [VHDL-02-Sol-Problema-3.3.md](VHDL-02-Sol-Problema-3.3.md) | ⭐⭐⭐ |

### Nivel 4: Señales Internas ⭐⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 4.1 | Señales intermedias | [VHDL-02-Sol-Problema-4.1.md](VHDL-02-Sol-Problema-4.1.md) | ⭐⭐⭐ |

---

## Referencia Rápida

### Modos de Puerto

| Modo | Dirección | Lectura | Escritura | Uso |
|------|:---------:|:-------:|:---------:|-----|
| `in` | Entrada | ✅ | ❌ | Entradas |
| `out` | Salida | ❌ | ✅ | Salidas (no feedback) |
| `inout` | Bidireccional | ✅ | ✅ | Buses bidireccionales |
| `buffer` | Salida | ✅ | ✅ | Salidas con feedback |

### Plantilla de Entidad

```vhdl
entity nombre_entidad is
    generic (
        PARAM1 : integer := valor_defecto;
        PARAM2 : natural := 8
    );
    port (
        -- Entradas
        clk     : in  std_logic;
        reset   : in  std_logic;
        data_in : in  std_logic_vector(PARAM2-1 downto 0);
        -- Salidas
        data_out : out std_logic_vector(PARAM2-1 downto 0);
        valid    : out std_logic
    );
end entity nombre_entidad;
```

### Estilos de Arquitectura

| Estilo | Descripción | Uso |
|--------|-------------|-----|
| Behavioral | Procesos con if/case | FSM, secuencial |
| Dataflow | Asignaciones concurrentes | Combinacional simple |
| Structural | Instanciación de componentes | Jerárquico |

---

## Navegación

| ⬅️ Respuestas | 🏠 Intro | ➡️ Problemas |
|:-------------:|:--------:|:------------:|
| [VHDL-02-Respuestas.md](../VHDL-02-Respuestas.md) | [VHDL-02-Intro.md](../../VHDL-02-Intro.md) | [VHDL-02-Problemas.md](../../problems/VHDL-02-Problemas.md) |
