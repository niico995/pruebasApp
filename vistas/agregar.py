from PySide6.QtWidgets import QDialog, QVBoxLayout, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class Agregar(QDialog):
    def __init__(self) -> None:
        super().__init__()

        archivo_ui = QFile('./vistas/agregar_producto.ui')
        if not archivo_ui.open(QFile.ReadOnly):
            print("No se pudo abrir el archivo .ui")
            raise FileNotFoundError("No se pudo abrir/encontrar el archivo .ui")
        
        loader = QUiLoader()
        self.ui = loader.load(archivo_ui, self)  # Cargar el archivo .ui en la instancia de QDialog
        archivo_ui.close()
        
        if not self.ui:
            print("No se pudo cargar el archivo .ui en la instancia de QDialog")
            raise RuntimeError("No se pudo cargar el archivo .ui en la instancia de QDialog")
        
        print("Archivo .ui cargado correctamente")

        # Mostrar los nombres de los widgets para depuración
        self.print_widget_names(self.ui)

        

    def print_widget_names(self, widget):
        print(f'Widget: {widget.objectName()}')
        for child in widget.findChildren(QWidget):
            self.print_widget_names(child)
