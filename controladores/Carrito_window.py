from PyQt5.QtWidgets import QDialog, QComboBox, QWidget, QVBoxLayout, QMainWindow, QApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *
import sys, json
from cuartiary_window_ui import Ui_VentanaCuartaria
from Carrito_ui import Ui_Carrito

class Carrito(QDialog, Ui_Carrito):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PYMARKET - Carrito")
        self.productos = []    

# Inicialización de la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Carrito()
    ventana.show()
    sys.exit(app.exec_())