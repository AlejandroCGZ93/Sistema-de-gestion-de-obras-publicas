
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
        
        """print(cls.df.head()) 
        print(cls.df.count())
        print(cls.df.columns) """    

    @classmethod
    def conectar_db(cls):
        
       db.connect()
       

    @classmethod
    def mapear_orm(cls):
        try:
            db.create_tables([Entorno,Etapa, AreaResponsable,TipoObra,Barrio,TipoContratacion, Obra]) # se pasa como argumento una clase o una lista de clases (que son las tablas) que se quiere crear dentro de la base de datos este obra hace referencia a la clase obra del archivo modelo_orm
        except OperationalError as e:
            print("Se ha generado un error al crear las tablas en la Base de Datos.", e)
            exit()
        print("Se han creado la stablas en la base de datos")


    @classmethod
    def limpiar_datos(cls):
         # Realizar la limpieza de datos nulos y no accesibles en el DataFrame       

        # sacar solo los valores unicos
        cls.data_uniqueE = list(cls.df['entorno'].unique())  

        cls.data_uniqueT = list(cls.df['tipo'].unique()) 

        cls.data_uniqueA = list(cls.df['area_responsable'].unique())
        
        cls.data_uniqueB = list(cls.df['barrio'].unique())

        cls.data_uniqueEta = list(cls.df['etapa'].unique())

        cls.data_uniqueCo = list(cls.df['contratacion_tipo'].unique())



        #limpia todas las filas nulas en una sola vez no funciona con esto
        #cls.df.dropna(inplace=True)

    
        
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
        cls.df.dropna(subset = ['licitacion_oferta_empresa'], axis =0, inplace = True)
        cls.df.dropna(subset = ['licitacion_anio'], axis =0, inplace = True)
        cls.df.dropna(subset = ['contratacion_tipo'], axis =0, inplace = True)
        cls.df.dropna(subset = ['nro_contratacion'], axis =0, inplace = True)
        cls.df.dropna(subset = ['cuit_contratista'], axis =0, inplace = True)
        cls.df.dropna(subset = ['beneficiarios'], axis =0, inplace = True)                 
        cls.df.dropna(subset = ['link_interno'], axis =0, inplace = True)
        cls.df.dropna(subset = ['pliego_descarga'], axis =0, inplace = True)
              
        

      

    @classmethod
    def cargar_datos(cls):
    # Persistir los datos en la base de datos utilizando el método create() de peewee.Model
        for elem in cls.data_uniqueE:
            try:
                Entorno.create(nombre_entorno=elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Entorno", e)
        print("se han persistido los tipos de Entorno en la base de datos")

        for elem in cls.data_uniqueEta:
            try:
                Etapa.create(nombre_etapa=elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Etapa", e)
        print("se han persistido los tipos de Etapa en la base de datos")

        for elem in cls.data_uniqueT:
            try:
                TipoObra.create(nombre_Tipo=elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Tipo obra", e)
        print("Se han persistido los tipos de Obraen la base de datos")

        for elem in cls.data_uniqueA:
            try:
                AreaResponsable.create(nombre_Responsable=elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Area Responsable", e)
        print("Se han persistido las areas responsables en la base de datos")

        for elem in cls.data_uniqueB:
            try:
                Barrio.create(nombre_Barrio=elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Barrio", e)
        print("Se han persistido los barrios en la base de datos")

        for elem in cls.data_uniqueCo:
            try:
                TipoContratacion.create(nombre_tcontratacion=elem)
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla tipo de contratacion", e)
        print("Se han persistido los tipos de contratacion en la base de datos")

        for elem in cls.df.values:
            nombre_ent=Entorno.get(Entorno.nombre_entorno== elem[1])
            nombre_e=Etapa.get(Etapa.nombre_etapa==elem[3])
            nombre_Tip=TipoObra.get(TipoObra.nombre_Tipo== elem[4])
            nombre_Are=AreaResponsable.get(AreaResponsable.nombre_Responsable== elem[5])
            nombre_Bar=Barrio.get(Barrio.nombre_Barrio==elem[9])
            nombre_con=TipoContratacion.get(TipoContratacion.nombre_tcontratacion==elem[23])
            try:
                Obra.create(entorno=nombre_ent,nombre=elem[2], etapa = nombre_e,tipo = nombre_Tip ,area_responsable = nombre_Are, descripcion=elem[6], monto_contrato=elem[7],comuna=elem[8],barrio = nombre_Bar,direccion=elem[10],lat=elem[11],lng=elem[12],fecha_inicio = elem[13],fecha_fin_inicial = elem[14],plazo_meses = elem[15],porcentaje_avance =elem[16], licitacion_oferta_empresa=elem[21], licitacion_anio=elem[22],tipo_contratacion = nombre_con, nro_contratacion = elem[24], cuit_contratista=elem[25],beneficiarios=elem[26],link_interno = elem[31], pliego_descarga = elem[32])
            except ImportError as e:
                print("Error al insertar un registro en la tabla viakes.", e)
        print("los registros se han persistido en la tabla Obras.")     

    
        

    @classmethod
    def nueva_obra(cls):
       #busca dentro de la tabla entorno el entrono insertado por teclado
       

        validarEntorno=None
        encontrado=False
        while not encontrado:
            Entorno_nombre=input("ingrese el nombre del Entorno: ") 
            try:
                validarEntorno=Entorno.get(Entorno.nombre_entorno == Entorno_nombre)
                encontrado=True
                Entorno_nombre=validarEntorno
            except Entorno.DoesNotExist:
                print("el Entorno ingresado no coincide con los que se encuentran en la base de datos intente nuevamente")        

        Nombre_O=input("ingrese el nombre: ")  

        ##busca dentro de la tabla Etapa las etapas insertadas por teclado
        validarEtapa=None
        eta=False
        while not eta:
            estado_Etapa = input("ingrese el estado de la etapa: ")
            try:
                validarEtapa=Etapa.get(Etapa.nombre_etapa == estado_Etapa)
                eta=True
                estado_Etapa=validarEtapa
            except Etapa.DoesNotExist:
                print("la etapa ingresado no coincide con los que se encuentran en la base de datos intente nuevamente")

        
        
        #busca dentro de la tabla Tipo de obra el tipo de obra insertada por teclado
        validarTipo=None
        x=False
        while not x:
            Tipo = input("Tipo de obra: ")
            try:
                validarTipo=TipoObra.get(TipoObra.nombre_Tipo == Tipo)
                x=True
                Tipo=validarTipo
            except TipoObra.DoesNotExist:
                print("El tipo de obra ingresado no existe intente nuevamente")          
         
        Descripcion=input("ingrese una descripcion: ")
        
        #busca dentro de la tabla Area Responsable el area insertada por teclado
        validarArea=None
        m=False
        while not m:
            area_responsable = input("Tipo el area responsable: ")
            try:
                validarArea=AreaResponsable.get(AreaResponsable.nombre_Responsable == area_responsable)
                m=True
                area_responsable=validarArea
            except AreaResponsable.DoesNotExist:
                print("El tipo de area ingresado no existe intente nuevamente")  
        
       
        Monto_contrato=input("ingrese Monto de contrato: ")
        Comuna=input("ingrese la comuna: ")

        #busca dentro de la tabla Area Responsable el area insertada por teclado
        validarBarrio=None
        j=False
        while not j:
            barrio_nombre = input("Ingrese el Barrio: ")
            try:
                validarBarrio=Barrio.get(Barrio.nombre_Barrio == barrio_nombre)
                j=True
                barrio_nombre=validarBarrio
            except Barrio.DoesNotExist:
                print("El barrio ingresado no existe intente nuevamente")  
        
        Direccion=input("ingrese la direccion: ")
        Lat=input("ingrese la latitud de la obra: ")
        Lng=input("ingrese la longitud de la obra: ")
        Fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
        Fecha_fin_inicial = input("Fecha de finalización inicial (YYYY-MM-DD): ")
        Plazo_meses = input("ingrese el plazo en meses: ")
        Porcentaje_avance = input("ingrese el porcentaje de avance: ")  
        Licitacion_oferta_empresa=input("ingrese la licitacion de oferta: ")
        Licitacion_anio=input("ingrese el año de la licitacion: ")
        
        #busca dentro de la tabla Tipo de contratacion el tipo insertada por teclado
        validarTCon=None
        tc=False
        while not tc:
            Tipo_contratacion = input("ingrese el tipo de contratacion: ")
            try:
                validarTCon=TipoContratacion.get(TipoContratacion.nombre_tcontratacion == Tipo_contratacion)
                tc=True
                Tipo_contratacion=validarTCon
            except TipoContratacion.DoesNotExist:
                print("El tipo de contratacion ingresado no existe intente nuevamente") 
        
        Nro_contratacion =input("ingrese el numero de la contratacion: ")
        Cuit_contratista=input("ingrese el cuit del contratista: ")
        Beneficiarios=input("ingrese la cantidad de beneficiarios por esta obra: ")
        Link_interno = input("ingrese el link interno: ")
        Pliego_descarga = input("ingrese el link pliego descarga: ")
        
        

        obra = Obra.create(
            
                entorno=Entorno_nombre,
                nombre=Nombre_O,
                etapa = estado_Etapa,
                tipo = Tipo,
                area_responsable = area_responsable,
                descripcion=Descripcion,
                monto_contrato=Monto_contrato,
                comuna=Comuna,
                barrio = barrio_nombre,
                direccion=Direccion,
                lat=Lat,
                lng=Lng,
                fecha_inicio = Fecha_inicio,
                fecha_fin_inicial = Fecha_fin_inicial,
                plazo_meses = Plazo_meses,
                porcentaje_avance = Porcentaje_avance,  
                licitacion_oferta_empresa=Licitacion_oferta_empresa,
                licitacion_anio=Licitacion_anio,
                tipo_contratacion = Tipo_contratacion,
                nro_contratacion = Nro_contratacion,
                cuit_contratista=Cuit_contratista,
                beneficiarios=Beneficiarios, 
                link_interno = Link_interno,
                pliego_descarga = Pliego_descarga
        )
        
        obra.save()
        return obra

    @classmethod
    def obtener_indicadores(cls):

        obras_totales = Obra.select().count()
        obras_finalizadas = Obra.select().where(Obra.etapa == "Finalizada").count()
        obras_en_progreso = Obra.select().where(Obra.etapa != "Finalizada").count()   

        cls.indicadores = {
            "obras_totales": obras_totales,
            "obras_finalizadas": obras_finalizadas,
            "obras_en_progreso": obras_en_progreso,
            
            
        }
        #print(indicadores)
        return cls.indicadores

    


#testear
#Tabla=GestionarObra()

#Tabla.extraer_datos()
#Tabla.mapear_orm()
#Tabla.limpiar_datos()
#Tabla.cargar_datos()
#Tabla.nueva_obra()
#Tabla.obtener_indicadores()

