<!--
::METADATA::
type: problem
topic_id: vhdl-02-entidades-arquitecturas
file_id: problemas-entidades-arq
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [ejercicios, VHDL, entidad, arquitectura]
search_keywords: "ejercicios, problemas, entity, architecture"
-->

> 🏠 **Navegación:** [← Métodos](../methods/VHDL-02-Metodos-EntidadesArq.md) | [Respuestas →](../solutions/VHDL-02-Respuestas.md)

---

# Problemas: Entidades y Arquitecturas

## Nivel 1: Declaración de Entidades

### Problema 1.1
Escribir la entidad para una compuerta NAND de 3 entradas.

### Problema 1.2
Escribir la entidad para un multiplexor 4:1 con:
- 4 entradas de datos de 8 bits
- Selector de 2 bits
- 1 salida de 8 bits

### Problema 1.3
Identificar y corregir los errores en esta entidad:
```vhdl
entity mi_modulo
    port
        clk : in std_logic
        data_in : in std_logic_vector(7 to 0);
        data_out : out std_logic_vector(7 downto 0),
        status : buffer std_logic
end entity;
```

---

## Nivel 2: Arquitecturas Básicas

### Problema 2.1
Completar la arquitectura para una compuerta XOR de 2 entradas:
```vhdl
entity xor_gate is
    port (a, b : in std_logic; y : out std_logic);
end entity;

architecture _______ of _______ is
begin
    -- Completar
end architecture;
```

### Problema 2.2
Escribir entidad y arquitectura para un buffer tri-state:
- Entrada de datos de 8 bits
- Señal de habilitación (output enable)
- Salida de 8 bits

### Problema 2.3
Implementar un comparador de igualdad de 4 bits con arquitectura dataflow.

---

## Nivel 3: Genéricos

### Problema 3.1
Crear un registro parametrizable con:
- Genérico WIDTH para el ancho
- Genérico RESET_VAL para el valor de reset
- Entrada de reloj, reset, enable y datos
- Salida de datos

### Problema 3.2
Modificar el siguiente código para que WIDTH sea genérico:
```vhdl
entity contador is
    port (
        clk   : in  std_logic;
        reset : in  std_logic;
        q     : out std_logic_vector(7 downto 0)
    );
end entity;
```

### Problema 3.3
Escribir la instanciación de un contador genérico para:
- a) 4 bits
- b) 12 bits
- c) 16 bits con valor inicial 100

---

## Nivel 4: Señales Internas

### Problema 4.1
¿Por qué este código produce error y cómo se soluciona?
```vhdl
entity contador is
    port (
        clk : in std_logic;
        q   : out std_logic_vector(3 downto 0)
    );
end entity;

architecture bad of contador is
begin
    process(clk)
    begin
        if rising_edge(clk) then
            q <= q + 1;  -- ERROR
        end if;
    end process;
end architecture;
```

### Problema 4.2
Declarar las señales internas necesarias para:
- Un contador de 8 bits
- Un flag de overflow
- Un registro temporal de 16 bits
- Un estado de máquina con 4 valores posibles

### Problema 4.3
¿Cuál es la diferencia entre una señal y una variable? Dar ejemplo de cada una.

---

## Nivel 5: Componentes

### Problema 5.1
Dado el siguiente componente:
```vhdl
entity full_adder is
    port (
        a, b, cin : in std_logic;
        sum, cout : out std_logic
    );
end entity;
```

Escribir la declaración del componente y dos instanciaciones para crear un sumador de 2 bits.

### Problema 5.2
Usar instanciación directa (sin declarar componente) para instanciar:
- Entidad: `registro`
- Arquitectura: `rtl`
- Biblioteca: `work`

### Problema 5.3
¿Cuál es la diferencia entre port map posicional y nominal? ¿Cuál se recomienda?

---

## Nivel 6: Estilos de Arquitectura

### Problema 6.1
Implementar un multiplexor 2:1 en tres estilos diferentes:
- a) Behavioral (con process)
- b) Dataflow (con when-else)
- c) Structural (con compuertas)

### Problema 6.2
¿Cuál estilo de arquitectura es más apropiado para?
- a) Una máquina de estados
- b) Un sumador aritmético
- c) Conectar varios módulos existentes
- d) Lógica combinacional simple

### Problema 6.3
Convertir esta arquitectura behavioral a dataflow:
```vhdl
architecture behavioral of decoder2to4 is
begin
    process(sel, en)
    begin
        y <= "0000";
        if en = '1' then
            case sel is
                when "00" => y(0) <= '1';
                when "01" => y(1) <= '1';
                when "10" => y(2) <= '1';
                when "11" => y(3) <= '1';
                when others => null;
            end case;
        end if;
    end process;
end architecture;
```

---

## Nivel 7: Generate

### Problema 7.1
Usar for-generate para crear un banco de 8 flip-flops D.

### Problema 7.2
Usar if-generate para:
- Si DEBUG = true, incluir un contador de ciclos
- Si DEBUG = false, no incluir nada

### Problema 7.3
Crear un sumador de n bits usando for-generate e instancias de full_adder.

---

## Nivel 8: Diseño Jerárquico

### Problema 8.1
Diseñar la jerarquía para un UART simple:
- Top level: uart
  - uart_rx
  - uart_tx
  - baud_generator

Escribir las entidades de cada módulo.

### Problema 8.2
Implementar el top level que instancie los tres submódulos del problema anterior.

### Problema 8.3
Un procesador simple tiene:
- ALU (8 bits, operaciones +, -, AND, OR)
- Banco de registros (4 registros de 8 bits)
- Unidad de control

Diseñar la entidad del top level y las entidades de los submódulos.

---

## Nivel 9: Constantes y Alias

### Problema 9.1
Definir constantes para:
- Ancho de bus de datos: 32
- Frecuencia de reloj: 100 MHz
- Período de reloj correspondiente
- Valor inicial todo ceros de 32 bits

### Problema 9.2
Usar alias para extraer campos de una instrucción de 16 bits:
- Bits 15-12: opcode
- Bits 11-8: registro destino
- Bits 7-4: registro fuente 1
- Bits 3-0: registro fuente 2

### Problema 9.3
¿Cuándo conviene usar constantes vs genéricos?

---

## Nivel 10: Integración Completa

### Problema 10.1
Diseñar completamente (entidad + arquitectura) un registro de desplazamiento de 8 bits con:
- Carga paralela
- Desplazamiento izquierda/derecha
- Salida serial y paralela

### Problema 10.2
Diseñar un módulo ALU de 8 bits con:
- Operaciones: ADD, SUB, AND, OR, XOR, NOT, SHL, SHR
- Selector de operación de 3 bits
- Flags: Zero, Carry, Negative

### Problema 10.3
Crear un sistema completo con:
- Contador de 4 bits
- Comparador
- Display 7 segmentos
- Top module que los integre

---

<!-- IA_CONTEXT
PROPÓSITO: Ejercicios sobre entidades y arquitecturas VHDL
RESPUESTAS: Ver archivo solutions/VHDL-02-Respuestas.md
HERRAMIENTAS: ModelSim, GHDL, Quartus, Vivado
-->
