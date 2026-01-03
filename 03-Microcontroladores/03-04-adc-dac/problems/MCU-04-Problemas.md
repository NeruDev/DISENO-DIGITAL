<!--
::METADATA::
type: problem
topic_id: mcu-04-adc-dac
file_id: problemas-adc
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 2
tags: [ejercicios, microcontrolador, ADC, DAC, sensores]
search_keywords: "ejercicios, problemas, ADC, conversión"
-->

> 🏠 **Navegación:** [← Métodos](../methods/MCU-04-Metodos-ADC.md) | [Respuestas →](../solutions/MCU-04-Respuestas.md)

---

# Problemas: ADC y DAC

## Nivel 1: Conceptos Básicos

### Problema 1.1
¿Qué significa que un ADC tiene resolución de 10 bits?

### Problema 1.2
¿Cuál es la diferencia entre ADC y DAC?

### Problema 1.3
Si V_REF = 5V y el ADC es de 10 bits, ¿cuál es el valor del LSB?

---

## Nivel 2: Cálculos de Conversión

### Problema 2.1
Con un ADC de 10 bits y V_REF = 5V:
- ¿Qué valor digital produce una entrada de 2.5V?
- ¿Qué voltaje representa el valor digital 768?

### Problema 2.2
Un ADC de 12 bits con V_REF = 3.3V:
- Calcula el LSB en mV
- ¿Qué rango de voltaje representa el código 1000?

### Problema 2.3
¿Cuántos niveles de cuantización tiene un ADC de 8 bits?

---

## Nivel 3: Configuración de ADC (AVR)

### Problema 3.1
Escribe el código para configurar el ADC con:
- Referencia AVCC (5V)
- Prescaler /128
- Canal 0

### Problema 3.2
¿Qué bits debes configurar para usar la referencia interna de 1.1V?

### Problema 3.3
¿Por qué el prescaler del ADC debe dar una frecuencia entre 50-200 kHz?

---

## Nivel 4: Lectura de Sensores

### Problema 4.1
El sensor LM35 produce 10mV/°C. Si el ADC lee 150 con V_REF=5V:
- ¿Qué temperatura está midiendo?

### Problema 4.2
Un potenciómetro de 10kΩ está conectado como divisor de voltaje entre VCC y GND. Si el ADC lee 512:
- ¿En qué posición está el potenciómetro?
- ¿Cuál es la resistencia al cursor?

### Problema 4.3
Diseña un circuito para leer un sensor que produce 0-10V con un ADC de 0-5V.

---

## Nivel 5: Filtrado y Promediado

### Problema 5.1
¿Por qué es necesario promediar múltiples lecturas del ADC?

### Problema 5.2
Implementa una función que tome 16 muestras y retorne el promedio, descartando las 2 lecturas más altas y las 2 más bajas.

### Problema 5.3
¿Qué es un filtro de media móvil y cuándo se usa con ADC?

---

## Nivel 6: PWM como DAC

### Problema 6.1
¿Cómo se puede usar PWM como sustituto de un DAC?

### Problema 6.2
Si tienes PWM de 8 bits a 62.5 kHz:
- ¿Qué valores de R y C usarías para un filtro RC que elimine el ripple?

### Problema 6.3
Diseña un sistema que genere 2.5V usando PWM con filtro RC.

---

## Nivel 7: Aplicaciones de Sensores

### Problema 7.1
Diseña un termómetro digital:
- Sensor LM35
- Display de 2 dígitos
- Rango 0-99°C

### Problema 7.2
Implementa un medidor de luz:
- LDR con resistencia de 10kΩ
- PWM para ajustar brillo de LED inversamente proporcional

### Problema 7.3
Diseña un voltímetro 0-20V:
- Divisor de voltaje apropiado
- Display muestra voltaje con 1 decimal

---

## Nivel 8: Conversión y Calibración

### Problema 8.1
¿Cómo calibrarías un sensor de temperatura si conoces dos puntos de referencia (hielo 0°C y agua hirviendo 100°C)?

### Problema 8.2
Un sensor de presión tiene salida 0.5-4.5V para 0-100 PSI. Escribe función que convierta lectura ADC a PSI.

### Problema 8.3
Implementa detección de umbral con histéresis para un sensor de temperatura:
- Umbral: 30°C
- Histéresis: ±2°C
- Activar ventilador cuando supera umbral

---

## Nivel 9: Optimización y Ruido

### Problema 9.1
¿Qué técnicas se usan para reducir el ruido en las lecturas del ADC?

### Problema 9.2
¿Qué hace el registro DIDR0 y cuándo se debe usar?

### Problema 9.3
Diseña un sistema de adquisición de audio de baja calidad:
- Tasa de muestreo: 8 kHz
- Resolución: 8 bits
- Almacenamiento en buffer circular

---

## Nivel 10: Proyectos Integradores

### Problema 10.1
Diseña un datalogger de temperatura:
- Lectura cada segundo
- Almacena en EEPROM
- Transmite por UART cuando se solicita

### Problema 10.2
Implementa un controlador de carga de batería LiPo:
- Monitorea voltaje de batería (0-4.2V)
- Control de corriente de carga con PWM
- LED indica estado de carga

### Problema 10.3
Diseña un osciloscopio simple:
- Muestreo hasta 10 kHz
- Trigger por nivel
- Envía datos por UART para visualizar en PC

---

<!-- IA_CONTEXT
PROPÓSITO: Ejercicios sobre ADC y DAC
RESPUESTAS: Ver archivo solutions/MCU-04-Respuestas.md
HERRAMIENTAS: AVR-GCC, multímetro, osciloscopio
-->
