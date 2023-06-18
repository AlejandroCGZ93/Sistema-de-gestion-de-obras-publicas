import pandas as pd
from peewee import *
from modelo_orm import *
from leer_archivo import *

db = SqliteDatabase('./sistema-de-gestion-de-obras-publicas/obras_urbanas.db')


class GestionarObra():
    @classmethod
    def extraer_datos(cls):
        cls.df=leer_archivo()
        
        if cls.df is False:
            exit()
        
        print(cls.df.head()) 
        print(cls.df.count())
        print(cls.df.columns)     

    @classmethod
    def conectar_db(cls):
        
       db.connect()

    @classmethod
    def mapear_orm(cls):
        try:
            db.create_tables([Entorno,Obra]) # se pasa como argumento una clase o una lista de clases (que son las tablas) que se quiere crear dentro de la base de datos este obra hace referencia a la clase obra del archivo modelo_orm
        except OperationalError as e:
            print(" se ha generado un error al crear las tablas en la Base de Datos.", e)
            exit()


    @classmethod
    def limpiar_datos(cls):
         # Realizar la limpieza de datos nulos y no accesibles en el DataFrame
        cls.df=leer_archivo()
        
        if cls.df is False:
            exit() 

        # sacar solo los valores unicos
        cls.data_unique = list(cls.df['entorno'].unique())  
        #limpiar datos nulos     
        cls.df.dropna(subset = ['tipo'], axis =0, inplace = True)
        cls.df.dropna(subset = ['descripcion'], axis =0, inplace = True)
        cls.df.dropna(subset = ['monto_contrato'], axis =0, inplace = True)
        cls.df.dropna(subset = ['comuna'], axis =0, inplace = True)
        cls.df.dropna(subset = ['barrio'], axis =0, inplace = True)
        cls.df.dropna(subset = ['direccion'], axis =0, inplace = True)
        cls.df.dropna(subset = ['lat'], axis =0, inplace = True)
        cls.df.dropna(subset = ['lng'], axis =0, inplace = True)
        cls.df.dropna(subset = ['fecha_inicio'], axis =0, inplace = True)
        cls.df.dropna(subset = ['fecha_fin_inicial'], axis =0, inplace = True)
        cls.df.dropna(subset = ['plazo_meses'], axis =0, inplace = True)
        cls.df.dropna(subset = ['porcentaje_avance'], axis =0, inplace = True)
        cls.df.dropna(subset = ['imagen_1'], axis =0, inplace = True)
        cls.df.dropna(subset = ['imagen_2'], axis =0, inplace = True)
        cls.df.dropna(subset = ['imagen_3'], axis =0, inplace = True)
        cls.df.dropna(subset = ['imagen_4'], axis =0, inplace = True)
        cls.df.dropna(subset = ['licitacion_oferta_empresa'], axis =0, inplace = True)
        cls.df.dropna(subset = ['licitacion_anio'], axis =0, inplace = True)
        cls.df.dropna(subset = ['contratacion_tipo'], axis =0, inplace = True)
        cls.df.dropna(subset = ['nro_contratacion'], axis =0, inplace = True)
        cls.df.dropna(subset = ['cuit_contratista'], axis =0, inplace = True)
        cls.df.dropna(subset = ['beneficiarios'], axis =0, inplace = True)
        cls.df.dropna(subset = ['mano_obra'], axis =0, inplace = True)
        cls.df.dropna(subset = ['compromiso'], axis =0, inplace = True)
        cls.df.dropna(subset = ['destacada'], axis =0, inplace = True)
        cls.df.dropna(subset = ['ba_elige'], axis =0, inplace = True)        
        cls.df.dropna(subset = ['link_interno'], axis =0, inplace = True)
        cls.df.dropna(subset = ['pliego_descarga'], axis =0, inplace = True)
        cls.df.dropna(subset = ['expediente-numero'], axis =0, inplace = True)
        cls.df.dropna(subset = ['estudio_ambiental_descarga'], axis =0, inplace = True)
        cls.df.dropna(subset = ['financiamiento'], axis =0, inplace = True)

       

    @classmethod
    def cargar_datos(cls):
    # Persistir los datos en la base de datos utilizando el método create() de peewee.Model
        for elem in cls.data_unique:
            try:
                Entorno.create(nombre_entorno=elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Entorno", e)
        print("se han persistido los tipos de Entorno en la base de datos")

        for elem in cls.df.values:
            nombre_ent=Entorno.get(Entorno.nombre_entorno== elem[0])
            try:
                Obra.create(entorno=nombre_ent,nombre=elem[1], etapa = elem[2],tipo = elem[3],area_responsable = elem[4], descripcion=elem[5], monto_contrato=elem[6],comuna=elem[7],barrio = elem[8],direccion=elem[9],lat=elem[10],lng=elem[11],fecha_inicio = elem[12],fecha_fin_inicial = elem[13],plazo_meses = elem[14],porcentaje_avance =elem[15],imagen_1=elem[16],imagen_2=elem[17], imagen_3=elem[18],imagen_4=elem[19],   licitacion_oferta_empresa=elem[20], licitacion_anio=elem[21],tipo_contratacion = elem[22], nro_contratacion = elem[23], cuit_contratista=elem[24],beneficiario=elem[25], mano_obra = elem[26],compromiso = elem[27],destacada = elem[28],ba_elige = elem[29], link_interno = elem[30], pliego_descarga = elem[31],nro_expediente = elem[32],   estudio_ambiental_descarga = elem[33], financiamiento = elem[34])
            except ImportError as e:
                print("Error al insertar un registro en la tabla viakes.", e)
        print("los registros se han persistido en la tabla Obras.")

        #no m esta almacenando estos valores por alguna razon
        

    """ @classmethod
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
        pass"""


#testear
"""Tabla=GestionarObra()
Tabla.mapear_orm()
Tabla.limpiar_datos()
Tabla.cargar_datos()"""