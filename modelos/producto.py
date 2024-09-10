from sqlalchemy import Column, Integer, String, Float
from config.conexionDb import Base

#Definimos la clase Producto

class Producto(Base): #Tiene importado como parametro la conexión hecha en config
    __tablename__ = 'productos'
    
    #Declaramos las columnas de la tabla
    id = Column(Integer, primary_key=True, index=True) 
    #Seguimos con el resto aqui abajo...
    
    
    
    #Esto es para que podamos ver los datos bien y no como si fuesemos una placa madre
    def __repr__(self):
        return f"<Producto(nombre={self.nombre}, precio={self.precio}, stock={self.stock})>"