from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#Dirección de la bd
DATABASE_URL = "mysql+pymysql://root:root@localhost/pruebasapp"

#Creamos el motor para manejar la bd
engine = create_engine(DATABASE_URL, echo=True)

#Creamos la clase para utilizar con los modelos
Base = declarative_base()


#Creamos las sesiones
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


#Función para tener una sesión de la bd

def obtener_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()