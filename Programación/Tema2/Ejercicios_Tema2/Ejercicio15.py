forma = input("Elije triángulo, rectángulo o círculo: ")

if forma == "triángulo":
    base = float(input("Dime la longitud de la base: "))
    altura = float(input("Dime la longitud de la altura: "))
    print(f"El area es {base*altura/2}")
elif forma == "rectángulo":
    lado1 = float(input("Dime la longitud del lado 1: "))
    lado2 = float(input("Dime la longitud del lado 2: "))
    print(f"El area es {lado1*lado2}")
else:
    radio = float(input("Dime la longitud de la base: "))
    print(f"El area es {3.14*radio^2}")