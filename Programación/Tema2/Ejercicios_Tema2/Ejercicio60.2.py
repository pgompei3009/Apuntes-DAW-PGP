num1 = num2 = None

try:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
except Exception as error:
    print(f"No has introducido un valor válido: {error}")
else:
    print(f"La suma de los dos número es: {num1 + num2}")