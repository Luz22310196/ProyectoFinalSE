import re

def procesar_mensaje(mensaje):
    mensaje = mensaje.lower().strip()

    productos = []

    # Buscar patrones con cantidad
    patron = r'(\d+)\s*(motores|motor|drivers|driver|nema17|nema)'
    resultados = re.findall(patron, mensaje)

    for cantidad, producto in resultados:
        productos.append({
            "producto": normalizar_producto(producto),
            "cantidad": int(cantidad)
        })

    # Si no encontró cantidad, buscar palabras sueltas
    if not productos:
        if "nema17" in mensaje or "nema" in mensaje:
            productos.append({
                "producto": "NEMA17",
                "cantidad": 1
            })
        elif "motor" in mensaje or "motores" in mensaje:
            productos.append({
                "producto": "motor",
                "cantidad": 1
            })
        elif "driver" in mensaje or "drivers" in mensaje:
            productos.append({
                "producto": "driver",
                "cantidad": 1
            })

    return productos


def normalizar_producto(producto):
    producto = producto.lower()

    if producto in ["nema17", "nema"]:
        return "NEMA17"
    elif producto in ["motor", "motores"]:
        return "motor"
    elif producto in ["driver", "drivers"]:
        return "driver"
    else:
        return producto
``
``