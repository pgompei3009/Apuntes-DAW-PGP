dias = diasDescuento = llantas = precio = 0

elec = input("¿Quieres que la bici sea eléctrica (S/N)?: ")
while elec != "S" and elec != "N":
    print("Valor no válido. Por favor, especifica S o N")
    elec = input("¿Quieres que la bici sea eléctrica (S/N)?: ")

llanta = int(input("¿Qué tamaño de llanta?: "))
while llanta < 12 or llanta > 29:
    print("Número no válido. Por favor, especifica un número válido: entre 12 y 29 ambos inclusive")
    llanta = int(input("¿Qué tamaño de llanta?: "))

dias = int(input("¿Cuántos días?: "))
while dias < 1 or dias > 7:
    print("Número no válido. Por favor, especifica un número válido: entre 1 y 7 ambos inclusive")
    dias = int(input("¿Cuántos días?: "))

match elec:
    case "S":
        if llanta < 20:
            precio = 30
        elif llanta < 27.5:
            precio = 70
        else:
            precio = 100

    case "N":
        if llanta < 20:
            precio = 15
        elif llanta < 27.5:
            precio = 30
        else:
            precio = 45

if dias > 3:
    diasDescuento = dias - 3
    dias = 3

precioTotal = (dias * precio) + (diasDescuento * (precio/2))

print(f"Tienes que pagar {round(precioTotal, 2)}€")