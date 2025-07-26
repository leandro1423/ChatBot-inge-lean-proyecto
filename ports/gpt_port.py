from abc import ABC, abstractmethod

class GPTPort(ABC):
    @abstractmethod
    def responder(self, mensaje: str) -> str:
        pass
