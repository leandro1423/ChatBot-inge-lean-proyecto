# adapters/telegram_adapter.py
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from domain.chatbot_service import ChatbotService
from domain.opciones_menu import obtener_menu
from adapters.gpt_adapter import GPTAdapter

load_dotenv()

# Obtener la clave de API desde las variables de entorno
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la variable de entorno OPENAI_API_KEY")

# Instanciar el núcleo del bot con GPT
chatbot = ChatbotService(GPTAdapter(api_key))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje_bienvenida = chatbot.presentacion_empresa()
    opciones = obtener_menu()
    mensaje_completo = f"{mensaje_bienvenida}\n\nOpciones disponibles:\n{opciones}\n\nEscríbeme lo que quieras saber:"
    await update.message.reply_text(mensaje_completo)

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text
    respuesta = chatbot.procesar_mensaje(mensaje)
    await update.message.reply_text(respuesta)

def main():
    TOKEN = os.getenv("TELEGRAM_TOKEN")

    if not TOKEN:
        raise ValueError("No se encontró la variable de entorno TELEGRAM_TOKEN")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    app.run_polling()

if __name__ == "__main__":
    main()
