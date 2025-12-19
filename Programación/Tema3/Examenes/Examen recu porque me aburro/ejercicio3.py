def diagonales(matriz: list[list[int]]) -> tuple[list[int]]:
    diagonalPrim = []
    for i, fila in enumerate(matriz):
        diagonalPrim.append(fila[i])

    diagonalSecu = []
    for i, fila in enumerate(matriz):
        diagonalSecu.append(fila[3-i])


    return (diagonalPrim, diagonalSecu)

matriz = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13,14, 15,16]
]

print(diagonales(matriz))