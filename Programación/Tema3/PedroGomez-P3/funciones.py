import random

def imprimirNivel(nivel: int):
    print('--------------\n'
         f'    NIVEL {nivel+1}\n'
          '--------------')

def generarNivel(palabrasNiveles: list[str], nivel) -> list[str]:
    enunciadoNivel = []
    palabraNivel = palabrasNiveles[nivel][random.randint(0,7)]

    for char in palabraNivel:
        enunciadoNivel.append('_')
    
    return palabraNivel, enunciadoNivel

def comprobarLetra(vidas: int, letra: str, nivel: list[str], palabraNivel: list[str], letrasUtilizadas: list[str]) -> list[int, list[str]]:
    letraEncontrada = False
    for i, char in enumerate(palabraNivel):
        if char == letra:
            nivel[i] = letra
            letraEncontrada = True
    
    if letraEncontrada == False:
        print('Has fallado :(, pierdes una vida')
        vidas -= 1
    elif letra in letrasUtilizadas:
        print('Ya has puesto esa letra... -1 vida')
        vidas -= 1
    else:
        print('Has encontrado una letra!!! Te sumo una vida')
        vidas += 1

    letrasUtilizadas.append(letra)
    return nivel, letrasUtilizadas, vidas