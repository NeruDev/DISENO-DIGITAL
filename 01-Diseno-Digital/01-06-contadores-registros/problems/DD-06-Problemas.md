<!--
::METADATA::
type: problem
topic_id: dd-06-contadores-registros
file_id: problemas-contadores-registros
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [ejercicios, contadores, registros]
search_keywords: "ejercicios, problemas, contadores, registros"
-->

> 🏠 **Navegación:** [← Métodos](../methods/DD-06-Metodos-Contadores.md) | [Respuestas →](../solutions/DD-06-Respuestas.md)

---

# Problemas: Contadores y Registros

## Nivel 1: Contadores Asíncronos

### Problema 1.1
Para un contador asíncrono de 4 bits:
- a) Dibujar el diagrama de tiempo para los primeros 8 pulsos
- b) ¿Cuál es la frecuencia de Q3 si CLK = 1 MHz?
- c) ¿Cuál es el retardo máximo de propagación si cada FF tiene tpd = 10ns?

### Problema 1.2
Diseñar un contador asíncrono módulo 10 usando flip-flops JK:
- a) ¿Cuántos flip-flops se necesitan?
- b) ¿Cuál estado activa el reset?
- c) Dibujar el circuito

### Problema 1.3
Un contador asíncrono de 3 bits con tpd = 15ns por flip-flop:
- a) Calcular el retardo total en el peor caso
- b) ¿Cuál es la frecuencia máxima de operación?
- c) ¿Qué estados pueden mostrar glitches?

---

## Nivel 2: Contadores Síncronos

### Problema 2.1
Diseñar un contador síncrono de 3 bits ascendente usando flip-flops D:
- a) Tabla de transición
- b) Ecuaciones de excitación
- c) Circuito completo

### Problema 2.2
Diseñar un contador síncrono módulo 6 (0-5) con flip-flops JK:
- a) Tabla de estados
- b) Tabla de excitación JK
- c) Mapas K y ecuaciones
- d) ¿Qué pasa con los estados no usados (6,7)?

### Problema 2.3
Comparar para un contador de 4 bits:
- a) Número de compuertas (síncrono vs asíncrono)
- b) Retardo máximo
- c) Frecuencia máxima de operación

---

## Nivel 3: Contadores con CI

### Problema 3.1
Usando el 74LS163:
- a) Diseñar contador módulo 12
- b) ¿Cómo se detecta el fin de cuenta?
- c) Conexión para carga de valor inicial

### Problema 3.2
Usando el 74LS93:
- a) Configurar como divisor por 16
- b) Configurar como divisor por 12
- c) ¿Por qué no se puede hacer divisor por 15 fácilmente?

### Problema 3.3
Usando el 74LS193:
- a) Diseñar contador up/down de 0 a 9
- b) ¿Qué señales indican overflow/underflow?
- c) Conexión para cascada de dos contadores

---

## Nivel 4: Contadores Especiales

### Problema 4.1
Diseñar un contador de anillo de 4 bits:
- a) Diagrama del circuito
- b) Secuencia de estados
- c) Circuito de inicialización

### Problema 4.2
Diseñar un contador Johnson de 3 bits:
- a) Secuencia completa de estados
- b) ¿Cuántos estados válidos tiene?
- c) Decodificación para cada estado

### Problema 4.3
Diseñar un contador que siga la secuencia: 0, 2, 4, 6, 0, 2, ...
- a) Diagrama de estados
- b) Implementación con flip-flops D
- c) ¿Es esto un contador módulo 4?

---

## Nivel 5: Contadores Bidireccionales

### Problema 5.1
Diseñar un contador up/down de 3 bits con señal de control DIR:
- a) DIR=1 → cuenta arriba
- b) DIR=0 → cuenta abajo
- c) Implementar con flip-flops JK

### Problema 5.2
Un contador debe contar en la secuencia:
- UP: 0→1→3→7→0
- DOWN: 7→3→1→0→7

Diseñar el circuito completo.

### Problema 5.3
Modificar el 74LS163 para contar de 5 a 12:
- a) ¿Qué valor se carga?
- b) ¿Cuándo se detecta el fin?
- c) Diagrama de conexiones

---

## Nivel 6: Registros de Desplazamiento

### Problema 6.1
Para un registro de desplazamiento de 4 bits:
- a) Si la entrada es 1011 (serial, MSB primero), ¿cuál es la salida paralela después de 4 CLK?
- b) Dibujar diagrama de tiempos
- c) ¿Cuántos ciclos para recibir un byte?

### Problema 6.2
Usando el 74LS164 (8-bit SIPO):
- a) Conexión para recibir datos seriales
- b) ¿Para qué sirven las dos entradas A y B?
- c) Diseñar receptor serial de 8 bits con señal "dato listo"

### Problema 6.3
Usando el 74LS165 (8-bit PISO):
- a) Conexión para transmitir datos paralelos en serial
- b) Secuencia de señales de control
- c) ¿Cuántos ciclos para enviar un byte?

---

## Nivel 7: Registros Bidireccionales

### Problema 7.1
Usando el 74LS194:
- a) Configurar para shift right
- b) Configurar para shift left
- c) Diseñar multiplicador por 2 (shift left) y divisor por 2 (shift right)

### Problema 7.2
Diseñar un registro universal de 4 bits con:
- Modo 0: Mantener
- Modo 1: Shift Right
- Modo 2: Shift Left
- Modo 3: Carga paralela

Implementar con flip-flops D y MUX.

### Problema 7.3
Con el 74LS194, crear un generador de secuencia que produzca:
0001 → 0010 → 0100 → 1000 → 0001...

(contador de anillo)

---

## Nivel 8: Divisores de Frecuencia

### Problema 8.1
Diseñar un divisor de frecuencia de 10 MHz a:
- a) 1 MHz
- b) 100 kHz
- c) 1 Hz

### Problema 8.2
Un cristal de 32.768 kHz debe generar 1 Hz:
- a) ¿Por qué se usa esta frecuencia? (Pista: $2^{15}$)
- b) Diseñar el divisor
- c) ¿Cuántos flip-flops se necesitan?

### Problema 8.3
Generar una señal de 60 Hz a partir de 1 MHz:
- a) Factor de división necesario
- b) Diseño con contadores en cascada
- c) Verificar que 1000000/60 ≈ 16667

---

## Nivel 9: Aplicaciones

### Problema 9.1: Reloj Digital
Diseñar la lógica de un reloj digital que cuente:
- Segundos: 0-59
- Minutos: 0-59
- Horas: 0-23

Especificar:
- Contadores necesarios
- Conexiones en cascada
- Señales de carry

### Problema 9.2: Medidor de Frecuencia
Diseñar un frecuencímetro simple:
- Entrada: señal de frecuencia desconocida
- Base de tiempo: 1 segundo
- Salida: contador de pulsos

### Problema 9.3: Generador de PWM
Usando un contador y comparador:
- a) Generar PWM con ciclo de trabajo variable
- b) Resolución de 8 bits
- c) Frecuencia PWM de 1 kHz

---

## Nivel 10: Problemas Integradores

### Problema 10.1
Diseñar un transmisor serial:
- 8 bits de datos
- 1 bit de start (0)
- 1 bit de stop (1)
- Baudrate: 9600

Incluir:
- Registro de desplazamiento
- Contador de bits
- Control de transmisión

### Problema 10.2
Diseñar un contador de eventos con display:
- Cuenta de 0 a 9999
- 4 dígitos BCD
- Botón de reset
- Retención del último valor

### Problema 10.3
Diseñar un secuenciador de 8 pasos:
- Cada paso activa una salida diferente
- Control de avance manual y automático
- Modo cíclico o single-shot

---

<!-- IA_CONTEXT
PROPÓSITO: Banco de ejercicios para contadores y registros
RESPUESTAS: Ver archivo solutions/DD-06-Respuestas.md
HERRAMIENTAS: LogiSim, Digital
-->
