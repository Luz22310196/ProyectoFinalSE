from DataBase.db import obtener_stock, insertar_pedido

def generar_pedido(productos):
    resultado = []
    explicacion = []

    if not productos:
        explicacion.append("No se detectó ningún producto válido en el mensaje.")
        return resultado, explicacion

    for item in productos:
        producto = item["producto"]
        cantidad = item["cantidad"]

        stock = obtener_stock(producto)

        # Regla 1: stock suficiente
        if stock >= cantidad:
            estado = "APROBADO"
            insertar_pedido(producto, cantidad)

            explicacion.append(
                f"Se detectó el producto '{producto}' con cantidad {cantidad}. "
                f"Hay stock suficiente ({stock} disponibles), por lo tanto el pedido fue aprobado."
            )

        # Regla 2: stock insuficiente
        else:
            estado = "RECHAZADO"

            explicacion.append(
                f"Se detectó el producto '{producto}' con cantidad {cantidad}. "
                f"El stock disponible es {stock}, por lo tanto el pedido fue rechazado por stock insuficiente."
            )

        resultado.append({
            "producto": producto,
            "cantidad": cantidad,
            "stock": stock,
            "estado": estado
        })

    return resultado, explicacion

``