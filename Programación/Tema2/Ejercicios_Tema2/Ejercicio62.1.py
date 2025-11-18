import math

while True:
    try:
        a = int(input("Dime cuanto vale a: "))
        if a == 0:
            break
        b = int(input("Dime cuanto vale b: "))
        c = int(input("Dime cuanto vale c: "))
        print(f"a = {a}, b = {b} y c = {c}")
        try:
            print(f"Los resultado de la ecuación son {(-b+math.sqrt(b**2-a*c))/(a*2)} y {(-b+math.sqrt(b**2-a*c))/(a*2)}")
        except Exception as error:
            print(f"El resultado a salido rarillo ... {error}")

    except Exception as error:
        print(f"Introduce números enteros o esto peta ... {error} ... ves?")