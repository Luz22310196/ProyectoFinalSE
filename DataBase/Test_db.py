import sqlite3

conexion = sqlite3.connect("Sistema.db")
cursor = conexion.cursor()

print("PRODUCTOS:")
cursor.execute("SELECT * FROM productos")
for row in cursor.fetchall():
    print(row)

print("\nCLIENTES:")
cursor.execute("SELECT * FROM clientes")
for row in cursor.fetchall():
    print(row)

conexion.close()