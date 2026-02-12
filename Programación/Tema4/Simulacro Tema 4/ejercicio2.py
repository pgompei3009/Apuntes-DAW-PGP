from datetime import datetime
from Jugador import Jugador
from ejercicio1 import atletico_madrid


def f2a(jugadores: list) -> Jugador:
    masPartidos = max(jugadores, key = lambda j: j.partidos_jugados)
    return masPartidos

def f2b(jugadores: list) -> Jugador:
    mayorRatio = max(jugadores, key = lambda j: j.ratio_goles())
    return mayorRatio

'''
def f2c(jugadores: list) -> Jugador:
    defensaMasGoles = max([j for j in jugadores])
    return defensaMasGoles
'''
def f2d(jugadores: list) -> list:
    lista2d = []
    lista2d.append(max(jugadores, key = lambda j: Jugador.ratio_goles(j) and j.posicion == 'Defensa'))
    lista2d.append(max(jugadores, key = lambda j: Jugador.ratio_goles(j) and j.posicion == 'Centrocampista'))
    lista2d.append(max(jugadores, key = lambda j: Jugador.ratio_goles(j) and j.posicion == 'Delantero'))
    return lista2d

def f2e(jugadores: list) -> list:
    hoy = datetime.now()
    lista2e = [j.nombre for j in jugadores if hoy.year - j.fecha_nacimiento.year - ((hoy.month, hoy.day) < (j.fecha_nacimiento.month, j.fecha_nacimiento.day)) <= 28]
    return lista2e

def f2f(jugadores: list) -> list:
    return [j.nombre for j in jugadores if j.goles == 0 and j.posicion != 'Portero']

def f2g(jugadores: list) -> list:
    return [j.nombre for j in jugadores if j.fecha_alta.year < 2015]

def f2h(jugadores: list) -> list:
    delanteroMenosGoles = min([j for j in jugadores if j.posicion == 'Delantero'], key=lambda j: j.goles)
    return [j.nombre for j in jugadores if j.posicion == 'Centrocampista' and j.goles > delanteroMenosGoles.goles]

def f2i(jugadores: list) -> dict[str, int]:
    datos = {}
    posiciones = ['Portero', 'Defensa', 'Centrocampista', 'Delantero']
    for p in posiciones:
        datos[p] = sum([j.goles for j in jugadores if j.posicion == p])

    return datos

def f2j(jugadores: list) -> dict[str, list[Jugador]]:
    lista = {}
    posiciones = ['Portero', 'Defensa', 'Centrocampista', 'Delantero']
    for p in posiciones:
        lista[p] = [j for j in jugadores if j.posicion == p]

    return lista

def f2k(jugadores: list) -> dict[str, list[Jugador]]:
    cosas = {}
    rangos = ['Debutante', 'Principiante', 'Senior', 'Veterano']
    for r in rangos:
        for


print(f'2a. Jugador con más partidos: {f2a(atletico_madrid).nombre}\n------------------')

print(f'2b. Jugador con mejro ratio goleador: {f2b(atletico_madrid).nombre}\n------------------')
'''
print(f'2c. Defensa con más goles: {f2c(atletico_madrid).nombre}\n------------------')
'''
print(f'2d. Los jugadores, por posición, con mejor ratio goleador son: ')

[print(f'\t{j.posicion}: {j.nombre}') for j in f2d(atletico_madrid)]
print('------------------')
print(f'2e. Los jugadores con 28 o menos años son: {f2e(atletico_madrid)}\n------------------')

print(f'2f. Los jugadores que nunca han metido gol y no son porteros son: {f2f(atletico_madrid)}\n------------------')

print(f'2g. Los jugadores que llevan en el equipo desde antes de 2015 son: {f2g(atletico_madrid)}\n------------------')

print(f'2h. Los jugadores que llevan en el equipo desde antes de 2015 son: {f2h(atletico_madrid)}')

print(f'2i.')
datos = f2i(atletico_madrid)
print(datos)

print(f'2j.')
lista = f2j(atletico_madrid)
print(lista)
