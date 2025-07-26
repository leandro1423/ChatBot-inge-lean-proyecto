import sqlite3
import os

# Crear carpeta 'datasets' si no existe
os.makedirs("datasets", exist_ok=True)

# Ruta del archivo de base de datos
ruta_db = "datasets/usuarios.db"

# Conexión a la base de datos
conn = sqlite3.connect(ruta_db)
cursor = conn.cursor()

# Crear tabla 'usuarios' si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    nombre TEXT,
    username TEXT,
    servicio_consultado TEXT,
    fecha TEXT
)
''')

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("✅ Base de datos creada exitosamente en 'datasets/usuarios.db'")
