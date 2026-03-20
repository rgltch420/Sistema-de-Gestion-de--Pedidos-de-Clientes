def get_total_orders(orders):
    return len(orders)


def calculate_total_income(orders):
    total = 0
    for order in orders.values():
        total += order["total"]
    return total


def group_by_client(orders):
    grouped = {}

    for order_id, order in orders.items():
        client = order["client"]

        if client not in grouped:
            grouped[client] = {}

        grouped[client][order_id] = order

    return grouped


def sold_products(orders):
    count = {}

    for order in orders.values():
        product = order["product"]

        if product not in count:
            count[product] = 0

        count[product] += order["quantity"]

    return count


def generate_report(orders):
    report = {
        "total_orders": get_total_orders(orders),
        "total_income": calculate_total_income(orders),
        "orders_by_client": group_by_client(orders),
        "sold_products": sold_products(orders)
    }

    return report