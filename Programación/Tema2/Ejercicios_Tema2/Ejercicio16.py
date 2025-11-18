lado1 = float(input("Dime cuando mide el lado 1: "))
lado2 = float(input("Dime cuando mide el lado 2: "))
lado3 = float(input("Dime cuando mide el lado 3: "))

if lado1 == lado2 and lado1 == lado3:
    print("Es un triángulo equilátero")
elif (lado1 == lado2 and lado1 != lado3) or (lado1 == lado3 and lado1 != lado2):
    print("Es un triángulo isósceles")
else:
    print("Es un triángulo escaleno")