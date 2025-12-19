from random import randint

def menuPrincipal() -> None:
    print('''
    1. Jugar 
    2. Cambiar Dificultad 
    0. Salir''')

    opcion = int(input("Selecciona una opción: "))
    return opcion
          

def imprimir_tablero(tableroPantalla: list[list[int]]) -> None:
    print('  A   B   C   D   E   F   G   H   I   J  ')
    print('-----------------------------------------')
    for i, fila in enumerate(tableroPantalla):
        print(end='| ')
        for j, casilla in enumerate(fila):
            signo = '-'
            if casilla != -1:
                signo = tableroPantalla[i][j]

            print(signo, end=' | ')
        print(f'\n----------------------------------------- {i+1}')


def generar_barcos(tablero: list[list[int]]) -> list[list[int]]:
    idBarco = 1
    
    while True:
        if idBarco < 2:
            tablero[randint(0, 9)][randint(0, 9)] = idBarco
        
        elif idBarco < 4:
            while True:
                fila = randint(0, 9)
                columna = randint(0, 9)
                orientacion = randint(0, 1)
                if columna-1 >= 0 and fila+1 <= 9:
                    match orientacion:
                        case 0:
                            if tablero[fila][columna] == 0 and tablero[fila][columna+1] == 0:
                                for i in range(0, 2):
                                    tablero[fila][columna+i] = idBarco
                                break
                        case 1:
                            if tablero[fila][columna] == 0 and tablero[fila+1][columna] == 0:
                                for i in range(0, 2):
                                    tablero[fila+i][columna] = idBarco
                                break

        elif idBarco < 8:    
            while True:        
                fila = randint(0, 9)
                columna = randint(0, 9)
                orientacion = randint(0, 1)
                if (columna+2 <= 9 and fila+2 <= 9):
                    match orientacion:
                        case 0:
                            if tablero[fila][columna] == 0 and tablero[fila][columna+1] == 0 and tablero[fila][columna+2] == 0:
                                for i in range(0, 3):
                                    tablero[fila][columna+i] = idBarco
                                break
                        case 1:
                            if tablero[fila][columna] == 0 and tablero[fila+1][columna] == 0 and tablero[fila+2][columna] == 0:
                                for i in range(0, 3):
                                    tablero[fila+i][columna] = idBarco
                                break
        
        elif idBarco < 10:
            while True:        
                fila = randint(0, 9)
                columna = randint(0, 9)
                orientacion = randint(0, 1)
                if (columna+3 <= 9 and fila+3 <= 9):
                    match orientacion:
                        case 0:
                            if tablero[fila][columna] == 0 and tablero[fila][columna+1] == 0 and tablero[fila][columna+2] == 0 and tablero[fila][columna+3] == 0:
                                for i in range(0, 4):
                                    tablero[fila][columna+i] = idBarco
                                break
                        case 1:
                            if tablero[fila][columna] == 0 and tablero[fila+1][columna] == 0 and tablero[fila+2][columna] == 0 and tablero[fila+3][columna] == 0:
                                for i in range(0, 4):
                                    tablero[fila+i][columna] = idBarco
                                break

        elif idBarco == 10:
            while True:        
                fila = randint(0, 9)
                columna = randint(0, 9)
                orientacion = randint(0, 1)
                if (columna+4 <= 9 and fila+4 <= 9):
                    match orientacion:
                        case 0:
                            if tablero[fila][columna] == 0 and tablero[fila][columna+1] == 0 and tablero[fila][columna+2] == 0 and tablero[fila][columna+3] == 0 and tablero[fila][columna+4] == 0:
                                for i in range(0, 5):
                                    tablero[fila][columna+i] = idBarco
                                break
                        case 1:
                            if tablero[fila][columna] == 0 and tablero[fila+1][columna] == 0 and tablero[fila+2][columna] == 0 and tablero[fila+3][columna] == 0 and tablero[fila+4][columna] == 0:
                                for i in range(0, 5):
                                    tablero[fila+i][columna] = idBarco
                                break

        idBarco += 1
        if idBarco == 11:
            break

    return tablero
    

def pedir_coordenada() -> tuple[int, int]:
    letras = ['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I', 'J']
    columna = letras.index(input(f'Ingrese la columna (letra): '))
    fila = int(input(f'Ingrese la fila (nº): '))-1
    return fila, columna


def jugar_turno(barcosDestruidos: int, tablero: list[list[int]], tableroPantalla: list[list[int]]) -> tuple[int, list[list[int]], list[list[int]], bool]:
    gabe = False
    fila, columna = pedir_coordenada()
    tableroPantalla[fila][columna] = tablero[fila][columna]
    if tablero[fila][columna] == 1:
        gabe = True

    if tablero[fila][columna] != 0:
        noHundido = False
        idBuscado = tablero[fila][columna]
        tablero[fila][columna] = 0
        for fila in tablero:
            if idBuscado in fila:
                noHundido = True
                break
        
        if noHundido == True:
            print('Tocado!')
        else:
            print('Tocado y hundido!!!')
            barcosDestruidos += 1

    return barcosDestruidos, tablero, tableroPantalla, gabe


def dificulates():
    print()
    dificultad= int(input('''
    1. Fácil
    2. Normal
    3. Dificil 
                        
    Selecciona tu dificultad: '''))
    match dificultad:
        case 1:
            nMisiles = 80
        case 2:
            nMisiles = 60
        case 3:
            nMisiles = 40

    return nMisiles