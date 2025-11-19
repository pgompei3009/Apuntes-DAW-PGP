matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

#Sin index
for i, fila in enumerate(matriz):
    for j, n in enumerate(fila):
        if n == 5:
            print(f"Hay un 5 en la posición [{i}][{j}]")

#Con index
for i, fila in enumerate(matriz):
    if 5 in fila:
        print(f"Hay un 5 en la posición [{i}][{fila.index(5)}]")