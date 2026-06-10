from pathlib import Path


class Banda:
    def __init__(self, id: int, nombre: str, albums: int, cantante: str):
        self.id = id
        self.nombre = nombre
        self.albums = albums
        self.cantante = cantante

    def __str__(self):
        return (
            f'{self.id} | {self.nombre} | Albums: {self.albums} | Cantante: {self.cantante}'
        )
    

if __name__ == '__main__':
    bandas = []
    ruta = Path(__file__).parent.parent / '.csv' / 'ej9.csv'
    with open(ruta, 'r', encoding='utf-8') as f:
        next(f)
        for linea in f:
            id, nombre, albums, cantante = linea.strip().split(',')
            banda = Banda(id, nombre, albums, cantante)
            bandas.append(banda)

    [print(b) for b in bandas]
    
