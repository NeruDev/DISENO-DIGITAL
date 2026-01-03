# 🔧 Aplicación: Termómetro con LM35 y ADC

```
::METADATA::
tipo: aplicacion
tema: MCU-04-adc-dac
dificultad: intermedia
objetivo: Leer temperatura con LM35, filtrar y mostrar en LCD/UART
::END::
```

## 📋 Descripción del Proyecto

Leer un sensor LM35 con el ADC del PIC16F887, aplicar filtrado promedio móvil y mostrar la temperatura en °C en un LCD 16x2 y por UART.

## 🎯 Objetivos de Aprendizaje

- Configurar ADC (ADCON0/ADCON1) con referencia VDD
- Calcular resolución y conversión a °C (10 mV/°C)
- Implementar filtro promedio móvil de N muestras
- Mostrar datos en LCD y UART

## 🛠️ Pasos Clave

1) Configurar RA0 como entrada analógica (AN0), reloj Fosc/32.
2) Tomar N=16 muestras, sumar y promediar.
3) Convertir a milivoltios: `mv = (adc * 5000) / 1023`.
4) Temperatura: `temp_c = mv / 10`.
5) Mostrar en LCD: "T=xx.x C"; enviar por UART cada 1 s.

## 🧩 Código Base (fragmento)

```c
#define N_SAMPLES 16

uint16_t read_adc(uint8_t ch) {
    ADCON0bits.CHS = ch;
    __delay_us(5);        // tiempo de muestreo
    ADCON0bits.GO = 1;
    while (ADCON0bits.GO);
    return ((uint16_t)ADRESH << 8) | ADRESL;
}

uint16_t average_adc(void) {
    uint32_t acc = 0;
    for (uint8_t i=0; i<N_SAMPLES; i++) {
        acc += read_adc(0);
    }
    return (uint16_t)(acc / N_SAMPLES);
}

void loop(void) {
    uint16_t adc = average_adc();
    uint32_t mv = (adc * 5000UL) / 1023UL;
    uint16_t temp10 = mv / 10; // décimas de grado
    uart_printf("T=%u.%u C\r\n", temp10/10, temp10%10);
    lcd_set_cursor(0,0); lcd_printf("T=%u.%u C", temp10/10, temp10%10);
    __delay_ms(1000);
}
```

## ✅ Checklist

- [x] ADC configurado
- [x] Promedio móvil
- [x] Conversión mV→°C
- [x] Visualización LCD
- [x] Log por UART

## 🔗 Referencias

- [MCU-04-Teoria-ADC.md](../theory/MCU-04-Teoria-ADC.md)
- Hoja de datos LM35
