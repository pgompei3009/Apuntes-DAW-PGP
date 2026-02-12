from datetime import datetime
from Jugador import Jugador
from ejercicio1 import atletico_madrid


def elegir_capitan(jugadores: list) -> Jugador:
    mayorCap = min([j for j in jugadores if j.pos_capitan != 0], key=lambda j: j.pos_capitan)
    capitanes_provisionales = [j for j in jugadores if j.pos_capitan ==  mayorCap.pos_capitan]

    return max(capitanes_provisionales, key = lambda j: j.fecha_nacimiento)


print(f'Capitan del equipo: \n{elegir_capitan(atletico_madrid)}')