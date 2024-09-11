from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QPushButton, QFileDialog
from PySide6.QtCore import QFile
from vistas.agregar import Agregar

class Principal:
    def __init__(self) -> None:
        # Cargamos el archivo .ui que nos da el Designer
        archivo_ui = QFile('./vistas/principal.ui')  # Corrige la ruta si es necesario
        if not archivo_ui.open(QFile.ReadOnly):
            raise FileNotFoundError("No se pudo abrir/encontrar el archivo .ui")
        
        # Cargamos el archivo y lo cerramos
        cargar = QUiLoader()
        self.principal = cargar.load(archivo_ui)
        archivo_ui.close()
        
        # Buscamos el botón agregar Producto
        self.btnAgregarProducto = self.principal.findChild(QPushButton, 'btnAgregarProducto')
        # Hacemos que abra una ventana nueva
        self.btnAgregarProducto.clicked.connect(self.abrir_agregar_producto)
        
    def abrir_agregar_producto(self):
        self.ventana_agregar = Agregar()  # Crear una instancia de Agregar
        self.ventana_agregar.show()       # Mostrar la ventana
