import random

contador = 0
pares = 0
impares = 0

while True:
    if contador == 10:
        break

    num = random.randint (11, 21)
    if num%2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

    porcentajePares = (pares/10)*100
    porcentajeImpares = (impares/10)*100
    print(num)
    contador = contador + 1

print(f"El porcentaje de numeros pares es {porcentajePares} %")
print(f"El porcentaje de numeros impares es {porcentajeImpares} %")
