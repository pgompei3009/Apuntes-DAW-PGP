from pathlib import Path


class Producto():
    def __init__(self, id: int, nombre: str, precio: float, stock: int) -> None:
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self) -> str:
        return (
            f'{self.id} - {self.nombre} - Precio: {self.precio}€ - Stock: {self.stock}'
        )
    

if __name__ == '__main__':

    ruta = Path(__file__).parent.parent / '.csv' / 'productos.csv'

    with open(ruta, 'r', encoding='utf-8') as f:
        productos = []
        next(f)
        for linea in f:
            linea = linea.strip()
            id, nombre, precio, stock = linea.split(',')
            productos.append(Producto(id, nombre, precio, stock))

    for p in productos:
        print(p)