def suma_horror(lista):
    suma = 0
    for n in lista:
        if n < 0:
            break
        suma += n
    return suma
