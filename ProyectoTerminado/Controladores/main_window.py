import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem, QPixmap
from main_window_ui import Ui_MainWindow  
import serial
import time
from secondary_window import VentanaSecundaria  
from tertiary_window import VentanaTerciaria 


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.arduino= self.configurar_arduino
        self.setWindowTitle("PYMARKET - Inicio")
        self.setMinimumSize(1000, 600)
        self.setMaximumSize(1000, 600)
        self.boton_abrir_secundaria.clicked.connect(self.abrir_ventana_secundaria)
        self.boton_abrir_terciaria.clicked.connect(self.abrir_ventana_terciaria)
        self.label_2.setPixmap(QPixmap("PYMARKET2.jpg"))

    def configurar_arduino(self):
        try:
            arduino =serial.Serial("USB0", 9600)
            print("conexion establecida con el arduino")
            return arduino
        except serial.SerialException as e:
            print(f"error al conectar con el arduino: {e}")
            
    def abrir_ventana_secundaria(self):
        """Abre la ventana secundaria."""
        self.ventana_secundaria = VentanaSecundaria()
        self.ventana_secundaria.show()

    def abrir_ventana_terciaria(self):
        """Abre la ventana terciaria."""
        self.ventana_terciaria = VentanaTerciaria()
        self.ventana_terciaria.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
