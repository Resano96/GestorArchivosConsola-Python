
from funciones import cambiar_ubicacion, mostrar_historial, comando, mostrar_ubicacion
from funciones_arch import eliminar_archivo, escribir_en_archivo_ia, escribir_en_archivo, crear_archivo_texto, \
    mostrar_informacion_archivo
from funciones_dir import listar_directorio, crear_directorio, eliminar_directorio


def print_menu():
    print("\n-_-_-_-_-Gestor de Archivos en Consola-_-_-_-_-")
    print("------------Comandos de directorios------------")
    print("\t1. Listar contenido del directorio actual")
    print("\t2. Crear un nuevo directorio")
    print("\t3. Eliminar un directorio")
    print("\t4. Cambiar de directorio")
    print("------------Comandos de archivos---------------")
    print("\t5. Crear un nuevo archivo de texto")
    print("\t6. Escribir en un archivo de texto")
    print("\t7. Eliminar un archivo")
    print("\t8. Mostrar informacion del archivo")
    print("------------Salir------------------------------")
    print("\t9. Historial y salir\n")




def main():

    while True:
        print_menu()
    
        try:
            choice = int(input("Elige una opcion: \n"))

            match choice:
                case 1:
                    elementos= comando("n", listar_directorio)
                    directorios = '\n'. join(elementos["directorios"])
                    archivos = '\n'.join(elementos["archivos"])
                    print(f"en la carpeta actual tenemos \n"
                          f"{len(elementos["directorios"])} carpetas \n"
                          f"______________________\n"
                          f"{directorios}\n\n"
                          f"{len(elementos["archivos"])} archivos de diferentes tipos\n"
                          f"___________________________________\n"
                          f"{archivos}")

                case 2:
                    pregunta ="Nombre del nuevo directorio: \n"

                    print(comando(pregunta,crear_directorio))

                case 3:

                    print(mostrar_ubicacion())
                    elementos = listar_directorio()
                    directorios = '\n'.join(elementos["directorios"])
                    print(f"en la carpeta actual tenemos \n"
                          f"{len(elementos["directorios"])} directorios \n"
                          f"______________________\n"
                          f"{directorios}\n")

                    pregunta ="Que directorio quieres eliminar?\n"

                    print(comando(pregunta, eliminar_directorio))

                case 4:

                    print(mostrar_ubicacion())

                    elementos = listar_directorio()
                    directorios = '\n'.join(elementos["directorios"])

                    print(f"Puedes acceder a estos directorios desde aqui: \n{directorios}")

                    pregunta ="A que directorio quieres ir?\n"


                    print(comando(pregunta, cambiar_ubicacion))

                case 5:
                    pregunta ="Como llamamos al txt? \n"
                    print(comando(pregunta,crear_archivo_texto))

                case 6:
                    ia = input("Quieres usar la ia? (s/n) \n(Para usarla hay que poner primero la api)\n")

                    pregunta = ("Que archivo rellenamos? \n"
                                    "damelo con extension \n"
                                    "con .env puedes meter la api de ia\n")
                    if ia.lower() == "s":

                        print(comando(pregunta,escribir_en_archivo_ia))
                    else:

                        print(comando(pregunta,escribir_en_archivo))

                case 7:
                    elementos = listar_directorio()
                    archivos = '\n'.join(elementos["archivos"])
                    print(f"en la carpeta actual tenemos \n"
                          f"{len(elementos["archivos"])} archivos \n"
                          f"______________________\n"
                          f"{archivos}\n")
                    pregunta ="Que archivo quieres eliminar?\n"
                    print(comando(pregunta,eliminar_archivo))

                case 8:
                    pregunta ="Dime cual es el archivo del que quieres ver la info\n(con extension)\n"
                    info = comando(pregunta,mostrar_informacion_archivo)
                    print("No se que archivo es ese") if len(info) !=5 else (
                        print(  f"El nombre del archivo es: {info[0]}\n"
                            f"La extension del archivo es: {info[1]}\n"
                            f"El tamanio en bytes es: {info[2]}\n"
                            f"La fecha y hora de creacion es: {info[3]}\n"
                            f"La ultima fecha y hora del acceso es: {info[4]}"
                          ))

                case 9:

                    print("El historial actual es :\n")
                    mostrar_historial()

                    break

                case _:
                    print("Opcion no valida. Selecciona otra.")

        except ValueError as e:
            print(f"Solo sirven numeros. ")



if __name__ == "__main__":
    main()