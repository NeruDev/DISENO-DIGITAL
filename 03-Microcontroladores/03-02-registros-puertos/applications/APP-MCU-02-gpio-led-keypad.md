# 🔧 Aplicación: Control de LEDs y Keypad 4x4 (GPIO)

```
::METADATA::
tipo: aplicacion
tema: MCU-02-registros-puertos
dificultad: basica
objetivo: Practicar TRIS/PORT/LAT con entrada de keypad y salida a LEDs
::END::
```

## 📋 Descripción del Proyecto

Implementar lectura de un keypad 4x4 usando escaneo por filas/columnas y mostrar el código de tecla en un conjunto de 4 LEDs (binario) y en UART.

## 🎯 Objetivos de Aprendizaje

- Configurar TRIS/ANSEL para entradas y salidas digitales
- Usar LATx para escritura y PORTx para lectura
- Aplicar antirrebote por software
- Multiplexar filas/columnas para detectar teclas

## 🛠️ Pasos Clave

1) Fijar filas como salidas (LATx) y columnas como entradas con pull-up.
2) Escanear: poner una fila en 0, leer columnas; repetir por cada fila.
3) Debounce simple: confirmar la misma lectura N veces.
4) Traducir fila/columna a código 0-15 y mostrar en LEDs (PORTB<3:0>).
5) Enviar el valor por UART para monitoreo.

## 🧩 Código Base (fragmento)

```c
// Asume keypad en RA0-RA3 (filas) y RA4-RA7 (columnas)
#define ROW_PORT  LATA
#define ROW_TRIS  TRISA
#define COL_PORT  PORTA
#define COL_TRIS  TRISA

const uint8_t key_map[4][4] = {
    {1, 2, 3, 0xA},
    {4, 5, 6, 0xB},
    {7, 8, 9, 0xC},
    {0xE,0, 0xF,0xD}
};

uint8_t scan_key(void) {
    for (uint8_t r=0; r<4; r++) {
        ROW_PORT = ~(1 << r);      // fila activa en 0
        __nop(); __nop();          // pequeño delay
        uint8_t cols = (~COL_PORT >> 4) & 0x0F; // columnas activas en 0
        if (cols) {
            for (uint8_t c=0; c<4; c++) {
                if (cols & (1 << c)) return key_map[r][c];
            }
        }
    }
    return 0xFF; // nada
}
```

## ✅ Checklist

- [x] TRIS/ANSEL configurados
- [x] Escaneo por filas/columnas
- [x] Antirrebote básico
- [x] Salida a LEDs (4 bits)
- [x] Log por UART

## 🔗 Referencias

- [MCU-02-Teoria-RegistrosPuertos.md](../theory/MCU-02-Teoria-RegistrosPuertos.md)
