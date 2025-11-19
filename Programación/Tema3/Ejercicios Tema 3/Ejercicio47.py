matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

#Sin index
row = 0
for i, fila in enumerate(matriz):
    for j, n in enumerate(fila):
        if n == 5:
            print(f"El número 5 se encuentra en la posición [{i}][{j}]")
            break

#Con index
for i, fila in enumerate(matriz):
    if 5 in fila:
        print(f"El número 5 se encuentra en la posición [{i}][{fila.index(5)}]")