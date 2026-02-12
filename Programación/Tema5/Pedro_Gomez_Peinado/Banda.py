from datetime import datetime


class Banda:
    def __init__(self, id: int, nombre: str, nota_discografia: float, activa: bool, fecha_primer_album: datetime, fecha_muerte: datetime, integrantes: list[str]):
        self.id = id
        self.nombre = nombre
        self.nota_discografia = nota_discografia
        self.activa = activa
        self.fecha_primer_album = fecha_primer_album
        self.fecha_muerte = fecha_muerte
        self.integrantes = integrantes

    
    def __str__(self):
        if len(self.artistas) > 1:
            str_integrantes = ', '.join(self.integrantes[:-1])
            str_integrantes += ' y '.join(self.integrantes[-1])
        else:
            str_integrantes = self.integrantes[0]

        return (
            f'Código: {self.id}\n'
            f'Nombre de la banda: {self.nombre}\n'
            f'Nota de la discografía: {self.nota_discografia}\n'
            f'¿Sigue activa la banda?: {self.activa}\n'
            f'Año de fundación: {self.fecha_primer_album}\n'
            f'Fecha de la muerte del cantante: {self.fecha_muerte}\n'
            f'Integrantes: {str_integrantes}\n'
        )
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Banda):
            return self.id == other.id
        return True
    

    def integrantes_comunes(self, other) -> None:
        integrantes_comunes = []
        for i in self.integrantes:
            if i in other.integrantes:
                integrantes_comunes.append(i)

        print(f'La banda {self.nombre} comparte los siguientes integrantes con la banda {other.nombre}:')
        [print(i) for i in integrantes_comunes]

