from PyQt5.QtWidgets import QDialog, QComboBox, QWidget, QVBoxLayout, QMainWindow, QApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *
import sys, json
from PyQt5.QtWidgets import QAbstractItemView
from vehiculos_ui import Ui_vehiculos
from Carrito_window import Carrito
from Carrito_ui import Ui_Carrito


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
            "stock": self.stock
        }

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class VentanaVehiculos(QDialog, Ui_vehiculos):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PYMARKET - Comprar / Vehiculos.")
        self.lBuscar.setPlaceholderText("Buscar...")

        # Inicializa la lista de productos predefinidos
        self.productos = [
            Productos_Vehiculos("Pizza", 200, "Pizza de pepperoni tamaño grande", "Vehiculos", 1, 50),
            Productos_Vehiculos("Hamburguesa", 150, "Hamburguesa con queso, carne de res y pan artesanal", "Vehiculos", 0.5, 30),
            Productos_Vehiculos("Tacos", 100, "Tacos de pollo con salsa especial", "Vehiculos", 0.2, 100),
            Productos_Vehiculos("Burritos", 120, "Burrito de carne y frijoles con guacamole", "Vehiculos", 0.3, 50),
            Productos_Vehiculos("Sushi", 300, "Sushi de salmón y aguacate", "Vehiculos", 0.1, 20),
            Productos_Vehiculos("Fideos", 80, "Fideos italianos al estilo boloñesa", "Vehiculos", 0.4, 60),
            Productos_Vehiculos("Tortas", 90, "Torta de jamón con mayonesa y lechuga", "Vehiculos", 0.3, 70),
            Productos_Vehiculos("Fruta", 50, "Fruta variada, manzanas, plátanos, y uvas", "Vehiculos", 0.5, 80)
        ]

        # Lista del carrito
        self.Carrito = []

        # Crea el modelo de lista para el QListView
        self.model = QStandardItemModel(self.listView)

        # Agregar productos predefinidos al QListView
        self.cargar_productos_predefinidos()

        # Carga productos del JSON y los agrega al modelo
        self.cargar_productos_desde_json("productos_agregados.json")

        # Configura el modelo en el QListView
        self.listView.setModel(self.model)

        # Desactiva la edición de los items en el QListView
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Conecta la señal de clic en el QListView a la función para actualizar los labels
        self.listView.clicked.connect(self.mostrar_detalle_producto)

        # Conecta el botón 'pCarrito' para agregar al carrito
        self.pCarrito.clicked.connect(self.agregar_al_carrito)

        # Conecta el botón para abrir el carrito
        self.pVerCarrito.clicked.connect(self.abrir_Carrito)

    def cargar_productos_predefinidos(self):
        """Carga los productos predefinidos en el QListView."""
        for producto in self.productos:
            item = QStandardItem(producto.nombre)
            self.model.appendRow(item)

    def cargar_productos_desde_json(self, ruta_json):
        """Carga los productos desde un archivo JSON y los agrega solo si son de la categoría 'Vehiculos'."""
        try:
            with open(ruta_json, "r") as file:
                productos_json = json.load(file)
            
            for p in productos_json:
                if p["categoria"] == "Vehiculos":  # Asegúrate de que la categoría sea 'Vehiculos', sin el punto
                    producto = Productos_Vehiculos(
                        nombre=p["nombre"],
                        precio=p["precio"],
                        descripcion=p["descripcion"],
                        categoria=p["categoria"],
                        peso=p["peso"],
                        stock=p["stock"],
                    )
                    self.productos.append(producto)

                    # Agrega el producto al modelo del QListView
                    item = QStandardItem(producto.nombre)
                    self.model.appendRow(item)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No se encontró el archivo JSON o contiene errores.")

    def abrir_Carrito(self):
        self.Carrito = Carrito()
        self.Carrito.exec_()

    def mostrar_detalle_producto(self, index):
        """Muestra el detalle del producto seleccionado en los labels."""
        producto = self.productos[index.row()]
        self.TextLabel1.setText(producto.nombre)
        self.TextLabel2.setText(producto.descripcion)

    def agregar_al_carrito(self):
        """Agrega el producto seleccionado al carrito."""
        index = self.listView.selectedIndexes()[0]
        producto = self.productos[index.row()]
        self.Carrito.append(producto)
        print(f"Producto '{producto.nombre}' agregado al carrito.")

# Inicialización de la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaVehiculos()
    ventana.show()
    sys.exit(app.exec_())
