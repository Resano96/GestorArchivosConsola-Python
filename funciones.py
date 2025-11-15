
import os
from pathlib import Path


def cambiar_ubicacion(ruta):
    try:
        os.chdir(ruta)
        return mostrar_ubicacion()
    except FileNotFoundError:
        return  f"no hay un directorio llamado {ruta}"
    except OSError:
        return f"ruta no valida: {ruta}"



def montar_ubicacion(*ruta):
    base= os.getcwd()
    ruta_completa = os.path.join(base,*ruta)
    return ruta_completa


def mostrar_ubicacion():
    return f"Actualmente estas en: \n"+ os.getcwd()



def guardar_historial(tipo,command):
    ubicacion_padre = Path(__file__).parent
    ubicacion =ubicacion_padre / "historial" / "historial.txt"

    if tipo =="pregunta":
        hist = "Se actua sobre: "+ montar_ubicacion(command)
    elif tipo == "funcion":
        hist = "La funcion ha sido: "+ command
    elif tipo == "resultado":
        hist = "El resultado es: "+ (str(command))
    elif tipo == "dict":
        hist = command
    else:
        hist = "Nada"
    try:
        with open(ubicacion, 'a', encoding='utf-8') as archivo:
            archivo.write(str(hist) + "\n")

    except Exception as e:
        print(f"Error al guardar el comando: {e}")

def comando(pregunta, funcion):
    respuesta_cli = "."
    if pregunta.lower() != "n":
        respuesta_cli =input(pregunta)

    respuesta = funcion(respuesta_cli)
    funcion_texto = repr(funcion)
    guardar_historial("funcion", funcion_texto)
    guardar_historial("pregunta", respuesta_cli)
    guardar_historial("resultado", respuesta)
    return respuesta

def mostrar_historial():
    ubicacion_padre = Path(__file__).parent
    ubicacion = ubicacion_padre / "historial" / "historial.txt"
    try:
        with open(ubicacion, 'r', encoding='utf-8') as archivo:
            comandos = archivo.read()
    except Exception as e:
        print(f"Error: {e} al leer el archivo ")
    print(comandos)

