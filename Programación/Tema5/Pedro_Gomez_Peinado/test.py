from datetime import date
from datos import get_datos
from Banda import Banda
from BibliotecaBandas import Biblioteca_Bandas


lista = get_datos(1)

mj = Banda(0, 'Michael Jackson', ['Pop', 'Funk', 'Acid Jazz'], 9, False, date(1972, 1, 24), date(2009, 6, 25), {'Michael Jackson': 'Cantante'})

print('---Listado de bandas---')
[print(f'{b.id} | {b.nombre}: {b.nota_discografia}') for b in lista.bandas]
input()

print('\nProbando añadir banda...')
Biblioteca_Bandas.añadir_banda(lista, mj)
[print(f'{b.id} | {b.nombre}: {b.nota_discografia}') for b in lista.bandas]
input()

print('\nProbando eliminar la banda de ID 11...')
Biblioteca_Bandas.eliminar_banda(lista, 11)
[print(f'{b.id} | {b.nombre}: {b.nota_discografia}') for b in lista.bandas]
input()

print('\nProbando padre divorciado...')
lista.bandas = Biblioteca_Bandas.musica_padre_divorciado(lista.bandas)
print(lista.bandas[4].generos)
input()

print('\nProbando chester idolo...')
lista.bandas = Biblioteca_Bandas.chester_idolo(lista.bandas)
[print(f'{b.id} | {b.nombre}: {b.nota_discografia}') for b in lista.bandas]
input()

print('\nBanda más corta:')
print(Biblioteca_Bandas.banda_mas_corta(lista).nombre)
input()

print('\nBanda más duradera:')
print(Biblioteca_Bandas.banda_mas_duradera(lista).nombre)
input()

print('\nProbando post kurt....')
Biblioteca_Bandas.post_kurt(lista)
input()

print('\nBandas que aparecieron entre 1990 y 1995...')
Biblioteca_Bandas.aparicion_durante_periodo(lista, 1990, 1995)
input()

print('\nBuscando las bandas en las que aparece Scott Weiland...')
Biblioteca_Bandas.buscador_bandas_por_artista(lista, 'Scott Weiland')
input()

Biblioteca_Bandas.ordenar_por_nombres(lista)
input()

Biblioteca_Bandas.ordenar_por_nota(lista)
input()

Biblioteca_Bandas.ordenar_por_actividad(lista)
input()

Biblioteca_Bandas.ordenar_por_fecha_inicio(lista)
input()

Biblioteca_Bandas.ordenar_por_fecha_muerte(lista)