<!--
::METADATA::
type: theory
topic_id: mcu-01-arquitectura
file_id: teoria-arquitectura-mcu
status: draft
audience: both
last_updated: 2026-01-02
difficulty: 1
tags: [microcontrolador, arquitectura, CPU, memoria, periféricos]
search_keywords: "microcontrolador, MCU, arquitectura, CPU, ALU, memoria"
-->

> 🏠 **Navegación:** [← Volver al Índice](../03-01-Intro.md) | [Métodos →](../methods/MCU-01-Metodos-Arquitectura.md)

---

# Arquitectura de Microcontroladores

## 1. Introducción

### 1.1 ¿Qué es un Microcontrolador?

Un **microcontrolador (MCU)** es un circuito integrado que contiene:
- Procesador (CPU)
- Memoria (RAM, ROM/Flash)
- Periféricos (I/O, Timers, ADC, etc.)
- Bus interno

Todo en un **único chip**, diseñado para aplicaciones embebidas.

### 1.2 Microcontrolador vs Microprocesador

| Característica | Microcontrolador | Microprocesador |
|----------------|------------------|-----------------|
| Memoria | Integrada | Externa |
| Periféricos | Integrados | Externos |
| Costo | Bajo | Alto |
| Consumo | Bajo | Alto |
| Aplicación | Embebida/Control | Computación general |
| Ejemplo | PIC, AVR, STM32 | Intel Core, ARM Cortex-A |

---

## 2. Arquitecturas de Computadores

### 2.1 Arquitectura Von Neumann

```
┌─────────────────────────────────────────────────┐
│                     CPU                         │
│  ┌───────────┐         ┌──────────────────┐   │
│  │    ALU    │◄───────▶│    Registros     │   │
│  └───────────┘         └──────────────────┘   │
│        ▲                       ▲               │
│        └───────────┬───────────┘               │
│                    ▼                           │
│           ┌──────────────┐                     │
│           │ Unidad de    │                     │
│           │ Control      │                     │
│           └──────────────┘                     │
└────────────────────┬────────────────────────────┘
                     │ Bus Único
                     ▼
            ┌──────────────┐
            │   Memoria    │
            │ (Programa +  │
            │   Datos)     │
            └──────────────┘
```

**Características:**
- Bus único para instrucciones y datos
- Memoria compartida
- Cuello de botella de Von Neumann

### 2.2 Arquitectura Harvard

```
┌─────────────────────────────────────────────────┐
│                     CPU                         │
│  ┌───────────┐         ┌──────────────────┐   │
│  │    ALU    │◄───────▶│    Registros     │   │
│  └───────────┘         └──────────────────┘   │
└────────┬───────────────────────┬────────────────┘
         │ Bus de               │ Bus de
         │ Instrucciones        │ Datos
         ▼                      ▼
┌──────────────┐        ┌──────────────┐
│   Memoria    │        │   Memoria    │
│   Programa   │        │    Datos     │
│   (Flash)    │        │    (RAM)     │
└──────────────┘        └──────────────┘
```

**Características:**
- Buses separados
- Acceso simultáneo a programa y datos
- Mayor rendimiento
- Usada en la mayoría de MCUs

### 2.3 Harvard Modificada

Combinación práctica:
- Buses separados internamente
- Interfaz externa unificada
- Permite ejecutar código desde RAM

---

## 3. Componentes de un MCU

### 3.1 Unidad Central de Proceso (CPU)

#### ALU (Unidad Aritmético-Lógica)
```
         ┌───────────────┐
Operando A ──▶│               │
              │     ALU      │──▶ Resultado
Operando B ──▶│               │
              └───────┬───────┘
                      │
                      ▼
                   Flags
              (Z, C, N, V)
```

Operaciones:
- **Aritméticas:** ADD, SUB, MUL, DIV
- **Lógicas:** AND, OR, XOR, NOT
- **Desplazamiento:** LSL, LSR, ROL, ROR
- **Comparación:** CMP, TST

#### Registros

| Tipo | Función | Ejemplo |
|------|---------|---------|
| Acumulador | Operaciones ALU | A, W |
| Índice | Direccionamiento | X, Y, Z |
| Puntero de pila | Gestión de pila | SP |
| Contador de programa | Dirección instrucción | PC |
| Estado | Flags de resultado | STATUS, SREG |

#### Unidad de Control

Decodifica instrucciones y genera señales de control:
1. Fetch (buscar instrucción)
2. Decode (decodificar)
3. Execute (ejecutar)
4. Write-back (escribir resultado)

### 3.2 Memoria

#### Tipos de Memoria en MCU

| Tipo | Volatilidad | Uso | Tecnología |
|------|-------------|-----|------------|
| Flash | No volátil | Programa | EEPROM mejorada |
| RAM | Volátil | Datos | SRAM |
| EEPROM | No volátil | Configuración | EEPROM |
| Registros | Volátil | Trabajo CPU | Flip-flops |

#### Mapa de Memoria (Ejemplo AVR)

```
0x0000 ┌──────────────────┐
       │    Registros     │ 32 registros (R0-R31)
0x0020 ├──────────────────┤
       │   I/O Registers  │ 64 registros I/O
0x0060 ├──────────────────┤
       │  Extended I/O    │ Registros adicionales
0x0100 ├──────────────────┤
       │                  │
       │      SRAM        │ Datos
       │                  │
       └──────────────────┘

Flash (separado):
0x0000 ┌──────────────────┐
       │    Vectores de   │
       │   Interrupción   │
       ├──────────────────┤
       │                  │
       │  Código Programa │
       │                  │
       └──────────────────┘
```

### 3.3 Bus del Sistema

```
┌─────────────────────────────────────────────────────────┐
│                    BUS DE DATOS                         │
│  ◄──────────────────────────────────────────────────►  │
└─────────────────────────────────────────────────────────┘
     ▲           ▲           ▲           ▲
     │           │           │           │
┌────┴────┐ ┌────┴────┐ ┌────┴────┐ ┌────┴────┐
│   CPU   │ │  Flash  │ │   RAM   │ │Periféricos│
└────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘
     │           │           │           │
     ▼           ▼           ▼           ▼
┌─────────────────────────────────────────────────────────┐
│                  BUS DE DIRECCIONES                     │
│  ──────────────────────────────────────────────────►   │
└─────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────┐
│                  BUS DE CONTROL                         │
│  (RD, WR, CLK, RESET, etc.)                            │
└─────────────────────────────────────────────────────────┘
```

---

## 4. Sistema de Reloj

### 4.1 Fuentes de Reloj

| Fuente | Precisión | Velocidad | Uso |
|--------|-----------|-----------|-----|
| RC interno | ±1-10% | 1-8 MHz | General |
| Cristal externo | ±20 ppm | 1-20 MHz | Precisión |
| Resonador cerámico | ±0.5% | 1-20 MHz | Balance |
| PLL | Variable | Hasta GHz | Alta velocidad |

### 4.2 Distribución de Reloj

```
                    ┌─────────┐
   Cristal ────────▶│ Oscilador│
                    └────┬────┘
                         │
                         ▼
                    ┌─────────┐
                    │   PLL   │ (opcional)
                    └────┬────┘
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
         ┌────────┐ ┌────────┐ ┌────────┐
         │ /1     │ │ /2     │ │ /4     │ Prescalers
         └───┬────┘ └───┬────┘ └───┬────┘
             │          │          │
             ▼          ▼          ▼
           CPU      Periféricos  Timers
```

### 4.3 Modos de Bajo Consumo

| Modo | CPU | Periféricos | Reloj | Despertar |
|------|-----|-------------|-------|-----------|
| Run | ON | ON | ON | - |
| Idle | OFF | ON | ON | Cualquier INT |
| Sleep | OFF | Algunos | Reducido | INT específicas |
| Power-down | OFF | OFF | OFF | Reset, WDT, INT ext |

---

## 5. Periféricos Integrados

### 5.1 Periféricos Comunes

```
┌─────────────────────────────────────────────────────────┐
│                    MICROCONTROLADOR                     │
│                                                         │
│  ┌─────┐  ┌─────────┐  ┌─────────┐  ┌──────────────┐  │
│  │ CPU │  │  Flash  │  │  SRAM   │  │   Periféricos │  │
│  └──┬──┘  └─────────┘  └─────────┘  └──────┬───────┘  │
│     │                                       │          │
│     └───────────────────────────────────────┘          │
│                         │                              │
│     ┌───────────────────┼───────────────────┐         │
│     │         │         │         │         │         │
│  ┌──┴──┐  ┌──┴──┐  ┌───┴──┐  ┌──┴──┐  ┌──┴──┐      │
│  │GPIO │  │Timer│  │ UART │  │ ADC │  │ I2C │      │
│  └──┬──┘  └──┬──┘  └───┬──┘  └──┬──┘  └──┬──┘      │
└─────┼───────┼─────────┼───────┼────────┼───────────┘
      │       │         │       │        │
      ▼       ▼         ▼       ▼        ▼
   Pines    PWM       TX/RX   Analog   SCL/SDA
```

### 5.2 Tabla de Periféricos

| Periférico | Función | Aplicación |
|------------|---------|------------|
| GPIO | Entrada/Salida digital | LEDs, botones |
| Timer/Counter | Temporización, conteo | PWM, delays |
| UART | Comunicación serial | Terminal, módems |
| SPI | Bus serial síncrono | SD card, displays |
| I2C/TWI | Bus serial 2 hilos | Sensores, EEPROM |
| ADC | Conversión A/D | Sensores analógicos |
| DAC | Conversión D/A | Audio, control |
| PWM | Modulación de ancho | Motores, LEDs |
| WDT | Watchdog timer | Recuperación errores |

---

## 6. Familias Populares de MCU

### 6.1 Comparación

| Familia | Arquitectura | Bits | Fabricante | Características |
|---------|--------------|------|------------|-----------------|
| AVR | Harvard | 8 | Microchip | Simple, Arduino |
| PIC | Harvard | 8/16/32 | Microchip | Amplia gama |
| STM32 | ARM Cortex-M | 32 | ST | Alto rendimiento |
| ESP32 | Xtensa/RISC-V | 32 | Espressif | WiFi/Bluetooth |
| MSP430 | Von Neumann | 16 | TI | Ultra bajo consumo |

### 6.2 Arquitectura ARM Cortex-M

```
┌──────────────────────────────────────────────────────┐
│                  ARM Cortex-M Core                   │
│  ┌────────────────────────────────────────────────┐ │
│  │  ┌───────┐  ┌──────────┐  ┌────────────────┐  │ │
│  │  │ CPU   │  │ NVIC     │  │ Debug/Trace    │  │ │
│  │  │ (ALU, │  │ (Nested  │  │ (SWD, JTAG)    │  │ │
│  │  │ Regs) │  │ Vectored │  │                │  │ │
│  │  └───────┘  │ Int Ctrl)│  └────────────────┘  │ │
│  │             └──────────┘                       │ │
│  └────────────────────┬───────────────────────────┘ │
│                       │ Bus Matrix                   │
│  ┌────────────────────┼────────────────────────────┐│
│  │      │      │      │      │      │      │       ││
│  ▼      ▼      ▼      ▼      ▼      ▼      ▼       ││
│ Flash  SRAM  GPIO  Timers  UART   ADC   DMA       ││
└──────────────────────────────────────────────────────┘
```

---

## 7. Ciclo de Desarrollo

### 7.1 Flujo de Desarrollo

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Escribir   │───▶│  Compilar   │───▶│   Enlazar   │
│   Código    │    │  (Assembler/│    │   (Linker)  │
│   (C/ASM)   │    │   Compiler) │    │             │
└─────────────┘    └─────────────┘    └──────┬──────┘
                                             │
                                             ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Depurar   │◀───│  Programar  │◀───│   Generar   │
│  (Debug)    │    │    MCU      │    │   .hex/.bin │
└─────────────┘    └─────────────┘    └─────────────┘
```

### 7.2 Herramientas

| Herramienta | Función | Ejemplos |
|-------------|---------|----------|
| IDE | Entorno integrado | MPLAB X, Keil, STM32CubeIDE |
| Compilador | C a código máquina | XC8, GCC-ARM, avr-gcc |
| Programador | Cargar código | PICkit, ST-Link, USBasp |
| Debugger | Depuración | JTAG, SWD |

---

## Referencias

- Mazidi, M.A. *The AVR Microcontroller and Embedded Systems*
- Yiu, J. *The Definitive Guide to ARM Cortex-M*
- Datasheets de fabricantes (Microchip, ST, Espressif)

---

<!-- IA_CONTEXT
NIVEL: Básico (1/3)
PREREQUISITOS: Electrónica digital básica
CONEXIONES: Base para todos los temas de MCU
ERRORES_COMUNES: Confundir MCU con CPU, ignorar mapa de memoria
-->
