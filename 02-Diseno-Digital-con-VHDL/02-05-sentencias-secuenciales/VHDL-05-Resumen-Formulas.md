<!--
::METADATA::
type: reference
topic_id: vhdl-05-sentencias-secuenciales
file_id: resumen-secuenciales
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [cheatsheet, VHDL, process, secuencial]
search_keywords: "resumen, process, secuencial, cheatsheet"
-->

> 🏠 **Navegación:** [← Volver al Índice](./02-05-Intro.md)

---

# 📋 Cheatsheet: Sentencias Secuenciales

## Estructura de Process

```vhdl
etiqueta: process(lista_sensibilidad)
    variable v : tipo;
begin
    -- Sentencias secuenciales
end process;
```

---

## Variables vs Señales

| Variable | Señal |
|----------|-------|
| `:=` para asignar | `<=` para asignar |
| Actualización inmediata | Actualización al final |
| Solo dentro de process | En toda la arquitectura |

---

## Plantillas de Process

### Combinacional
```vhdl
process(all)  -- o todas las entradas
begin
    -- Asignar TODAS las salidas
    -- en TODOS los caminos
end process;
```

### Registro (Reset Asíncrono)
```vhdl
process(clk, reset)
begin
    if reset = '1' then
        q <= '0';
    elsif rising_edge(clk) then
        q <= d;
    end if;
end process;
```

### Registro (Reset Síncrono)
```vhdl
process(clk)
begin
    if rising_edge(clk) then
        if reset = '1' then
            q <= '0';
        else
            q <= d;
        end if;
    end if;
end process;
```

---

## if-then-else

```vhdl
if condicion1 then
    sentencias;
elsif condicion2 then
    sentencias;
else
    sentencias;  -- SIEMPRE incluir
end if;
```

---

## case

```vhdl
case selector is
    when "00" => sentencias;
    when "01" => sentencias;
    when "10" | "11" => sentencias;  -- OR
    when others => sentencias;  -- SIEMPRE
end case;
```

---

## for loop

```vhdl
for i in 0 to N-1 loop
    -- sentencias
end loop;

for i in data'range loop
    -- sentencias
end loop;
```

---

## Control de Bucles

```vhdl
exit;           -- Salir del loop
exit when cond; -- Salir si condición
next;           -- Siguiente iteración
next when cond; -- Siguiente si condición
```

---

## Detectar Flancos

```vhdl
if rising_edge(clk) then    -- Flanco subida
if falling_edge(clk) then   -- Flanco bajada

-- Alternativa
if clk'event and clk = '1' then
```

---

## Evitar Latches

```vhdl
-- ✗ LATCH
if sel = '1' then
    y <= a;
end if;

-- ✓ CORRECTO
if sel = '1' then
    y <= a;
else
    y <= b;
end if;

-- ✓ ALTERNATIVA: Default al inicio
y <= '0';  -- Default
if sel = '1' then
    y <= a;
end if;
```

---

## Lista de Sensibilidad

### Combinacional
```vhdl
process(a, b, c, sel)  -- TODAS las entradas
-- o
process(all)  -- VHDL-2008
```

### Secuencial
```vhdl
process(clk)        -- Solo reloj
process(clk, rst)   -- Reloj + reset asíncrono
```

---

## Contadores

### Ascendente
```vhdl
count <= count + 1;
```

### Descendente
```vhdl
count <= count - 1;
```

### Up/Down
```vhdl
if up = '1' then
    count <= count + 1;
else
    count <= count - 1;
end if;
```

---

## Registros de Desplazamiento

### Izquierda
```vhdl
reg <= reg(6 downto 0) & serial_in;
```

### Derecha
```vhdl
reg <= serial_in & reg(7 downto 1);
```

---

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| Latch | Falta else/when others | Cubrir todos los casos |
| Comportamiento erróneo | Lista incompleta | Agregar señales |
| Timing incorrecto | Variable vs señal | Entender diferencia |

---

## Regla de Oro

⚠️ **En lógica combinacional:**
- Lista de sensibilidad completa
- Asignar TODAS las salidas en TODOS los caminos

---

<!-- IA_CONTEXT
TIPO: Cheatsheet/Referencia rápida
USO: Consulta durante desarrollo VHDL
-->
