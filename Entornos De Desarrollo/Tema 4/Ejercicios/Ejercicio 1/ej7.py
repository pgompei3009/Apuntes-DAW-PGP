suma = 0
numMin = 0
numMax = 0
cantidad = 0

while suma < 100:
    num = int(input("Inserta un número: "))
    suma += num
    if numMin == 0:
        numMin = num

    if num > numMax:
        numMax = num

    if num < numMin:
        numMin = num

    cantidad += 1

print(f"La cantidad de número introducidos es {cantidad}")
print(f"La suma total es {suma}")
print(f"La media es {suma/cantidad}")
print (f"El número mayor es: {numMax}")
print (f"El número menor es: {numMin}")