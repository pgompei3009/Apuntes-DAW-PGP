from datetime import date
from Banda import Banda


class Biblioteca_Bandas:
    def __init__(self, id_biblioteca: int, titulo: str, bandas: list[Banda]) -> None:
        self.id_biblioteca = id_biblioteca
        self.titulo = titulo
        self.bandas = bandas


    def añadir_banda(self, banda: Banda) -> None:
        self.bandas.append(banda)


    def eliminar_banda(self, id: int) -> bool:
        for b in self.bandas:
            if b.id == id:
                self.bandas.remove(b)
                return True
        return False
    
    #Modificar segun una condición
    def musica_padre_divorciado(bandas: list[Banda]) -> list[Banda]:
        for b in bandas:
            if b.fecha_primer_album.year < 2000:
                b.generos.append('Padre divorciado')
        return bandas


    def chester_idolo(bandas: list[Banda]) -> list[Banda]:
        for b in bandas:
            if 'Chester Bennington' in b.integrantes:
                b.nota_discografia = 10
        return bandas

    #Max y min
    def banda_mas_corta(self) -> Banda:
        if len(self.bandas) == 0:
            return None
        return min(self.bandas, key = lambda b: b.fecha_muerte.year - b.fecha_primer_album.year)
    

    def banda_mas_duradera(self) -> Banda:
        if len(self.bandas) == 0:
            return None
        return max(self.bandas, key = lambda b: b.fecha_muerte.year - b.fecha_primer_album.year)
        
    #Fechas
    def post_kurt(self) -> None:
        print('Lista de bandas que aparecieron despues de la muerte de Kurt Cobain:')
        [print(f'ID: {b.id} | {b.nombre}') for b in self.bandas if b.fecha_primer_album > date(1994, 4, 5)]


    def aparicion_durante_periodo(self, inicio: int, fin: int) -> None:
        [print(f'ID: {b.id} | {b.nombre}') for b in self.bandas if b.fecha_primer_album.year >= inicio and b.fecha_primer_album.year <= fin]

    #Ordenar
    def ordenar_por_nombres(self) -> None:
        lista_nombres = sorted([b.nombre for b in self.bandas])
        print('---Bandas ordenadas por nombre')
        for n in lista_nombres:
            for b in self.bandas:
                if b.nombre == n:
                    print(f'ID: {b.id} | {b.nombre}: {b.nota_discografia}')


    def ordenar_por_nota(self) -> None:
        lista_notas = list(set([b.nota_discografia for b in self.bandas]))
        lista_notas = sorted(lista_notas, reverse=True)
        print('---Bandas ordenadas por nota---')
        for n in lista_notas:
            for b in self.bandas:
                if b.nota_discografia == n:
                    print(f'ID: {b.id} | {b.nombre}: {b.nota_discografia}')


    def ordenar_por_actividad(self) -> None:
        lista_actividad = [True, False]
        print('---Bandas ordenadas por actividad---')
        for a in lista_actividad:
            for b in self.bandas:
                if b.activa == a:
                    print(f'ID: {b.id} | {b.nombre}: {b.activa}')


    def ordenar_por_fecha_inicio(self) -> None:
        lista_fechas_inicio = sorted([b.fecha_primer_album for b in self.bandas])
        print('---Bandas ordenadas por la fecha de su primer album---')
        for f in lista_fechas_inicio:
            for b in self.bandas:
                if b.fecha_primer_album == f:
                    print(f'ID: {b.id} | {b.nombre}: {b.fecha_primer_album}')


    def ordenar_por_fecha_muerte(self) -> None:
        lista_fechas_muerte = list(set([b.fecha_muerte for b in self.bandas]))
        lista_fechas_muerte = sorted(lista_fechas_muerte)
        print('---Bandas ordenadas por la fecha de la muerte del cantante---')
        for f in lista_fechas_muerte:
            for b in self.bandas:
                if b.fecha_muerte == f:
                    print(f'ID: {b.id} | {b.nombre}: {b.fecha_muerte}')                    
        
    #Extra
    def buscador_bandas_por_artista(self, nombre_artista: str) -> None:
        print(f'El artista {nombre_artista} ha participado en las siguientes bandas:')
        [print(f'ID: {b.id} | {b.nombre}') for b in self.bandas if nombre_artista in b.integrantes]

