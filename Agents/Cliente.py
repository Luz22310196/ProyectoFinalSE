import re
import sqlite3

numeros_texto = {
    "uno":1, "dos":2, "tres":3, "cuatro":4, "cinco":5,
    "seis":6, "siete":7, "ocho":8, "nueve":9, "diez":10
}

def convertir_numeros(texto):
    for palabra, numero in numeros_texto.items():
        texto = re.sub(rf'\b{palabra}\b', str(numero), texto)
    return texto

def obtener_productos_db():
    conn = sqlite3.connect("DataBase/Sistema.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM productos")
    productos = [p[0] for p in cursor.fetchall()]
    conn.close()
    return productos

def interpretar_mensaje(texto):
    productos_detectados = []

    texto = texto.lower()
    texto = convertir_numeros(texto)

    lista = obtener_productos_db()

    for producto in lista:
        match = re.findall(rf'(\d+)\s*{producto}', texto)
        for m in match:
            productos_detectados.append({
                "nombre": producto,
                "cantidad": int(m)
            })

    return productos_detectados