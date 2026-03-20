import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

import clientes as cl
import productos as pr
import pedidos as pd
import reportes as rp
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
    
def pause():
    input("\nPress Enter to continue...")    


def menu():
    while True:
        
        clear()
        
        print("\n===== ORDER MANAGEMENT SYSTEM =====")
        print("1. Register clients")
        print("2. Register products")
        print("3. Create order")
        print("4. View report")
        print("5. Exit")

        option = input("Select an option: ").strip()

        if option == "1":
            cl.create_clients()
            pause()

        elif option == "2":
            pr.create_products(pr.products)
            pause()

        elif option == "3":
            if not cl.client:
                print("You must register clients first")
                pause()
                continue

            if not pr.products:
                print("You must register products first")
                pause()
                continue

            pd.create_order()
            pause()

        elif option == "4":
            if not pd.order_food:
                print("No orders registered")
                continue

            report = rp.generate_report(pd.order_food)
            show_report(report)
            pause()

        elif option == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid option")


def show_report(report):
    print("\n===== FINAL REPORT =====")
    print(f"Total orders: {report['total_orders']}")
    print(f"Total income: {report['total_income']}")

    print("\n--- Orders by client ---")
    for client, orders in report["orders_by_client"].items():
        print(f"{client}: {len(orders)} orders")

    print("\n--- Products sold ---")
    for product, quantity in report["sold_products"].items():
        print(f"{product}: {quantity}")


if __name__ == "__main__":
    menu()