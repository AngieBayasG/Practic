import sqlite3

# Nombre del archivo de base de datos
DB_NAME = "inventario.db"

def inicializar_db():
    # El bloque 'with' maneja la conexión automáticamente
    with sqlite3.connect(DB_NAME) as conexion:
        cursor = conexion.cursor()
        
        # Creamos la tabla con tipos de datos específicos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                stock INTEGER DEFAULT 0
            )
        """)
        print("Tabla 'productos' lista.")

def agregar_productos():
    # Lista para insertar varios registros a la vez
    datos = [
        ('Teclado Mecánico', 85.50, 15),
        ('Mouse Gamer', 45.00, 5),
        ('Monitor 24"', 150.00, 2),
        ('Cable HDMI', 12.99, 20)
    ]
    
    with sqlite3.connect(DB_NAME) as conexion:
        cursor = conexion.cursor()
        # executemany es mucho más rápido para cargas masivas
        cursor.executemany("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", datos)
        conexion.commit()
        print(f"Se agregaron {len(datos)} productos.")

def consultar_bajo_stock(limite):
    print(f"\n--- Productos con stock menor a {limite} ---")
    with sqlite3.connect(DB_NAME) as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, stock FROM productos WHERE stock < ?", (limite,))
        
        resultados = cursor.fetchall()
        for fila in resultados:
            print(f"Producto: {fila[0]} | Stock actual: {fila[1]}")

# --- Ejecución del ejemplo ---
if __name__ == "__main__":
    inicializar_db()
    agregar_productos()
    consultar_bajo_stock(10) # Buscamos productos que se están agotando