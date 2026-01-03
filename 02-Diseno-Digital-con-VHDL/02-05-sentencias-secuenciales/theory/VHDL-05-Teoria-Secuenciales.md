<!--
::METADATA::
type: theory
topic_id: vhdl-05-sentencias-secuenciales
file_id: teoria-sentencias-secuenciales
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 2
tags: [VHDL, process, secuencial, if, case, loop, variable]
search_keywords: "sentencias secuenciales, process, if, case, loop"
-->

> 🏠 **Navegación:** [← Volver al Índice](../02-05-Intro.md) | [Métodos →](../methods/VHDL-05-Metodos-Secuenciales.md)

---

# Sentencias Secuenciales en VHDL

## 1. El Process

### 1.1 Concepto

El `process` es una **sentencia concurrente** que contiene **sentencias secuenciales**.
Las sentencias dentro del process se ejecutan **en orden**, una después de otra.

```vhdl
architecture ejemplo of modulo is
begin
    -- El process como un todo es concurrente
    process(lista_sensibilidad)
    begin
        -- Aquí dentro: secuencial
        a := b;
        c <= a;  -- Usa el nuevo valor de a
    end process;
end architecture;
```

### 1.2 Lista de Sensibilidad

El process se **activa** cuando cambia alguna señal de su lista de sensibilidad.

```vhdl
-- Se activa cuando cambia clk
process(clk)
begin
    ...
end process;

-- Se activa cuando cambia a, b o sel
process(a, b, sel)
begin
    ...
end process;
```

### 1.3 Regla de Oro

**Lógica combinacional:** Incluir TODAS las señales leídas en la lista.
**Lógica secuencial:** Solo `clk` (y `reset` si es asíncrono).

---

## 2. Estructura del Process

### 2.1 Sintaxis Completa

```vhdl
etiqueta: process(lista_sensibilidad)
    -- Zona de declaraciones
    variable var1 : tipo;
    variable var2 : tipo := valor_inicial;
begin
    -- Zona de sentencias secuenciales
    sentencias;
end process etiqueta;
```

### 2.2 Process sin Lista de Sensibilidad

Se usa con `wait` para testbenches:

```vhdl
process
begin
    wait for 10 ns;
    clk <= not clk;
end process;
```

⚠️ **No sintetizable** - Solo para simulación.

---

## 3. Variables vs Señales

### 3.1 Comparación

| Característica | Variable | Señal |
|----------------|----------|-------|
| Declaración | Dentro de process | En arquitectura |
| Actualización | Inmediata | Al final del delta cycle |
| Alcance | Solo el process | Toda la arquitectura |
| Síntesis | Almacenamiento temporal | Cables o registros |

### 3.2 Ejemplo Comparativo

```vhdl
process(clk)
    variable v : integer := 0;
begin
    if rising_edge(clk) then
        v := v + 1;       -- Actualización inmediata
        sig <= v;         -- sig toma el nuevo valor de v
    end if;
end process;
```

### 3.3 Cuándo Usar Variables

- Cálculos intermedios dentro de un process
- Evitar señales auxiliares
- Cuando se necesita el valor inmediatamente

```vhdl
process(a, b, c, d)
    variable suma : integer;
begin
    suma := a + b;      -- Valor disponible inmediatamente
    suma := suma + c;   -- Acumular
    resultado <= suma + d;
end process;
```

---

## 4. Sentencia `if-then-else`

### 4.1 Sintaxis

```vhdl
if condicion1 then
    sentencias;
elsif condicion2 then
    sentencias;
else
    sentencias;
end if;
```

### 4.2 Ejemplo: Flip-Flop D con Reset

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

### 4.3 Prioridad

Las condiciones se evalúan **en orden**. La primera verdadera se ejecuta.

```vhdl
if a = '1' then      -- Mayor prioridad
    y <= "01";
elsif b = '1' then   -- Segunda prioridad
    y <= "10";
else                 -- Default
    y <= "00";
end if;
```

---

## 5. Sentencia `case`

### 5.1 Sintaxis

```vhdl
case expresion is
    when valor1 =>
        sentencias;
    when valor2 =>
        sentencias;
    when others =>
        sentencias;
end case;
```

### 5.2 Ejemplo: Decodificador

```vhdl
process(sel)
begin
    case sel is
        when "00" => y <= "0001";
        when "01" => y <= "0010";
        when "10" => y <= "0100";
        when "11" => y <= "1000";
        when others => y <= "0000";
    end case;
end process;
```

### 5.3 Múltiples Valores

```vhdl
case opcode is
    when "000" | "001" =>  -- OR de opciones
        resultado <= a + b;
    when "010" =>
        resultado <= a - b;
    when others =>
        resultado <= (others => '0');
end case;
```

### 5.4 `if` vs `case`

| `if-then-else` | `case` |
|----------------|--------|
| Condiciones arbitrarias | Basado en expresión |
| Con prioridad | Sin prioridad |
| Puede inferir cadena de MUX | Genera MUX directo |
| Más flexible | Más eficiente para selectores |

---

## 6. Bucles: `for loop`

### 6.1 Sintaxis

```vhdl
for variable in rango loop
    sentencias;
end loop;
```

### 6.2 Ejemplo: Contador de Bits

```vhdl
process(data)
    variable count : integer := 0;
begin
    count := 0;
    for i in data'range loop
        if data(i) = '1' then
            count := count + 1;
        end if;
    end loop;
    bit_count <= count;
end process;
```

### 6.3 Bucles Sintetizables

El rango debe ser **conocido en tiempo de compilación**:

```vhdl
-- ✓ Sintetizable
for i in 0 to 7 loop ...

-- ✓ Sintetizable (N es genérico constante)
for i in 0 to N-1 loop ...

-- ✗ NO sintetizable (n es señal)
for i in 0 to n loop ...
```

---

## 7. Bucles: `while loop`

### 7.1 Sintaxis

```vhdl
while condicion loop
    sentencias;
end loop;
```

### 7.2 Uso

Generalmente **no sintetizable** porque el número de iteraciones no es fijo.

```vhdl
-- Solo para simulación
process
    variable i : integer := 0;
begin
    while i < 10 loop
        wait for 10 ns;
        i := i + 1;
    end loop;
    wait;
end process;
```

---

## 8. Control de Bucles

### 8.1 `exit`

Termina el bucle inmediatamente:

```vhdl
for i in 0 to 15 loop
    if encontrado = '1' then
        exit;  -- Sale del loop
    end if;
    -- procesar
end loop;
```

### 8.2 `next`

Salta a la siguiente iteración:

```vhdl
for i in 0 to 15 loop
    if skip(i) = '1' then
        next;  -- Salta esta iteración
    end if;
    -- procesar
end loop;
```

### 8.3 `exit when` / `next when`

```vhdl
exit when condicion;
next when condicion;
```

---

## 9. Lógica Combinacional en Process

### 9.1 Reglas

1. Incluir **todas** las señales leídas en la lista de sensibilidad
2. Asignar **todas** las salidas en **todos** los caminos
3. No usar `rising_edge` ni `falling_edge`

### 9.2 Ejemplo Correcto

```vhdl
-- Multiplexor combinacional
process(sel, a, b, c, d)
begin
    case sel is
        when "00" => y <= a;
        when "01" => y <= b;
        when "10" => y <= c;
        when others => y <= d;
    end case;
end process;
```

### 9.3 Latch Inferido (Error Común)

```vhdl
-- ✗ PELIGRO: Infiere latch
process(sel, a, b)
begin
    if sel = '1' then
        y <= a;
    end if;
    -- ¿Qué pasa cuando sel = '0'? → Latch
end process;

-- ✓ CORRECTO
process(sel, a, b)
begin
    if sel = '1' then
        y <= a;
    else
        y <= b;  -- Caso else incluido
    end if;
end process;
```

---

## 10. Lógica Secuencial en Process

### 10.1 Plantilla de Registro con Reset Asíncrono

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

### 10.2 Plantilla de Registro con Reset Síncrono

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

### 10.3 Contador con Enable

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

---

## 11. Atributos de Señales

### 11.1 Atributos para Simulación

| Atributo | Significado |
|----------|-------------|
| `signal'event` | True si la señal cambió |
| `signal'last_value` | Valor anterior |
| `signal'last_event` | Tiempo desde último cambio |

### 11.2 Detectar Flancos

```vhdl
-- Método 1: rising_edge (recomendado)
if rising_edge(clk) then

-- Método 2: 'event
if clk'event and clk = '1' then

-- Flanco de bajada
if falling_edge(clk) then
if clk'event and clk = '0' then
```

---

## Referencias

- IEEE Std 1076-2008
- Ashenden, P.J. (2008). *The Designer's Guide to VHDL*

---

<!-- IA_CONTEXT
NIVEL: Intermedio (2/3)
PREREQUISITOS: 02-01, 02-02, 02-03, 02-04
CONEXIONES: Fundamental para registros, FSM, contadores
ERRORES_COMUNES: Listas de sensibilidad incompletas, latches no intencionales
-->
