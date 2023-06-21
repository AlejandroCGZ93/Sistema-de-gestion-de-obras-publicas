from gestionar_obras import *

def main():
    obras=GestionarObra()
    obras.extraer_datos()
    obras.mapear_orm()
    obras.conectar_db()
    obras.limpiar_datos()
    obras.cargar_datos()

    while True:
        print("\n===== Menú Principal =====")
        print("1. Crear nueva obra")
        print("2. Obtener indicadores")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            obras.nueva_obra()
            print(f"\nSe ha creado la obra con ID: {obras.id}")

        elif opcion == "2":
            obras.obtener_indicadores()
            print("\n====Indicadores====")
            print(obras.indicadores)
                       
            

        elif opcion == "0":
            print("\n¡Hasta luego!")
            break

        else:
            print("\n¡Opción inválida! Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()