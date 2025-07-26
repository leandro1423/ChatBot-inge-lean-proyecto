import sqlite3
from datetime import datetime
from ports.output_ports import UsuarioRepositoryPort
import os

class SQLiteUserRepository(UsuarioRepositoryPort):
    def __init__(self, db_path="datasets/usuarios.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)  # Crea la carpeta si no existe
        self._crear_tabla_si_no_existe()

    def _crear_tabla_si_no_existe(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                nombre TEXT NOT NULL,
                username TEXT NOT NULL,
                servicio_consultado TEXT,
                fecha TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def guardar_usuario(self, user_id, nombre, username, servicio):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute('''
            INSERT INTO usuarios (user_id, nombre, username, servicio_consultado, fecha)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, nombre, username, servicio, fecha_actual))

        conn.commit()
        conn.close()
