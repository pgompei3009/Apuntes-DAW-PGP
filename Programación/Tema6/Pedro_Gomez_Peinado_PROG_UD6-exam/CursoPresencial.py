from Curso import Curso


class CursoPresencial(Curso):
    PRECIO_CREDITO = 15

    def __init__(self, id: int, nombre: str, creditos: int, profesor: str, plazas_totales: int, direccion: str, aula: str):
        super().__init__(id, nombre, creditos, profesor, plazas_totales)
        self.direccion = direccion
        self.aula = aula
        self.asistencia = {}


    def calcular_coste(self) -> float:
        return self.creditos*self.PRECIO_CREDITO
    

    def pasar_lista(self, fecha: str, alumnos_presentes: list[int]) -> None:
        if fecha not in self.asistencia:
            self.asistencia[fecha] = [a for a in alumnos_presentes if a in self.alumnos]
        else:
            print('Ya se paso lista ese dia')


    def __str__(self) -> str:
        base = super().__str__()
        return (
            f'{base} | Tipo: Presencial | Aula: {self.aula} | Coste: {self.calcular_coste()}€'
        )
