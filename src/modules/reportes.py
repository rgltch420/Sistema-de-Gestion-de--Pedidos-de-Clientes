def obtener_total_pedidos(pedidos):
    return len(pedidos)


def calcular_total_ingresos(pedidos):
    total = 0
    for pedido in pedidos.values():
        total += pedido["total"]
    return total


def agrupar_por_cliente(pedidos):
    agrupado = {}

    for pedido in pedidos.values():
        cliente = pedido["client"]

        if cliente not in agrupado:
            agrupado[cliente] = {}

        # guardamos pedidos por cliente
        id_pedido = pedido.get("id", len(agrupado[cliente]) + 1)
        agrupado[cliente][id_pedido] = pedido

    return agrupado


def productos_vendidos(pedidos):
    conteo = {}

    for pedido in pedidos.values():
        producto = pedido["product"]

        if producto not in conteo:
            conteo[producto] = 0

        conteo[producto] += pedido["quantity"]

    return conteo

def generar_reporte(pedidos):
    reporte = {
        "total_pedidos": obtener_total_pedidos(pedidos),
        "total_ingresos": calcular_total_ingresos(pedidos),
        "pedidos_por_cliente": agrupar_por_cliente(pedidos),
        "productos_vendidos": productos_vendidos(pedidos)
    }

    return reporte