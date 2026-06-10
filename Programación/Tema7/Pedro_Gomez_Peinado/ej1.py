from pathlib import Path
import json


class Vertice():
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z


class Poligono():
    def __init__(self, id: int, textura: str, vertices: list[Vertice]) -> None:
        self.id = id
        self.textura = textura
        self.vertices = vertices


if __name__ == '__main__':

    ruta = Path(__file__).parent / 'datos' / 'poligonos.json'

    with open(ruta, 'r', encoding='utf-8') as f:
        fichero = json.load(f)

    lista_poligonos = []
    dict_texturas = {}
    poligonos_z_positivo = []
    poligonos = fichero['poligonos']

    for p in poligonos:
        vertices = []
        datos_vertices = p['vertices']
        
        for vertice in datos_vertices:
            nuevo_vertice = Vertice(
                vertice['x'],
                vertice['y'],
                vertice['z']
            )
            vertices.append(nuevo_vertice)

        nuevo_poligono = Poligono(
            p['id'],
            p['textura'],
            vertices
        )
        lista_poligonos.append(nuevo_poligono)

        if nuevo_poligono.textura not in dict_texturas:
            dict_texturas[nuevo_poligono.textura] = [nuevo_poligono.id]
        else:
            dict_texturas[nuevo_poligono.textura].append(nuevo_poligono.id)
        
        z_positivo = True
        for v in nuevo_poligono.vertices:
            if v.z < 0:
                z_positivo = False
        
        if z_positivo:
            poligonos_z_positivo.append(nuevo_poligono.id)

    print('POLÍGONOS AGRUPADOS POR TEXTURA')
    print('===============================')
    for clave, valor in dict_texturas.items():
        print(f'{clave}:')
        for v in valor:
            print(f'  - {v}')
        print('')

    print('POLÍGONOS CON TODOS SUS VÉRTICES EN O SOBRE EL PLANO Z = 0')
    print('=========================================================')
    for p in poligonos_z_positivo:
        print(f'- {p}')

        