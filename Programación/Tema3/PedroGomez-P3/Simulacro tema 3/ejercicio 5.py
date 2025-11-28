from random import randint

def generar_partitura(longitud: int, nRepeticiones: int) -> list[str]:
    notas = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']
    partitura = []
    racha = 0
    for i in range(0, longitud):
        nota = notas[randint(0, len(notas)-1)]
        if len(partitura) == 0:
            partitura.append(nota)
            racha += 1
        elif racha == nRepeticiones and partitura[i-1] == nota:
            racha = 0
        else:
            partitura.append(nota)
            racha += 1

    return partitura

longitud = int(input('Dime la longitud de la partitutra: '))
nRepeticiones = int(input('Dime el número de repeticiones máxima: '))

print(generar_partitura(longitud, nRepeticiones))