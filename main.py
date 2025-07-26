# main.py

import os
from dotenv import load_dotenv

# Adaptadores
from adapters.gpt_adapter import GPTAdapter
from adapters.console_adapter import iniciar_consola

# Dominio del chatbot
from domain.chatbot_service import ChatbotService

# Cargar variables de entorno desde .env
load_dotenv()

def main():
    # Obtener API key desde el archivo .env o usar valor por defecto
    api_key = os.getenv("OPENAI_API_KEY") or "PEGA_AQUI_TU_API_KEY_SI_NO_USAS_ENV"

    # Inicializar el motor GPT y el servicio del chatbot
    gpt_engine = GPTAdapter(api_key)
    chatbot = ChatbotService(gpt_engine)

    # Iniciar la consola de interacción
    iniciar_consola(chatbot)

if __name__ == "__main__":
    main()
