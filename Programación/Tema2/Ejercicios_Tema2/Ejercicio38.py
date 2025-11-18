num = int(input("Dime un número: "))

for i in range(2, num, 1):
    if num == 2:
        esPrimo = True
    elif (num%i) == 0:
        print("No es primo")
        break
    else:
        esPrimo = True

if esPrimo:
    print("Es primo")