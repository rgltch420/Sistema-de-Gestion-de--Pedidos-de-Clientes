import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

import clientes as cl
import productos as pr
import pedidos as pd
import reportes as rp


def menu():
    while True:
        print("\n===== ORDER MANAGEMENT SYSTEM =====")
        print("1. Register clients")
        print("2. Register products")
        print("3. Create order")
        print("4. View report")
        print("5. Exit")

        option = input("Select an option: ").strip()

        if option == "1":
            cl.createClients()

        elif option == "2":
            pr.create_products(pr.products)

        elif option == "3":
            if not cl.client:
                print("You must register clients first")
                continue

            if not pr.products:
                print("You must register products first")
                continue

            pd.create_order()

        elif option == "4":
            if not pd.order_food:
                print("No orders registered")
                continue

            report = rp.generar_reporte(pd.order_food)
            show_report(report)

        elif option == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid option")


def show_report(report):
    print("\n===== FINAL REPORT =====")
    print(f"Total orders: {report['total_pedidos']}")
    print(f"Total income: {report['total_ingresos']}")

    print("\n--- Orders by client ---")
    for client, orders in report["pedidos_por_cliente"].items():
        print(f"{client}: {len(orders)} orders")

    print("\n--- Products sold ---")
    for product, quantity in report["productos_vendidos"].items():
        print(f"{product}: {quantity}")


if __name__ == "__main__":
    menu()