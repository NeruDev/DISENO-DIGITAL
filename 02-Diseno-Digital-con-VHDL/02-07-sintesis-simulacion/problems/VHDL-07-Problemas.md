<!--
::METADATA::
type: problem
topic_id: vhdl-07-sintesis-simulacion
file_id: problemas-sintesis-simulacion
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [ejercicios, VHDL, síntesis, simulación, testbench]
search_keywords: "ejercicios, problemas, síntesis, testbench"
-->

> 🏠 **Navegación:** [← Métodos](../methods/VHDL-07-Metodos-Verificacion.md) | [Respuestas →](../solutions/VHDL-07-Respuestas.md)

---

# Problemas: Síntesis y Simulación

## Nivel 1: Conceptos Básicos

### Problema 1.1
¿Cuál es la diferencia entre simulación funcional y simulación temporal?

### Problema 1.2
¿Por qué el tipo `real` no es sintetizable?

### Problema 1.3
¿Qué hardware se infiere de este código?
```vhdl
process(clk)
begin
    if rising_edge(clk) then
        if en = '1' then
            q <= d;
        end if;
    end if;
end process;
```

---

## Nivel 2: Testbench Básico

### Problema 2.1
Escribir un testbench básico para un inversor:
```vhdl
entity inverter is
    port (
        a : in  std_logic;
        y : out std_logic
    );
end entity;
```

### Problema 2.2
Crear un generador de reloj de 100 MHz.

### Problema 2.3
Crear un generador de reset que dure 200 ns.

---

## Nivel 3: Generadores de Estímulos

### Problema 3.1
Escribir un proceso que genere la secuencia: 0, 1, 2, 3, 4, 5, 6, 7 en un contador de 3 bits, con un ciclo de reloj entre cada valor.

### Problema 3.2
Generar un patrón de datos aleatorio usando la función `rand` (conceptual - describir el enfoque).

### Problema 3.3
Leer vectores de prueba desde un archivo y aplicarlos a las entradas.

---

## Nivel 4: Verificación con Assert

### Problema 4.1
Escribir un assert que verifique que un sumador de 4 bits produce el resultado correcto.

### Problema 4.2
Agregar asserts para verificar:
- Reset funciona correctamente
- Salida válida aparece después de 3 ciclos de reloj

### Problema 4.3
¿Cuál es la diferencia entre `severity error` y `severity failure`?

---

## Nivel 5: Código Sintetizable

### Problema 5.1
Identificar qué líneas NO son sintetizables:
```vhdl
signal a, b, c : real;
signal d : std_logic;
signal e : integer range 0 to 100;

process(clk)
begin
    if rising_edge(clk) then
        c <= a + b;
        wait for 10 ns;
        d <= '1';
        e <= e / 2;
    end if;
end process;
```

### Problema 5.2
Corregir este código para evitar el latch:
```vhdl
process(sel, a, b, c, d)
begin
    case sel is
        when "00" => y <= a;
        when "01" => y <= b;
        when "10" => y <= c;
    end case;
end process;
```

### Problema 5.3
¿Qué problema tiene esta lista de sensibilidad?
```vhdl
process(a, b)
begin
    if c = '1' then
        y <= a and b;
    else
        y <= a or b;
    end if;
end process;
```

---

## Nivel 6: Testbench para FSM

### Problema 6.1
Escribir un testbench para una FSM de 3 estados (IDLE, RUN, DONE) que:
- Verifica la secuencia de estados
- Prueba el reset desde cada estado

### Problema 6.2
Agregar verificación de que la FSM nunca entra en un estado ilegal.

### Problema 6.3
¿Cómo verificar que todas las transiciones posibles han sido probadas?

---

## Nivel 7: Procedimientos en Testbench

### Problema 7.1
Crear un procedimiento `apply_reset` que active reset por N ciclos.

### Problema 7.2
Crear un procedimiento `send_uart_byte` que simule la transmisión de un byte por UART a 9600 baud.

### Problema 7.3
Crear un procedimiento `check_and_report` que compare actual vs esperado y genere reporte.

---

## Nivel 8: Análisis de Síntesis

### Problema 8.1
Este código genera un warning de latch. Identificar y corregir:
```vhdl
process(state, input)
begin
    case state is
        when IDLE =>
            output <= '0';
            if input = '1' then
                next_state <= RUN;
            end if;
        when RUN =>
            output <= '1';
            next_state <= IDLE;
    end case;
end process;
```

### Problema 8.2
¿Qué recursos usa este código después de síntesis?
```vhdl
signal counter : unsigned(7 downto 0);
signal product : unsigned(15 downto 0);

process(clk)
begin
    if rising_edge(clk) then
        counter <= counter + 1;
        product <= counter * counter;
    end if;
end process;
```

### Problema 8.3
¿Cómo optimizar este código para usar menos recursos?
```vhdl
y <= a * 5;  -- Multiplicador
```

---

## Nivel 9: Simulación Avanzada

### Problema 9.1
Escribir un testbench auto-verificante que:
- Cuenta tests ejecutados
- Cuenta errores
- Genera reporte final

### Problema 9.2
Implementar timeout en un testbench para detectar si la simulación se "cuelga".

### Problema 9.3
Crear un testbench que use un archivo para entradas y otro para salidas esperadas.

---

## Nivel 10: Proyecto Completo

### Problema 10.1
Crear un diseño completo y su testbench para un contador BCD de 2 dígitos:
- Cuenta de 00 a 99
- Reset síncrono
- Enable
- Salida BCD de 8 bits

### Problema 10.2
Diseñar y verificar un FIFO de 8 posiciones x 8 bits:
- Señales: write, read, data_in, data_out, full, empty
- Testbench debe verificar:
  - Escritura hasta lleno
  - Lectura hasta vacío
  - Operaciones simultáneas

### Problema 10.3
Crear un sistema completo con:
- FSM de control
- Datapath
- Testbench con cobertura completa
- Verificar síntesis sin warnings

---

<!-- IA_CONTEXT
PROPÓSITO: Ejercicios sobre síntesis y verificación VHDL
RESPUESTAS: Ver archivo solutions/VHDL-07-Respuestas.md
HERRAMIENTAS: ModelSim, GHDL, Vivado, Quartus
-->
