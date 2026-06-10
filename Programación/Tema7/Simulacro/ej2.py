from pathlib import Path
import json


class Campeon:
    def __init__(self, nombre: str, posiciones: list[str], dificultad: str) -> None:
        self.id = id
        self.nombre = nombre
        self.posiciones = posiciones
        self.dificultad = dificultad


    def __str__(self) -> str:
        return (
            f'{self.nombre} | Posiciones: {self.posiciones} | Dificultad: {self.dificultad}'
        )


if __name__ == "__main__":

    ruta = "lol.json"
    campeones = []

    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f)

        for d in datos:
            camp = Campeon(
                d["nombre"],
                d["posiciones"],
                d["dificultad"],
            )
            campeones.append(camp)

    for c in campeones:
        if 'Top' in c.posiciones and c.dificultad == 'Baja':
            print(c)