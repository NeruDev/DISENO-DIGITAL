<!--
::METADATA::
type: method
topic_id: mcu-01-arquitectura
file_id: metodos-arquitectura-mcu
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [microcontrolador, metodología, selección, arquitectura]
search_keywords: "metodología, selección MCU, arquitectura"
-->

> 🏠 **Navegación:** [← Teoría](../theory/MCU-01-Teoria-ArquitecturaMCU.md) | [Problemas →](../problems/MCU-01-Problemas.md)

---

# Métodos: Arquitectura de Microcontroladores

## Método 1: Selección de Microcontrolador

### Paso 1: Definir Requisitos

| Criterio | Preguntas Clave |
|----------|-----------------|
| **I/O** | ¿Cuántos pines digitales? ¿Analógicos? |
| **Velocidad** | ¿Qué frecuencia de CPU necesito? |
| **Memoria** | ¿Cuánta Flash para código? ¿RAM para datos? |
| **Periféricos** | ¿UART? ¿SPI? ¿I2C? ¿ADC? ¿PWM? |
| **Consumo** | ¿Funciona con batería? |
| **Costo** | ¿Producción masiva o prototipo? |

### Paso 2: Tabla de Comparación

```
Proyecto: Control de motor con sensor de temperatura

| Requisito        | PIC16F | ATmega328 | STM32F0 |
|------------------|--------|-----------|---------|
| GPIO (mín. 8)    | 15 ✓   | 23 ✓      | 32 ✓    |
| ADC (mín. 2)     | 8 ✓    | 6 ✓       | 10 ✓    |
| PWM (mín. 1)     | 2 ✓    | 6 ✓       | 8 ✓     |
| UART (mín. 1)    | 1 ✓    | 1 ✓       | 2 ✓     |
| Flash (mín. 8K)  | 14K ✓  | 32K ✓     | 64K ✓   |
| Precio           | $1.50  | $2.00     | $2.50   |
| Disponibilidad   | Alta   | Alta      | Media   |
| Ecosistema       | MPLAB  | Arduino   | STM32Cube|
```

### Paso 3: Decisión

Elegir basándose en:
1. Cumple todos los requisitos mínimos
2. Margen de seguridad (20-30% extra)
3. Disponibilidad de herramientas
4. Experiencia previa del equipo

---

## Método 2: Lectura de Datasheet

### Secciones Clave

1. **Features** (primera página)
   - Resumen rápido de capacidades

2. **Pin Diagram/Pinout**
   - Identificar pines de alimentación
   - Pines de I/O y funciones alternativas

3. **Memory Map**
   - Direcciones de registros
   - Tamaño de memoria

4. **Electrical Characteristics**
   - Voltajes de operación
   - Corrientes máximas
   - Consumo de energía

5. **Peripheral Registers**
   - Configuración de cada periférico

### Ejemplo: Extraer Información

```
Tarea: Configurar UART a 9600 baud con cristal de 16 MHz

1. Buscar sección "USART" o "Serial Communication"
2. Encontrar fórmula de baud rate:
   UBRR = (F_CPU / (16 * BAUD)) - 1
   UBRR = (16000000 / (16 * 9600)) - 1 = 103

3. Identificar registros:
   - UBRRnH, UBRRnL: Valor de baud
   - UCSRnB: Habilitar TX/RX
   - UCSRnC: Formato de frame
```

---

## Método 3: Calcular Recursos de Memoria

### Estimación de Flash (Código)

```
Regla general para C embebido:

Componente               | Tamaño estimado
-------------------------|----------------
Código de inicio         | 200-500 bytes
Librería printf          | 2-4 KB
Librería matemática      | 1-2 KB
Driver de periférico     | 100-500 bytes c/u
Código de aplicación     | Variable
Tablas/constantes        | Variable
```

### Estimación de RAM (Datos)

```
Componente               | Tamaño
-------------------------|----------------
Stack                    | 50-200 bytes
Variables globales       | Contar en código
Buffers de comunicación  | 2 × tamaño buffer
Variables locales        | En stack
```

### Fórmula de Verificación

```
Memoria usada ≤ 80% de memoria disponible

Flash: código_total < 0.8 × Flash_disponible
RAM: variables + stack < 0.8 × RAM_disponible
```

---

## Método 4: Configuración de Reloj

### Paso 1: Determinar Frecuencia Necesaria

```
Frecuencia mínima basada en:
1. Baud rate de comunicación: F_CPU ≥ 16 × BAUD (para UART)
2. Frecuencia de muestreo ADC: F_CPU ≥ 50 × F_sample
3. Frecuencia de PWM: F_CPU ≥ Resolución × F_PWM
4. Tiempo de respuesta requerido
```

### Paso 2: Seleccionar Fuente

| Necesidad | Fuente Recomendada |
|-----------|-------------------|
| Bajo costo, tolerante | RC interno |
| Comunicación serial | Cristal externo |
| USB | Cristal 8/16/48 MHz |
| RTC preciso | Cristal 32.768 kHz |
| Máxima velocidad | PLL desde cristal |

### Paso 3: Calcular Prescalers

```c
// Ejemplo: STM32 con cristal de 8 MHz, necesito 72 MHz
// HSE = 8 MHz
// PLL multiplier = 9
// F_CPU = 8 MHz × 9 = 72 MHz

// Para periférico que necesita 36 MHz:
// APB prescaler = 2
// F_periph = 72 MHz / 2 = 36 MHz
```

---

## Método 5: Análisis de Consumo de Energía

### Calcular Consumo Total

```
I_total = I_CPU + Σ I_periféricos + I_externo

Ejemplo:
- CPU activa @ 8 MHz: 5 mA
- ADC activo: 0.5 mA
- UART activo: 0.3 mA
- LED (20 mA × 2): 40 mA
- Total: 45.8 mA
```

### Calcular Duración de Batería

```
Duración (horas) = Capacidad_batería (mAh) / I_promedio (mA)

Ejemplo:
- Batería: 2000 mAh
- Consumo promedio: 50 mA
- Duración = 2000 / 50 = 40 horas
```

### Optimizar Consumo

1. Reducir frecuencia de CPU
2. Usar modos de bajo consumo
3. Apagar periféricos no usados
4. Minimizar tiempo activo (duty cycle)

---

## Método 6: Diseño del Mapa de Pines

### Plantilla de Asignación

```
MCU: ATmega328P (28 pines)

Pin | Nombre   | Función Asignada  | Notas
----|----------|-------------------|-------
1   | PC6/RESET| Reset             | Pullup externo
2   | PD0/RXD  | UART RX           | Comunicación
3   | PD1/TXD  | UART TX           | Comunicación
4   | PD2/INT0 | Botón             | Interrupción
5   | PD3/OC2B | PWM Motor         | Timer2
6   | PD4      | LED Status        | Salida
7   | VCC      | +5V               | Bypass cap
8   | GND      | Tierra            | 
...
```

### Reglas de Asignación

1. **Funciones especiales primero:** UART, I2C, SPI en pines dedicados
2. **Entradas analógicas:** Solo pines ADC
3. **PWM:** Solo pines con Timer/OC
4. **Interrupciones:** Pines INTx o PCINT
5. **Dejar pines libres:** Para expansión futura

---

## Método 7: Estructura de Proyecto Embebido

### Organización de Archivos

```
proyecto/
├── src/
│   ├── main.c           # Punto de entrada
│   ├── init.c           # Inicialización
│   ├── gpio.c           # Driver GPIO
│   ├── uart.c           # Driver UART
│   └── adc.c            # Driver ADC
├── inc/
│   ├── config.h         # Configuración global
│   ├── gpio.h           # Header GPIO
│   ├── uart.h           # Header UART
│   └── adc.h            # Header ADC
├── lib/                 # Librerías externas
├── build/               # Archivos compilados
└── Makefile            # Script de compilación
```

### Plantilla main.c

```c
#include "config.h"
#include "gpio.h"
#include "uart.h"

int main(void) {
    // 1. Inicializar sistema
    system_init();
    
    // 2. Inicializar periféricos
    gpio_init();
    uart_init(9600);
    
    // 3. Bucle principal
    while (1) {
        // Código de aplicación
        
        // Opcional: modo bajo consumo
        // sleep_mode();
    }
    
    return 0;  // Nunca llega aquí
}
```

---

## Método 8: Debug Básico

### Técnicas sin Debugger

1. **LED de estado**
   ```c
   // Parpadeo indica que llega a ese punto
   LED_TOGGLE();
   _delay_ms(100);
   ```

2. **UART para printf**
   ```c
   printf("Variable x = %d\n", x);
   ```

3. **Pin de test**
   ```c
   // Medir con osciloscopio
   DEBUG_PIN_HIGH();
   // código a medir
   DEBUG_PIN_LOW();
   ```

### Con Debugger (JTAG/SWD)

1. Breakpoints
2. Inspección de variables
3. Ejecución paso a paso
4. Visualización de registros

---

## Método 9: Checklist de Hardware

### Antes de Diseñar PCB

- [ ] Capacitores de bypass en VCC (100nF cerca del pin)
- [ ] Capacitor de filtro en AVCC (para ADC)
- [ ] Resistor de pullup en RESET
- [ ] Cristal con capacitores de carga correctos
- [ ] Protección ESD en pines expuestos
- [ ] Conector de programación accesible
- [ ] LEDs de status (power, actividad)
- [ ] Puntos de test para debug

### Circuito Mínimo (AVR)

```
         VCC
          │
          ├─── 10kΩ ───┐
          │            │
    ┌─────┴─────┐      │
    │    AVR    │      │
    │           ├──────┘ RESET
    │    VCC ───┼─── VCC
    │    GND ───┼─── GND
    │    AVCC ──┼─── VCC (con filtro LC)
    │           │
    │  XTAL1 ───┼───┬──[Crystal]──┬─── GND
    │  XTAL2 ───┼───┤             │
    │           │   ├── 22pF ─────┤
    │           │   └── 22pF ─────┘
    └───────────┘
```

---

## Método 10: Documentación de Proyecto

### Información a Documentar

1. **Descripción del sistema**
2. **Diagrama de bloques**
3. **Lista de materiales (BOM)**
4. **Esquemático**
5. **Mapa de pines**
6. **Diagrama de flujo del software**
7. **Protocolo de comunicación**
8. **Procedimiento de programación**
9. **Procedimiento de pruebas**

---

<!-- IA_CONTEXT
USO: Métodos prácticos para trabajar con arquitectura de MCU
NIVEL: Básico (1/3)
HERRAMIENTAS: Datasheets, IDE (MPLAB, Arduino, STM32CubeIDE)
-->
