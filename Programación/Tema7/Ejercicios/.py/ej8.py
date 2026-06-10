from pathlib import Path


class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return (
            f"{self.id} | {self.nombre} | {self.precio} | {self.stock}"
        )


if __name__ == '__main__':
    ruta = Path(__file__).parent.parent / '.csv' / 'ej8.csv'
    productos = []

    with open(ruta, 'r', encoding='utf-8') as f:
        next(f)
        for linea in f:
            id, nombre, precio, stock = linea.strip().split(',')
            producto = Producto(id, nombre, precio, stock)
            productos.append(producto)

    [print(p) for p in productos]