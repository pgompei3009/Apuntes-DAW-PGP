matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] < 0:
            matriz[i][j] *= -1

print(matriz)