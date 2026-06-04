import sqlite3

conexion = sqlite3.connect("Sistema.db")
cursor = conexion.cursor()

cursor.execute("SELECT COUNT(*) FROM productos")
if cursor.fetchone()[0] == 0:

    productos = [
        ("Motor NEMA17", 20, 250),
        ("Driver A4988", 50, 80),
        ("ESP32", 30, 180),
        ("Sensor Ultrasonico", 40, 70)
    ]

    cursor.executemany(
        "INSERT INTO productos(nombre, stock, precio) VALUES(?,?,?)",
        productos
    )

cursor.execute("SELECT COUNT(*) FROM clientes")
if cursor.fetchone()[0] == 0:

    clientes = [
        ("Juan Perez", 1),
        ("Maria Lopez", 0)
    ]

    cursor.executemany(
        "INSERT INTO clientes(nombre, frecuente) VALUES(?,?)",
        clientes
    )

conexion.commit()
conexion.close()

print("Datos insertados correctamente")