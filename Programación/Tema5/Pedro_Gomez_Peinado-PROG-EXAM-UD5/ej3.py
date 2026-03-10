from datetime import datetime
from datos import get_productos
from Producto import Producto


def productos_caros(productos: list[Producto], precio_min: float) -> list[Producto]:
    return [p for p in productos if p.precio >= precio_min]

def productos_de_categoria(productos: list[Producto], categoria: str) -> list[Producto]:
    return [p for p in productos if categoria in p.categorias]

def productos_multicategoria(productos: list[Producto]) -> list[Producto]:
    return [p for p in productos if len(p.categorias) > 1]

def productos_caducados(productos: list[Producto]) -> list[Producto]:
    return [p for p in productos if p.fecha_caducidad < datetime.today()]

def producto_mas_caro(productos: list[Producto]) -> Producto | None:
    mas_caro = None
    for p in productos:
        if mas_caro is None:
            mas_caro = p
        elif p > mas_caro:
            mas_caro = p
    return mas_caro

def ordenar_por_caducidad(productos: list[Producto]) -> list[Producto]:
    fechas = sorted([p.fecha_caducidad for p in productos])
    productos_ordenados = []
    for f in fechas:
        for p in productos:
            if p.fecha_caducidad == f:
                productos_ordenados.append(p)
                break
    return productos_ordenados

def hay_productos_caducados(productos: list[Producto]) -> bool:
    for p in productos:
        if p.fecha_caducidad < datetime.today():
            return True
    return False

def eliminar_caducados(productos: list[Producto]) -> list[Producto]:
    nueva_lista = productos.copy()
    eliminar = productos_caducados(productos)
    for p in nueva_lista:
        for e in eliminar:
            if p == e:
                nueva_lista.remove(p)
                break
    return nueva_lista

def dias_en_super(productos: list[Producto]) -> dict[str, int]:
    reporte = {}
    for p in productos:
        reporte[p.id] = (datetime.today() - p.fecha_entrada).days
    return reporte

def conteo_por_categoria(productos: list[Producto]) -> dict[str, int]:
    conteo = {}
    for p in productos:
        for c in p.categorias:
            if c not in conteo:
                conteo[c] = 1
            else:
                conteo[c] += 1
    return conteo


if __name__ == '__main__':
    productos = get_productos()

    print('=== PRODUCTOS CAROS (>= 2.0€) ===')
    id_productos = [p.id for p in productos_caros(productos, 2.0)]
    print(id_productos)

    print('\n=== PRODUCTOS DE CATEGORÍA "Lácteos" ===')
    id_productos = [p.id for p in productos_de_categoria(productos, 'Lácteos')]
    print(id_productos)

    print('\n=== PRODUCTOS MULTICATEGORÍA ===')
    id_productos = [p.id for p in productos_multicategoria(productos)]
    print(id_productos)

    print('\n=== PRODUCTOS CADUCADOS ===')
    id_productos = [p.id for p in productos_caducados(productos)]
    print(id_productos)

    print('\n=== PRODUCTO MÁS CARO ===')
    print(producto_mas_caro(productos).id)

    print('\n=== ORDENADOS POR CADUCIDAD ===')
    id_productos = [p.id for p in ordenar_por_caducidad(productos)]
    print(id_productos)

    print('\n=== ¿HAY PRODUCTOS CADUCADOS? ===')
    print(hay_productos_caducados(productos))

    print('\n=== ELIMINAR CADUCADOS ===')
    nueva_lista = eliminar_caducados(productos)
    id_productos = [p.id for p in nueva_lista]
    print(id_productos)

    print('\n=== DÍAS EN EL SUPERMERCADO ===')
    reporte = dias_en_super(productos)
    print(reporte)

    print('\n=== CONTEO POR CATEGORÍA ===')
    conteo = conteo_por_categoria(productos)
    print(conteo)