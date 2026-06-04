def explicar(pedidos, explicaciones):
    if not pedidos:
        return "No fue posible generar un pedido.\n\nMotivo:\n- " + "\n- ".join(explicaciones)

    respuesta = "RESULTADO DEL SISTEMA EXPERTO\n\n"

    for p in pedidos:
        respuesta += f"Producto: {p['producto']}\n"
        respuesta += f"Cantidad solicitada: {p['cantidad']}\n"
        respuesta += f"Stock disponible: {p['stock']}\n"
        respuesta += f"Estado: {p['estado']}\n\n"

    respuesta += "EXPLICACIÓN DEL RAZONAMIENTO\n"
    for e in explicaciones:
        respuesta += f"- {e}\n"

    return respuesta
