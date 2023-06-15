import pandas as pd
from peewee import *
from modelo_orm import *

db = SqliteDatabase('obras_urbanas.db')

class GestionarObra():
    @classmethod
    def extraer_datos(cls):
        # Leer el archivo CSV y crear un objeto DataFrame
        url = 'observatorio-de-obras-urbanas.csv'
        df = pd.read_csv(url)

        # Realizar manipulaciones necesarias en el DataFrame

    @classmethod
    def conectar_db(cls):
        db.connect()

    @classmethod
    def mapear_orm(cls):
        db.create_tables([Obra])

    @classmethod
    def limpiar_datos(cls):
        pass
        # Realizar la limpieza de datos nulos y no accesibles en el DataFrame

    @classmethod
    def cargar_datos(cls):
        pass
        # Persistir los datos en la base de datos utilizando el método create() de peewee.Model

    @classmethod
    def nueva_obra(cls):
        # Crear una nueva instancia de Obra y persistirla en la base de datos
        obra = Obra()
        # Solicitar los valores requeridos por teclado y asignarlos a los atributos de la obra
        # Realizar búsqueda ORM de registros relacionados y asignarlos a los atributos correspondientes
        obra.save()
        return obra

    @classmethod
    def obtener_indicadores(cls):
        # Obtener información de las obras existentes en la base de datos SQLite utilizando sentencias ORM
        # Mostrar los indicadores por consola
        pass
