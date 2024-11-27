#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Configura la dirección I2C del LCD y el tamaño (16 columnas x 2 filas)
LiquidCrystal_I2C lcd(0x3F, 16, 2); // Reemplaza 0x27 con la dirección encontrada.
// Cambia 0x27 si tu dirección es diferente.

void setup() {
  lcd.init();            // Inicializa el LCD
  lcd.backlight();       // Enciende la luz de fondo

  // Primera línea
  lcd.setCursor(0, 0);   // Coloca el cursor en la primera columna, primera fila
  lcd.print("Carrito PYMKT"); // Mensaje resumido para la primera línea

  // Segunda línea
  lcd.setCursor(0, 1);   // Coloca el cursor en la primera columna, segunda fila
  lcd.print("300 prod $20k"); // Mensaje compacto con productos y costo total
}

void loop() {
  // No se necesita código en el loop para este ejemplo simple.
}
