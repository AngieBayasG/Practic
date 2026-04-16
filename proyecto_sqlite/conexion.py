import sqlite3

# 1. Conectar a la base de datos (usa la misma ruta donde está tu .db)
conexion = sqlite3.connect(r"C:\Users\Admin\Desktop\Mis Documentos\Angie\Practic\proyecto_sqlite\estudiantes.db")

# 2. Crear cursor
cursor = conexion.cursor()

# 3. Ejecutar consulta
cursor.execute("SELECT * FROM estudiantes")

# 4. Obtener datos
datos = cursor.fetchall()

# 5. Mostrar resultados
for fila in datos:
    print(fila)

# 6. Cerrar conexión
conexion.close()