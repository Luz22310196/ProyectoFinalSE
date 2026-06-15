from DataBase.db import obtener_producto

def explicar(detalle, total, alertas):

    texto = "SISTEMA DE VENTA INTELIGENTE\n\n"

    texto += "Resumen del pedido:\n"

    if not detalle:
        texto += "- No se pudo generar un pedido valido\n"

    for item in detalle:
        texto += f"- {item['cantidad']} unidades de {item['nombre']} (Subtotal: ${item['subtotal']})\n"

    texto += f"\nTotal a pagar: ${round(total,2)}\n\n"

    texto += "Analisis del sistema:\n"

    for item in detalle:
        data = obtener_producto(item["nombre"])

        if data:
            stock = data["stock"]

            if stock <= 3:
                texto += f"- El producto {item['nombre']} esta por agotarse\n"
                texto += f"- Se recomienda surtir {item['nombre']} urgentemente\n"

            elif stock <= 5:
                texto += f"- El producto {item['nombre']} tiene poco inventario\n"

    if total > 200:
        texto += "- Se aplico un descuento por volumen de compra\n"

    if any(item["cantidad"] >= 5 for item in detalle):
        texto += "- Compra por mayoreo detectada\n"

    texto += "\nRecomendacion general:\n"

    if total > 300:
        texto += "- Cliente con alto consumo, posible cliente frecuente\n"
    else:
        texto += "- Operacion normal del sistema\n"

    texto += "\nOperacion validada correctamente"

    return texto