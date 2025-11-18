lado1 = float(input("Dime lo que mide el lado 1: "))
lado2 = float(input("Dime lo que mide el lado 2: "))
lado3 = float(input("Dime lo que mide el lado 3: "))

if lado1 + lado2 <= lado3 or lado2 + lado3 <= lado1 or lado1 + lado3 <= lado2:
    print("No se puede hacer un triángulo")
else:
    print("Sí puedes hacer un triángulo")