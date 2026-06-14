import sqlite3

conn = sqlite3.connect("DataBase/Sistema.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    precio REAL,
    stock INTEGER
)
""")

conn.commit()
conn.close()

print("DB creada")