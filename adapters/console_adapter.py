# adapters/console_adapter.py

def iniciar_consola(chatbot):
    # Mostrar presentación de la empresa y menú al inicio
    print(chatbot.presentacion_empresa())
    print()
    print(chatbot.procesar_mensaje("menu"))  # Esto imprime el menú directamente

    print("\n💬 Puedes empezar a chatear con el bot. Escribe 'salir' para terminar.\n")

    # Bucle de conversación
    while True:
        mensaje_usuario = input("Tú: ")
        if mensaje_usuario.lower() in ["salir", "exit", "quit"]:
            print("👋 ¡Hasta luego!")
            break

        respuesta = chatbot.procesar_mensaje(mensaje_usuario)
        print("Bot:", respuesta)
