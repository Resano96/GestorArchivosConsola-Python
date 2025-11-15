import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# esto sirve para cargar un archivo del env, env sirve para ocultar apis y cosas que no interesa subir
load_dotenv()

# aqui le pasamos la api key de la ia en cuestion al cliente
client = InferenceClient(token=os.getenv("HUGGINGFACE_API_KEY"))


# Esta funcion es para usar HuggingFace, una ia limitada pero gratuita.
# Cada IA tiene su estructura que puedes encontrar en la documentacion.
def write_text_hugging(tema, numero_de_lineas, nivel_seriedad):
    """
    Genera texto con la API de Hugging Face y lo devuelve.

    Entrada:

    tema--->Tema a escribir

    lineas-->Lineas a escribir

    seriedad-->1-5nivel de seriedad

    imaginacion -->1-5Cuanto se puede inventar


    Salida:

    Texto solicitado
    """

    # si la api esta mal montada return error
    if not client.token:

        return "Error: la Api no esta bien montada. Revisa tu HUGGINGFACE_API_KEY."

    try:
        # prompt de lo que quieres hacer
        prompt =f"""Escribe un texto que cumpla OBLIGATORIAMENTE las siguientes reglas:
        
        REGLA 1 (MÁS IMPORTANTE): El texto debe tener **exactamente {numero_de_lineas} líneas en total**. Ni una más, ni una menos.
        REGLA 2: El tema es: {tema}.
        REGLA 3: El nivel de seriedad debe ser {nivel_seriedad} (1=informal, 5=formal).
        REGLA 4: El nivel de imaginación debe ser el minimo posible, cumple todas las reglas obligatoriamente.
        REGLA 5 (MUY IMPORTANTE): **El idioma es castellano (español de España)**.

        Responde únicamente con el texto de {numero_de_lineas} líneas. No incluyas títulos, saludos, introducciones, ni explicaciones.
        """

        # --- Estos son los parámetros (payload) ---
        params = {
            "model": "mistralai/Mistral-7B-Instruct-v0.2",
            "messages": [
                {
                    "role": "Escritor de textos breves",
                    "content": "Eres un generador de contenido experto. Tu única función es escribir texto que se ajuste perfectamente a las especificaciones del usuario, listo para ser guardado directamente en un archivo."
                },
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 1500,
            "temperature": 0.7,
            "top_p": 0.9
        }

        # 3. Intentar llamar a la API
        print(f"Pensando en {tema}...")
        response = client.chat_completion(**params)
        generated_text = response.choices[0].message.content
        print("Tengo una idea!")


        return generated_text


    # 5. Manejar los posibles errores
    except AttributeError as e:
        print(f"Error: La respuesta de la API no tuvo el formato esperado: {e}")


    except IOError as e:
        print(f"Error al escribir en el archivo 'archivo.txt': {e}")


    except Exception as e:
        print(f"Error inesperado al conectar con la API o procesar: {e}")
