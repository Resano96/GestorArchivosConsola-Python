import funciones
from funciones import cambiar_ubicacion
from funciones_arch import eliminar_archivo, escribir_en_archivo_ia, escribir_en_archivo, crear_archivo_texto
from funciones_dir import listar_directorio, crear_directorio, eliminar_directorio


def print_menu():
    print("\n-_-_-_-_-Gestor de Archivos en Consola-_-_-_-_-")
    print("------Comandos de directorios------")
    print("1. Listar contenido del directorio actual")
    print("2. Crear un nuevo directorio")
    print("3. Eliminar un directorio")
    print("4. Cambiar de directorio")
    print("------Comandos de archivos------")
    print("5. Crear un nuevo archivo de texto")
    print("6. Escribir en un archivo de texto")
    print("7. Eliminar un archivo")
    print("8. Mostrar informacion del archivo")
    print("------Salir------")
    print("9. Historial y salir")




def main():

    while True:
        print_menu()
    
        try:
            choice = int(input("Elige una opcion: "))

            match choice:
                case 1:
                    elementos= funciones.comando("n", listar_directorio)
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

                    print(funciones.comando(pregunta,crear_directorio))

                case 3:

                    print(funciones.mostrar_ubicacion())

                    pregunta ="Que directorio quieres eliminar?\n"

                    print(funciones.comando(pregunta, eliminar_directorio))

                case 4:

                    funciones.mostrar_ubicacion()

                    elementos = listar_directorio()
                    directorios = '\n'.join(elementos["directorios"])

                    print(f"Puedes acceder a estos directorios desde aqui: {directorios}")

                    pregunta ="A que directorio quieres ir?"


                    print(funciones.comando(pregunta, cambiar_ubicacion))

                case 5:
                    pregunta ="Como llamamos al txt? \n"
                    print(funciones.comando(pregunta,crear_archivo_texto))

                case 6:

                    ia = input("Quieres usar la ia? (s/n) (Para usarla hay que poner primero la api)")
                    pregunta = input("Que archivo rellenamos? \n"
                                    "damelo con extension y todo \n"
                                    "con .env puedes meter la api de ia")
                    if ia.lower() == "s":
                        print(funciones.comando(pregunta,escribir_en_archivo_ia))
                    else:
                        print(funciones.comando(pregunta,escribir_en_archivo))


                case 7:
                    elementos = listar_directorio()
                    print(f"En la ubicacion actual tienes: \n"
                          f"{elementos["archivos"]}")
                    pregunta ="Que archivo quieres eliminar?"
                    print(funciones.comando(pregunta,eliminar_archivo))


                case 8:
                    preguntas = [

                    ]
                    archivo= input("Dime cual es el archivo del que quieres ver la info(con extension)")
                    info = funciones.mostrar_informacion_archivo(archivo)
                    print("No se que archivo es ese") if len(info) !=5 else (
                        print(  f"El nombre del archivo es: {info[0]}\n"
                            f"La extension del archivo es: {info[1]}\n"
                            f"El tamaño en bytes es: {info[2]}\n"
                            f"La fecha y hora de creacion es: {info[3]}\n"
                            f"La ultima fecha y hora del acceso es: {info[4]}"
                          ))

                case 9:

                    print("Durante esta sesion has hecho las siguientes acciones:")

                    break

                case _:
                    print("Opcion no valida. Selecciona otra.")

        except ValueError as e:
            print(f"Solo sirven numeros. ")



if __name__ == "__main__":
    main()