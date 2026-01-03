<!--
::METADATA::
type: solution
topic_id: vhdl-05-sentencias-secuenciales
file_id: respuestas-secuenciales
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [respuestas, soluciones, VHDL, process]
search_keywords: "respuestas, soluciones, process, secuencial"
-->

> 🏠 **Navegación:** [← Problemas](../problems/VHDL-05-Problemas.md)

---

# Respuestas: Sentencias Secuenciales

## Nivel 1: Process Básico

### Respuesta 1.1

**Concurrentes:**
- Se ejecutan simultáneamente
- Fuera de process
- Representan hardware paralelo

**Secuenciales:**
- Se ejecutan en orden
- Dentro de process
- El process como un todo es concurrente

### Respuesta 1.2

```vhdl
process(sel, a, b, c, d)  -- Todas las señales leídas
begin
    if sel = '1' then
        y <= a and b;
    else
        y <= c or d;
    end if;
end process;
```

### Respuesta 1.3

Cuando `en = '0'`, no hay asignación a `output`. VHDL infiere un latch para mantener el valor anterior.

**Solución:**
```vhdl
process(en, data)
begin
    if en = '1' then
        output <= data;
    else
        output <= '0';  -- O cualquier valor por defecto
    end if;
end process;
```

---

## Nivel 2: Variables vs Señales

### Respuesta 2.1

- `y <= '1'` (variable v se actualiza inmediatamente a '1')
- `z <= '0'` (señal a aún tiene el valor anterior '0')

Las variables se actualizan inmediatamente; las señales se actualizan al final del delta cycle.

### Respuesta 2.2

```vhdl
process(a, b, c, d)
    variable temp1, temp2 : std_logic;
begin
    temp1 := a and b;      -- Inmediato
    temp2 := temp1 or c;   -- Usa nuevo valor de temp1
    y <= temp2 and d;      -- Usa nuevo valor de temp2
end process;
```

### Respuesta 2.3

Variables son preferibles cuando:
- Se necesita el valor inmediatamente en cálculos posteriores
- Se quiere evitar crear señales auxiliares
- Se realizan acumulaciones o cálculos iterativos

---

## Nivel 3: if-then-else

### Respuesta 3.1

```vhdl
process(sel, d0, d1, d2, d3)
begin
    if sel = "00" then
        y <= d0;
    elsif sel = "01" then
        y <= d1;
    elsif sel = "10" then
        y <= d2;
    else
        y <= d3;
    end if;
end process;
```

### Respuesta 3.2

```vhdl
process(input)
begin
    valid <= '1';
    if input(3) = '1' then
        code <= "11";
    elsif input(2) = '1' then
        code <= "10";
    elsif input(1) = '1' then
        code <= "01";
    elsif input(0) = '1' then
        code <= "00";
    else
        code <= "00";
        valid <= '0';
    end if;
end process;
```

### Respuesta 3.3

Es un **registro de desplazamiento con carga paralela**:
- Cuando `load = '1'`: carga paralela de d
- Cuando `shift = '1'`: desplazamiento a la izquierda
- Si ambos son '0': mantiene el valor (implícito)

---

## Nivel 4: case

### Respuesta 4.1

```vhdl
process(sel)
begin
    case sel is
        when "000" => y <= "00000001";
        when "001" => y <= "00000010";
        when "010" => y <= "00000100";
        when "011" => y <= "00001000";
        when "100" => y <= "00010000";
        when "101" => y <= "00100000";
        when "110" => y <= "01000000";
        when "111" => y <= "10000000";
        when others => y <= "00000000";
    end case;
end process;
```

### Respuesta 4.2

```vhdl
process(op, a, b)
begin
    case op is
        when "000" => result <= std_logic_vector(unsigned(a) + unsigned(b));
        when "001" => result <= std_logic_vector(unsigned(a) - unsigned(b));
        when "010" => result <= a and b;
        when "011" => result <= a or b;
        when "100" => result <= a xor b;
        when "101" => result <= not a;
        when "110" => result <= a(6 downto 0) & '0';  -- Shift left
        when "111" => result <= '0' & a(7 downto 1);  -- Shift right
        when others => result <= (others => '0');
    end case;
end process;
```

### Respuesta 4.3

`when others` es necesario porque:
1. `std_logic_vector` tiene 9 valores posibles por bit
2. Evita inferir latches para casos no cubiertos
3. Es requerido por el estándar para cubrir todos los casos

### Respuesta 4.4

```vhdl
process(sel, a, b, c, d)  -- Agregar todas las entradas
begin
    case sel is
        when "00" => y <= a;
        when "01" => y <= b;
        when "10" => y <= c;
        when others => y <= d;  -- Agregar when others
    end case;
end process;
```

---

## Nivel 5: Bucles

### Respuesta 5.1

```vhdl
process(data)
    variable count : integer range 0 to 8;
begin
    count := 0;
    for i in 0 to 7 loop
        if data(i) = '1' then
            count := count + 1;
        end if;
    end loop;
    ones_count <= std_logic_vector(to_unsigned(count, 4));
end process;
```

### Respuesta 5.2

```vhdl
process(data_in)
begin
    for i in 0 to 7 loop
        data_out(i) <= data_in(7-i);
    end loop;
end process;
```

### Respuesta 5.3

El número de iteraciones depende del contenido de `data`, que es una señal. El sintetizador no puede determinar cuántas iteraciones habrá en tiempo de compilación.

### Respuesta 5.4

```vhdl
process(a, b)
    variable equal : boolean;
begin
    equal := true;
    for i in a'range loop
        if a(i) /= b(i) then
            equal := false;
            exit;
        end if;
    end loop;
    
    if equal then
        eq <= '1';
    else
        eq <= '0';
    end if;
end process;
```

---

## Nivel 6: Flip-Flops y Registros

### Respuesta 6.1

```vhdl
process(clk, reset)
begin
    if reset = '1' then
        q <= '0';
    elsif rising_edge(clk) then
        if enable = '1' then
            q <= d;
        end if;
    end if;
end process;
```

### Respuesta 6.2

```vhdl
process(clk, reset)
begin
    if reset = '1' then
        q <= '0';
    elsif rising_edge(clk) then
        if t = '1' then
            q <= not q_int;
        end if;
    end if;
end process;
q <= q_int;
```

### Respuesta 6.3

```vhdl
process(clk)
begin
    if rising_edge(clk) then
        if clear = '1' then
            q <= (others => '0');
        elsif load = '1' then
            q <= d;
        end if;
    end if;
end process;
```

### Respuesta 6.4

**Reset Asíncrono:**
- Se activa independientemente del reloj
- Usa flip-flops con clear asíncrono
- Más rápido para inicialización

**Reset Síncrono:**
- Solo se activa en el flanco de reloj
- Usa lógica adicional antes del FF
- Más seguro para timing

---

## Nivel 7: Contadores

### Respuesta 7.1

```vhdl
process(clk, reset)
begin
    if reset = '1' then
        count <= (others => '0');
    elsif rising_edge(clk) then
        if enable = '1' then
            count <= count + 1;
        end if;
    end if;
end process;
```

### Respuesta 7.2

```vhdl
process(clk, reset)
begin
    if reset = '1' then
        count <= (others => '1');
    elsif rising_edge(clk) then
        if load = '1' then
            count <= data_in;
        else
            count <= count - 1;
        end if;
    end if;
end process;
```

### Respuesta 7.3

```vhdl
process(clk, reset)
begin
    if reset = '1' then
        count <= (others => '0');
        overflow <= '0';
    elsif rising_edge(clk) then
        overflow <= '0';
        if count = "1001" then  -- 9
            count <= "0000";
            overflow <= '1';
        else
            count <= count + 1;
        end if;
    end if;
end process;
```

### Respuesta 7.4

```vhdl
process(clk, reset)
begin
    if reset = '1' then
        count <= (others => '0');
    elsif rising_edge(clk) then
        if up_down = '1' then
            count <= count + 1;
        else
            count <= count - 1;
        end if;
    end if;
end process;
```

---

## Nivel 8: Registros de Desplazamiento

### Respuesta 8.1

```vhdl
process(clk, reset)
begin
    if reset = '1' then
        reg <= (others => '0');
    elsif rising_edge(clk) then
        reg <= reg(6 downto 0) & serial_in;
    end if;
end process;
```

### Respuesta 8.2

```vhdl
process(clk, reset)
begin
    if reset = '1' then
        reg <= (others => '0');
    elsif rising_edge(clk) then
        case mode is
            when "00" =>  -- Hold
                null;
            when "01" =>  -- Load
                reg <= parallel_in;
            when "10" =>  -- Shift left
                reg <= reg(6 downto 0) & '0';
            when others =>  -- Shift right
                reg <= '0' & reg(7 downto 1);
        end case;
    end if;
end process;
```

### Respuesta 8.3

```vhdl
-- LFSR 4 bits con polinomio x^4 + x^3 + 1
process(clk, reset)
begin
    if reset = '1' then
        lfsr <= "0001";  -- No puede ser todo ceros
    elsif rising_edge(clk) then
        lfsr <= lfsr(2 downto 0) & (lfsr(3) xor lfsr(2));
    end if;
end process;
```

---

## Nivel 9: Combinacional en Process

### Respuesta 9.1

```vhdl
process(sel, d0, d1, d2, d3)
begin
    case sel is
        when "00" => y <= d0;
        when "01" => y <= d1;
        when "10" => y <= d2;
        when others => y <= d3;
    end case;
end process;
```

### Respuesta 9.2

**Problema:** `z` no se asigna cuando `sel = '0'`, infiriendo un latch.

**Solución:**
```vhdl
process(a, b, sel)
begin
    if sel = '1' then
        y <= a;
        z <= b;
    else
        y <= b;
        z <= a;  -- Agregar asignación
    end if;
end process;
```

### Respuesta 9.3

```vhdl
process(add_sub, a, b)
begin
    if add_sub = '0' then
        result <= std_logic_vector(unsigned(a) + unsigned(b));
    else
        result <= std_logic_vector(unsigned(a) - unsigned(b));
    end if;
end process;
```

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para ejercicios de sentencias secuenciales
NOTA: Pueden existir soluciones alternativas válidas
-->
