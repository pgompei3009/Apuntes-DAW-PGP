from datetime import datetime


class Cancion:

    def __init__(self, id: int, titulo: str, artistas: list[str], album: str, generos: list[str], duracion: int, fecha_salida: datetime):
        self.id = id
        self.titulo = titulo
        self.artistas = artistas
        self.album = album
        self.generos = generos
        self.duracion = duracion #en segundos
        self.fecha_salida = fecha_salida

    def __str__(self):
        return (
            f'Título: {self.titulo}\n'
            f'Artistas: {", ".join(self.artistas)}\n'
            f'Duración: {self.duracion/60}:{self.duracion%60}\n'
        )


    def __eq__(self, other):
        if isinstance(other, Cancion):
            return self.id == other.id
        return False


