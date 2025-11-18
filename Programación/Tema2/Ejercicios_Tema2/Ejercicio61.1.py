import math

while True:
    try:
        num = int(input("Inserta un número (0 o menor para salir): "))
        if num <= 0:
            break
        else:
            print(math.sqrt(num))
    except Exception as error:
        print(f"Introduce números o esto peta ... {error} ... ves?")