from Agents.Cliente import interpretar_mensaje
from Agents.Pedido import generar_pedido
from Agents.Supervisor import explicar

def main():
    print("Sistema Experto de Ventas")

    texto = input("Cliente: ")

    productos = interpretar_mensaje(texto)

    if not productos:
        print("No se entendió el pedido")
        return

    detalle, total, alertas = generar_pedido(productos)

    respuesta = explicar(detalle, total, alertas)

    print(respuesta)

if __name__ == "__main__":
    main()