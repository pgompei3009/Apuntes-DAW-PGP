import random

def imprimirNivel(nivel: int):
    print('--------------\n'
         f'    NIVEL {nivel+1}\n'
          '--------------')

def generarNivel(palabrasNiveles: list[str], nivel) -> list[str]:
    enunciadoNivel = []
    palabraNivel = palabrasNiveles[nivel][random.randint(0,7)]

    for _ in palabraNivel:
        enunciadoNivel.append('_')
    
    return palabraNivel, enunciadoNivel

def comprobarLetra(vidas: int, letra: str, enunciadoNivel: list[str], palabraNivel: list[str], letrasUtilizadas: list[str]) -> list[int, list[str]]:
    if letra in letrasUtilizadas:
        print('Ya has puesto esa letra... -1 vida')
        vidas -= 1

    elif letra in palabraNivel:
        print('Has encontrado una letra!!! Te sumo una vida')
        letrasUtilizadas.append(letra)
        vidas += 1
        for i, char in enumerate(palabraNivel):
            if char == letra:
                enunciadoNivel[i] = letra

    else:
        print('Has fallado :(, pierdes una vida')
        letrasUtilizadas.append(letra)
        vidas -= 1
     
    
    return enunciadoNivel, letrasUtilizadas, vidas

def jugar_nivel(nivel: int, vidas: int, enunciadoNivel: list[str], palabraNivel: list  [str]) -> list[int, int]:
    letrasUtilizadas = []   
    while True:
        if vidas == 0:
                print('Has perdido')
                SystemExit
        if '_' not in enunciadoNivel:
                print('Enhorabuena, has encontrado la palabra:\n'
                    f'{enunciadoNivel}')
                nivel += 1
                break
                
        print(f'Tienes: {vidas} vidas\n'
                f'Palabra que debes encontrar:\n {enunciadoNivel}')
        letra = input('Inserta una letra: ')
        enunciadoNivel, letrasUtilizadas, vidas = comprobarLetra(vidas, letra, enunciadoNivel, palabraNivel, letrasUtilizadas)
 
    return nivel, vidas