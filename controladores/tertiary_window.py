import json
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from tertiary_window_ui import Ui_VentanaTerciaria
import serial
import time


filename = "productos_agregados.json"


class VentanaTerciaria(QDialog, Ui_VentanaTerciaria):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PYMARKET - Vender")
        self.setMinimumSize(1000, 600)
        self.setMaximumSize(1000, 600)
        
        self.lineNOMBRE.setPlaceholderText("Escriba aquí...")
        self.lineDESCRIPCION.setPlaceholderText("Escriba aquí...")
        self.linePESO.setPlaceholderText("Escriba aquí...")
        self.linePRECIO.setPlaceholderText("Escriba aquí...")
        self.lineSTOCK.setPlaceholderText("Escriba aquí...")
        self.lineNOMBRE.setPlaceholderText("Escriba aquí...")

        # Conectar el botón de publicar con la función de guardar
        self.pPUBLICAR.clicked.connect(self.guardar_producto)

    def validar_numerico(self, valor):
        """Verificar si el valor es numérico y positivo."""
        try:
            float(valor)
            return True
        except ValueError:
            return False

    def guardar_producto(self):
        # Obtener los valores de los line edits y del combobox
        nombre = self.lineNOMBRE.text()
        descripcion = self.lineDESCRIPCION.text()
        precio = self.linePRECIO.text()
        stock = self.lineSTOCK.text()
        peso = self.linePESO.text()
        categoria = self.comboCATEGORIA.currentText()

        # Verificar que los campos obligatorios no estén vacíos
        if not nombre or not descripcion or not precio or not stock or not peso or categoria == "":
            QMessageBox.warning(self, "Campos incompletos", "Por favor, complete todos los campos antes de publicar el producto.")
            return
        
        # Validar que precio, stock y peso sean números válidos
        if not self.validar_numerico(precio):
            QMessageBox.warning(self, "Error en Precio", "El precio debe ser un valor numérico válido.")
            return
        if not self.validar_numerico(stock):
            QMessageBox.warning(self, "Error en Stock", "El stock debe ser un valor numérico válido.")
            return
        if not self.validar_numerico(peso):
            QMessageBox.warning(self, "Error en Peso", "El peso debe ser un valor numérico válido.")
            return

        # Crear un diccionario con los datos
        producto = {
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock,
            "peso": peso,
            "categoria": categoria
        }
            
        # Leer el archivo JSON existente o crear uno nuevo
        try:
            with open("productos_agregados.json", "r") as file:
                productos = json.load(file)
        except FileNotFoundError:
            productos = []

        # Agregar el nuevo producto a la lista
        productos.append(producto)

        # Escribir los datos actualizados en el archivo JSON
        try:
            with open("productos_agregados.json", "w") as file:
                json.dump(productos, file, indent=4)
            
            # Mostrar un mensaje de éxito
            QMessageBox.information(self, "Producto publicado", "El producto se ha publicado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el producto. Error: {e}")
            return

        # Limpiar los campos después de guardar
        self.lineNOMBRE.clear()
        self.lineDESCRIPCION.clear()
        self.linePRECIO.clear()
        self.lineSTOCK.clear()
        self.linePESO.clear()
        self.comboCATEGORIA.setCurrentIndex(0)

        try:
            with open("productos_agregados.json", "w") as file:
                json.dump(productos, file, indent=4)
            
            # Mostrar un mensaje de éxito
            QMessageBox.information(self, "Producto publicado", "El producto se ha publicado correctamente.")
        except Exception as e:
            # Mostrar un mensaje de error si algo falla al guardar
            QMessageBox.critical(self, "Error", f"No se pudo guardar el producto. Error: {e}")
            puerto = '/dev/ttyUSB0'  # Cambia esto al puerto adecuado en tu sistema
            arduino = serial.Serial(puerto, 9600, timeout=1)

# Espera para asegurar que la comunicación se haya establecido
            time.sleep(2)

# Enviar un mensaje al LCD
            mensaje = "Error", f"No se pudo guardar el producto. Error: {e}"
            arduino.write(mensaje.encode())  # Envía el mensaje como bytes

# Cierra la conexión serial
arduino.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = VentanaTerciaria()
    main_window.show()
    sys.exit(app.exec_())
    
    
    