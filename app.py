from config.conexionDb import engine
from modelos.producto import Producto
# Crear las tablas
Producto.metadata.create_all(engine)



