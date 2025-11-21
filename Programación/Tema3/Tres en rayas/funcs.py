import random

def imprimir_tablero(matriz: list[list[int]]):
    print('-------------')
    for fila in matriz:
        print(end='| ')
        for casilla in fila:
            signo = '-'
            if casilla == 1:
                signo = 'X'
            elif casilla == -1:
                signo = 'O'

            print(signo, end=' | ')
        print('\n-------------')
    
def movimiento_jugador(matriz: list[list[int]]) -> list[list[list[int]]]:
    print('Turno Jugador!!!\n')
    while True:
        imprimir_tablero(matriz)
        filaJugador = int(input('Dime en qué fila quieres poner un X: '))-1
        colJugador = int(input('Dime en qué columna quieres poner un X: '))-1
        if matriz[filaJugador][colJugador] == 0:
            matriz[filaJugador][colJugador] = 1
            break
        print('Casilla ya usada, intente de nuevo...')
    return matriz

def movimiento_ia(matriz: list[list[int]]) -> list[list[list[int]]]:
    print('Turno Máquina!!!\n')
    imprimir_tablero(matriz)            
    while True:
        filaIA = random.randint(0, 2)
        colIA = random.randint(0, 2)
        if matriz[filaIA][colIA] == 0:
            matriz[filaIA][colIA] = -1
            break
    return matriz

def resumen(matriz: list[int]) -> tuple[int]:
    estadoMatriz = (
            sum(matriz[0]), 
            sum(matriz[1]), 
            sum(matriz[2]), 
            sum((matriz[0][0] , matriz[1][1] , matriz[2][2])), 
            sum((matriz[0][0] , matriz[1][0] , matriz[2][0])), 
            sum((matriz[0][1] , matriz[1][1] , matriz[2][1])), 
            sum((matriz[0][2] , matriz[1][2] , matriz[2][2])), 
            sum((matriz[0][2] , matriz[1][1] , matriz[2][0])))
    return estadoMatriz

def comprobar_resultado(matriz: list[list[int]]) -> str:
    resultado = None
    estadoMatriz = resumen(matriz)
    tableroCompleto = True

    for fila in matriz:
        if 0 in fila:
            tableroCompleto = False
            break

    if tableroCompleto == True:
        resultado = 'Empate!!!'

    if 3 in estadoMatriz:
        resultado = 'Victoria!!!!'
    
    elif -3 in estadoMatriz:
        resultado = 'Derrota...'

    return resultado