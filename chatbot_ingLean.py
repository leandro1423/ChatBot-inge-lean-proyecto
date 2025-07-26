from openai import OpenAI

# Reemplaza esto con tu clave real
client = OpenAI(api_key="TU_API_KEY")

def responder_pregunta(pregunta_usuario):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Usa "gpt-4" si tienes acceso
        messages=[
            {"role": "system", "content": "Eres un asistente experto en los servicios que ofrece la empresa INGE LEAN. Responde de forma clara, útil y profesional."},
            {"role": "user", "content": pregunta_usuario}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Chatbot INGE LEAN - Escribe 'salir' para terminar.\n")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("Chatbot: ¡Hasta luego!")
            break
        respuesta = responder_pregunta(user_input)
        print("Chatbot:", respuesta)
