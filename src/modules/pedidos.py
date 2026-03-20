import clientes as cl
import productos as pr

order_food = {}

def create_order():
    try:
        id_order = int(input("Ingresa el ID del pedido: ").strip())
        id_client = int(input("Ingresa el ID del cliente: ").strip())
        id_product = int(input("Ingresa el ID del producto: ").strip())
        quantity = int(input("Ingresa la cantidad: ").strip())
    except ValueError:
        print("Datos inválidos")
        return None

    # validar cliente
    cliente = cl.get_client(id_client)
    if cliente is None:
        print("Cliente no existe")
        return None

    # validar producto
    producto = pr.get_product(id_product)
    if producto is None:
        print("Producto no existe")
        return None

    # desempaquetar tupla
    _, product_name, unit_price = producto

    total = unit_price * quantity

    order_food[id_order] = {
        "client": cliente["Name"],
        "product": product_name,
        "unit_price": unit_price,
        "quantity": quantity,
        "total": total
    }

    print(f"Pedido creado correctamente")

    return order_food[id_order]