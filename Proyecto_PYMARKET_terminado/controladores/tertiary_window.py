import json
from PyQt5.QtWidgets import QDialog, QMessageBox
import sys
from PyQt5.QtWidgets import QApplication
from tertiary_window_ui import Ui_VentanaTerciaria
import os


ARCHIVO_PRODUCTOS = os.path.join(os.getcwd(), "productos_agregados.json")

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

 
        
        self.pPUBLICAR.clicked.connect(self.guardar_producto)

    def validar_numerico(self, valor):
        """Verificar si el valor es numérico y positivo."""
        try:
            float(valor)
            return True
        except ValueError:
            return False

    def guardar_producto(self):
        nombre = self.lineNOMBRE.text()
        descripcion = self.lineDESCRIPCION.text()
        precio = self.linePRECIO.text()
        stock = self.lineSTOCK.text()
        peso = self.linePESO.text()
        categoria = self.comboCATEGORIA.currentText()

        if not nombre or not descripcion or not precio or not stock or not peso or categoria == "":
            QMessageBox.warning(self, "Campos incompletos", "Por favor, complete todos los campos antes de publicar el producto.")
            return
        
        if not self.validar_numerico(precio):
            QMessageBox.warning(self, "Error en Precio", "El precio debe ser un valor numérico válido.")
            return
        if not self.validar_numerico(stock):
            QMessageBox.warning(self, "Error en Stock", "El stock debe ser un valor numérico válido.")
            return
        if not self.validar_numerico(peso):
            QMessageBox.warning(self, "Error en Peso", "El peso debe ser un valor numérico válido.")
            return

        producto = {
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock,
            "peso": peso,
            "categoria": categoria
        }

        try:
            if os.path.exists(ARCHIVO_PRODUCTOS):
                with open(ARCHIVO_PRODUCTOS, "r") as file:
                    productos = json.load(file)
            else:
                productos = []
        except FileNotFoundError:
            productos = []

        productos.append(producto)

        try:
            with open(ARCHIVO_PRODUCTOS, "w") as file:
                json.dump(productos, file, indent=4)
            
            QMessageBox.information(self, "Producto publicado", "El producto se ha publicado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el producto. Error: {e}")
            return

        self.lineNOMBRE.clear()
        self.lineDESCRIPCION.clear()
        self.linePRECIO.clear()
        self.lineSTOCK.clear()
        self.linePESO.clear()
        self.comboCATEGORIA.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = VentanaTerciaria()
    main_window.show()
    sys.exit(app.exec_())
