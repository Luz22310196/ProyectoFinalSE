def explicar(detalle, total, alertas):
    texto = "\n🧾 RESUMEN DEL PEDIDO:\n"

    for item in detalle:
        texto += f"- {item['cantidad']} x {item['nombre']} = ${item['subtotal']}\n"

    texto += f"\n Total final: ${total}\n"

    if alertas:
        texto += "\n Inferencias realizadas:\n"
        for a in alertas:
            texto += f"- {a}\n"

    return texto
