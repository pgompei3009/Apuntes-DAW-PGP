while True:
    num = float(input("Inserta un número: "))
    if num == 0:
        break
    cifras = int(input("Dime la cifra a la que quieres redondear: "))
    numR = round(num, cifras)
    print(f"El número {num} redondeado es {numR}")