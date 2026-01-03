<!--
::METADATA::
type: reference
topic_id: glossary-index
file_id: glossary-readme
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [glosario, referencia, terminos]
search_keywords: "glosario, definiciones, terminos tecnicos"
-->

# GLOSARIO DE TÉRMINOS - DISEÑO DIGITAL

Este glosario contiene las definiciones de los términos técnicos más importantes utilizados en los módulos de Diseño Digital, VHDL y Microcontroladores.

## Navegación

- [A](#a) | [B](#b) | [C](#c) | [D](#d) | [E](#e) | [F](#f) | [G](#g) | [H](#h) | [I](#i) | [J](#j) | [K](#k) | [L](#l) | [M](#m) | [N](#n) | [O](#o) | [P](#p) | [Q](#q) | [R](#r) | [S](#s) | [T](#t) | [U](#u) | [V](#v) | [W](#w) | [X](#x) | [Y](#y) | [Z](#z)

---

## A

### adc
**ADC (Analog-to-Digital Converter)**: Conversor analógico a digital. Dispositivo que convierte señales analógicas continuas en valores digitales discretos.
- **Resolución**: Número de bits del resultado (8, 10, 12 bits)
- **Fórmula**: `ADC = (Vin × 2^n) / Vref`
- 📚 Ver: [MCU-04 ADC/DAC](../03-Microcontroladores/03-04-adc-dac/)

### algebra-booleana
**Álgebra Booleana**: Sistema matemático para análisis y diseño de circuitos lógicos usando operaciones AND, OR, NOT.
- 📚 Ver: [DD-02 Álgebra Booleana](../01-Diseno-Digital/01-02-algebra-booleana/)

### arquitectura
**Arquitectura**: En VHDL, describe el comportamiento o estructura interna de una entidad. Tipos: behavioral, structural, dataflow.
- 📚 Ver: [VHDL-02 Entidades y Arquitecturas](../02-Diseno-Digital-con-VHDL/02-02-entidades-arquitecturas/)

### asincronico
**Asíncrono**: Sistema o señal que no depende de un reloj común para su sincronización. Opuesto a síncrono.

---

## B

### baud-rate
**Baud Rate**: Velocidad de transmisión en símbolos por segundo en comunicación serial.
- **Fórmula UBRR**: `UBRR = (F_CPU / (16 × Baud)) - 1`
- 📚 Ver: [MCU-05 Comunicación Serial](../03-Microcontroladores/03-05-comunicacion-serial/)

### biestable
**Biestable**: Circuito digital que puede almacenar un bit de información. Incluye tipos como D, JK, T, SR.
- **Flip-Flop**: Sensible a flancos
- **Latch**: Sensible a niveles
- 📚 Ver: [DD-05 Circuitos Secuenciales](../01-Diseno-Digital/01-05-circuitos-secuenciales/)

### binario
**Sistema Binario**: Sistema numérico de base 2 usando dígitos 0 y 1.
- **Conversión**: Dividir entre 2 sucesivamente
- 📚 Ver: [DD-01 Sistemas Numéricos](../01-Diseno-Digital/01-01-sistemas-numericos/)

### bus
**Bus**: Conjunto de líneas de comunicación que transportan datos, direcciones o señales de control.
- **Bus de datos**: Transporta información
- **Bus de direcciones**: Indica ubicación de memoria
- **Bus de control**: Señales de sincronización

---

## C

### ca1
**Complemento a 1 (CA1)**: Representación de números negativos invirtiendo todos los bits.
- 📚 Ver: [DD-01 Sistemas Numéricos](../01-Diseno-Digital/01-01-sistemas-numericos/)

### ca2
**Complemento a 2 (CA2)**: Representación más usada para números con signo. CA1 + 1.
- **Rango n bits**: -2^(n-1) a 2^(n-1) - 1
- 📚 Ver: [DD-01 Sistemas Numéricos](../01-Diseno-Digital/01-01-sistemas-numericos/)

### clock
**Clock (Reloj)**: Señal periódica utilizada para sincronizar operaciones en circuitos secuenciales.
- **Período**: T = 1/f
- **Duty cycle**: Porcentaje en HIGH

### combinacional
**Circuito Combinacional**: Circuito cuya salida depende únicamente de las entradas actuales, sin memoria.
- Ejemplos: MUX, decodificador, sumador
- 📚 Ver: [DD-04 Circuitos Combinacionales](../01-Diseno-Digital/01-04-circuitos-combinacionales/)

### compuerta
**Compuerta Lógica**: Circuito electrónico que implementa una función booleana básica.
- **Básicas**: AND, OR, NOT
- **Universales**: NAND, NOR
- 📚 Ver: [DD-03 Compuertas Lógicas](../01-Diseno-Digital/01-03-compuertas-logicas/)

### contador
**Contador**: Circuito secuencial que cuenta pulsos de reloj y almacena el conteo.
- **Asíncrono (ripple)**: Cada FF depende del anterior
- **Síncrono**: Todos los FF con mismo reloj
- 📚 Ver: [DD-06 Contadores y Registros](../01-Diseno-Digital/01-06-contadores-registros/)

### ctc
**CTC (Clear Timer on Compare)**: Modo de timer que resetea al alcanzar valor de comparación.
- **Fórmula OCR**: `OCR = (T × F_CPU / Prescaler) - 1`
- 📚 Ver: [MCU-03 Timers](../03-Microcontroladores/03-03-timers-interrupciones/)

---

## D

### dac
**DAC (Digital-to-Analog Converter)**: Conversor digital a analógico. Genera voltaje proporcional al valor digital.
- 📚 Ver: [MCU-04 ADC/DAC](../03-Microcontroladores/03-04-adc-dac/)

### datapath
**Datapath**: Ruta de datos en un procesador donde se realizan operaciones aritméticas y lógicas.

### debounce
**Debounce**: Técnica para eliminar rebotes mecánicos en botones/switches.
- **Hardware**: Filtro RC o Schmitt trigger
- **Software**: Retardo o muestreo múltiple
- 📚 Ver: [MCU-02 Registros y Puertos](../03-Microcontroladores/03-02-registros-puertos/)

### decodificador
**Decodificador**: Circuito combinacional que activa una única salida basándose en el código de entrada.
- **n:2^n**: n entradas, 2^n salidas
- 📚 Ver: [DD-04 Circuitos Combinacionales](../01-Diseno-Digital/01-04-circuitos-combinacionales/)

### demux
**Demultiplexor (DEMUX)**: Circuito que dirige una entrada a una de varias salidas según selector.
- 📚 Ver: [DD-04 Circuitos Combinacionales](../01-Diseno-Digital/01-04-circuitos-combinacionales/)

---

## E

### encoder
**Encoder (Codificador)**: Circuito que convierte 2^n entradas en n salidas binarias.
- **Priority encoder**: Solo codifica entrada de mayor prioridad
- 📚 Ver: [DD-04 Circuitos Combinacionales](../01-Diseno-Digital/01-04-circuitos-combinacionales/)

### entidad
**Entidad**: En VHDL, define la interfaz externa de un componente (puertos de entrada/salida).
- Sintaxis: `entity nombre is port(...); end entity;`
- 📚 Ver: [VHDL-02 Entidades y Arquitecturas](../02-Diseno-Digital-con-VHDL/02-02-entidades-arquitecturas/)

### eeprom
**EEPROM**: Memoria de solo lectura borrable eléctricamente y programable. No volátil.
- **Ciclos escritura**: ~100,000
- 📚 Ver: [DD-07 Memorias](../01-Diseno-Digital/01-07-memorias/)

---

## F

### flash
**Memoria Flash**: Memoria no volátil, programable eléctricamente en bloques.
- **Ciclos escritura**: ~10,000
- 📚 Ver: [DD-07 Memorias](../01-Diseno-Digital/01-07-memorias/) | [MCU-01 Arquitectura](../03-Microcontroladores/03-01-arquitectura-mcu/)

### flip-flop
**Flip-Flop**: Biestable sensible a flancos. Tipos: D, JK, T, SR.
- **D**: Dato → Q en flanco
- **JK**: Set/Reset sin estado prohibido
- **T**: Toggle
- 📚 Ver: [DD-05 Circuitos Secuenciales](../01-Diseno-Digital/01-05-circuitos-secuenciales/)

### fpga
**FPGA (Field-Programmable Gate Array)**: Dispositivo de lógica programable en campo. Matriz de CLBs.
- 📚 Ver: [VHDL-07 Síntesis](../02-Diseno-Digital-con-VHDL/02-07-sintesis-simulacion/)

### fsm
**FSM (Finite State Machine)**: Máquina de estados finitos. Modelo computacional con estados definidos.
- **Moore**: Salida depende solo del estado
- **Mealy**: Salida depende del estado y entradas
- 📚 Ver: [VHDL-06 Máquinas de Estados](../02-Diseno-Digital-con-VHDL/02-06-maquinas-estados/) | [DD-05 Circuitos Secuenciales](../01-Diseno-Digital/01-05-circuitos-secuenciales/)

---

## G

### generic
**Generic**: En VHDL, parámetro configurable de una entidad para diseños reutilizables.
- Ejemplo: `generic (N : integer := 8);`
- 📚 Ver: [VHDL-02 Entidades](../02-Diseno-Digital-con-VHDL/02-02-entidades-arquitecturas/)

### gpio
**GPIO (General Purpose Input/Output)**: Pines de entrada/salida de propósito general en microcontroladores.
- **Registros AVR**: DDRx, PORTx, PINx
- 📚 Ver: [MCU-02 Registros y Puertos](../03-Microcontroladores/03-02-registros-puertos/)

---

## H

### harvard
**Arquitectura Harvard**: Arquitectura de computadora con memorias separadas para programa y datos.
- Permite acceso simultáneo a instrucción y dato
- Usada en la mayoría de MCUs
- 📚 Ver: [MCU-01 Arquitectura](../03-Microcontroladores/03-01-arquitectura-mcu/)

### hdl
**HDL (Hardware Description Language)**: Lenguaje de descripción de hardware como VHDL o Verilog.
- 📚 Ver: [VHDL-01 Introducción](../02-Diseno-Digital-con-VHDL/02-01-introduccion-vhdl/)

### hexadecimal
**Sistema Hexadecimal**: Sistema numérico de base 16 (0-9, A-F).
- Prefijo: 0x o sufijo h
- 📚 Ver: [DD-01 Sistemas Numéricos](../01-Diseno-Digital/01-01-sistemas-numericos/)

---

## I

### interrupcion
**Interrupción (IRQ)**: Mecanismo que suspende la ejecución normal para atender un evento prioritario.
- **ISR**: Interrupt Service Routine
- **Vector**: Dirección de la ISR
- 📚 Ver: [MCU-03 Timers e Interrupciones](../03-Microcontroladores/03-03-timers-interrupciones/)

### i2c
**I2C (Inter-Integrated Circuit)**: Protocolo de comunicación serie de dos hilos (SDA, SCL).
- **Velocidades**: Standard 100kHz, Fast 400kHz
- **Direccionamiento**: 7-bit o 10-bit
- 📚 Ver: [MCU-06 Protocolos I2C/SPI](../03-Microcontroladores/03-06-protocolos-i2c-spi/)

### ieee-1164
**IEEE 1164**: Estándar que define el tipo `std_logic` con 9 valores posibles.
- Valores: 'U', 'X', '0', '1', 'Z', 'W', 'L', 'H', '-'
- 📚 Ver: [VHDL-03 Tipos de Datos](../02-Diseno-Digital-con-VHDL/02-03-tipos-datos/)

---

## J

### jtag
**JTAG (Joint Test Action Group)**: Estándar para pruebas y programación de dispositivos.

---

## K

### karnaugh
**Mapa de Karnaugh (K-map)**: Método gráfico para simplificación de funciones booleanas.
- Agrupa términos adyacentes
- Potencias de 2: 1, 2, 4, 8...
- 📚 Ver: [DD-02 Álgebra Booleana](../01-Diseno-Digital/01-02-algebra-booleana/)

---

## L

### latch
**Latch**: Biestable sensible a niveles (no a flancos).
- **SR Latch**: Set-Reset básico
- **D Latch**: Transparente cuando enable=1
- 📚 Ver: [DD-05 Circuitos Secuenciales](../01-Diseno-Digital/01-05-circuitos-secuenciales/)

### lsb
**LSB (Least Significant Bit)**: Bit menos significativo (posición 0).
- En ADC: Resolución mínima = Vref / 2^n
- 📚 Ver: [DD-01 Sistemas Numéricos](../01-Diseno-Digital/01-01-sistemas-numericos/)

### lut
**LUT (Look-Up Table)**: Tabla de consulta utilizada en FPGAs para implementar lógica combinacional.
- 📚 Ver: [VHDL-07 Síntesis](../02-Diseno-Digital-con-VHDL/02-07-sintesis-simulacion/)

---

## M

### mcu
**MCU (Microcontroller Unit)**: Microcontrolador. Sistema completo en un chip: CPU + Memoria + Periféricos.
- 📚 Ver: [MCU-01 Arquitectura](../03-Microcontroladores/03-01-arquitectura-mcu/)

### mealy
**Máquina Mealy**: FSM donde la salida depende del estado actual Y las entradas.
- Salida puede cambiar asíncronamente
- 📚 Ver: [VHDL-06 Máquinas de Estados](../02-Diseno-Digital-con-VHDL/02-06-maquinas-estados/)

### moore
**Máquina Moore**: FSM donde la salida depende SOLO del estado actual.
- Salida sincronizada con reloj
- 📚 Ver: [VHDL-06 Máquinas de Estados](../02-Diseno-Digital-con-VHDL/02-06-maquinas-estados/)

### msb
**MSB (Most Significant Bit)**: Bit más significativo (mayor peso).
- En números con signo: indica polaridad
- 📚 Ver: [DD-01 Sistemas Numéricos](../01-Diseno-Digital/01-01-sistemas-numericos/)

### mux
**Multiplexor (MUX)**: Circuito selector que elige una de varias entradas para la salida.
- **2^n:1**: n bits de selección, 2^n entradas
- 📚 Ver: [DD-04 Circuitos Combinacionales](../01-Diseno-Digital/01-04-circuitos-combinacionales/)

---

## N

### nand
**NAND**: Compuerta lógica AND negada. Funcionalmente completa (puede implementar cualquier función).
- `Y = NOT(A AND B)`
- 📚 Ver: [DD-03 Compuertas Lógicas](../01-Diseno-Digital/01-03-compuertas-logicas/)

### nor
**NOR**: Compuerta lógica OR negada. Funcionalmente completa.
- `Y = NOT(A OR B)`
- 📚 Ver: [DD-03 Compuertas Lógicas](../01-Diseno-Digital/01-03-compuertas-logicas/)

### numeric-std
**IEEE.NUMERIC_STD**: Paquete VHDL con tipos `signed` y `unsigned` para aritmética.
- Funciones: `to_unsigned()`, `to_integer()`, `resize()`
- 📚 Ver: [VHDL-03 Tipos de Datos](../02-Diseno-Digital-con-VHDL/02-03-tipos-datos/)

---

## O

### octal
**Sistema Octal**: Sistema numérico de base 8 (dígitos 0-7).
- 1 dígito octal = 3 bits
- 📚 Ver: [DD-01 Sistemas Numéricos](../01-Diseno-Digital/01-01-sistemas-numericos/)

### overflow
**Overflow (Desbordamiento)**: Condición que ocurre cuando el resultado excede la capacidad de representación.
- En CA2: cuando el signo del resultado es incorrecto
- 📚 Ver: [DD-01 Sistemas Numéricos](../01-Diseno-Digital/01-01-sistemas-numericos/)

---

## P

### pic
**PIC**: Familia de microcontroladores de Microchip Technology (8, 16, 32 bits).
- 📚 Ver: [MCU-01 Arquitectura](../03-Microcontroladores/03-01-arquitectura-mcu/)

### prescaler
**Prescaler**: Divisor de frecuencia de reloj para timers y periféricos.
- Valores típicos: 1, 8, 64, 256, 1024
- 📚 Ver: [MCU-03 Timers](../03-Microcontroladores/03-03-timers-interrupciones/)

### process
**Process**: En VHDL, bloque de código secuencial que se ejecuta cuando cambian señales de sensibilidad.
- Sintaxis: `process(lista_sensibilidad) begin ... end process;`
- 📚 Ver: [VHDL-05 Sentencias Secuenciales](../02-Diseno-Digital-con-VHDL/02-05-sentencias-secuenciales/)

### pull-up
**Pull-up**: Resistencia que mantiene una señal en nivel alto cuando no hay driver activo.
- Típico: 4.7kΩ - 10kΩ
- 📚 Ver: [MCU-02 Registros y Puertos](../03-Microcontroladores/03-02-registros-puertos/)

### pwm
**PWM (Pulse Width Modulation)**: Modulación por ancho de pulso. Técnica para controlar potencia/señales analógicas.
- **Duty Cycle**: % del período en HIGH
- **Fórmula DC**: `DC = (OCR + 1) / (TOP + 1) × 100%`
- 📚 Ver: [MCU-03 Timers](../03-Microcontroladores/03-03-timers-interrupciones/)

---

## Q

### quine-mccluskey
**Quine-McCluskey**: Algoritmo para minimización de funciones booleanas.

---

## R

### ram
**RAM (Random Access Memory)**: Memoria de acceso aleatorio. Volátil.
- **SRAM**: Estática, más rápida
- **DRAM**: Dinámica, mayor densidad
- 📚 Ver: [DD-07 Memorias](../01-Diseno-Digital/01-07-memorias/)

### registro
**Registro**: Conjunto de flip-flops que almacenan múltiples bits. Base de la arquitectura digital.
- **Shift Register**: Desplaza bits
- **Parallel Load**: Carga paralela
- 📚 Ver: [DD-06 Contadores y Registros](../01-Diseno-Digital/01-06-contadores-registros/)

### rising-edge
**Rising Edge (Flanco de Subida)**: Transición de 0 a 1 en una señal digital.
- En VHDL: `rising_edge(clk)` o `clk'event and clk='1'`
- 📚 Ver: [VHDL-05 Sentencias Secuenciales](../02-Diseno-Digital-con-VHDL/02-05-sentencias-secuenciales/)

### rom
**ROM (Read-Only Memory)**: Memoria de solo lectura. No volátil.
- 📚 Ver: [DD-07 Memorias](../01-Diseno-Digital/01-07-memorias/)

### rtl
**RTL (Register Transfer Level)**: Nivel de abstracción para diseño digital que describe transferencias entre registros.
- 📚 Ver: [VHDL-07 Síntesis](../02-Diseno-Digital-con-VHDL/02-07-sintesis-simulacion/)

---

## S

### secuencial
**Circuito Secuencial**: Circuito cuya salida depende de las entradas Y del estado anterior (tiene memoria).
- Elementos: Flip-flops, latches
- 📚 Ver: [DD-05 Circuitos Secuenciales](../01-Diseno-Digital/01-05-circuitos-secuenciales/)

### signal
**Signal**: En VHDL, representa conexiones físicas entre componentes. Se actualiza al final del delta cycle.
- 📚 Ver: [VHDL-04 Sentencias Concurrentes](../02-Diseno-Digital-con-VHDL/02-04-sentencias-concurrentes/)

### spi
**SPI (Serial Peripheral Interface)**: Protocolo de comunicación serie síncrona de 4 hilos.
- Señales: MOSI, MISO, SCK, CS
- Modos: CPOL, CPHA (0-3)
- 📚 Ver: [MCU-06 Protocolos I2C/SPI](../03-Microcontroladores/03-06-protocolos-i2c-spi/)

### sram
**SRAM**: Memoria RAM estática. Más rápida que DRAM, usada en MCUs para variables.
- 📚 Ver: [DD-07 Memorias](../01-Diseno-Digital/01-07-memorias/) | [MCU-01 Arquitectura](../03-Microcontroladores/03-01-arquitectura-mcu/)

### std-logic
**STD_LOGIC**: Tipo de dato en VHDL para representar señales digitales con 9 estados posibles.
- '0', '1': Valores lógicos fuertes
- 'Z': Alta impedancia
- 'X': Desconocido/conflicto
- 📚 Ver: [VHDL-03 Tipos de Datos](../02-Diseno-Digital-con-VHDL/02-03-tipos-datos/)

### std-logic-vector
**STD_LOGIC_VECTOR**: Array de std_logic para representar buses de datos.
- Declaración: `signal data : std_logic_vector(7 downto 0);`
- 📚 Ver: [VHDL-03 Tipos de Datos](../02-Diseno-Digital-con-VHDL/02-03-tipos-datos/)

### sumador
**Sumador**: Circuito combinacional que realiza suma aritmética.
- **Half Adder**: 2 entradas, sum + carry
- **Full Adder**: 3 entradas (incluye carry in)
- **Ripple Carry**: Cascada de FAs
- 📚 Ver: [DD-04 Circuitos Combinacionales](../01-Diseno-Digital/01-04-circuitos-combinacionales/)

---

## T

### testbench
**Testbench**: Entorno de simulación para verificar diseños HDL. Entidad sin puertos que instancia el DUT.
- Self-checking: Verifica automáticamente resultados
- 📚 Ver: [VHDL-07 Síntesis y Simulación](../02-Diseno-Digital-con-VHDL/02-07-sintesis-simulacion/)

### timer
**Timer**: Módulo de temporización en microcontroladores. Contador con prescaler.
- Modos: Normal, CTC, PWM
- 📚 Ver: [MCU-03 Timers e Interrupciones](../03-Microcontroladores/03-03-timers-interrupciones/)

### tri-state
**Tri-State (Tres Estados)**: Salida que puede ser alta (1), baja (0) o alta impedancia (Z).
- En VHDL: `output <= data when enable='1' else 'Z';`
- 📚 Ver: [DD-03 Compuertas Lógicas](../01-Diseno-Digital/01-03-compuertas-logicas/)

### truth-table
**Tabla de Verdad**: Representación tabular de todas las combinaciones de entrada y sus salidas correspondientes.
- 📚 Ver: [DD-02 Álgebra Booleana](../01-Diseno-Digital/01-02-algebra-booleana/)

---

## U

### uart
**UART (Universal Asynchronous Receiver-Transmitter)**: Protocolo de comunicación serial asíncrono.
- Parámetros: Baud rate, bits de datos (8), paridad, bits de stop
- Full-duplex: TX y RX independientes
- Frame: Start bit + Data + Parity(opt) + Stop bit(s)
- 📚 Ver: [MCU-05 Comunicación Serial](../03-Microcontroladores/03-05-comunicacion-serial/)

### underflow
**Underflow**: Condición cuando resultado es menor que el mínimo representable.
- En CA2: Cruce de límite negativo
- 📚 Ver: [DD-01 Sistemas Numéricos](../01-Diseno-Digital/01-01-sistemas-numericos/)

### unsigned
**Unsigned**: En VHDL, tipo de dato para números sin signo (IEEE.NUMERIC_STD).
- Rango: 0 a 2^n - 1
- 📚 Ver: [VHDL-03 Tipos de Datos](../02-Diseno-Digital-con-VHDL/02-03-tipos-datos/)

---

## V

### variable
**Variable**: En VHDL, objeto que se actualiza inmediatamente (solo dentro de process).
- Declaración: `variable temp : integer := 0;`
- 📚 Ver: [VHDL-05 Sentencias Secuenciales](../02-Diseno-Digital-con-VHDL/02-05-sentencias-secuenciales/)

### vhdl
**VHDL (VHSIC Hardware Description Language)**: Lenguaje de descripción de hardware estándar IEEE.
- Estructura: Entity + Architecture
- Estilos: Comportamental, Estructural, Dataflow
- 📚 Ver: [VHDL-01 Introducción](../02-Diseno-Digital-con-VHDL/02-01-introduccion-vhdl/)

### von-neumann
**Arquitectura Von Neumann**: Arquitectura donde programa y datos comparten mismo bus de memoria.
- Contraste con Harvard (buses separados)
- 📚 Ver: [MCU-01 Arquitectura](../03-Microcontroladores/03-01-arquitectura-mcu/)

### volatile
**Volatile**: Variable que puede cambiar fuera del flujo normal del programa (interrupciones).
- En C: `volatile uint8_t flag;`
- 📚 Ver: [MCU-03 Interrupciones](../03-Microcontroladores/03-03-timers-interrupciones/)

---

## W

### watchdog
**Watchdog Timer (WDT)**: Temporizador de vigilancia que reinicia el sistema ante bloqueos.
- Requiere "patada" periódica para evitar reset
- Protección contra loops infinitos
- 📚 Ver: [MCU-03 Timers](../03-Microcontroladores/03-03-timers-interrupciones/)

### when-else
**When-Else**: Sentencia concurrente en VHDL para asignación condicional.
- Sintaxis: `output <= A when sel='1' else B;`
- 📚 Ver: [VHDL-04 Sentencias Concurrentes](../02-Diseno-Digital-con-VHDL/02-04-sentencias-concurrentes/)

### with-select
**With-Select**: Sentencia concurrente en VHDL para selección múltiple (equivalente a MUX).
- Sintaxis: `with sel select output <= A when "00", B when "01", ...;`
- 📚 Ver: [VHDL-04 Sentencias Concurrentes](../02-Diseno-Digital-con-VHDL/02-04-sentencias-concurrentes/)

---

## X

### xor
**XOR (Exclusive OR)**: Compuerta lógica OR exclusiva. Salida alta cuando entradas son diferentes.
- `Y = A ⊕ B = A'B + AB'`
- Aplicaciones: Paridad, sumadores, detección de cambios
- 📚 Ver: [DD-03 Compuertas Lógicas](../01-Diseno-Digital/01-03-compuertas-logicas/)

### xnor
**XNOR (Exclusive NOR)**: Compuerta XOR negada. Salida alta cuando entradas son iguales.
- `Y = (A ⊕ B)' = AB + A'B'`
- Aplicaciones: Comparadores de igualdad
- 📚 Ver: [DD-03 Compuertas Lógicas](../01-Diseno-Digital/01-03-compuertas-logicas/)

---

## Y

### yosys
**Yosys**: Framework open-source para síntesis de VHDL/Verilog.
- Soporta FPGAs iCE40, ECP5, Gowin
- 📚 Ver: [VHDL-07 Síntesis](../02-Diseno-Digital-con-VHDL/02-07-sintesis-simulacion/)

---

## Z

### zero-flag
**Zero Flag (Z)**: Bandera de estado que indica si el resultado de una operación es cero.
- Parte del registro de estado (SREG en AVR)
- 📚 Ver: [MCU-01 Arquitectura](../03-Microcontroladores/03-01-arquitectura-mcu/)

---

## Contribuir al Glosario

Para agregar nuevos términos:

1. Utilizar el formato de ancla normalizado: minúsculas, sin caracteres especiales.
2. Incluir siglas expandidas cuando aplique.
3. Agregar referencias cruzadas con enlaces internos.
4. Mantener orden alfabético estricto.
