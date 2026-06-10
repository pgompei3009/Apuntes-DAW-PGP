from datetime import date


class Planta:
    def __init__(self, id: int, producto: str, fecha: date, precio: float) -> None:
        self.id = id
        self.producto = producto
        self.fecha = fecha
        self.precio = precio

    def __str__(self) -> str:
        fecha_str = self.fecha.strftime('%d/%m/%Y')
        return (
            f'{self.id} - {self.producto} - {fecha_str} - {self.precio:.2f}€'
        )
    
if __name__ == '__main__':
    ruta = 'vivero.csv'
    plantas = []
    total = producto_mas_caro = 0

    with open(ruta, 'r', encoding='utf-8') as f:
        next(f)
        for linea in f:
            id, producto, fecha, precio = linea.strip().split(',')
            precio = float(precio)
            dia, mes, año = fecha.split('/')
            fecha = date(int(año), int(mes), int(dia))
            planta = Planta(id, producto, fecha, precio)
            if planta.fecha.month == 1 and planta.fecha.year == 2022:
                plantas.append(planta)
                if precio > producto_mas_caro:
                    producto_mas_caro = precio

                total += precio

    [print(p) for p in plantas]
    print(f'\nImporte total: {total:.2f}€')
    for p in plantas:
        if p.precio == producto_mas_caro:
            print(f'Producto más caro: {p.producto} ({p.precio:.2f}€)')
    
    print(f'Precio medio: {total/len(plantas):.2f}€')