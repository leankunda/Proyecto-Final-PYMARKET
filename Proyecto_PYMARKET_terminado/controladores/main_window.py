import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem, QPixmap
from main_window_ui import Ui_MainWindow  


from secondary_window import VentanaSecundaria  
from tertiary_window import VentanaTerciaria 


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PYMARKET - Inicio")
        self.setMinimumSize(1000, 600)
        self.setMaximumSize(1000, 600)

        
        self.boton_abrir_secundaria.clicked.connect(self.abrir_ventana_secundaria)
        self.boton_abrir_terciaria.clicked.connect(self.abrir_ventana_terciaria)
        
    
        self.label.setPixmap(QPixmap("PYMARKET2.jpg"))


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
