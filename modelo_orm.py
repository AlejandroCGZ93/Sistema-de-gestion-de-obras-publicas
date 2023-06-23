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

class Etapa(BaseModel):
    nombre_etapa=CharField(unique=True)

class AreaResponsable(BaseModel):
    nombre_Responsable = CharField(unique=True)

class TipoObra(BaseModel):
    nombre_Tipo = CharField(unique=True)

class Barrio(BaseModel):
    nombre_Barrio = CharField(unique=True)

class Empresa(BaseModel):
    nombre_empresas= CharField(unique=True)
    cuit_contratista=CharField()


class TipoContratacion(BaseModel):
    nombre_tcontratacion = CharField(unique=True)

class Empresa(BaseModel):
    nombre_empresa=CharField()
    cuit_empresa=CharField()

class Obra(BaseModel): 
      
    entorno=ForeignKeyField(Entorno)
    nombre=CharField()
    etapa = ForeignKeyField(Etapa)
    tipo = ForeignKeyField(TipoObra)
    area_responsable = ForeignKeyField(AreaResponsable)
    descripcion=CharField()
    monto_contrato=CharField()
    comuna=CharField()
    barrio = ForeignKeyField(Barrio)
    direccion=CharField(null=True)
    lat=CharField(null=True)
    lng=CharField(null=True)
    fecha_inicio = DateField(null=True)
    fecha_fin_inicial = DateField(null=True)
    plazo_meses = CharField(null=True)
    porcentaje_avance = CharField(null=True)    
    empresa=ForeignKeyField(Empresa)
    licitacion_anio=CharField(null=True)
    tipo_contratacion = ForeignKeyField(TipoContratacion)    
    nro_contratacion = CharField(null=True)    
    beneficiarios=CharField()   
    link_interno = CharField()
    pliego_descarga = CharField()   

    def nuevo_proyecto(self):
        
        try:
            etapa=Etapa.get(nombre_etapa="Proyecto")
            self.etapa=etapa
        except Etapa.DoesNotExist:
            etapa=Etapa.create(nombre_etapa="Proyecto") 
            self.etapa=etapa       
        

    def iniciar_contratacion(self):
        validarTCon=None
        tc=False
        while not tc:
            Tipo_contratacion = input("ingrese el tipo de contratacion: ")
            try:
                validarTCon=TipoContratacion.get(TipoContratacion.nombre_tcontratacion == Tipo_contratacion)
                tc=True
                self.tipo_contratacion=validarTCon
            except TipoContratacion.DoesNotExist:
                print("El tipo de contratacion ingresado no existe intente nuevamente") 
        self.nro_contratacion =input("ingrese el numero de la contratacion: ")

    def adjudicar_obra(self):
        validarEmpresa=None
        em=False
        while not em:
            Tipo_empresa = input("ingrese el nombre de la empresa : ")
            try:
                validarEmpresa=Empresa.get(Empresa.nombre_empresa == Tipo_empresa)
                em=True
                self.empresa=validarEmpresa
            except Empresa.DoesNotExist:
                print("El nombre de la empresa ingresado no existe intente nuevamente") 
        #pide a de mas que ponga el numero de expediente pero el numero de expediente es uno de los atributos que elimine por que tiene muy pocos registros con valores asignados y hace que el data set quede vacio agregue año de licitacion.
        self.licitacion_anio=input("ingrese el año de la licitacion: ") 

    def iniciar_obra(self, fecha_inicio, fecha_fin_inicial, direccion,lat,lon):
        
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_inicial = fecha_fin_inicial
        self.direccion = direccion
        self.lat=lat
        self.lng=lon
        
        #pide tambien fuente de financiamiento que era tambien un atributo con muy pocos registros con valores tambien lo elimine, al igual que mano de obra y destacada, agregue aqui direccion, la latitud, la longitud y plazo meses
        

    def actualizar_porcentaje_avance(self, nuevo_porcentaje_avance):
        self.porcentaje_avance=nuevo_porcentaje_avance
        

    def incrementar_plazo(self, nuevo_plazo_meses):
        self.plazo_meses=nuevo_plazo_meses
        

    def incrementar_mano_obra(self, mano_obra):
        pass

    def finalizar_obra(self):
        self.etapa="Finalizada"
        self.porcentaje_avance=100
        

    def rescindir_obra(self):
        self.etapa="Recindida"

#no se como hacer el proceso de iniciar proyecto y eso y como siguen los pasos desde ahi
# como hago para usar estos metodos en testear tengo que llamarlos desde getionar_obras?

