# imports
import funciones



def print_menu():
    print("\n---------Gestor de Archivos en Consola------")
    print("1. Listar contenido del directorio actual")
    print("2. Crear un nuevo directorio")
    print("3. Eliminar de directorio")
    print("4. Cambiar de directorio")
    print("5. Crear un nuevo archivo de texto")
    print("6. Escribir en un archivo de texto")
    print("7. Eliminar un archivo o directorio")
    print("8. Mostrar informacion del archivo")
    print("9. Salir")

def main():

    while True:

        print_menu()
    
        try: 

            choice = int(input("Elige una opcion: "))

            match choice:

                case 1:
                    funciones.listar_directorio()

                case 2:
                    funciones.crear_directorio(input("Nombre del nuevo directorio: "))

                case 3:
                    funciones.eliminar_directorio()

                case 4:
                    pass

                case 5:
                    pass

                case 6:
                    pass

                case _:
                    print("Opcion no valida. Selecciona otra.")
        except ValueError:
            print("Opcion no valida. Selecciona otra.")


if __name__ == "__main__":
    main()