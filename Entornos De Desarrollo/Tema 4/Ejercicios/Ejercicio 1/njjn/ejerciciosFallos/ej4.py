suma=0
cantidad=0
nummax=0
nummin=0
while suma<100:
    num=int(input("inserta  un numero: "))
    if nummin==0:
        nummin=num
    elif num>nummax:
        nummax=num
    elif num<nummin:
        nummin=num
    suma = suma + num
    cantidad += 1
media=suma/cantidad
print(f"La suma total es: {suma}")
print(f"La media es: {media}")
print(f"La cantidad de numeros introducidos es: {cantidad}")
print(f"El numero mayor es: {nummax}")
print(f"El numero menor es: {nummin}")