<!--
::METADATA::
type: reference
topic_id: vhdl-02-entidades-arquitecturas
file_id: resumen-entidades-arq
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [cheatsheet, VHDL, entity, architecture]
search_keywords: "resumen, entidad, arquitectura, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./02-02-Intro.md)

---

# 📋 Cheatsheet: Entidades y Arquitecturas

## Estructura de Entity

```vhdl
entity nombre is
    generic (
        PARAM : tipo := valor_default
    );
    port (
        entrada : in  tipo;
        salida  : out tipo
    );
end entity nombre;
```

---

## Estructura de Architecture

```vhdl
architecture nombre_arq of nombre_ent is
    -- Declaraciones (señales, constantes, componentes)
    signal sig : tipo;
begin
    -- Implementación
end architecture;
```

---

## Modos de Puerto

| Modo | Dirección | Legible Internamente |
|------|-----------|----------------------|
| `in` | → | Sí |
| `out` | ← | No |
| `inOut` | ↔ | Sí |
| `buffer` | ← | Sí (obsoleto) |

---

## Genéricos Comunes

```vhdl
generic (
    WIDTH      : integer := 8;
    USE_RESET  : boolean := true;
    CLK_PERIOD : time := 10 ns
);
```

---

## Estilos de Arquitectura

| Estilo | Uso |
|--------|-----|
| Behavioral | Procesos, if/case |
| Dataflow | Asignaciones concurrentes |
| Structural | Instanciación de componentes |
| RTL | Registros + lógica |

---

## Declarar Componente

```vhdl
component nombre is
    generic (...);
    port (...);
end component;
```

---

## Instanciar Componente

### Tradicional
```vhdl
INST: nombre
    generic map (PARAM => valor)
    port map (
        puerto => señal
    );
```

### Directa (VHDL-93)
```vhdl
INST: entity work.nombre(arq)
    generic map (...)
    port map (...);
```

---

## Señales Internas

```vhdl
architecture rtl of mod is
    signal contador : unsigned(7 downto 0);
    signal flag     : std_logic := '0';
begin
    ...
end architecture;
```

---

## Constantes

```vhdl
constant NOMBRE : tipo := valor;
constant WIDTH  : integer := 8;
constant ZERO   : std_logic_vector(7 downto 0) := x"00";
```

---

## Alias

```vhdl
signal word : std_logic_vector(15 downto 0);
alias msb : std_logic_vector(7 downto 0) is word(15 downto 8);
alias lsb : std_logic_vector(7 downto 0) is word(7 downto 0);
```

---

## Generate

### For-Generate
```vhdl
GEN: for i in 0 to N-1 generate
    INST_I: componente port map (...);
end generate;
```

### If-Generate
```vhdl
GEN: if CONDICION generate
    -- código
end generate;
```

---

## Puerto `open`

```vhdl
INST: entidad port map (
    usado   => señal,
    no_usado => open  -- Solo para out
);
```

---

## Leer Salida (Solución)

```vhdl
architecture rtl of mod is
    signal q_int : std_logic_vector(...);
begin
    -- Usar q_int internamente
    q <= q_int;  -- Asignar a salida
end architecture;
```

---

## Port Map

### Nominal (✓ Recomendado)
```vhdl
port map (
    clk => system_clk,
    rst => system_rst
);
```

### Posicional (✗ Evitar)
```vhdl
port map (system_clk, system_rst);
```

---

## Errores Comunes

| Error | Solución |
|-------|----------|
| Leer puerto `out` | Usar señal interna |
| Tipos no coinciden | Conversión explícita |
| Puerto sin conectar | Usar `open` o señal |
| Componente no declarado | Declarar o usar instanciación directa |

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante desarrollo VHDL
-->
