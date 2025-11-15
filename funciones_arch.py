from datetime import datetime
import os
from ai_service import write_text_hugging as IA

# Crear un nuevo archivo de texto
def crear_archivo_texto(nombre):
    # Aniade .txt si no lo tiene
    if not nombre.lower().endswith(".txt"):
        nombre = f"{nombre}.txt"
    # Si tiene mas de 1 . dice que el formato no es valido
    if nombre.count(".")!= 1:
        return "formato no valido, solo creo txt"
    # Si ya hay un archivo que se llame asi da error
    if os.path.isfile(nombre):
        return f"Ya hay un .txt llamado {nombre}"
    # Creamos el archivo nuevo
    with open(nombre, "w") as f:
        #Preguntamos si lo queremos rellenar
        selector = input("Lo rellenamos con IA? (S/N)")
        if selector.lower() == "s":
            #Con s lanza el comando escribir IA
            texto= escribir_en_archivo_ia(nombre)
        elif selector.lower()== "n":
            #Con n lanza el comando escribir sin Ia
            texto= escribir_en_archivo(nombre)
            #Si no pones cualquier otra cosa solo pone Hola en el archivo
        else:
            texto= "Hola"
        f.write(texto)
        #Devuelve un mensaje de confirmacion
    return f"{nombre} creado"


# Escribir en un archivo de texto con IA
def escribir_en_archivo_ia(archivo):
    #Comprueba si es un archivo
    if os.path.isfile(archivo):
        #Separa entre nombre y extension
        nombre, ext = os.path.splitext(archivo)
        #Si no tiene extension o es .txt
        if ext== ".txt"or ext =="":
            tema = input(f"Sobre que tema quieres escribir en {archivo}?")
            lineas = input("Cuantas lineas rellenamos?")
            seriedad = input("Como de serio lo escribimos? 1-humor 5-serio")
            imaginacion = input("Tengo demasiada imaginacion... cuanta uso? 1-creativo 5-literal")
            texto = IA(tema, lineas, seriedad, imaginacion)
            with open(archivo, "w", encoding="utf-8") as f:
                f.write(texto)
                return f"No me gustaba el tema de los {tema} pero algo hemos conseguido hacer"
        #Si la extension es .py
        elif ext== ".py":
            print("Uf, un script en py? mi papa me ha dicho que si lo hago con IA no aprendo...\neres mala influencia\n\n")
            return "ADIOS"
        #Si la extension es .env sirve para poner la API de ia
        elif ext== ".env":
            contenido_env = f"HUGGINGFACE_API_KEY = {input("Dame la key de api que quieres poner")}"
            with open(".env", "w", encoding="utf-8") as f:
                f.write(contenido_env)
            with open(".gitignore", "a", encoding="utf-8") as g:
                g.write("\n" + ".env")
            return "API de hugginface configurada"

    elif os.path.exists(archivo):
        return "el archivo que me has nombrado es un directorio, como a a escribir la ia ahi?"

    else:
        return "te acabas de inventar el archivo y no se te ha cambiado ni el color, \nsinvergüenza"


# Escribir en un archivo de texto sin IA
def escribir_en_archivo(archivo):
    if os.path.isfile(archivo):
        nombre, ext = os.path.splitext(archivo)
        if ext== ".txt"or ext =="":

            texto = input("Dime el texto que quieras poner en el archivo\n")
            with open(archivo, "w") as f:
                f.write(texto)
                return "Hecho"

        elif ext== ".py":
            codigo = input("Es mas facil que lo abras y escribas tu pero bueno....\nDime que ponemos\n")
            with open(archivo, "w") as f:
                f.write(codigo)
                return "Hecho, el debug, lo haces tu"


        elif ext== ".env":
            contenido_env = f"HUGGINGFACE_API_KEY = {input("Dame la key de api que quieres poner")}"
            with open(".env", "w", encoding="utf-8") as f:
                f.write(contenido_env)
            with open(".gitignore", "a", encoding="utf-8") as g:
                g.write("\n" + ".env")
            return "API de hugginface configurada"


    elif os.path.exists(archivo):
        return "el archivo que me has nombrado es un directorio"

    elif not os.path.exists(archivo):
        return "te acabas de inventar el archivo y no se te ha cambiado ni el color, \nSinvergüenza"


# Eliminar un archivo
def eliminar_archivo(archivo):
    if os.path.isfile(archivo):
        os.remove(archivo)
        return f"{archivo} ha sido eliminado"
    elif os.path.isdir(archivo):
        return f"{archivo} es un directorio, usa otra opcion para ello"
    else:
        return f"{archivo} no ha sido eliminado"


def mostrar_informacion_archivo(archivo):
    try:
        nombre, ext = os.path.splitext(archivo)
        stats = os.stat(archivo)
        tamanio_bytes = stats.st_size
        formato ="%c"
        formato2 ='%Y-%m-%d %H:%M:%S'
        fecha_creacion = datetime.fromtimestamp(stats.st_ctime).strftime(formato)
        fecha_acceso = datetime.fromtimestamp(stats.st_atime).strftime(formato)
        if ext =="":
            ext= "Sin extension"

        info = [nombre, ext, tamanio_bytes, fecha_creacion, fecha_acceso]
        return info
    except FileNotFoundError:
        return f"Error: Archivo '{archivo}' no encontrado."
    except Exception as e:
        return f"Error inesperado al leer el archivo: {e}"