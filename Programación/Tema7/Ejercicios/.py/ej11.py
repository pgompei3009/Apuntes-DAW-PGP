from pathlib import Path
import json


class Aportacion:
    def __init__(self, nombre, anio, importancia):
        self.nombre = nombre
        self.anio = anio
        self.importancia = importancia

    def __str__(self):
        return (
            f'{self.nombre} ({self.anio}): {self.importancia}'
        )


class Cientifico:
    def __init__(self, id: int, nombre: str, campo: str, aportacion: dict):
        self.id = id
        self.nombre = nombre
        self.campo = campo
        self.aportacion = aportacion


    def __str__(self):
        return (
            f'{self.id} | {self.nombre} | Campo: {self.campo} | Aportacion: {self.aportacion}'
        )


if __name__ == "__main__":

    ruta = Path(__file__).parent.parent / ".json" / "ej11.json"

    cientificos = []

    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f)

        for d in datos:
            datos_aportacion = d['aportacion']
            aportacion = Aportacion(
                datos_aportacion["nombre"],
                datos_aportacion['anio'],
                datos_aportacion['importancia']
            )

            cientifico = Cientifico(
                d["id"],
                d["nombre"],
                d["campo"],
                aportacion,
            )
            cientificos.append(cientifico)

    for c in cientificos:
        print(c)