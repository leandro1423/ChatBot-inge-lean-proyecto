from abc import ABC, abstractmethod

class UsuarioRepositoryPort(ABC):

    @abstractmethod
    def guardar_usuario(self, user_id: str, nombre: str, username: str, servicio: str):
        pass
