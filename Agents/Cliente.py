import re

def interpretar_mensaje(texto):
    productos = []

    patrones = [
        (r'(\d+)\s*motores?\s*nema17', "NEMA17"),
        (r'(\d+)\s*drivers?\s*a4988', "A4988")
    ]

    for patron, nombre in patrones:
        coincidencias = re.findall(patron, texto.lower())
        for c in coincidencias:
            productos.append({
                "nombre": nombre,
                "cantidad": int(c)
            })

    return productos