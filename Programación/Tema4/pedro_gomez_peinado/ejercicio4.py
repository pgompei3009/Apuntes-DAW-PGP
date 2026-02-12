from datetime import datetime
from Pedido import Pedido
from datos import get_datos


def aplicar_sobrecoste(pedidos: list[Pedido]) -> None:
    for p in pedidos:
        if p.fecha_pedido >= datetime(2024, 1, 10):
            p.precio = round(p.precio*1.1, 2)

    [print(p.precio) for p in pedidos]

datos = get_datos()

aplicar_sobrecoste(datos)