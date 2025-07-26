from openai import OpenAI
from ports.gpt_port import GPTPort

class GPTAdapter(GPTPort):
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def responder(self, mensaje: str) -> str:
        try:
            respuesta = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un asistente útil y amigable."},
                    {"role": "user", "content": mensaje}
                ]
            )
            return respuesta.choices[0].message.content
        except Exception as e:
            return f"Error al generar respuesta: {e}"
