import clientes as cl
import productos as pr

order_food = {}

def create_order():
    try:
        id_order = int(input("Enter order ID: ").strip())
        id_client = int(input("Enter client ID: ").strip())
        id_product = int(input("Enter product ID: ").strip())
        quantity = int(input("Enter quantity: ").strip())
    except ValueError:
        print("Invalid data")
        return None

    
    client = cl.get_client(id_client)
    if client is None:
        print("Client does not exist")
        return None

  
    product = pr.get_product(id_product)
    if product is None:
        print("Product does not exist")
        return None

   
    _, product_name, unit_price = product

    total = unit_price * quantity

    order_food[id_order] = {
        "client": client["Name"],
        "product": product_name,
        "unit_price": unit_price,
        "quantity": quantity,
        "total": total
    }

    print("Order created successfully")

    return order_food[id_order]