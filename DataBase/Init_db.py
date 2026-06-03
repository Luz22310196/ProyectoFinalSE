import sqlite3

conexion = sqlite3.connect("Sistema.db")
cursor = conexion.cursor()

# Tabla productos
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    stock INTEGER NOT NULL,
    precio REAL NOT NULL
)
""")

# Tabla clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    frecuente INTEGER DEFAULT 0
)
""")

# Tabla pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    total REAL,
    fecha TEXT,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id)
)
""")

conexion.commit()
conexion.close()

print("Base de datos creada correctamente")
