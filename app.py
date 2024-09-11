from PySide6.QtCore import QCoreApplication, Qt

# Configura OpenGL
QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)


from PySide6.QtWidgets import QApplication

from config.conexionDb import engine
from modelos.producto import Producto

from vistas.principal import Principal

# Crear las tablas
Producto.metadata.create_all(engine)



if __name__ == "__main__":
    
    import sys
    
    #Creamos la app
    app = QApplication(sys.argv)
    
    #Creamos la instancia de la ventana principal
    ventana_principal = Principal()
    
    #Mostramos la ventana
    ventana_principal.principal.show()
    
    
    #Ejecutamos 
    sys.exit(app.exec())