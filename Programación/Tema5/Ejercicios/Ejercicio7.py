from random import shuffle
from Ejercicio6 import Cancion


class Playlist:
    
    def __init__(self, id_playlist: int, nombre: str, canciones: list[Cancion] | None = None):
        self.id_playlist = id_playlist
        self.nombre = nombre
        self.canciones = canciones

        if canciones is None:
            self.canciones: list[Cancion] = []
        else:
            self.canciones = canciones

    
    def __str__(self):
        if len(self.canciones) > 1:
            str_canciones = ', '.join(self.canciones)[:-1]
            str_canciones += ' y '.join(self.cancuones)[-1]
        else:
            str_canciones = self.canciones[0]
            
        return (
            f'Nombre: {self.nombre}\n'
            f'Número de canciones: {len(self.canciones)}\n'
            f'Listado de canciones: {self.canciones}'
        )


    def añadir_cancion(self, cancion: Cancion):
        self.canciones.append(cancion)


    def eliminar_cancion(self, id: int):
        for c in self.canciones:
            if c.id == id:
                self.canciones.remove(c)
                return True
        return False


    def duracion_total(self):
        return sum(c.duracion for c in self.canciones)
    

    def buscar_por_artista(self, artista: str):
        resultado = []
        for c in self.canciones:
            if artista in c.artistas:
                resultado.append(c)
        return resultado
    

    def buscar_por_genero(self, genero: str):
        resultado = []
        for c in self.canciones:
            if genero in c.generos:
                resultado.append(c)
        return resultado
    

    def cancion_mas_corta(self):
        if len(self.canciones) == 0:
            return None
        return min(self.canciones, key = lambda c: c.duracion)
    

    def cancion_mas_larga(self):
        if len(self.canciones) == 0:
            return None
        return max(self.canciones, key = lambda c: c.duracion)


    def ordenar_por_duracion(self):
        canciones_ordenadas = []
        canciones_ordenadas = sorted(self.canciones, key = lambda c: c.duracion)
        return canciones_ordenadas
    

    def año(self, año: int):
        resultado = []
        for c in self.canciones:
            if año == c.fecha_salida.year:
                resultado.append(c)
        return resultado
    

    def aleatorio(self):
        canciones_shuffle = []
        canciones_shuffle = shuffle(self.canciones)
        return canciones_shuffle