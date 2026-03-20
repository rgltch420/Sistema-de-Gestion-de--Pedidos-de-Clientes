products = {}

def create_products(products_dict):
    count = 0

    while True:
        try:
            total = int(input("How many products do you want to register?: ").strip())
            if total < 1:
                print("You must register at least 1 product")
                continue
            break
        except ValueError:
            print("Enter only positive numbers")

    while count < total:
        try:
            product_id = int(input("Enter product ID: ").strip())
            if product_id < 1:
                print("ID must be greater than 0")
                continue
        except ValueError:
            print("Invalid ID")
            continue

        product_name = input("Enter product name: ").strip()

        try:
            unit_price = float(input("Enter product price: ").strip())
            if unit_price <= 0:
                print("Price must be greater than 0")
                continue
        except ValueError:
            print("Invalid price")
            continue

        if not product_name:
            print("Product name cannot be empty")
            continue

        product_tuple = (product_id, product_name, unit_price)
        products_dict[product_id] = product_tuple

        print(f"Product '{product_name}' registered successfully")
        count += 1

    return products_dict