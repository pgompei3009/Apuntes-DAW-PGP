from Banda import Banda

class Biblioteca_Bandas:
    def __init__(self, id_biblioteca: int, titulo: str, lista_bandas: list[Banda]):
        self.id_biblioteca = id_biblioteca
        self.titulo = titulo
        self.lista_bandas = lista_bandas