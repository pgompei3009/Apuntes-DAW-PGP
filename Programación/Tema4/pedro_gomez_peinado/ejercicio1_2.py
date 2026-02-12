from datetime import datetime
from Pedido import Pedido
from datos import get_datos


def f2a(pedidos: list[Pedido]) -> Pedido:
    return max(pedidos, key = lambda p: p.precio)

def f2b(pedidos: list[Pedido]) -> float:
    return sum([p.precio for p in pedidos])/len(datos)

def f2c(pedidos: list[Pedido], transportista: str) -> list[Pedido]:
    return [p.id_pedido for p in pedidos if p.transportista == transportista]

def f2d(pedidos: list[Pedido]) -> Pedido:
    return max(pedidos, key = lambda p: p.fecha_pedido)

def f2e(pedidos: list[Pedido]) -> Pedido:
    return min(pedidos, key = lambda p: p.fecha_entrega-p.fecha_pedido)

def f2f(pedidos: list[Pedido]) -> Pedido:
    return max(pedidos, key = lambda p: Pedido.precio_por_kg(p))

def f2g(pedidos: list[Pedido]) -> dict[str, float]:
    leñas = {}
    tipos = ['Cerezo', 'Olivo', 'Almendro']
    for t in tipos:
        leñas[t] = sum([p.precio for p in pedidos if p.tipo == t])
    
    return leñas

def f2h(pedidos: list[Pedido]) -> dict[str, int]:
    reporte = {}
    localidades = ['Monachil', 'Cájar', 'Huétor Vega', 'La Zubia', 'Granada']
    for l in localidades:
        numPedidos = 0
        for p in pedidos:
            if p.direccion[2] == l:
                numPedidos += 1

        reporte[l] = numPedidos

    return reporte

datos = get_datos()

datos.insert(0, Pedido(21, 'Cerezo', 450, ['Camino del Río', 3, 'Cájar'], datetime(2024, 2, 10), datetime(2024, 2, 17), 360, 'Raulito'))
datos.insert(1, Pedido(22, 'Olivo', 600, ['Calle Real', 8, 'Monachil'], datetime(2024, 2, 5), datetime(2024, 2, 12), 420, 'Manolito'))

print(f'2a. El id del pedido con mayor precio es: {f2a(datos).id_pedido} y su precio es: {f2a(datos).precio} €')

print(f'2b. El precio medio de los pedidos es: {round(f2b(datos), 2)} €')

print(f'2c. Pedidos realizados por "Manolito": {f2c(datos, 'Manolito')}')

print(f'2d. El id del pedido más reciente (fecha en la que se hizo el pedido no en la que se entregó) es: {f2d(datos).id_pedido}')

print(f'2e. El id del pedido con menor tiempo de entrega es: {f2e(datos).id_pedido} y su tiempo de entrega fue de {f2e(datos).fecha_entrega.day - f2e(datos).fecha_pedido.day} días')

print(f'2f. El id del pedido con mayor precio por kg es: {f2f(datos).id_pedido} y su precio por kg es: {Pedido.precio_por_kg(f2f(datos))} €/kg')

print(f'2g. Resumen de precios por tipo de leña: {f2g(datos)}')

print(f'2h. Resumen de pedidos por localidad {f2h(datos)}')

