#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Configura la dirección I2C del LCD y el tamaño (20 columnas x 4 filas)
LiquidCrystal_I2C lcd(0x27, 20, 4); // Cambia 0x27 si tu dirección es diferente.

void setup() {
  lcd.init();            // Inicializa el LCD
  lcd.backlight();       // Enciende la luz de fondo

  lcd.setCursor(0, 0);   // Coloca el cursor en la primera columna, primera fila
  lcd.print("Carrito PYMARKET"); // Escribe el mensaje en la primera línea

  lcd.setCursor(0, 1);   // Coloca el cursor en la primera columna, segunda fila
  lcd.print("Productos: 300");  // Muestra el número total de productos

  lcd.setCursor(0, 2);   // Coloca el cursor en la primera columna, tercera fila
  lcd.print("Coste total: $20.000");  // Muestra el coste total

  lcd.setCursor(0, 3);   // Coloca el cursor en la primera columna, cuarta fila
  lcd.print("Gracias por comprar!");  // Mensaje en la última fila
}

void loop() {
  // No se necesita código en el loop para este ejemplo simple.
}
