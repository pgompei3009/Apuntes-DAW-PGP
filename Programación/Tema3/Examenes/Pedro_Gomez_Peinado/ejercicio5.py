from random import randint

elementos = [
    ["Hidrógeno", "H"],
    ["Helio", "He"],
    ["Litio", "Li"],
    ["Berilio", "Be"],
    ["Boro", "B"],
    ["Carbono", "C"],
    ["Nitrógeno", "N"],
    ["Oxígeno", "O"],
    ["Flúor", "F"],
    ["Neón", "Ne"]
]
vidas = 3

print('=== JUEGO DE SÍMBOLOS QUÍMICOS ===\n'
      f'Adivina el símbolo del elemento. Tienes {vidas} vidas\n')

while True:
    if vidas == 0:
        print('\nTe has quedado sin vidas. Fin del juego.')
        break
    
    if len(elementos) == 0:
        print('\n¡Has acertado todos los elementos! ¡Victoria!')
        break

    elem = randint(0, len(elementos)-1)
    print(f'Adivina el símbolo del elemento: {elementos[elem][0]}')
    respuesta = input('Tu respuesta: ')
    if respuesta == elementos[elem][1]:
        print('¡Correcto!')
        elementos.remove(elementos[elem])
    else:
        vidas -= 1
        print(f'Incorrecto. El símbolo correcto era {elementos[elem][1]}. Vidas restantes: {vidas}')