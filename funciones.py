import json
from datetime import datetime
import os

def cambiar_ubicacion(ruta):
    try:
        os.chdir(ruta)
        return f"Ruta actual {mostrar_ubicacion()}"
    except FileNotFoundError:
        print( f"no hay un directorio llamado {ruta}")


def montar_ubicacion(*ruta):
    base= os.getcwd()
    ruta_completa = os.path.join(base,*ruta)
    return ruta_completa


def mostrar_ubicacion():
    return f"Actualmente estas en: \n"+ os.getcwd()

def guardar_historial(tipo,command):

    if tipo =="pregunta":
        hist = "Se actua sobre: "+ montar_ubicacion(command)
    elif tipo == "funcion":
        hist = "La funcion ha sido: "+ command
    elif tipo == "resultado":
        hist = "El resultado es: "+ command
    elif tipo == "dict":
        hist = command
    else:
        hist = "Nada"
    try:
        with open("historial.txt", 'a', encoding='utf-8') as archivo:
            archivo.write(str(hist) + "\n")

    except Exception as e:
        print(f"Error al guardar el comando: {e}")

def generar_log_accesos():
    #nombre del JSON
    logger = "hist.json"
    if not os.path.isfile:
        return

    #extraemos los datos del JSON

    with open(logger, "r") as f:
        datos = json.load(f)

    #verificamos contraseña
    verificacion = comprobar_contraseña(input("dime la contraseña"))
    #fecha actual
    fecha = datetime.now()
    #formateamos la fecha
    fecha_formateada = fecha.strftime("%c")
    #diccionareamos la respuesta de comprobar contraseña con fecha

    intento ={
        "fecha": fecha_formateada,
        "passIntroducida": verificacion[1],
        "passCorrecta": verificacion[0],
        "accesoConcedido": verificacion[2]
        }
    datos.append(intento)
    with open(logger, "w") as f:
            json.dump(datos, f)
    return "Hecho"

#recibe una contraseña del cliente y la comprueba con la que esta en .env
def comprobar_contraseña(password):
    from dotenv import load_dotenv
    load_dotenv()

    pass_real = os.getenv("CONTRASEÑA")
    if pass_real is not None:
        return [pass_real,password,True] if pass_real==password else [pass_real,password,False]
#devuelve un array [pass_real,password introducida, True/False]



def comando(pregunta, funcion):

    if pregunta.lower() != "n":
        respuesta_cli =input(pregunta)
        respuesta = funcion(respuesta_cli)
        funcion_texto = repr(funcion)
        guardar_historial("funcion", funcion_texto)
        guardar_historial("pregunta", respuesta_cli)
        guardar_historial("resultado",respuesta)
        return respuesta

    respuesta_cli ="."

    respuesta = funcion(respuesta_cli)
    funcion_texto = repr(funcion)
    guardar_historial("funcion", funcion_texto)
    guardar_historial("pregunta", respuesta_cli)
    guardar_historial("dict", respuesta)
    return respuesta


