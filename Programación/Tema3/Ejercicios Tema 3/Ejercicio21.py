nums = []
numsOrden = []

#Añadir
while True:
    num = int(input("Dame un número (0 para terminar): "))
    if num == 0:
        break

    nums.append(num)

#Ordenar
for i, num in enumerate(nums):
    if i == 0:
        numsOrden.append(num)
    else:
        añadido = False
        for j, numOrden in enumerate(numsOrden):
            if num < numOrden:
                numsOrden.insert(j, num)
                añadido = True
                break
        
        if añadido == False:
            numsOrden.append(num)
            
print(f"Numeros ordenados de menor a mayor: {numsOrden}")