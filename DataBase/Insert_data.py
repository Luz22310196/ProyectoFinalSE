import sqlite3

conn = sqlite3.connect("DataBase/Sistema.db")
cursor = conn.cursor()

productos = [
    ("NEMA17", 200, 10),
    ("A4988", 80, 5)
]

cursor.executemany("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", productos)

conn.commit()
conn.close()

print("Datos insertados")