import random

def lanzarMoneda() -> str:
    lanzamiento = random.randint(1, 2)
    if lanzamiento == 1:
        print ("cara")
    else:
        print("cruz")

def lanzarMonedas(n: int) -> str:
    for i in range(1, n+1, 1):
        lanzarMoneda()

def lanzarDado() -> int:
    print(random.randint(1, 6))

def lanzarDados(n: int) -> int:
    for i in range(1, n+1, 1):
        lanzarDado()