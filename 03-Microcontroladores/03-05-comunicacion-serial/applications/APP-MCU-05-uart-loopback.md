# 🔧 Aplicación: Monitor Serial con Loopback y Eco

```
::METADATA::
tipo: aplicacion
tema: MCU-05-comunicacion-serial
dificultad: basica
objetivo: Probar TX/RX UART con eco y comandos sencillos
::END::
```

## 📋 Descripción del Proyecto

Implementar un monitor serial que haga eco de los caracteres recibidos y responda a comandos simples (`LED ON/OFF`, `READ ADC`, `HELP`). Permite validar la configuración TX/RX y la integración con periféricos.

## 🎯 Objetivos de Aprendizaje

- Configurar baud rate y verificar errores porcentuales
- Implementar búfer RX circular
- Detectar comandos terminados en `\n`
- Controlar GPIO y ADC desde comandos UART

## 🛠️ Pasos Clave

1) Inicializar UART (9600 bps), habilitar interrupción RX.
2) Al recibir byte: guardar en buffer; si es `\n`, procesar comando.
3) Comandos soportados:
   - `LED ON` / `LED OFF`: controla RB0.
   - `READ`: lee AN0 via ADC y devuelve valor en mV.
   - `HELP`: muestra lista de comandos.
4) Hacer eco inmediato de cada carácter para validación.

## 🧩 Código Base (fragmento)

```c
#define RX_BUF_SIZE 32
volatile char rx_buf[RX_BUF_SIZE];
volatile uint8_t rx_head=0, rx_tail=0;

void __interrupt() isr(void) {
    if (PIR1bits.RCIF) {
        char c = RCREG;
        rx_buf[rx_head] = c;
        rx_head = (rx_head + 1) % RX_BUF_SIZE;
        if (c == '\n') process_command();
    }
}

void process_command(void) {
    // Extraer línea completa
    char line[RX_BUF_SIZE]; uint8_t i=0;
    while (rx_tail != rx_head && i < RX_BUF_SIZE-1) {
        char c = rx_buf[rx_tail];
        rx_tail = (rx_tail + 1) % RX_BUF_SIZE;
        line[i++] = c;
        if (c == '\n') break;
    }
    line[i] = '\0';
    
    if (strstr(line, "LED ON")) LATBbits.LATB0 = 1;
    else if (strstr(line, "LED OFF")) LATBbits.LATB0 = 0;
    else if (strstr(line, "READ")) {
        uint16_t adc = read_adc(0);
        printf("ADC=%u mV\r\n", (adc*5000)/1023);
    } else {
        printf("CMD? Use: LED ON|OFF, READ, HELP\r\n");
    }
}
```

## ✅ Checklist

- [x] TX/RX funcionando
- [x] Eco inmediato
- [x] Comandos básicos
- [x] Control GPIO
- [x] Lectura ADC vía comando

## 🔗 Referencias

- [MCU-05-Teoria-UART.md](../theory/MCU-05-Teoria-UART.md)
