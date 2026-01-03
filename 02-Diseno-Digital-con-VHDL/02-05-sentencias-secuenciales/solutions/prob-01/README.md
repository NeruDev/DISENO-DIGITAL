# Soluciones Detalladas: Sentencias Secuenciales (VHDL-05)

```
::METADATA::
tipo: indice-soluciones
tema: vhdl-05-sentencias-secuenciales
actualizado: 2026-01-03
::END::
```

## Estructura de Niveles de Solución

| Nivel | Archivo | Contenido |
|-------|---------|-----------|
| 1️⃣ | [`VHDL-05-Respuestas.md`](../VHDL-05-Respuestas.md) | Solo respuestas finales |
| 2️⃣ | Esta carpeta `prob-01/` | Soluciones paso a paso |
| 3️⃣ | Secciones "Conceptos Clave" | Explicación profunda del método |

---

## Índice de Soluciones Detalladas

### Nivel 1: Procesos Básicos ⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 1.1 | Estructura de proceso | [VHDL-05-Sol-Problema-1.1.md](VHDL-05-Sol-Problema-1.1.md) | ⭐⭐ |
| 1.2 | Lista de sensibilidad | [VHDL-05-Sol-Problema-1.2.md](VHDL-05-Sol-Problema-1.2.md) | ⭐⭐ |
| 1.3 | Variables vs Señales | [VHDL-05-Sol-Problema-1.3.md](VHDL-05-Sol-Problema-1.3.md) | ⭐⭐ |

### Nivel 2: IF-THEN-ELSE ⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 2.1 | IF simple | [VHDL-05-Sol-Problema-2.1.md](VHDL-05-Sol-Problema-2.1.md) | ⭐⭐ |
| 2.2 | IF-ELSIF-ELSE | [VHDL-05-Sol-Problema-2.2.md](VHDL-05-Sol-Problema-2.2.md) | ⭐⭐ |
| 2.3 | IF anidados | [VHDL-05-Sol-Problema-2.3.md](VHDL-05-Sol-Problema-2.3.md) | ⭐⭐ |

### Nivel 3: CASE ⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 3.1 | CASE básico | [VHDL-05-Sol-Problema-3.1.md](VHDL-05-Sol-Problema-3.1.md) | ⭐⭐ |
| 3.2 | CASE con rangos | [VHDL-05-Sol-Problema-3.2.md](VHDL-05-Sol-Problema-3.2.md) | ⭐⭐ |
| 3.3 | CASE vs IF | [VHDL-05-Sol-Problema-3.3.md](VHDL-05-Sol-Problema-3.3.md) | ⭐⭐ |

### Nivel 4: Procesos Sincronos ⭐⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 4.1 | Flip-Flop D | [VHDL-05-Sol-Problema-4.1.md](VHDL-05-Sol-Problema-4.1.md) | ⭐⭐⭐ |
| 4.2 | Registro con reset | [VHDL-05-Sol-Problema-4.2.md](VHDL-05-Sol-Problema-4.2.md) | ⭐⭐⭐ |
| 4.3 | Contador síncrono | [VHDL-05-Sol-Problema-4.3.md](VHDL-05-Sol-Problema-4.3.md) | ⭐⭐⭐ |

### Nivel 5: Loops ⭐⭐⭐

| Problema | Tema | Archivo | Dificultad |
|----------|------|---------|:----------:|
| 5.1 | FOR loop | [VHDL-05-Sol-Problema-5.1.md](VHDL-05-Sol-Problema-5.1.md) | ⭐⭐⭐ |
| 5.2 | WHILE loop | [VHDL-05-Sol-Problema-5.2.md](VHDL-05-Sol-Problema-5.2.md) | ⭐⭐⭐ |

---

## Referencia de Sentencias Secuenciales

### Plantilla de Proceso Combinacional

```vhdl
process(a, b, sel)  -- Lista de sensibilidad: TODAS las entradas
begin
    if sel = '1' then
        y <= a;
    else
        y <= b;
    end if;
end process;
```

### Plantilla de Proceso Síncrono

```vhdl
process(clk)
begin
    if rising_edge(clk) then
        if reset = '1' then
            q <= (others => '0');
        else
            q <= d;
        end if;
    end if;
end process;
```

### Plantilla de Proceso con Reset Asíncrono

```vhdl
process(clk, reset)
begin
    if reset = '1' then
        q <= (others => '0');
    elsif rising_edge(clk) then
        q <= d;
    end if;
end process;
```

---

## Comparación IF vs CASE

| Característica | IF-THEN-ELSE | CASE |
|----------------|--------------|------|
| Prioridad | Sí (primera condición verdadera) | No (mutuamente exclusivo) |
| Condiciones | Cualquier expresión booleana | Valor de una expresión |
| Exhaustividad | No requerida (else opcional) | Requerida (when others) |
| Legibilidad | Mejor para pocas opciones | Mejor para muchas opciones |
| Síntesis | Puede generar lógica priorizada | Generalmente MUX paralelo |

---

## Señales vs Variables

| Característica | Signal | Variable |
|----------------|--------|----------|
| Ámbito | Arquitectura | Proceso |
| Actualización | Fin del ciclo delta | Inmediata |
| Declaración | architecture...begin | process...begin |
| Asignación | `<=` | `:=` |
| Síntesis | Cables/registros | Pueden optimizarse |

### Ejemplo

```vhdl
process(clk)
    variable v : integer := 0;  -- Variable local
begin
    if rising_edge(clk) then
        v := v + 1;         -- Actualización inmediata
        count <= v;         -- Signal se actualiza al final
    end if;
end process;
```

---

## Navegación

| ⬅️ Respuestas | 🏠 Intro | ➡️ Problemas |
|:-------------:|:--------:|:------------:|
| [VHDL-05-Respuestas.md](../VHDL-05-Respuestas.md) | [VHDL-05-Intro.md](../../VHDL-05-Intro.md) | [VHDL-05-Problemas.md](../../problems/VHDL-05-Problemas.md) |
