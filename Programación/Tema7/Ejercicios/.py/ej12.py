from pathlib import Path
import json


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


if __name__ == "__main__":

    ruta = Path(__file__).parent.parent / ".json" / "ej12.json"

    bandas = []

    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f)

        for d in datos:
            banda = Banda(
                d["id"],
                d["nombre"],
                d["albums"],
                d["cantante"],
            )
            bandas.append(banda)

    for b in bandas:
        print(b)