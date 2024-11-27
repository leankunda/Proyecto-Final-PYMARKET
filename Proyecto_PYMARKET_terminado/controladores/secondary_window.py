from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from cuartiary_window import VentanaCuartaria
from secondary_window_ui import Ui_VentanaSecundaria
from vehiculos_window import VentanaVehiculos
from comida_window import VentanaComida
from tecnologia_window import VentanaTecnologia
from Carrito_window import Carrito

from Carrito_ui import Ui_Carrito


class VentanaSecundaria(QDialog, Ui_VentanaSecundaria):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PYMARKET - Comprar")
        self.pARTE.clicked.connect(self.abrir_ventana_cuartaria)
        self.pushButton_4.clicked.connect(self.abrir_comida)
        self.pVEHICULOS.clicked.connect(self.abrir_vehiculos)
        self.pTECNOLOGIA.clicked.connect(self.abrir_tecnologia)
        self.pushButton.clicked.connect(self.abrir_Carrito)
    
    
    
    def abrir_ventana_cuartaria(self):
        self.ventana_cuartaria = VentanaCuartaria()
        self.ventana_cuartaria.show()
        
    def abrir_comida(self):
        self.ventana_comida = VentanaComida()
        self.ventana_comida.show()

    def abrir_vehiculos(self):
        self.ventana_vehiculos = VentanaVehiculos()
        self.ventana_vehiculos.exec_()

    def abrir_tecnologia(self):
        self.ventana_tecnologia = VentanaTecnologia()
        self.ventana_tecnologia.exec_()
        
    def abrir_Carrito(self):
        self.Carrito = Carrito()
        self.Carrito.exec_()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = VentanaSecundaria()
    main_window.show()
    sys.exit(app.exec_())