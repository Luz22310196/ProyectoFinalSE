import sqlite3

conn = sqlite3.connect("DataBase/Sistema.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM productos")

productos = [
    ("arroz", 25, 20),
    ("leche", 22, 10),
    ("pan", 10, 15),
    ("refresco", 18, 12)
]

cursor.executemany(
    "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
    productos
)

conn.commit()
conn.close()

print("Datos cargados")