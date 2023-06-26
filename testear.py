from gestionar_obras import *

def main():
    #GestionarObra.extraer_datos()
    #GestionarObra.mapear_orm()
    #GestionarObra.conectar_db()
    #GestionarObra.limpiar_datos()
    #GestionarObra.cargar_datos()
    
    

    while True:
        print("\n===== Menú Principal =====")
        print("1. Crear nueva obra")
        print("2. Obtener indicadores")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            print("\n=====Inserte los datos para la Obra numero 1=====")
            obra = GestionarObra.nueva_obra()
            obra.nuevo_proyecto()
            obra.save()
            obra.iniciar_contratacion()
            obra.save()
            obra.adjudicar_obra()
            obra.save()
            Direccion=input("ingrese la direccion: ")
            Fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            Fecha_fin_inicial = input("Fecha de finalización inicial (YYYY-MM-DD): ")
            Lat=input("ingrese la latitud de la obra: ")
            Lng=input("ingrese la longitud de la obra: ")            
            obra.iniciar_obra(Fecha_inicio, Fecha_fin_inicial, Direccion,Lat,Lng)
            obra.save()
            Porcentaje_avance = input("ingrese el porcentaje de avance de la obra: ") 
            obra.actualizar_porcentaje_avance( Porcentaje_avance)
            obra.save()
            Plazo_meses = input("ingrese el plazo en meses: ")
            obra.incrementar_plazo(Plazo_meses)
            obra.save()
            obra.finalizar_obra()
            obra.save()
            #Segunda intancia de obra
            print("\n======Inserte los datos para la Obra numero 2======")
            segunda_obra = GestionarObra.nueva_obra()
            segunda_obra.nuevo_proyecto()
            segunda_obra.save()
            segunda_obra.iniciar_contratacion()
            segunda_obra.save()
            segunda_obra.adjudicar_obra()
            segunda_obra.save()
            Direccion=input("ingrese la direccion: ")
            Fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            Fecha_fin_inicial = input("Fecha de finalización inicial (YYYY-MM-DD): ")
            Lat=input("ingrese la latitud de la obra: ")
            Lng=input("ingrese la longitud de la obra: ")            
            segunda_obra.iniciar_obra(Fecha_inicio, Fecha_fin_inicial, Direccion,Lat,Lng)
            segunda_obra.save()
            Porcentaje_avance = input("ingrese el porcentaje de avance de la obra: ") 
            segunda_obra.actualizar_porcentaje_avance( Porcentaje_avance)
            segunda_obra.save()
            Plazo_meses = input("ingrese el plazo en meses: ")
            segunda_obra.incrementar_plazo(Plazo_meses)
            segunda_obra.save()
            segunda_obra.rescindir_obra()
            segunda_obra.save()


        elif opcion == "2":
            print("\n====Indicadores====")
            GestionarObra.obtener_indicadores()
            
            
                       
            

        elif opcion == "0":
            print("\n¡Hasta luego!")
            break

        else:
            print("\n¡Opción inválida! Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()

    """me falta terminar los metodos de modelo_orm, armar los indicadores, ver como hacer para crear la tabla empresa y agegarle el cuit"""