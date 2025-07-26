from abc import ABC, abstractmethod

class NLPInterface(ABC):
    @abstractmethod
    def responder(self, mensaje_usuario: str) -> str:
        pass
