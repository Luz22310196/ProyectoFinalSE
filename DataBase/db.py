import sqlite3

def get_connection():
    return sqlite3.connect("DataBase/Sistema.db")

def obtener_productos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT nombre, stock, precio FROM productos")
    datos = cursor.fetchall()

    conn.close()
    return datos

def obtener_stock(nombre_producto):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT stock FROM productos WHERE nombre LIKE ?",
        ('%' + nombre_producto + '%',)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return 0

def insertar_pedido(producto, cantidad):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO pedidos (producto, cantidad) VALUES (?, ?)",
        (producto, cantidad)
    )

    conn.commit()
    conn.close()
