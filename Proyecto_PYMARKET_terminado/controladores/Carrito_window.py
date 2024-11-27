from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QVBoxLayout, QMessageBox, QSlider, QPushButton, QLabel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
import sys, json
from Carrito_ui import Ui_Carrito


class Carrito(QDialog, Ui_Carrito):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PYMARKET - Carrito")
        
        # Cargar productos del carrito
        self.carrito_data = self.cargar_json("carrito.json")
        self.agregar_productos_data = self.cargar_json("agregar_productos.json")
        
        # Modelo para QListView
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        
        # Mostrar los productos en el ListView
        self.mostrar_productos_carrito()

        # Conectar los botones con las funciones correspondientes
        self.pEliminar.clicked.connect(self.eliminar_producto)
        self.pComprar.clicked.connect(self.confirmar_compra)

    def cargar_json(self, archivo):
        """Carga datos desde un archivo JSON."""
        try:
            with open(archivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []  # Retorna una lista vacía si el archivo no existe

    def guardar_json(self, archivo, data):
        """Guarda datos en un archivo JSON."""
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)

    def mostrar_productos_carrito(self):
        """Muestra los productos cargados en el carrito en el QListView."""
        self.model.clear()
        total = 0
        for producto in self.carrito_data:
            item = QStandardItem(f"{producto['nombre']} x{producto['cantidad']} - ${producto['precio'] * producto['cantidad']}")
            item.setData(producto)
            self.model.appendRow(item)
            total += producto['precio'] * producto['cantidad']
        
        # Asegúrate de que las etiquetas se llamen correctamente según el archivo .ui
        if hasattr(self, 'TextLabel1'):
            self.TextLabel1.setText(f"Total: ${total}")

    def eliminar_producto(self):
        """Elimina el producto seleccionado del carrito y actualiza el JSON."""
        index = self.listView.selectedIndexes()
        if index:
            item = self.model.itemFromIndex(index[0])
            producto = item.data()
            self.carrito_data.remove(producto)
            self.guardar_json("carrito.json", self.carrito_data)
            self.mostrar_productos_carrito()

    def confirmar_compra(self):
        """Confirma la compra y muestra la ventana de confirmación."""
        if not self.carrito_data:  # Verifica si el carrito está vacío
            QMessageBox.warning(self, "Carrito Vacío", "El carrito está vacío. No se puede confirmar la compra.")
            return

        total = sum([producto['precio'] * producto['cantidad'] for producto in self.carrito_data])
        
        # Ventana de confirmación
        respuesta = QMessageBox.question(self, "Confirmar Compra",
                                         f"¿Estás seguro que quieres comprar todo lo que hay en el carrito? Total: ${total}",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.ventana_slider(total)

    def ventana_slider(self, total):
        """Muestra la ventana con el slider para confirmar el pago."""
        # Crear una nueva ventana para el slider
        ventana_slider = QWidget(self)
        ventana_slider.setWindowTitle("Confirmar Pago")
        
        # Layout vertical para organizar los elementos
        layout = QVBoxLayout()

        # Etiqueta que muestra el total
        etiqueta_total = QLabel(f"Total a pagar: ${total}", ventana_slider)
        layout.addWidget(etiqueta_total)

        # Slider para confirmar pago
        slider = QSlider(Qt.Horizontal, ventana_slider)
        slider.setRange(0, 100)
        slider.setValue(0)
        slider.setTickInterval(1)
        slider.setTickPosition(QSlider.TicksBelow)

        # Botón para confirmar
        boton_confirmar = QPushButton("Confirmar Pago", ventana_slider)
        boton_confirmar.setEnabled(False)  # Inicialmente deshabilitado

        # Conectar el slider al botón para habilitarlo cuando esté lleno
        slider.valueChanged.connect(lambda: self.activar_boton(slider, boton_confirmar))

        # Añadir el slider y el botón al layout
        layout.addWidget(slider)
        layout.addWidget(boton_confirmar)

        # Conectar el botón a la función que procesará el pago
        boton_confirmar.clicked.connect(lambda: self.procesar_pago(total))

        # Configurar la ventana
        ventana_slider.setLayout(layout)
        ventana_slider.setGeometry(300, 300, 300, 150)  # Tamaño y posición de la ventana
        ventana_slider.show()

    def activar_boton(self, slider, boton):
        """Habilita el botón cuando el slider está lleno (valor 100)."""
        if slider.value() == 100:
            boton.setEnabled(True)  # Habilitar el botón si el slider está lleno
        else:
            boton.setEnabled(False)  # Deshabilitar el botón si el slider no está lleno

    def procesar_pago(self, total):
        """Procesa la compra, muestra el mensaje de pago completado y cierra la ventana del carrito."""
        # Actualizar el stock
        self.actualizar_stock()

        # Vaciar el carrito
        self.carrito_data.clear()
        self.guardar_json("carrito.json", self.carrito_data)

        # Mostrar mensaje de éxito
        QMessageBox.information(self, "Pago Completado", "¡Pago realizado con éxito!")
        
        # Cerrar la ventana del carrito
        self.close()

        # Actualizar la vista del carrito
        self.mostrar_productos_carrito()

    def actualizar_stock(self):
        """Actualiza el stock de los productos en agregar_productos.json."""
        for producto in self.carrito_data:
            for item in self.agregar_productos_data:
                if item['nombre'] == producto['nombre']:
                    item['stock'] -= producto['cantidad']
                    break
        
        # Guardar los cambios en el archivo de stock
        self.guardar_json("agregar_productos.json", self.agregar_productos_data)


# Inicialización de la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Carrito()
    ventana.show()
    sys.exit(app.exec_())
