import os
import shutil

import funciones
import funciones as FUN #importo con mayus para verlas mas facil
import funciones_arch as FUNARCH


# Listar contenido del directorio actual
def listar_directorio(ruta = "."):

    elementos = os.listdir(FUN.montar_ubicacion(ruta)) # Listar contenido
    resultado = {"archivos": [], "directorios": []} # Diccionario para separar archivos y directorios

    for elem in elementos: # Separar archivos y directorios

        if os.path.isfile(elem):
            resultado["archivos"].append(elem) # Añadir a la lista de archivos
        elif os.path.isdir(elem):
            resultado["directorios"].append(elem) # Añadir a la lista de directorios

    return resultado #Devolver un diccionario con archivos y directorios por separado

# Crear un nuevo directorio
def crear_directorio(name):
    if os.path.exists(name): # Comprobar si ya existe
        return f"El directorio {name} ya existe.\n"
    if "/"in name:
        os.makedirs(name)
        return f"Directorios creados con exito\n"
    else:
        os.mkdir(name) # Crear directorio
    return f"Directorio {name} creado con exito\n"




def eliminar_directorio(ruta):
    try:
        os.rmdir(ruta)
        return f" Carpeta {ruta} eliminada con exito\n"
    except FileNotFoundError:
        return f"{ruta} no existe en este directorio\n"

    except NotADirectoryError:  # Comprobar si es un directorio
        return f"{ruta} no es un directorio.\n"

    except OSError:
        shutil.rmtree(ruta)

        return f" Carpeta {ruta} y sus subelementos eliminada con exito\n"

