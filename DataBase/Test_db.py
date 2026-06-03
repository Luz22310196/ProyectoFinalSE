import sqlite3

conexion = sqlite3.connect("Sistema.db")
cursor = conexion.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tablas = cursor.fetchall()

print("Tablas encontradas:")
for tabla in tablas:
    print(tabla[0])

conexion.close()