from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
import sys, json, threading, time
import serial
from Carrito_ui import Ui_Carrito

CARRITO_JSON_PATH = "carrito.json" 

class Carrito(QDialog, Ui_Carrito):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PYMARKET - Carrito")
        
        self.carrito_data = self.cargar_json(CARRITO_JSON_PATH)
        self.agregar_productos_data = self.cargar_json("agregar_productos.json")
        self.arduino = serial.Serial('/dev/ttyUSB1', 9600, timeout=1) 
        time.sleep(2) 
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.mostrar_productos_carrito()
        self.actualizar_display_thread = threading.Thread(target=self.actualizar_display_continuamente, daemon=True)
        self.actualizar_display_thread.start()
        self.pEliminar.clicked.connect(self.eliminar_producto)
        self.pComprar.clicked.connect(self.confirmar_compra)

    def cargar_json(self, archivo):
        """Carga datos desde un archivo JSON."""
        try:
            with open(archivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []  

    def guardar_json(self, archivo, data):
        """Guarda datos en un archivo JSON."""
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)

    def mostrar_productos_carrito(self):
        """Muestra los productos cargados en el carrito en el QListView."""
        self.model.clear()
        for producto in self.carrito_data:
            item = QStandardItem(f"{producto['nombre']} x{producto['cantidad']} - ${producto['precio'] * producto['cantidad']}")
            item.setData(producto)
            self.model.appendRow(item)

    def eliminar_producto(self):
        """Elimina el producto seleccionado del carrito y actualiza el JSON."""
        index = self.listView.selectedIndexes()
        if index:
            item = self.model.itemFromIndex(index[0])
            producto = item.data()
            self.carrito_data.remove(producto)
            self.guardar_json(CARRITO_JSON_PATH, self.carrito_data)
            self.mostrar_productos_carrito()

    def confirmar_compra(self):
        """Confirma la compra y muestra la ventana de confirmación."""
        if not self.carrito_data: 
            QMessageBox.warning(self, "Carrito Vacío", "El carrito está vacío. No se puede confirmar la compra.")
            return
        total = sum([producto['precio'] * producto['cantidad'] for producto in self.carrito_data])
        
        respuesta = QMessageBox.question(self, "Confirmar Compra",
                                         f"¿Estás seguro que quieres comprar todo lo que hay en el carrito? Total: ${total}",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.carrito_data.clear()
            self.guardar_json(CARRITO_JSON_PATH, self.carrito_data)
            QMessageBox.information(self, "Pago Completado", "¡Pago realizado con éxito!")
            self.mostrar_productos_carrito()

    def actualizar_display(self):
        """Envía al LCD el precio total y la cantidad de productos del carrito."""
        self.carrito_data = self.cargar_json(CARRITO_JSON_PATH)
        total_precio = sum(p['precio'] * p['cantidad'] for p in self.carrito_data)
        total_cantidad = sum(p['cantidad'] for p in self.carrito_data)
        mensaje = f"{total_precio},{total_cantidad}\n"
        self.arduino.write(mensaje.encode()) 

    def actualizar_display_continuamente(self):
        """Actualiza el display constantemente leyendo el archivo JSON."""
        while True:
            self.actualizar_display()
            time.sleep(1)  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Carrito()
    ventana.show()
    sys.exit(app.exec_())
