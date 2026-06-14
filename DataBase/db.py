import sqlite3

def conectar():
    return sqlite3.connect("DataBase/Sistema.db")

def obtener_producto(nombre):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT nombre, precio, stock FROM productos WHERE nombre=?", (nombre,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return {
            "nombre": result[0],
            "precio": result[1],
            "stock": result[2]
        }
    return None
``