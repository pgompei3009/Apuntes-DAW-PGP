from pathlib import Path
import json


class Habitat():
    def __init__(self, tipo: str, zona: str, clima: str) -> None:
        self.tipo = tipo
        self.zona = zona
        self.clima = clima


class Dinosaurio():
    def __init__(self, nombre: str, periodo: str, habitat: Habitat) -> None:
        self.nombre = nombre
        self.periodo = periodo
        self.habitat = habitat


if __name__ == '__main__':

    ruta = Path(__file__).parent / 'datos' / 'dinos.json'

    with open(ruta, 'r', encoding='utf-8') as f:
        dinosaurios = []
        datos = json.load(f)
        for d in datos:
            datos_habitat = d['habitat']
            nuevo_habitat = Habitat(
                datos_habitat['tipo'],
                datos_habitat['zona'],
                datos_habitat['clima']
            )

            nuevo_dino = Dinosaurio(
                d['nombre'],
                d['periodo'],
                nuevo_habitat
            )
            dinosaurios.append(nuevo_dino)

    dinos_zona = {}
    for d in dinosaurios:
        if d.habitat.zona not in dinos_zona:
            dinos_zona[d.habitat.zona] = [d.nombre]
        else:
            dinos_zona[d.habitat.zona].append(d.nombre)

    print('Dinosaurios por zona:')
    for zona, dinos in dinos_zona.items():
        print(f'{zona}: {dinos}')