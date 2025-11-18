import random

def cara_cruz(nTiradas: int) -> str:
    for i in range(1, nTiradas+1, 1):
        resultado = random.randint(0,1)
        if resultado == 0:
            print(f"Resultado {i}: cara")
        else:
            print(f"Resultado {i}: cruz")

nTiradas = int(input("Dime cuantas veces queiere tirar la moneda: "))
cara_cruz(nTiradas)