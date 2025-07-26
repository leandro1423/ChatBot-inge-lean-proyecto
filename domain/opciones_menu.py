# menu.py
import pandas as pd
import matplotlib.pyplot as plt
from adapters.sql_lite_user_repository import SQLiteUserRepository



# ----- MENÚ DE OPCIONES -----

menu_opciones = [
    "1. Ver nuestros servicios",
    "2. Solicitar una cotización",
    "3. ¿Dónde operamos?",
    "4. Consultar estado de mi proyecto",
    "5. Agendar una reunión con un asesor",
    "6. Contactar con un asesor urgente",
    "7. preguntas frecuentes",
    "8. Hablar directamente con un asesor humano",
    "9. Ver ubicación o sedes",
    "10. te enviamos un correo con toda la informacion"
    "11. Otro"

]


def obtener_menu():
    mensaje = "¡Hola! ¿En qué puedo ayudarte hoy? Estas son algunas cosas que puedo hacer:\n"
    mensaje += "\n".join(menu_opciones)
    return mensaje


def ejecutar_opcion(opcion):
    opciones_funciones = {
        "1": ver_servicios,
        "2": solicitar_cotizacion,
        "3": donde_operamos,
        "4": consultar_estado,
        "5": agendar_reunion,
        "6": solicitar_soporte,
        "7": hablar_virtual,
        "8": hablar_humano,
        "9": ver_ubicacion,
        "10": enviar_correo,
        "11": otro
    }

    funcion = opciones_funciones.get(opcion)
    if funcion:
        return funcion()
    else:
        return "❌ Opción no válida. Por favor, selecciona una opción del 1 al 10."


# ---------- FUNCIONES DE COTIZACIÓN ----------

def cargar_datos_cotizacion(ruta_archivo):
    return pd.read_excel(ruta_archivo)


def calcular_cotizacion(servicio, datos_df):
    resultado = datos_df[datos_df["servicio"].str.lower() == servicio.lower()]
    if not resultado.empty:
        precio = resultado.iloc[0]["Precio"]
        return f"💼 El valor estimado para el servicio '{servicio}' es: ${precio:,.0f} COP."
    else:
        return f"⚠️ No encontramos una cotización para el servicio '{servicio}'."


def solicitar_cotizacion():
    ruta_archivo = "C:/Users/cesii/OneDrive/Documentos/talento tech/Hackaton/datasets/servicios_ingelean.xlsx"

    try:
        datos = cargar_datos_cotizacion(ruta_archivo)
        lista_servicios = datos["servicio"].dropna().unique()  # Evita nulos y duplicados

        mensaje = "📋 Estos son los servicios disponibles para cotizar:\n"
        for idx, servicio in enumerate(lista_servicios, 1):
            mensaje += f"{idx}. {servicio}\n"
        mensaje += "\n✏️ Por favor, responde con el número del servicio para conocer su valor."
        return mensaje

    except FileNotFoundError:
        return "⚠️ Error: No se encontró el archivo de cotizaciones. Verifica la ruta."
    except Exception as e:
        return f"⚠️ Ocurrió un error inesperado: {e}"


def obtener_precio_por_indice(indice_usuario, datos_df):
    try:
        servicios = datos_df["servicio"].dropna().unique()
        indice = int(indice_usuario) - 1

        if 0 <= indice < len(servicios):
            servicio = servicios[indice]
            precio = datos_df[datos_df["servicio"] == servicio].iloc[0]["Precio"]
            return f"💰 El servicio de desarrollo de '{servicio}' vale ${precio:,.0f} COP."
        else:
            return "❌ Índice fuera de rango. Por favor, selecciona un número válido."

    except ValueError:
        return "⚠️ Por favor ingresa un número válido."
    except Exception as e:
        return f"⚠️ Ocurrió un error: {e}"


# ---------- FUNCIONES DE OPCIONES DEL MENÚ ----------

def ver_servicios():
    return (
        "Nuestros servicios incluyen:\n"
        "- Página Web\n"
        "- Tienda Virtual\n"
        "- App Móvil\n"
        "- Automatización de procesos\n"
        "- Software a medida\n"
    )


def donde_operamos():
    return "🌍 Operamos en todo Colombia y partes de Latinoamérica."


def consultar_estado():
    return "🔍 Por favor, proporciona tu número de proyecto para consultar el estado."


def agendar_reunion():
    return "📅 Puedes agendar una reunión en este enlace: [https://calendly.com/ivanzho97/asesoria-personalizada]"


def solicitar_soporte():
    return "🛠️ Describe tu problema técnico para poder ayudarte."


def hablar_virtual():
    return (
        "🤖 Estoy aquí para ayudarte. Estas son algunas preguntas frecuentes:\n\n"
        "💼 *¿Qué servicios ofrecen?*\n"
        "Desarrollo de software a medida, integración de IA, automatización de procesos y análisis de datos.\n\n"
        "🧠 *¿Qué tecnologías utilizan?*\n"
        "Python, Java, JavaScript, TensorFlow, PyTorch, React, Node.js, entre otros.\n\n"
        "💰 *¿Cómo puedo cotizar un servicio?*\n"
        "Selecciona la opción 2 del menú para iniciar una cotización personalizada.\n\n"
        "🕒 *¿Cuál es el tiempo de desarrollo promedio?*\n"
        "Depende del proyecto, pero los desarrollos van desde 2 semanas hasta varios meses.\n\n"
        "🌐 *¿Tienen soluciones con inteligencia artificial?*\n"
        "Sí, ofrecemos chatbots, visión por computador, procesamiento de lenguaje natural y más.\n\n"
        "📍 *¿Dónde están ubicados?*\n"
        "Tenemos sedes en Bogotá, Medellín y Cali. Puedes ver la ubicación exacta con la opción correspondiente del menú.\n\n"
        "Si tienes otra pregunta, ¡escríbela y te responderé enseguida! 😊"
    )

def hablar_humano():
    return "👤 En breve te conectaremos con un asesor humano."


def ver_ubicacion():
    return (
        "📍 *Nuestras sedes son:*\n\n"
        "🏙️ *Pereira*: [Ver ubicación](https://maps.app.goo.gl/XQzktPC3AbxHjeYC8) – Barrio La victoria.\n"
    )
def enviar_correo():
    return "<UNK> Correo enviado correctamente."


def otro():
    return "✍️ Por favor, describe con más detalle tu solicitud."
