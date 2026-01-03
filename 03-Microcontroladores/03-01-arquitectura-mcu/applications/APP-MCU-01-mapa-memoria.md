# 🔧 Aplicación: Explorador de Mapa de Memoria (PIC16F887)

```
::METADATA::
tipo: aplicacion
tema: MCU-01-arquitectura-mcu
dificultad: basica
objetivo: Comprender la organización de memoria y los SFR clave
::END::
```

## 📋 Descripción del Proyecto

Construir un programa en C que muestre, vía UART, las secciones de memoria del PIC16F887 (PROG, RAM, EEPROM) y los SFR esenciales, ayudando a visualizar la arquitectura Harvard y el mapa de memoria.

## 🎯 Objetivos de Aprendizaje

- Identificar bancos de RAM y SFR
- Leer y presentar contenido de registros clave (STATUS, INTCON, OSCCON)
- Usar punteros para recorrer RAM/EEPROM
- Enviar información formateada por UART

## 🛠️ Pasos Clave

1) Configurar reloj interno a 8 MHz.
2) Inicializar UART a 9600 bps.
3) Leer SFR principales y mostrarlos (hex).
4) Recorrer primera página de RAM (0x20-0x7F) y mostrar 16 bytes por línea.
5) Leer 16 bytes de EEPROM y mostrarlos.

## 🧩 Código Base (fragmento)

```c
#include <xc.h>
#include <stdint.h>
#include "uart.h"  // inicialización simple

void print_hex(uint8_t v);

void dump_ram(uint8_t start, uint8_t end) {
    for (uint8_t addr = start; addr <= end; addr++) {
        if ((addr - start) % 16 == 0) uart_puts("\r\n");
        print_hex(*((volatile uint8_t*)addr));
        uart_puts(" ");
    }
}

void main(void) {
    OSCCON = 0b01110010; // 8 MHz
    uart_init(9600);

    uart_puts("STATUS="); print_hex(STATUS);
    uart_puts(" INTCON="); print_hex(INTCON);
    uart_puts(" OSCCON="); print_hex(OSCCON);
    uart_puts("\r\nRAM 0x20-0x7F:");
    dump_ram(0x20, 0x7F);

    uart_puts("\r\nEEPROM 0x00-0x0F:");
    for (uint8_t i=0; i<16; i++) {
        EEADR = i; EECON1bits.RD = 1; // leer EEPROM
        print_hex(EEDATA); uart_puts(" ");
    }

    while(1);
}
```

## ✅ Checklist

- [x] UART inicializada
- [x] Lectura de SFR (STATUS/INTCON/OSCCON)
- [x] Dump de RAM (banco 0)
- [x] Dump de EEPROM (16 bytes)
- [x] Salida formateada en terminal

## 🔗 Referencias

- [MCU-01-Teoria-ArquitecturaMCU.md](../theory/MCU-01-Teoria-ArquitecturaMCU.md)
- Datasheet PIC16F887, secciones de memoria y SFR
