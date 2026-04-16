import sqlite3
import os

# Obtener la ruta del archivo actual
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construir ruta completa de la base de datos
ruta_db = os.path.join(base_dir, "mi_base.db")

# Conectar a la base de datos
conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()

# Crear una tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    edad INTEGER
)
""")

# Insertar datos
cursor.execute("INSERT INTO estudiantes (nombre, edad) VALUES (?, ?)", ("Ana", 20))

# Consultar datos
cursor.execute("SELECT * FROM estudiantes")
datos = cursor.fetchall()

print("Datos registrados:")
for fila in datos:
    print(fila)

# Actualizar datos
cursor.execute("UPDATE estudiantes SET edad = ? WHERE nombre = ?", (21, "Ana"))

# Eliminar datos
cursor.execute("DELETE FROM estudiantes WHERE nombre = ?", ("Ana",))

# Guardar cambios
conexion.commit()

# Cerrar conexión (AL FINAL)
conexion.close()