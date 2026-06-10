class Curso:
    def __init__(self, id: int, nombre: str, creditos: int, profesor: str, plazas_totales: int):
        self.id = id
        self.nombre = nombre
        self.creditos = creditos
        self.profesor = profesor
        self.alumnos = []
        self.plazas_totales = plazas_totales


    def matricular(self, alumno_id: int) -> bool:
        if alumno_id in self.alumnos or len(self.alumnos) == self.plazas_totales:
            return False
        self.alumnos.append(alumno_id)
        return True
    

    def desmatricular(self, alumno_id: int) -> bool:
        if alumno_id not in self.alumnos:
            return False
        self.alumnos.remove(alumno_id)
        return True
    

    def plazas_disponibles(self) -> int:
        return self.plazas_totales - len(self.alumnos)
    

    def esta_matriculado(self, alumno_id: int) -> bool:
        return alumno_id in self.alumnos
    

    def __eq__(self, other: Curso) -> bool:
        if isinstance(other, Curso):
            return self.id == other.id
        return False
    

    def __hash__(self) -> hash:
        return hash(self.id)
    

    def __str__(self) -> str:
        return (
            f'Curso | ID: {self.id} | Nombre: {self.nombre} | Créditos: {self.creditos} | Plazas libres: {self.plazas_disponibles()}'
        )