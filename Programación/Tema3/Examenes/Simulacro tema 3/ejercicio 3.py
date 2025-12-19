from random import randint

equipos1 = ["Real Madrid", "Atlético de Madrid", "FC Barcelona", "Athletic Bilbao"]
equipos2 = ["Real Sociedad", "Betis", "Granada", "Valencia"]

def emparejar(equipos1: list[str], equipos2: list[str]) -> print:
    print('------EMPAREJAMIENTOS------')
    for equipo in equipos1:
        contrincante = equipos2[randint(0,len(equipos2)-1)]
        print(f'{equipo}\tvs\t{contrincante}')
        equipos2.remove(contrincante)

emparejar(equipos1, equipos2)