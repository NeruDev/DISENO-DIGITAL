<!--
::METADATA::
type: method
topic_id: vhdl-05-sentencias-secuenciales
file_id: metodos-secuenciales
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [VHDL, metodologia, process, secuencial]
search_keywords: "metodología process, sentencias secuenciales"
-->

> 🏠 **Navegación:** [← Teoría](../theory/VHDL-05-Teoria-Secuenciales.md) | [Problemas →](../problems/VHDL-05-Problemas.md)

---

# Métodos: Sentencias Secuenciales

## Método 1: Plantillas de Process

### Lógica Combinacional

```vhdl
COMB: process(todas_las_entradas)
begin
    -- Asignar TODAS las salidas
    -- en TODOS los caminos
end process;
```

### Registro Simple

```vhdl
REG: process(clk)
begin
    if rising_edge(clk) then
        q <= d;
    end if;
end process;
```

### Registro con Reset Asíncrono

```vhdl
REG_ASYNC: process(clk, reset)
begin
    if reset = '1' then
        q <= '0';
    elsif rising_edge(clk) then
        q <= d;
    end if;
end process;
```

### Registro con Reset Síncrono

```vhdl
REG_SYNC: process(clk)
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

## Método 2: Evitar Latches

### Regla: Cubrir Todos los Casos

```vhdl
-- ✗ LATCH (falta else)
process(sel, a, b)
begin
    if sel = '1' then
        y <= a;
    end if;
end process;

-- ✓ CORRECTO
process(sel, a, b)
begin
    if sel = '1' then
        y <= a;
    else
        y <= b;
    end if;
end process;
```

### Técnica: Valor por Defecto

```vhdl
process(sel, a, b, c, d)
begin
    -- Valor por defecto al inicio
    y <= '0';
    
    -- Después las condiciones
    if sel = "00" then
        y <= a;
    elsif sel = "01" then
        y <= b;
    end if;
    -- No necesita else, tiene default
end process;
```

---

## Método 3: Lista de Sensibilidad Correcta

### Lógica Combinacional

```vhdl
-- Incluir TODAS las señales leídas
process(a, b, c, sel)
begin
    if sel = '1' then
        y <= a and b;
    else
        y <= c;
    end if;
end process;
```

### Lógica Secuencial

```vhdl
-- Solo clk (y reset si es asíncrono)
process(clk, reset)  -- reset es asíncrono
begin
    if reset = '1' then
        q <= '0';
    elsif rising_edge(clk) then
        q <= d;  -- d NO va en la lista
    end if;
end process;
```

### VHDL-2008: `all`

```vhdl
-- Incluye automáticamente todas las señales leídas
process(all)
begin
    y <= a when sel = '1' else b;
end process;
```

---

## Método 4: Variables para Cálculos Intermedios

### Acumulación

```vhdl
process(data)
    variable sum : unsigned(9 downto 0);
begin
    sum := (others => '0');
    for i in 0 to 7 loop
        sum := sum + unsigned("00" & data(i));
    end loop;
    total <= std_logic_vector(sum);
end process;
```

### Pipeline de Cálculos

```vhdl
process(a, b, c, d)
    variable temp1, temp2 : std_logic_vector(7 downto 0);
begin
    temp1 := a and b;      -- Paso 1
    temp2 := c or d;       -- Paso 2
    result <= temp1 xor temp2;  -- Paso 3
end process;
```

---

## Método 5: Estructuras if-case Anidadas

### Decodificación Jerárquica

```vhdl
process(mode, submode, data)
begin
    case mode is
        when "00" =>
            if submode = '0' then
                output <= data(7 downto 4);
            else
                output <= data(3 downto 0);
            end if;
        when "01" =>
            output <= not data(7 downto 4);
        when others =>
            output <= (others => '0');
    end case;
end process;
```

---

## Método 6: Múltiples Salidas en un Process

### Agrupación Lógica

```vhdl
-- Un process para lógica relacionada
process(clk, reset)
begin
    if reset = '1' then
        count <= (others => '0');
        overflow <= '0';
        zero_flag <= '1';
    elsif rising_edge(clk) then
        if enable = '1' then
            if count = MAX_COUNT then
                count <= (others => '0');
                overflow <= '1';
            else
                count <= count + 1;
                overflow <= '0';
            end if;
            
            if count = 0 then
                zero_flag <= '1';
            else
                zero_flag <= '0';
            end if;
        end if;
    end if;
end process;
```

---

## Método 7: Separar Lógica Combinacional y Secuencial

### Dos Procesos

```vhdl
-- Proceso combinacional: calcula siguiente estado/salida
COMB: process(current_state, inputs)
begin
    -- Calcular next_state y outputs
    case current_state is
        when IDLE =>
            if start = '1' then
                next_state <= RUN;
            else
                next_state <= IDLE;
            end if;
            output <= '0';
        when RUN =>
            next_state <= DONE;
            output <= '1';
        when others =>
            next_state <= IDLE;
            output <= '0';
    end case;
end process;

-- Proceso secuencial: registra el estado
SEQ: process(clk, reset)
begin
    if reset = '1' then
        current_state <= IDLE;
    elsif rising_edge(clk) then
        current_state <= next_state;
    end if;
end process;
```

---

## Método 8: Bucles Sintetizables

### For Loop para Hardware Replicado

```vhdl
-- Genera 8 comparadores en paralelo
process(input, pattern)
begin
    match <= (others => '0');
    for i in 0 to 7 loop
        if input(i) = pattern(i) then
            match(i) <= '1';
        end if;
    end loop;
end process;
```

### Encontrar Primer Bit Activo

```vhdl
process(data)
    variable found : boolean;
begin
    found := false;
    position <= (others => '0');
    valid <= '0';
    
    for i in data'high downto data'low loop
        if data(i) = '1' and not found then
            position <= std_logic_vector(to_unsigned(i, 4));
            valid <= '1';
            found := true;
        end if;
    end loop;
end process;
```

---

## Método 9: Debug con Variables

### Contador de Eventos

```vhdl
process(clk)
    variable event_count : integer := 0;
begin
    if rising_edge(clk) then
        if evento = '1' then
            event_count := event_count + 1;
            -- report para simulación
            report "Evento #" & integer'image(event_count);
        end if;
    end if;
end process;
```

---

## Método 10: Checklist de Process

### Antes de Síntesis

**Lógica Combinacional:**
- [ ] Lista de sensibilidad completa (o usar `all`)
- [ ] Todas las salidas asignadas en todos los caminos
- [ ] No hay `rising_edge` ni `falling_edge`
- [ ] `case` tiene `when others`
- [ ] `if` tiene `else` (o valor por defecto)

**Lógica Secuencial:**
- [ ] Solo `clk` en lista (+ reset si asíncrono)
- [ ] `rising_edge(clk)` o `falling_edge(clk)`
- [ ] Reset asíncrono fuera del `if rising_edge`
- [ ] Reset síncrono dentro del `if rising_edge`

### Errores Comunes

| Error | Síntoma | Solución |
|-------|---------|----------|
| Lista incompleta | Simulación incorrecta | Agregar señales |
| Latch inferido | Warning de síntesis | Cubrir todos los casos |
| Reset mal ubicado | Comportamiento erróneo | Revisar plantilla |
| Variable vs señal | Timing incorrecto | Entender diferencia |

---

<!-- IA_CONTEXT
USO: Métodos prácticos para process y sentencias secuenciales
NIVEL: Intermedio (2/3)
HERRAMIENTAS: Quartus, Vivado, ModelSim
-->
