def proporciones_matriz(matriz):
    row = col = 0
    for fila in matriz:
        row += 1
        for _ in fila:
            col += 1

    return row, col

matriz = [[1, 2, 3],
          [1, 2, 3],
          [1, 2, 3]]

row, col = proporciones_matriz(matriz)
print(f'La matriz tiene {row} filas y {col//row} columnas.')