import random

numeros = [random.randint(1, 1000) for _ in range(1000)]

menor = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero

print(f"El número menor de la lista es: {menor}")