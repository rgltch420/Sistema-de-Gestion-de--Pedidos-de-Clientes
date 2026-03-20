import clientes as cl
import productos as pr
order_food = {}

def create_order():
   try:
      id_order = int(input("Ingresa el ID del pedido: ").strip())
      id_client = int(input("Ingresa el ID del cliente: ").strip())
      id_product = int(input("Ingresar el ID del producto: ").strip())
   except ValueError:
      print("Datos invalidos")
      return None
      
      product = pr.get_all_orders(id_product)
      if id_product is None:
         print("El producto no existe")
         return None
      product_id, product_name, unit_price = producto
      total = unit_price * quantity
      
      order_food[id_order] = {
        "client": cliente["Name"],
        "product": product_name,
        "unit_price": unit_price,
        "quantity": quantity,
        "total": total
      }
      print(f"Pedido creado: {cliente['Name']} compró {quantity} de {product_name}")
      return order_food[id_order]
    
