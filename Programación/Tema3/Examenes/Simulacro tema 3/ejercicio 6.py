def es_cuadrada(m: list[list[int]]):
    for i, fila in enumerate(m):
        for j, columna in enumerate(fila):
            pass

    if i == j:
        return True
    else:
        return False

m = [
    [1, 2, 3],
    [1, 2, 3],
]

print(es_cuadrada(m))