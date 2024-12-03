#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4); // Cambia a 0x3F si 0x27 no funciona

void setup() {
    lcd.init();
    lcd.backlight();
    lcd.setCursor(0, 0);
    lcd.print("Esperando datos...");
    Serial.begin(9600); // Configura comunicación serial
}

void loop() {
    if (Serial.available() > 0) {
        String data = Serial.readStringUntil('\n'); // Lee datos hasta nueva línea
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Carrito de PYMARKET");
        lcd.setCursor(0, 1);
        lcd.print("Precio total:");
        lcd.setCursor(0, 2);
        lcd.print(data.substring(0, data.indexOf(','))); // Muestra el precio
        lcd.setCursor(0, 3);
        lcd.print("Cant. prod:");
        lcd.print(data.substring(data.indexOf(',') + 1)); // Muestra cantidad
    }
}
