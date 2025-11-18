num1 = num2 = None

while num1 is None:
    try:
        num1 = int(input("Introduce el primer número: "))
    except Exception as error:
        print(f"No has introducido un valor válido: {error}")

while num2 is None:
    try:
        num2 = int(input("Introduce el segundo número: "))
    except Exception as error:
        print(f"No has introducido un valor válido: {error}")

print(f"La suma de los dos número es: {num1 + num2}")