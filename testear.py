from gestionar_obras import GestionarObra

def main():
    GestionarObra.conectar_db()
    GestionarObra.cargar_datos()

    while True:
        print("\n===== Menú Principal =====")
        print("1. Crear nueva obra")
        print("2. Obtener indicadores")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            obra = GestionarObra.nueva_obra()
            print(f"\nSe ha creado la obra con ID: {obra.id}")

        elif opcion == "2":
            indicadores = GestionarObra.obtener_indicadores()
            print("\nIndicadores:")
            print(f"Obras totales: {indicadores['obras_totales']}")
            print(f"Obras finalizadas: {indicadores['obras_finalizadas']}")
            print(f"Obras en progreso: {indicadores['obras_en_progreso']}")            
            print(f"Porcentaje de avance promedio: {indicadores['porcentaje_avance_promedio']}%")

        elif opcion == "0":
            print("\n¡Hasta luego!")
            break

        else:
            print("\n¡Opción inválida! Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()