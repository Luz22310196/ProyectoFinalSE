from DataBase.db import obtener_producto, actualizar_stock

def generar_pedido(productos):
    total = 0
    detalle = []
    alertas = []

    for p in productos:
        data = obtener_producto(p["nombre"])

        if not data:
            continue

        if data["stock"] < p["cantidad"]:
            alertas.append(f"Stock insuficiente de {p['nombre']}")
            continue

        subtotal = data["precio"] * p["cantidad"]
        total += subtotal

        detalle.append({
            "nombre": p["nombre"],
            "cantidad": p["cantidad"],
            "subtotal": subtotal
        })

        actualizar_stock(p["nombre"], p["cantidad"])

    if total > 200:
        total *= 0.9

    return detalle, total, alertas