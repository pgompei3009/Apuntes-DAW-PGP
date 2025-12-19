import funcs

nMisiles = 60
barcosDestruidos = 0

tablero = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
]

tableroPantalla = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
]

while True:
    opcion = funcs.menuPrincipal()
    match opcion:
        case 0:
            print('Enga tira...')
            break
        case 1:
            funcs.generar_barcos(tablero)
            while True:
                funcs.imprimir_tablero(tableroPantalla)
                barcosDestruidos, tablero, tableroPantalla, gabe = funcs.jugar_turno(barcosDestruidos, tablero, tableroPantalla)
                nMisiles = nMisiles - 1

                if barcosDestruidos == 10:
                    print('Has ganado!!!')
                    break
                
                if gabe == True:
                    print('Acabas de matar a Gabe Newell, te quedaste sin Half Life 3, Team Fortress 3, Portal 3 y más juegos con el 3')
                    break

                if nMisiles == 0:
                    print("Has perdido. Game over.")
                    break
        case 2:
            nMisiles = funcs.dificulates()