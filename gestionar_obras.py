from peewee import *
from modelo_orm import *
from leer_archivo import *

db = SqliteDatabase('obras_urbanas.db')

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
            db.create_tables([Entorno,Etapa, AreaResponsable,TipoObra,Barrio,TipoContratacion, Empresa, Obra]) # se pasa como argumento una clase o una lista de clases (que son las tablas) que se quiere crear dentro de la base de datos este obra hace referencia a la clase obra del archivo modelo_orm
        except OperationalError as e:
            print("Se ha generado un error al crear las tablas en la Base de Datos.", e)
            exit()
        print("Se han creado la stablas en la base de datos")

    @classmethod
    def limpiar_datos(cls):
         # Realizar la limpieza de datos nulos y no accesibles en el DataFrame  
        #limpia todas las filas nulas en una sola vez no funciona con esto
        #cls.df.dropna(inplace=True)    
        
        #limpiar datos nulos     
        # cls.df.dropna(subset = ['tipo'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['descripcion'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['monto_contrato'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['comuna'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['barrio'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['direccion'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['lat'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['lng'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['fecha_inicio'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['fecha_fin_inicial'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['plazo_meses'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['porcentaje_avance'], axis =0, inplace = True)        
        # cls.df.dropna(subset = ['licitacion_oferta_empresa'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['licitacion_anio'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['contratacion_tipo'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['nro_contratacion'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['cuit_contratista'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['beneficiarios'], axis =0, inplace = True)                 
        # cls.df.dropna(subset = ['link_interno'], axis =0, inplace = True)
        # cls.df.dropna(subset = ['pliego_descarga'], axis =0, inplace = True)
        
        limpiar_columnas = ['tipo', 'descripcion', 'monto_contrato', 'comuna', 'barrio', 'direccion', 'lat', 'lng', 'fecha_inicio', 'fecha_fin_inicial', 'plazo_meses', 'porcentaje_avance', 'licitacion_oferta_empresa', 'licitacion_anio', 'contratacion_tipo', 'nro_contratacion', 'cuit_contratista', 'beneficiarios', 'link_interno', 'pliego_descarga']
        
        cls.df.dropna(subset = limpiar_columnas, axis =0, inplace = True)

        # sacar solo los valores unicos

        cls.data_uniqueE = list(cls.df['entorno'].unique())  

        cls.data_uniqueT = list(cls.df['tipo'].unique()) 

        cls.data_uniqueA = list(cls.df['area_responsable'].unique())
        
        cls.data_uniqueB = list(cls.df['barrio'].unique())

        cls.data_uniqueEta = list(cls.df['etapa'].unique())

        cls.data_uniqueCo = list(cls.df['contratacion_tipo'].unique())

        #valores unicos para la tabal empresa
              
        df_empresa=cls.df[['licitacion_oferta_empresa','nro_contratacion']]
        df_empresa=df_empresa.drop_duplicates()
        cls.lis_empresa=df_empresa.values

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

        for elem in cls.lis_empresa:
            try:
                Empresa.create(nombre_empresa=elem[0], cuit_empresa=elem[1])
            except IntegrityError as e:
                print("Error al insertar un nuevo registro en la tabla Empressa", e)
        print("Se han persistido las empresas en la base de datos")

        for elem in cls.df.values:
            nombre_ent=Entorno.get(Entorno.nombre_entorno== elem[1])
            nombre_e=Etapa.get(Etapa.nombre_etapa==elem[3])
            nombre_Tip=TipoObra.get(TipoObra.nombre_Tipo== elem[4])
            nombre_Are=AreaResponsable.get(AreaResponsable.nombre_Responsable== elem[5])
            nombre_Bar=Barrio.get(Barrio.nombre_Barrio==elem[9])
            nombre_con=TipoContratacion.get(TipoContratacion.nombre_tcontratacion==elem[23])
            nombre_emp=Empresa.get(Empresa.nombre_empresa==elem[21])
            try:
                Obra.create(entorno=nombre_ent,nombre=elem[2], etapa = nombre_e,tipo = nombre_Tip ,area_responsable = nombre_Are, descripcion=elem[6], monto_contrato=elem[7],comuna=elem[8],barrio = nombre_Bar,direccion=elem[10],lat=elem[11],lng=elem[12],fecha_inicio = elem[13],fecha_fin_inicial = elem[14],plazo_meses = elem[15],porcentaje_avance =elem[16], empresa=nombre_emp, licitacion_anio=elem[22],tipo_contratacion = nombre_con, nro_contratacion = elem[24],beneficiarios=elem[26],link_interno = elem[31], pliego_descarga = elem[32])
            except ImportError as e:
                print("Error al insertar un registro en la tabla viakes.", e)
        print("los registros se han persistido en la tabla Obras.")     

    @classmethod
    def nueva_obra(cls):
       #busca dentro de la tabla entorno el entrono insertado por teclado
       #tengo los valores asi para probar mas facil el entorno cuando terminemos antes de entregar hay que quitar esto. 

        validarEntorno=None
        encontrado=False
        while not encontrado:
            Entorno_nombre="Acumar"#input("ingrese el nombre del Entorno: ") 
            try:
                validarEntorno=Entorno.get(Entorno.nombre_entorno == Entorno_nombre)
                encontrado=True
                Entorno_nombre=validarEntorno
            except Entorno.DoesNotExist:
                print("el Entorno ingresado no coincide con los que se encuentran en la base de datos intente nuevamente")        

        Nombre_O="Mary"#input("ingrese el nombre de la obra: ")      
        
        #busca dentro de la tabla Tipo de obra el tipo de obra insertada por teclado
        validarTipo=None
        x=False
        while not x:
            Tipo ="Vivienda"# input("Tipo de obra: ")
            try:
                validarTipo=TipoObra.get(TipoObra.nombre_Tipo == Tipo)
                x=True
                Tipo=validarTipo
            except TipoObra.DoesNotExist:
                print("El tipo de obra ingresado no existe intente nuevamente")          
         
        Descripcion="sjhdfjsyhfyhf"#input("ingrese una descripcion para la obra: ")
        
        #busca dentro de la tabla Area Responsable el area insertada por teclado
        validarArea=None
        m=False
        while not m:
            area_responsable ="Instituto de la Vivienda"# input("Tipo el area responsable: ")
            try:
                validarArea=AreaResponsable.get(AreaResponsable.nombre_Responsable == area_responsable)
                m=True
                area_responsable=validarArea
            except AreaResponsable.DoesNotExist:
                print("El tipo de area ingresado no existe intente nuevamente")  
       
        Monto_contrato="250000" #input("ingrese Monto de contrato: ")
        Comuna="15"#input("ingrese la comuna: ")

        #busca dentro de la tabla Area Responsable el area insertada por teclado
        validarBarrio=None
        j=False
        while not j:
            barrio_nombre = "Villa Devoto"#input("Ingrese el Barrio: ")
            try:
                validarBarrio=Barrio.get(Barrio.nombre_Barrio == barrio_nombre)
                j=True
                barrio_nombre=validarBarrio
            except Barrio.DoesNotExist:
                print("El barrio ingresado no existe intente nuevamente")  
        
        Beneficiarios="25000"#input("ingrese la cantidad de beneficiarios por esta obra: ")
        Link_interno = "sdsdfdsfdsfds"#input("ingrese el link interno: ")
        Pliego_descarga = "dfsfsdfdffdf" #input("ingrese el link pliego descarga: ")

        obra = Obra.create(
            
                entorno=Entorno_nombre,
                nombre=Nombre_O,
                etapa = "Finalizada",
                tipo = Tipo,
                area_responsable = area_responsable,
                descripcion=Descripcion,
                monto_contrato=Monto_contrato,
                comuna=Comuna,
                barrio = barrio_nombre,                
                empresa="Pecam",                
                tipo_contratacion = "Contratacion Directa",                
                beneficiarios=Beneficiarios, 
                link_interno = Link_interno,
                pliego_descarga = Pliego_descarga
        )
        
        obra.save()
        print(f"\nSe ha creado la obra con ID: {obra.id}") 
        return obra

    @classmethod
    def obtener_indicadores(cls):
        # a. Listado de todas las áreas responsables
        areas_responsables = AreaResponsable.select()
        print("Áreas Responsables:")
        for area in areas_responsables:
            print(f"- {area.nombre_Responsable}")

        # b. Listado de todos los tipos de obra
        tipos_obra = TipoObra.select()
        print("\nTipos de Obra:")
        for tipo in tipos_obra:
            print(f"- {tipo.nombre_Tipo}")

        # c. Cantidad de obras que se encuentran en cada etapa
        etapas = Etapa.select()
        print("\nCantidad de obras por etapa:")
        for etapa in etapas:
            cantidad = Obra.select().where(Obra.etapa == etapa).count()
            print(f"- {etapa.nombre_etapa}: {cantidad}")

        # d. Cantidad de obras por tipo de obra
        print("\nCantidad de obras por tipo de obra:")
        for tipo in tipos_obra:
            cantidad = Obra.select().where(Obra.tipo == tipo).count()
            print(f"- {tipo.nombre_Tipo}: {cantidad}")

        # e. Listado de todos los barrios pertenecientes a las comunas 1, 2 y 3
        comuna_barrios = {}

        query = (Obra
                 .select(Obra.comuna, Barrio.nombre_Barrio)
                 .join(Barrio, on=(Obra.barrio_id == Barrio.id))
                 .where(Obra.comuna.in_([1, 2, 3]))
                 .group_by(Obra.comuna, Barrio.nombre_Barrio)
                 .order_by(Obra.comuna, Barrio.nombre_Barrio))
        
        for result in query:
            comuna = result.comuna
            barrio = result.barrio.nombre_Barrio
        
            if comuna in comuna_barrios:
                if barrio not in comuna_barrios[comuna]:
                    comuna_barrios[comuna].append(barrio)
            else:
                comuna_barrios[comuna] = [barrio]
                
        print("\nListado de los barrios pertenecientes a las comunas 1,2 y 3. En caso de no haber registros, no se mostraran en la pantalla:")        
        for comuna, barrios in comuna_barrios.items():
            print(f"Comuna {comuna}: {', '.join(barrios)}")
    
        #f. Cantidad de obras “Finalizadas” en la comuna 1
        obras_finalizadas_comuna1 = (
            Obra.select()
            .join(Barrio)
            .join(Etapa, on=(Obra.etapa_id == Etapa.id))
            .where(Etapa.nombre_etapa == "Finalizada", Obra.comuna == "1")
            .count()
        )
        print(f"\nObras finalizadas en la comuna 1: {obras_finalizadas_comuna1}")
        
        # g. Cantidad de obras “Finalizadas” en un plazo menor o igual a 24 meses
        obras_finalizadas_24_meses = (Obra.select()
                                          .join(Etapa, on=(Obra.etapa_id == Etapa.id))
                                          .where(Etapa.nombre_etapa == "Finalizada", Obra.plazo_meses >= 24).count())
        print(f"\nObras finalizadas en un plazo menor o igual a 24 meses: {obras_finalizadas_24_meses}")






