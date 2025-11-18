print("¿Qué pista vas a alquilar?\n"
      "1. Tenis\n"
      "2. Futbol sala\n"
      "3. Futbol 11\n"
      "4. Rugby")

pista = int(input("Elige el tipo de pista: "))
dia = input("Introduce el día de la semana (L, M, X, J, V, S, D): ")
focos = input("¿Quieres focos? (S/N): ")
alumno = input("¿Eres alumno/a de la UGR? (S/N): ")

match pista:
    case 1:
        if dia == "S" or dia == "D":
            precio = 10
        else:
            precio = 8
        if focos == "S":
            precio += 5
    case 2:
        if dia == "S" or dia == "D":
            precio = 30
        else:
            precio = 26
        if focos == "S":
            precio += 10
    case 3:
        if dia == "S" or dia == "D":
            precio = 79
        else:
            precio = 64
        if focos == "S":
            precio += 20
    case 4:
        if dia == "S" or dia == "D":
            precio = 94
        else:
            precio = 80
        if focos == "S":
            precio += 25

if alumno == "S":
    precio *= 0.85

precio = round(precio, 2)
print(f"Tienes que pagar {precio}€")