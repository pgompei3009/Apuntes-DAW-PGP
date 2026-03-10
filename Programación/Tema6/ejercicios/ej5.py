class Bolsa:
    MAX_ARTICULOS = 10

    def __init__(self, lista_productos: list[str]):
        self.lista_productos = lista_productos

    def añadir_producto(self, producto: Producto) -> None:
        if len(self.lista_productos) == self.MAX_ARTICULOS:
            print('Has alcanzado el máximo de productos')
        else:
            self.lista_productos.append(producto)


class Producto:
    def __init__(self, nombre: str):
        self.nombre = nombre

if __name__ == '__main__':
    b = Bolsa([])
    p = Producto('Cocacola')

    while True:
        opc = input('Quieres coca? (S/N): ')
        if opc == 'S':
            Bolsa.añadir_producto(b, p)
        else:
            break

