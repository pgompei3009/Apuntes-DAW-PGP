from Pedido import Pedido
from datos import get_datos


def ranking_empleados(pedidos: list[Pedido]) -> None:
    #Poner la puntuación a cada uno
    reporte = []
    transportistas = ['Manolito', 'Juanillo', 'Raulito', 'Pepillo', 'Antoñico']
    for t in transportistas:
        puntuacion = 0
        for p in pedidos:
            dif = p.fecha_entrega-p.fecha_pedido
            if p.transportista == t:
                puntuacion += 1
                
                if dif.days <= 1:
                    puntuacion += 1

                elif dif.days > 3:
                    puntuacion -= 0.25

        reporte.append(puntuacion)

    #Ordenar de mayor a menor
    for _ in range(len(transportistas)):
        mayor = max(reporte)
        print(f'Trabajador: {transportistas[reporte.index(mayor)]}, Puntos: {mayor}')

        transportistas.remove(transportistas[reporte.index(mayor)])
        reporte.remove(mayor)

datos = get_datos()

ranking_empleados(datos)

