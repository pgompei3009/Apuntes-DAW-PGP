import funcs

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

print('Bienvenid@ al 3 en rayas!!!')
while True:
    matriz = funcs.movimiento_jugador(matriz)
    resultado = funcs.comprobar_resultado(matriz) 
    if resultado is not None:
        break

    matriz = funcs.movimiento_ia(matriz)
    resultado = funcs.comprobar_resultado(matriz)
    if resultado is not None:
        break

print(resultado)
funcs.imprimir_tablero(matriz)