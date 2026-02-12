from random import randint
from ejercicio1 import atletico_madrid


def mostrar_alineacion(plantilla: list):
    titulares = [j for j in plantilla if j.titular == True]
    capis_titulares = [j for j in titulares if j.pos_capitan == 1]
    capi = capis_titulares[randint(0, len(capis_titulares)-1)]
    pos = None

    for j in titulares:
        if j.posicion != pos:
            print()
            pos = j.posicion
            if pos == 'Portero':
                print(f'{j.posicion}: ', end='')
            else:
                print(f'{j.posicion}s: ', end='')

        else:
            print('--', end='')

        print(f' ({j.dorsal}) {j.nombre} ', end='')
        if j == capi:
            print(f'[C] ', end='')


mostrar_alineacion(atletico_madrid)
    
