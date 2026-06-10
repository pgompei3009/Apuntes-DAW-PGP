from random import randint
from Curso import Curso


class CursoOnline(Curso):
    PRECIO_CREDITO = 10

    def __init__(self, id: int, nombre: str, creditos: int, profesor: str, plazas_totales: int, plataforma: str, url: str):
        super().__init__(id, nombre, creditos, profesor, plazas_totales)
        self.plataforma = plataforma
        self.url = url


    def calcular_coste(self) -> float:
        return self.creditos*self.PRECIO_CREDITO
    

    def generar_reunion(self) -> str:
        reunion = self.url + '/'
        for _ in range(10):
            reunion += str(randint(0, 9))
        return reunion


    def __str__(self) -> str:
        base = super().__str__()
        return (
            f'{base} | Tipo: Online | Plataforma: {self.plataforma} | Coste: {self.calcular_coste()}€'
        )