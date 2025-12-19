filas = ('1', '2', '3', '4', '5', '6', '7', '8')
columnas = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

while True:
    posiciones = []
    coord = input('Introduce posición de la torre (por ejemplo a4): ')
    for col in columnas:
        posiciones.append(f'{col}{coord[1]}')

    posiciones.remove(coord)
    for fil in filas:
        posiciones.append(f'{coord[0]}{fil}')

    posiciones.remove(coord)
    print(f'La torre puede moverse a: {posiciones}')