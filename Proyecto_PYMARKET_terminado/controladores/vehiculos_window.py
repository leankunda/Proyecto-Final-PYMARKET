from PyQt5.QtWidgets import QDialog, QComboBox, QWidget, QVBoxLayout, QMainWindow, QApplication, QInputDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *
import sys, json
import os
from PyQt5.QtWidgets import QAbstractItemView
from vehiculos_ui import Ui_vehiculos
from Carrito_window import Carrito
from Carrito_ui import Ui_Carrito
import serial
import time


USER_DIR = os.path.expanduser("~")  
CARPETA_RECUSOS = os.path.join(USER_DIR, "PROYECTO PYMARKET")  
PRODUCTOS_JSON_PATH = os.path.join(CARPETA_RECUSOS, "productos_agregados.json")
CARRITO_JSON_PATH = os.path.join(CARPETA_RECUSOS, "carrito.json")


class Productos_Vehiculos:
    def __init__(self, nombre, precio, descripcion, categoria, peso, stock):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.categoria = categoria
        self.peso = peso
        self.stock = stock

    def para_json(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "peso": self.peso,
            "descripcion": self.descripcion,
            "stock": self.stock,
        }

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


productos_predefinidos = [
    Productos_Vehiculos("Carro", 20000, "Carro deportivo de alta velocidad", "Comida", 1500, 10),
    Productos_Vehiculos("Moto", 5000, "Motocicleta económica y compacta", "Comida", 200, 15),
    Productos_Vehiculos("Bicicleta", 300, "Bicicleta de montaña resistente", "Comida", 15, 20),
    Productos_Vehiculos("Camión", 80000, "Camión para transporte de carga pesada", "Comida", 4000, 5),
    Productos_Vehiculos("Avión", 200000, "Avión ligero para transporte personal", "Comida", 10000, 2),
]


class SerialThread(QThread):
    error_signal = pyqtSignal(str)
    success_signal = pyqtSignal(str)

    def __init__(self, mensaje, parent=None):
        super().__init__(parent)
        self.mensaje = mensaje

    def run(self):
        try:
            arduino = serial.Serial('/dev/ttyUSB0', 9600)
            time.sleep(2)
            arduino.write(self.mensaje.encode())
            arduino.close()
            self.success_signal.emit("Mensaje enviado correctamente al Arduino.")
        except Exception as e:
            self.error_signal.emit(f"Error al comunicar con Arduino: {e}")


class VentanaVehiculos(QDialog, Ui_vehiculos):
    def __init__(self, nombre=None, precio=None, descripcion=None, categoria=None, peso=None, stock=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PYMARKET - Comprar / Comida.")
        self.lBuscar.setPlaceholderText("Buscar...")

        self.productos = productos_predefinidos
        self.carrito_lista = []
        self.model = QStandardItemModel(self.listView)

        self.cargar_productos_predefinidos()
        self.cargar_productos_desde_json(PRODUCTOS_JSON_PATH)

        self.listView.setModel(self.model)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.clicked.connect(self.mostrar_detalle_producto)
        self.pCarrito.clicked.connect(self.mostrar_stock_y_agregar)
        self.pVerCarrito.clicked.connect(self.abrir_Carrito)
        self.lBuscar.textChanged.connect(self.buscar_productos)

    def cargar_productos_predefinidos(self):
        for producto in self.productos:
            item = QStandardItem(producto.nombre)
            self.model.appendRow(item)

    def cargar_productos_desde_json(self, ruta_json):
        try:
            with open(ruta_json, "r") as file:
                productos_json = json.load(file)
            for p in productos_json:
                if p["categoria"] == "Comida":
                    producto = Productos_Vehiculos(
                        nombre=p["nombre"],
                        precio=p["precio"],
                        descripcion=p["descripcion"],
                        categoria=p["categoria"],
                        peso=p["peso"],
                        stock=p["stock"],
                    )
                    self.productos.append(producto)
                    item = QStandardItem(producto.nombre)
                    self.model.appendRow(item)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No se encontró el archivo JSON o contiene errores.")

    def guardar_producto_en_json(self, producto, stock):
        if not os.path.exists(CARPETA_RECUSOS):
            os.makedirs(CARPETA_RECUSOS)

        if not os.path.isfile(CARRITO_JSON_PATH):
            with open(CARRITO_JSON_PATH, 'w') as file:
                json.dump([], file)

        try:
            with open(CARRITO_JSON_PATH, "r") as file:
                carrito = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            carrito = []

        producto_en_carrito = next((p for p in carrito if p['nombre'] == producto.nombre), None)

        if producto_en_carrito:
            producto_en_carrito['stock'] += stock
        else:
            carrito.append({
                "nombre": producto.nombre,
                "precio": producto.precio,
                "descripcion": producto.descripcion,
                "stock": producto.stock,
            })

        with open(CARRITO_JSON_PATH, "w") as file:
            json.dump(carrito, file, indent=4)

    def abrir_Carrito(self):
        carrito_ventana = Carrito()
        carrito_ventana.exec_()

    def mostrar_detalle_producto(self, index):
        producto = self.productos[index.row()]
        self.TextLabel1.setText(producto.nombre)
        self.TextLabel2.setText(producto.descripcion)
        mensaje = f"{producto.peso},{producto.stock},{producto.precio}"
        self.hilo_serial = SerialThread(mensaje)
        self.hilo_serial.error_signal.connect(self.mostrar_error_serial)
        self.hilo_serial.success_signal.connect(self.mostrar_exito_serial)
        self.hilo_serial.start()

    def mostrar_error_serial(self, mensaje_error):
        print(mensaje_error)

    def mostrar_exito_serial(self, mensaje):
        print(mensaje)

    def mostrar_stock_y_agregar(self):
        if not self.listView.selectedIndexes():
            print("No se ha seleccionado ningún producto.")
            return

        index = self.listView.selectedIndexes()[0]
        producto = self.productos[index.row()]
        stock, ok = QInputDialog.getInt(
            self, "stock", f"¿Cuántas unidades de '{producto.nombre}' deseas agregar?",
            min=1, max=producto.stock, step=1
        )
        if ok and stock > 0:
            if stock <= producto.stock:
                producto.stock -= stock
                self.carrito_lista.append((producto, stock))
                self.guardar_producto_en_json(producto, stock)
                print(f"{stock} unidad(es) de '{producto.nombre}' agregadas al carrito.")
            else:
                print(f"Stock insuficiente. Solo hay {producto.stock} unidades disponibles.")

    def buscar_productos(self):
        texto_busqueda = self.lBuscar.text().lower()
        self.model.clear()
        productos_filtrados = [producto for producto in self.productos if texto_busqueda in producto.nombre.lower()]
        for producto in productos_filtrados:
            item = QStandardItem(producto.nombre)
            self.model.appendRow(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaVehiculos()
    ventana.show()
    sys.exit(app.exec_())
