from PyQt5.QtWidgets import QDialog, QComboBox, QWidget, QVBoxLayout, QMainWindow, QApplication, QInputDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *
import sys, json
from PyQt5.QtWidgets import QAbstractItemView
from tecnologia_ui import Ui_tecnologia
from Carrito_window import Carrito
from Carrito_ui import Ui_Carrito
import os
import serial
import time

USER_DIR = os.path.expanduser("~") 
CARPETA_RECUSOS = os.path.join(USER_DIR, "PROYECTO PYMARKET") 
PRODUCTOS_JSON_PATH = os.path.join(CARPETA_RECUSOS, "productos_agregados.json")  
CARRITO_JSON_PATH = os.path.join(CARPETA_RECUSOS, "carrito.json")

class Productos_Tecnologia:
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
            "categoria": self.categoria, 
        }

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

productos_predefinidos = [
    Productos_Tecnologia("Mouse", 20000, "Diferentes tipos de Mouse", "Tecnologia", 1500, 10),
    Productos_Tecnologia("Laptop", 5000, "Laptops con diferentes tamaños", "Tecnologia", 200, 15),
    Productos_Tecnologia("Mousepad", 300, "Mousepad de diferentes tamaños", "Tecnologia", 15, 20),
    Productos_Tecnologia("Teclados", 80000, "Teclados mecanicos y de membrana de diferentes tamaños", "Tecnologia", 4000, 5),
    Productos_Tecnologia("Celulares", 200000, "Celulares de marca Iphone,Samsung,Motorola", "Tecnologia", 10000, 2),
]

class VentanaTecnologia(QDialog, Ui_tecnologia):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PYMARKET - Comprar / Tecnologia.")
        self.lBuscar.setPlaceholderText("Buscar...")
        self.iniciar_comunicacion_serial()
        
        self.productos = [] 
        self.carrito_lista = []

        self.model = QStandardItemModel(self.listView)
        self.cargar_productos_predefinidos()
        self.cargar_productos_desde_json(PRODUCTOS_JSON_PATH)

        self.listView.setModel(self.model)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.clicked.connect(self.mostrar_detalle_producto)
        self.pCarrito.clicked.connect(self.mostrar_cantidad_y_agregar)
        self.pVerCarrito.clicked.connect(self.abrir_Carrito)
        self.lBuscar.textChanged.connect(self.buscar_productos)

    def cargar_productos_predefinidos(self):
        """Carga los productos predefinidos en el QListView ordenados alfabéticamente."""
        for producto in productos_predefinidos:
            if producto.categoria == "Tecnologia": 
                self.productos.append(producto)

        self.productos.sort(key=lambda producto: producto.nombre.lower())  

        for producto in self.productos:
            item = QStandardItem(producto.nombre)
            self.model.appendRow(item)

    def cargar_productos_desde_json(self, ruta_json):
        """Carga los productos desde un archivo JSON y los agrega solo si son de la categoría 'Tecnologia'."""
        try:
            with open(ruta_json, "r") as file:
                productos_json = json.load(file)

            for p in productos_json:
                if p["categoria"] == "Tecnologia": 
                    producto = Productos_Tecnologia(
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

    def guardar_producto_en_json(self, producto, cantidad):
        """Guarda la información del producto en un archivo JSON."""
        if not os.path.exists(CARPETA_RECUSOS):
            os.makedirs(CARPETA_RECUSOS)

        if not os.path.isfile(PRODUCTOS_JSON_PATH):
            with open(CARRITO_JSON_PATH, 'w') as file:
                json.dump([], file) 
        try:
            with open(CARRITO_JSON_PATH, "r") as file:
                carrito = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            carrito = []

        producto_en_carrito = next((p for p in carrito if p['nombre'] == producto.nombre), None)

        if producto_en_carrito:
            producto_en_carrito['cantidad'] += cantidad
        else:
            carrito.append({
                "nombre": producto.nombre,
                "precio": producto.precio,
                "descripcion": producto.descripcion,
                "cantidad": cantidad,
            })

        with open(CARRITO_JSON_PATH, "w") as file:
            json.dump(carrito, file, indent=4)

    def abrir_Carrito(self):
        """Abre la ventana del carrito."""
        carrito_ventana = Carrito()
        carrito_ventana.exec_()

    def iniciar_comunicacion_serial(self):
        """Inicia la comunicación serial con Arduino."""
        try:
            self.arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) 
            time.sleep(2) 
            print("Comunicación serial establecida.")
        except serial.SerialException as e:
            print(f"Error al inicializar la comunicación serial: {e}")

    def mostrar_detalle_producto(self, index):
        """Muestra el detalle del producto seleccionado en los labels y lo envía al Arduino."""
        producto = self.productos[index.row()]
        self.TextLabel1.setText(producto.nombre)
        self.TextLabel2.setText(producto.descripcion)

        if self.arduino and self.arduino.isOpen():  
            try:
                mensaje = f"{producto.nombre},{producto.precio},{producto.peso},{producto.stock}\n"
                self.arduino.write(mensaje.encode())  
                print(f"Enviado al Arduino: {mensaje.strip()}")
            except serial.SerialException as e:
                print(f"Error al enviar datos a Arduino: {e}")
        else:
            print("La comunicación serial no está establecida o está cerrada.")

    def mostrar_cantidad_y_agregar(self):
        """Muestra un cuadro para ingresar la cantidad de unidades a agregar al carrito."""
        if not self.listView.selectedIndexes():
            print("No se ha seleccionado ningún producto.")
            return
        index = self.listView.selectedIndexes()[0]
        producto = self.productos[index.row()]

        cantidad, ok = QInputDialog.getInt(
            self, "Cantidad", f"¿Cuántas unidades de '{producto.nombre}' deseas agregar?", 
            min=1, max=producto.stock, step=1
        )

        if ok and cantidad > 0:
            if cantidad <= producto.stock:
                producto.stock -= cantidad
                self.carrito_lista.append((producto, cantidad)) 
                self.guardar_producto_en_json(producto, cantidad)
                print(f"{cantidad} unidad(es) de '{producto.nombre}' agregadas al carrito.")
            else:
                print(f"Stock insuficiente. Solo hay {producto.stock} unidades disponibles.")

    def buscar_productos(self):
        """Busca productos por nombre en la lista."""
        texto_busqueda = self.lBuscar.text().lower()

        if texto_busqueda:
            self.model.clear() 
            productos_filtrados = [producto for producto in self.productos if texto_busqueda in producto.nombre.lower()]
        else:
            productos_filtrados = self.productos 

        for producto in productos_filtrados:
            item = QStandardItem(producto.nombre)
            self.model.appendRow(item)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaTecnologia()
    ventana.show()
    sys.exit(app.exec_())
