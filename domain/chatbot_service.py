
from adapters.sql_lite_user_repository import SQLiteUserRepository
from domain.opciones_menu import obtener_menu, ejecutar_opcion  # <-- CORREGIDO

class ChatbotService:
    def __init__(self, gpt_adapter=None):
        self.gpt_adapter = gpt_adapter
        self.user_repo = SQLiteUserRepository()
        self.estados_usuario = {}
        # Añade esto en __init__ si no lo tenías
        self.estado_cotizacion = {}  # Guarda si un usuario está cotizando y con qué datos
        # Dict que guarda el estado de cada user_id
        self.datos_cotizacion = None  # Cargaremos el Excel una sola vez

    def iniciar_chat(self) -> str:
        """
        Presenta la empresa y muestra el menú al inicio.
        """
        return self.presentacion_empresa() + "\n\n" + obtener_menu()

    def presentacion_empresa(self) -> str:
        return (
            "👋 ¡Bienvenido a *INGE LEAN*!\n"
            "Somos una empresa dedicada a ofrecer soluciones tecnológicas de última generación.\n"
            "Nuestro chatbot está aquí para ayudarte. 😊"
        )

    def procesar_mensaje(self, mensaje_usuario: str, user_id: str = None) -> str:
        mensaje_usuario = mensaje_usuario.strip().lower()

        # Si el usuario está en modo cotización, interpretar como número de servicio
        if user_id in self.estado_cotizacion:
            datos_df = self.estado_cotizacion[user_id]["datos"]
            try:
                indice = int(mensaje_usuario)
                servicios = datos_df["servicio"].dropna().unique()
                if 1 <= indice <= len(servicios):
                    servicio = servicios[indice - 1]
                    precio = datos_df[datos_df["servicio"] == servicio].iloc[0]["Precio"]

                    # Guardar el servicio consultado y registrar usuario
                    self.registrar_usuario(user_id, "-", "-", servicio)

                    # Limpiar estado y volver al menú
                    del self.estado_cotizacion[user_id]
                    return f"💰 El servicio *{servicio}* cuesta aproximadamente ${precio:,.0f} COP.\n\n" + obtener_menu()
                else:
                    return "❌ Índice fuera de rango. Por favor, selecciona un número válido."
            except ValueError:
                return "⚠️ Por favor, ingresa el número del servicio que deseas cotizar."

        # Mostrar menú si saluda o escribe "menu"
        if mensaje_usuario in ["hola", "hi", "buenas", "menú", "menu"]:
            return obtener_menu()

        # Si es un número, ejecutamos una opción
        if mensaje_usuario.isdigit():
            if mensaje_usuario == "2":  # Solicitar cotización
                return self.mostrar_servicios_para_cotizar(user_id)
            return ejecutar_opcion(mensaje_usuario)

        # GPT fallback
        if self.gpt_adapter:
            return self.gpt_adapter.enviar_mensaje(mensaje_usuario)

        return "Lo siento, no entendí tu mensaje. Por favor, elige una opción del 1 al 10."

    def registrar_usuario(self, user_id, nombre, username, servicio):
        self.user_repo.guardar_usuario(user_id, nombre, username, servicio)

    def manejar_peticion(self, user_id, nombre, username, opcion):
        if opcion == "2":
            servicio = "Consultar transacciones"
            self.registrar_usuario(user_id, nombre, username, servicio)
            return "Transacciones: ..."
        else:
            return "Opción aún no implementada."
