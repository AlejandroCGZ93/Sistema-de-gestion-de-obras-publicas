from peewee import *

#conexion a la base de dato
sqlite_db = SqliteDatabase('./sistema-de-gestion-de-obras-publicas/obras_urbanas.db', pragmas={'journal_mode': 'wal'}) 

try:
    sqlite_db.connect()
except OperationalError as e:
    print("Error al conectar con la Base de Dsatos.", e)
    exit()

class BaseModel(Model):
    class Meta:
        database = sqlite_db #apunta a la base de dato tod el modelo orm va persistir en esa base de dato

#se crea la tabla obra y los atributos son campos dentro de la tabla y lo que esta despues del igual el tipo de dato que va tomar dentro de la base de datos
class Entorno(BaseModel):
    nombre_entorno=CharField(unique=True)

class AreaResponsable(BaseModel):
    nombre_Responsable = CharField(unique=True)

class TipoObra(BaseModel):
    nombre_Tipo = CharField(unique=True)

class Barrio(BaseModel):
    nombre_Barrio = CharField(unique=True)

class Obra(BaseModel):    
    entorno=ForeignKeyField(Entorno)
    nombre=CharField()
    etapa = CharField()
    tipo = ForeignKeyField(TipoObra)
    area_responsable = ForeignKeyField(AreaResponsable)
    descripcion=CharField()
    monto_contrato=CharField()
    comuna=CharField()
    barrio = ForeignKeyField(Barrio)
    direccion=CharField()
    lat=CharField()
    lng=CharField()
    fecha_inicio = DateField()
    fecha_fin_inicial = DateField()
    plazo_meses = CharField()
    porcentaje_avance = CharField()    
    licitacion_oferta_empresa=CharField()
    licitacion_anio=CharField()
    tipo_contratacion = CharField()
    nro_contratacion = CharField()
    cuit_contratista=CharField()
    beneficiarios=CharField()   
    link_interno = CharField()
    pliego_descarga = CharField()
    
    
    def __str__(self):
        return self.nombre

    """def nuevo_proyecto(self):
        self.etapa = 'Proyecto'

    def iniciar_contratacion(self, tipo_contratacion, nro_contratacion):
        self.tipo_contratacion = tipo_contratacion
        self.nro_contratacion = nro_contratacion

    def adjudicar_obra(self, empresa, nro_expediente):
        self.empresa = empresa
        self.nro_expediente = nro_expediente

    def iniciar_obra(self, destacada, fecha_inicio, fecha_fin_inicial, fuente_financiamiento, mano_obra):
        self.destacada = destacada
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_inicial = fecha_fin_inicial
        self.fuente_financiamiento = fuente_financiamiento
        self.mano_obra = mano_obra

    def actualizar_porcentaje_avance(self, porcentaje_avance):
        self.porcentaje_avance = porcentaje_avance

    def incrementar_plazo(self, plazo_meses):
        self.plazo_meses += plazo_meses

    def incrementar_mano_obra(self, mano_obra):
        self.mano_obra += mano_obra

    def finalizar_obra(self):
        self.etapa = 'Finalizada'
        self.porcentaje_avance = 100

    def rescindir_obra(self):
        self.etapa = 'Rescindida'"""

