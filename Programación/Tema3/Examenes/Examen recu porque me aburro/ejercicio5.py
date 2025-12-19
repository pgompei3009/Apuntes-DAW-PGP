def coordenadas(coord: str) -> tuple[int, int]:
    filas = ('8', '7', '6', '5', '4', '3', '2', '1')
    columnas = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

    return (filas.index(coord[1]), columnas.index(coord[0]))

while True:
    coord = input('Introduce una coordenada: ')
    coordMatriz = coordenadas(coord)
    print(f'Fila: {coordMatriz[0]}, Columna: {coordMatriz[1]}')