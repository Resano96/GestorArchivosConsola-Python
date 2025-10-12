import os

# print(os.listdir())  # ['main.py', 'carpeta1', 'notas.txt']
# print(os.getcwd())  # C:\Users\Nekane\Desktop\Proyectos\GestorArchivosConsola-Python
# os.mkdir("nueva_carpeta")  # Crea una nueva carpeta
# os.chdir("nueva_carpeta")  # Cambia el directorio actual
# with open("archivo.txt", "w") as f:  # Crea un nuevo archivo de texto
#     f.write("Hola, mundo!")
# with open("archivo.txt", "a") as f:  # Escribe en un archivo de texto
#     f.write("\nOtra linea")
# os.remove("archivo.txt")  # Elimina un archivo
# os.rmdir("nueva_carpeta")  # Elimina un directorio (debe estar vacio)
# print(os.stat("notas.txt"))  # Muestra informacion del archivo
# print(os.path.exists("notas.txt"))  # True si el archivo o directorio existe
# print(os.path.isfile("notas.txt"))  # True si es un archivo
# print(os.path.isdir("carpeta1"))  # True si es un directorio



# Funciones para cada operacion

# Listar contenido del directorio actual
def listar_directorio():
    elementos = os.listdir() # Listar contenido
    resultado = {"archivos": [], "directorios": []} # Diccionario para separar archivos y directorios
    for elem in elementos: # Separar archivos y directorios
        if os.path.isfile(elem):
            resultado["archivos"].append(elem) # Añadir a la lista de archivos
        elif os.path.isdir(elem):
            resultado["directorios"].append(elem) # Añadir a la lista de directorios
    return resultado




# Crear un nuevo directorio
def crear_directorio(name):
    if os.path.exists(name): # Comprobar si ya existe
        return f"{name} ya existe."
    
    os.mkdir(name) # Crear directorio




# Eliminar un directorio
def eliminar_directorio(name, recordar = False):
    try:
        os.chdir(name) # Probar a cambiar al directorio a eliminar
    
    except FileNotFoundError: # Comprobar si existe
        return f"{name} no existe."
    
    except NotADirectoryError: # Comprobar si es un directorio
        return f"{name} no es un directorio."

    elementos = os.listdir()  # Listar contenido

    if elementos == []:  # Si esta vacio
        os.chdir("..")  # Volver al directorio padre
        os.rmdir(name)  # Eliminar directorio
        return f"Directorio {name} eliminado."
    else:
        
        if not recordar:
            verificador = input(f"El directorio {name} no esta vacio. Deseas eliminarlo y todo su contenido? (s/n): ")
        
        
            if verificador.lower() != 's':
                os.chdir("..")  # Volver al directorio padre
                return "Operacion cancelada."
        
        
            verificador2 = input("Quieres recordar la anterior respuesta? (s/n): ")
            if verificador2.lower() == "s":
                recordar = True
        
        elementos = listar_directorio()  # Listar contenido
        for directorio in elementos["directorios"]:  # Eliminar subdirectorios
            eliminar_directorio(directorio,recordar)  # Llamada recursiva

        for archivo in elementos["archivos"]:  # Eliminar archivos
            os.remove(archivo) # Eliminar archivo




# Cambiar de directorio
def cambiar_directorio():
    pass
# Crear un nuevo archivo de texto
def crear_archivo_texto():
    pass
# Escribir en un archivo de texto
def escribir_en_archivo():
    pass
# Eliminar un archivo
def eliminar_archivo():
    pass

def mostrar_informacion_archivo():
    pass

