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

def comprobar_resultado(matriz: list[list[int]]) -> str:
    resultado = None
    tableroCompleto = True

    for fila in matriz:
        if 0 in fila:
            tableroCompleto == False
            break

    if tableroCompleto == True:
        resultado = 'Empate!!!'

    if (matriz[0][0] == 1 and matriz[1][1] == 1 and matriz[2][2] == 1) or (matriz[0][0] == 1 and matriz[1][0] == 1 and matriz[2][0] == 1) or (matriz[0][1] == 1 and matriz[1][1] == 1 and matriz[2][1] == 1) or (matriz[0][2] == 1 and matriz[1][2] == 1 and matriz[2][2] == 1) or (matriz[0][0] == 1 and matriz[0][1] == 1 and matriz[0][2] == 1) or (matriz[0][2] == 1 and matriz[1][1] == 1 and matriz[2][0] == 1) or (matriz[1][0] == 1 and matriz[1][1] == 1 and matriz[1][2] == 1) or (matriz[2][0] == 1 and matriz[2][1] == 1 and matriz[2][2] == 1):
        resultado = 'Victoria!!!!'
    
    elif (matriz[0][0] == -1 and matriz[1][1] == -1 and matriz[2][2] == -1) or (matriz[0][0] == -1 and matriz[1][0] == -1 and matriz[2][0] == -1) or (matriz[0][1] == -1 and matriz[1][1] == -1 and matriz[2][1] == -1) or (matriz[0][2] == -1 and matriz[1][2] == -1 and matriz[2][2] == -1) or (matriz[0][0] == -1 and matriz[0][1] == -1 and matriz[0][2] == -1) or (matriz[0][2] == -1 and matriz[1][1] == -1 and matriz[2][0] == -1) or (matriz[1][0] == -1 and matriz[1][1] == -1 and matriz[1][2] == -1) or (matriz[2][0] == -1 and matriz[2][1] == -1 and matriz[2][2] == -1):
        resultado = 'Derrota...'

    return resultado