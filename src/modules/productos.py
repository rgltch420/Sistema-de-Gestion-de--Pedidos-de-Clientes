    # Task 4: Consult registered orders
# Rule: No lists allowed. Using Dictionary and Tuples only.

def get_all_orders(orders_dict):
    """
    Shows all orders stored in the dictionary.
    Returns: A status message (String).
    """
    # 1. Validation: Check if the dictionary is empty
    if len(orders_dict) == 0:
        return "No orders found"

    print("--- REGISTERED ORDERS ---")
    
    # 2. Loop: Go through each order in the dictionary
    for order_id in orders_dict:
        # Get the order info using its ID
        order_info = orders_dict[order_id]
        
        # RULE: product is a TUPLE (id, name, price)
        # Position 1 is the product name
        product_tuple = order_info["product"]
        product_name = product_tuple[1] 
        
        customer = order_info["customer"]
        quantity = order_info["quantity"]
        total = order_info["total"]

        # Display the info in a clear format
        print(f"Customer: {customer} | Product: {product_name} | Qty: {quantity} | Total: {total}")

    # RULE: All functions must return a value
    return "Report finished"
