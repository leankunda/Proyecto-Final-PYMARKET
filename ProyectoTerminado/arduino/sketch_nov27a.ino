#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Configura el LCD con la dirección I2C y el tamaño de la pantalla
LiquidCrystal_I2C lcd(0x27, 16, 2);  // Dirección I2C = 0x27, 16 columnas y 2 filas

void setup() {
  // Inicia la comunicación serial y el LCD
  lcd.init();            // Inicializar el LCD
  lcd.backlight();       // Encender la luz de fondo del LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Esperando datos");

  // Iniciar el puerto serial para depuración
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    // Lee los datos enviados desde Python
    String data = Serial.readStringUntil('\n');  // Asegúrate de leer hasta el salto de línea
    
    // Muestra los datos recibidos por el serial (para depuración)
    Serial.println("Datos recibidos: " + data);
    
    
    // Divide los datos en base a las comas
    int index1 = data.indexOf(',');
    int index2 = data.indexOf(',', index1 + 1);
    int index3 = data.indexOf(',', index2 + 1);
    int index4 = data.indexOf(',', index3 + 1);

    // Extrae los valores de cada variable
    String nombre = data.substring(0, index1);
    String precio = data.substring(index1 + 1, index2);
    String peso = data.substring(index2 + 1, index3);
    String stock = data.substring(index3 + 1, index4);

    // Muestra los valores en el LCD
    lcd.clear();  // Limpia la pantalla
    lcd.setCursor(0, 0);
    lcd.print("Nombre: " + nombre );  // Mostrar solo los primeros 8 caracteres
    lcd.setCursor(0, 1);
    lcd.print("P: " + precio + " Kg:" + peso.substring(0, 5));  // Asegúrate de que no exceda los 16 caracteres
    delay(2000);  // Tiempo para que el mensaje sea visible
  }
}
