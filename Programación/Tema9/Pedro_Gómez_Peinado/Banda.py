class Banda:
    def __init__(self, id_banda: int, nombre: str):
        self.id = id_banda
        self.nombre = nombre


    def __str__(self):
        return (
            f'{self.id} - {self.nombre}'
        )