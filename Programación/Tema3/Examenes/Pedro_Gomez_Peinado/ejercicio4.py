def generar_matriz(filas: int, columnas: int, inicial: int) -> list[list[int]]:
    matriz = []
    fila = []
    for _ in range(filas):
        for _ in range(columnas):
            fila.append(inicial)
            inicial += 1
        
        matriz.append(fila.copy())
        fila.clear()
        
    return matriz

print(generar_matriz(4, 4, 5))