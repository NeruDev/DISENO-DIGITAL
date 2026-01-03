<!--
::METADATA::
type: solution
topic_id: mcu-02-registros-puertos
file_id: respuestas-gpio
status: draft
audience: student
last_updated: 2026-01-02
difficulty: 1
tags: [respuestas, soluciones, microcontrolador, GPIO]
search_keywords: "respuestas, soluciones, GPIO, puertos"
-->

> 🏠 **Navegación:** [← Problemas](../problems/MCU-02-Problemas.md)

---

# Respuestas: Registros y Puertos GPIO

## Nivel 1: Conceptos Básicos

### Respuesta 1.1
**GPIO = General Purpose Input/Output**

Pines de propósito general que pueden configurarse como entrada o salida digital.

### Respuesta 1.2
Los tres registros por puerto en AVR:
1. **DDRx** - Data Direction Register (configura dirección)
2. **PORTx** - Port Data Register (salida o pull-up)
3. **PINx** - Port Input Register (lectura)

### Respuesta 1.3
Sin pull-up, una entrada desconectada queda "flotante" con valor indefinido (puede ser 0 o 1 aleatoriamente debido a ruido). El pull-up garantiza un estado HIGH definido cuando el botón no está presionado.

---

## Nivel 2: Configuración de Dirección

### Respuesta 2.1

```c
// PB0, PB1, PB2 como salidas
DDRB |= (1 << PB0) | (1 << PB1) | (1 << PB2);
// O: DDRB |= 0b00000111;

// PB3, PB4 como entradas con pull-up
DDRB &= ~((1 << PB3) | (1 << PB4));  // Entrada
PORTB |= (1 << PB3) | (1 << PB4);    // Pull-up

// PB5-PB7 como entradas sin pull-up
DDRB &= ~((1 << PB5) | (1 << PB6) | (1 << PB7));
PORTB &= ~((1 << PB5) | (1 << PB6) | (1 << PB7));

// Forma compacta:
DDRB = 0b00000111;   // 0=entrada, 1=salida
PORTB = 0b00011000;  // Pull-up en PB3, PB4
```

### Respuesta 2.2
```
Pines pares (0,2,4,6) como salidas
Pines impares (1,3,5,7) como entradas

DDRB = 0b01010101 = 0x55
```

### Respuesta 2.3
- DDRx = 0: Pin configurado como **entrada**
- PORTx = 1: **Pull-up interno activado**

El pin tiene una resistencia interna conectada a VCC (~20-50 kΩ).

---

## Nivel 3: Escritura de Salidas

### Respuesta 3.1

```c
// a) PB3 = HIGH
PORTB |= (1 << PB3);

// b) PB3 = LOW
PORTB &= ~(1 << PB3);

// c) Toggle PB3
PORTB ^= (1 << PB3);
// O en AVR moderno (atómico):
PINB = (1 << PB3);
```

### Respuesta 3.2
El problema es que `|=` realiza una operación **read-modify-write**:
1. Lee PORTB
2. Hace OR con la máscara
3. Escribe PORTB

Si una interrupción ocurre entre pasos 1 y 3, y esa ISR modifica PORTB, los cambios de la ISR se perderán.

### Respuesta 3.3
En AVR moderno, escribir a PINx realiza toggle atómico:
```c
PINB = (1 << PB0);  // Toggle atómico de PB0
```

---

## Nivel 4: Lectura de Entradas

### Respuesta 4.1

```c
uint8_t estado = (PIND & (1 << PD2)) ? 1 : 0;

// O más explícito:
uint8_t estado;
if (PIND & (1 << PD2)) {
    estado = 1;
} else {
    estado = 0;
}
```

### Respuesta 4.2
Cuando el botón está presionado, conecta el pin a GND.
- Pull-up activo mantiene el pin en HIGH cuando abierto
- Botón presionado → conecta a GND → **lee 0 (LOW)**

### Respuesta 4.3

```c
void esperar_flanco_subida(void) {
    // Esperar hasta que esté en LOW
    while (PIND & (1 << PD3));
    
    // Esperar hasta que cambie a HIGH
    while (!(PIND & (1 << PD3)));
}
```

---

## Nivel 5: Manipulación de Bits

### Respuesta 5.1

```c
a) PORTB |= 0x0F;    // Set bits 0-3 (OR con 00001111)
b) PORTB &= 0xF0;    // Clear bits 0-3 (AND con 11110000)
c) PORTB ^= 0x55;    // Toggle bits 0,2,4,6 (XOR con 01010101)
d) PORTB = (PORTB & 0xF0) | 0x05;  // Mantener bits 4-7, poner 0101 en bits 0-3
```

### Respuesta 5.2

```c
// Macro para set múltiples bits
#define BITS_SET(reg, mask) ((reg) |= (mask))
#define BITS_CLEAR(reg, mask) ((reg) &= ~(mask))

// Uso:
BITS_SET(PORTB, (1<<PB0)|(1<<PB3)|(1<<PB5));
```

### Respuesta 5.3

```c
// PINC = 0b10110100

a) uint8_t low = PINC & 0x0F;   // = 0b00000100 = 4
b) uint8_t high = (PINC >> 4) & 0x0F;  // = 0b00001011 = 11
c) uint8_t bit5 = (PINC >> 5) & 1;     // = 1
```

---

## Nivel 6: Aplicación LED

### Respuesta 6.1: Luz Viajera

```c
#include <avr/io.h>
#include <util/delay.h>

int main(void) {
    DDRB = 0xFF;  // Todo PORTB como salida
    uint8_t led = 0x01;
    
    while(1) {
        PORTB = led;
        _delay_ms(100);
        led <<= 1;        // Shift izquierda
        if (led == 0) {
            led = 0x01;   // Reiniciar
        }
    }
}
```

### Respuesta 6.2: Luz que Rebota

```c
int main(void) {
    DDRB = 0xFF;
    uint8_t led = 0x01;
    int8_t dir = 1;  // 1 = derecha, -1 = izquierda
    
    while(1) {
        PORTB = led;
        _delay_ms(100);
        
        if (dir == 1) {
            led <<= 1;
            if (led == 0x80) dir = -1;  // Llegó al final
        } else {
            led >>= 1;
            if (led == 0x01) dir = 1;   // Llegó al inicio
        }
    }
}
```

### Respuesta 6.3: Contador Binario

```c
int main(void) {
    DDRB |= 0x0F;  // PB0-PB3 como salida
    uint8_t contador = 0;
    
    while(1) {
        PORTB = (PORTB & 0xF0) | (contador & 0x0F);
        _delay_ms(1000);
        contador++;
        if (contador > 15) contador = 0;
    }
}
```

---

## Nivel 7: Aplicación Botones

### Respuesta 7.1: Debounce

```c
#define DEBOUNCE_MS 50

uint8_t button_read_debounced(void) {
    static uint8_t last_state = 1;  // Pull-up: reposo = HIGH
    
    uint8_t current = PIND & (1 << PD2);
    
    if (current != last_state) {
        _delay_ms(DEBOUNCE_MS);
        current = PIND & (1 << PD2);
        
        if (current != last_state) {
            last_state = current;
            if (current == 0) {  // Flanco de bajada = presión
                return 1;
            }
        }
    }
    return 0;
}
```

### Respuesta 7.2: Contador con Botones

```c
int main(void) {
    DDRB |= 0x0F;    // LEDs
    DDRD &= ~0x0C;   // PD2, PD3 entrada
    PORTD |= 0x0C;   // Pull-ups
    
    int8_t contador = 0;
    
    while(1) {
        if (button_pressed(PD2)) {
            if (contador < 15) contador++;
        }
        if (button_pressed(PD3)) {
            if (contador > 0) contador--;
        }
        PORTB = (PORTB & 0xF0) | contador;
    }
}
```

---

## Nivel 8: Display 7 Segmentos

### Respuesta 8.1

Para mostrar "5" en display cátodo común:
```
Segmentos activos: a, c, d, f, g
Segmentos: gfedcba

5 = segmentos a,c,d,f,g = 0b01101101 = 0x6D
```

### Respuesta 8.2: Multiplexado 4 Dígitos

```c
const uint8_t digits[] = {
    0x3F, 0x06, 0x5B, 0x4F, 0x66,  // 0-4
    0x6D, 0x7D, 0x07, 0x7F, 0x6F   // 5-9
};

volatile uint16_t display_value = 0;

ISR(TIMER0_COMPA_vect) {
    static uint8_t digit = 0;
    uint16_t temp = display_value;
    uint8_t val;
    
    // Extraer dígito
    switch(digit) {
        case 0: val = temp % 10; break;
        case 1: val = (temp / 10) % 10; break;
        case 2: val = (temp / 100) % 10; break;
        case 3: val = (temp / 1000) % 10; break;
    }
    
    PORTD = ~(1 << digit);  // Activar dígito
    PORTB = digits[val];    // Mostrar segmentos
    
    digit = (digit + 1) % 4;
}
```

---

## Nivel 9: Teclado Matricial

### Respuesta 9.1

**Principio de escaneo:**
1. Configurar filas como salidas, columnas como entradas con pull-up
2. Activar una fila a la vez (poner en LOW)
3. Leer todas las columnas
4. Si una columna está en LOW, hay tecla presionada en esa intersección
5. Repetir para cada fila

### Respuesta 9.2

```c
char keypad_scan(void) {
    const char keys[4][4] = {
        {'1','2','3','A'},
        {'4','5','6','B'},
        {'7','8','9','C'},
        {'*','0','#','D'}
    };
    
    for (uint8_t row = 0; row < 4; row++) {
        PORTB = ~(1 << row);  // Activar fila
        _delay_us(5);
        
        uint8_t cols = ~PINC & 0x0F;  // Leer columnas
        
        for (uint8_t col = 0; col < 4; col++) {
            if (cols & (1 << col)) {
                while (~PINC & 0x0F);  // Esperar release
                return keys[row][col];
            }
        }
    }
    return 0;
}
```

---

<!-- IA_CONTEXT
PROPÓSITO: Respuestas para ejercicios de GPIO
NOTA: Pueden existir soluciones alternativas válidas
-->
