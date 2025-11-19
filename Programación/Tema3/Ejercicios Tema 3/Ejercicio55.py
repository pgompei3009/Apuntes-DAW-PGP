import random

def crear_matriz(n: int, m: int, a: int, b: int) -> list[list[int]]:
    matriz = []
    for _ in range(0, n):
        matriz.append([random.randint(a, b) for _ in range(0, m)])
    
    return matriz

n = int(input("Dime cuántas filas quieres que tenga la matriz: "))
m = int(input("Dime cuántas columnas quieres que tenga la matriz: "))
a = int(input("Dime el inicio del intervalo de valores: "))
b = int(input("Dime el final del intervalo de valores: "))

matriz = crear_matriz(n, m, a, b)

print(matriz)