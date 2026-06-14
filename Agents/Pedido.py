from DataBase.db import obtener_producto

def generar_pedido(productos):
    total = 0
    alertas = []
    detalle = []

    for p in productos:
        data = obtener_producto(p["nombre"])

        if not data:
            alertas.append(f"{p['nombre']} no existe")
            continue

        if data["stock"] < p["cantidad"]:
            alertas.append(f"Stock insuficiente de {p['nombre']}")

        subtotal = data["precio"] * p["cantidad"]
        total += subtotal

        detalle.append({
            "nombre": p["nombre"],
            "cantidad": p["cantidad"],
            "subtotal": subtotal
        })

    # REGLA DE INFERENCIA
    if total > 500:
        total *= 0.9
        alertas.append("Se aplicó descuento del 10%")

    return detalle, total, alertas