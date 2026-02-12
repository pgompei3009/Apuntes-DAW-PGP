from datetime import datetime


def media(numeros: list[int]) -> float:
    sumatoria = 0
    for n in numeros:
        sumatoria =+ n

    if len(numeros) > 0:
        return sumatoria/len(numeros)
    else:
        return 0


def filtrar_pares(numeros: list[int]):
    pares = []

    for n in numeros:
        if n%2 == 0:
            pares.append(n)

    return pares


def numero_mayor(numeros: list[int]) -> int:
    numMayor = numeros[0]
    for n in numeros:
        if n > numMayor :
            nMayor = n

    return nMayor


def ordenar_menor_a_mayor(numeros: list):
    for i in range(len(numeros)):
        for j in range(len(numeros)):
            if numeros[i] < numeros[j]:
                t = numeros[i]
                numeros[i] = numeros[j]
                numeros[j] = t

    return numeros


datos = [12, 7, 4, 19, 2, 8, 3]

print("Datos:", datos)

r1 = media(datos)
print("Resultado 1:", r1)

r2 = filtrar_pares(datos)
print("Resultado 2:", r2)

r3 = numero_mayor(datos)
print("Resultado 3:", r3)

r4 = ordenar_menor_a_mayor(datos)
print("Resultado 4:", r4)

