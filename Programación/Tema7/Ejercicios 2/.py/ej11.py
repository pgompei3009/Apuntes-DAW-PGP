from pathlib import Path
import json


class Aportacion():
    def __init__(self, nombre: str, anio: int, importancia: str) -> None:
        self.nombre = nombre
        self.anio = anio
        self.importancia = importancia

    def __str__(self) -> str:
        return (
            f'{self.nombre}({self.anio}) {self.importancia}'
        )
    
class Cientifico():
    def __init__(self, nombre: str, campo: str, aportacion: Aportacion) -> None:
        self.nombre = nombre
        self.campo = campo
        self.aportacion = aportacion

    def __str__(self) -> str:
        return (
            (f'{self.nombre} ({self.campo}) -> Aportación: {self.aportacion}')
        )
    

if __name__ == '__main__':

    ruta = Path(__file__).parent.parent / '.json' / 'ej11.json'

    with open(ruta, 'r', encoding='utf-8') as f:
        cientificos = []
        datos = json.load(f)
        for d in datos:
            datos_aportacion = d['aportacion']
            nueva_aportacion = Aportacion(
                datos_aportacion['nombre'],
                datos_aportacion['anio'],
                datos_aportacion['importancia']
            )

            nuevo_cientifico = Cientifico(
                d['nombre'],
                d['campo'],
                nueva_aportacion
            )
            cientificos.append(nuevo_cientifico)

    for c in cientificos:
        print(c)