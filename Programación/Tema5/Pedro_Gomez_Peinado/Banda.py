from datetime import date


class Banda:
    def __init__(self, id: int, nombre: str, generos: list[str], nota_discografia: float, activa: bool, fecha_primer_album: date, fecha_muerte: date, integrantes: dict[str, str]):
        self.id = id
        self.nombre = nombre
        self.generos = generos
        self.nota_discografia = nota_discografia
        self.activa = activa
        self.fecha_primer_album = fecha_primer_album
        self.fecha_muerte = fecha_muerte
        self.integrantes = integrantes
    
    def __str__(self):
        if len(self.generos) > 1:
            str_generos = ', '.join(self.generos[:-1])
            str_generos += f' y {self.generos[-1]}'
        else:
            str_generos = self.generos[0]

        lista_str_integrantes = [f'{integrante}: {rol}' for integrante, rol in self.integrantes.items()]
        str_integrantes = f'\t{lista_str_integrantes[0]}\n\t'
        str_integrantes += ('\n\t').join(lista_str_integrantes[1:])

        return (
            f'1 - Nombre de la banda: {self.nombre}\n'
            f'2 - Géneros: {str_generos}\n'
            f'3 - Nota de la discografía: {self.nota_discografia}\n'
            f'4 - ¿Sigue activa la banda?: {self.activa}\n'
            f'5 - Año de fundación: {self.fecha_primer_album}\n'
            f'6 - Fecha de la muerte del cantante: {self.fecha_muerte}\n'
            f'7 - Integrantes:\n{str_integrantes}\n'
        )

    def __eq__(self, other) -> bool:
        if isinstance(other, Banda):
            return self.id == other.id
        return False

    def __hash__(self):
        return self.id