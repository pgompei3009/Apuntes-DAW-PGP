import random

numeros = [random.randint(1, 1000) for _ in range(1000)]

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print(f"El número mayor de la lista es: {mayor}")