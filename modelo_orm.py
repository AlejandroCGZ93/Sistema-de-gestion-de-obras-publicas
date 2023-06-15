from peewee import *

sqlite_db = SqliteDatabase('obras_urbanas.db', pragmas={'journal_mode': 'wal'})
try:
    sqlite_db.connect()
except OperationalError as e:
    print("Error al conectar con la BD.", e)
    exit()

class BaseModel(Model):
    class Meta:
        database = sqlite_db

class Obra(BaseModel):
    tipo_obra = CharField()
    area_responsable = CharField()
    barrio = CharField()
    etapa = CharField()
    destacada = BooleanField()
    fecha_inicio = DateField()
    fecha_fin_inicial = DateField()
    fuente_financiamiento = CharField()
    mano_obra = IntegerField()
    porcentaje_avance = IntegerField()
    plazo_meses = IntegerField()
    empresa = CharField()
    nro_expediente = CharField()
    tipo_contratacion = CharField()
    nro_contratacion = CharField()

    def nuevo_proyecto(self):
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
        self.etapa = 'Rescindida'

