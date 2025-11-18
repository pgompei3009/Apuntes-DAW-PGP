n = int(input("Dame un número: "))
i = 1
resultado = 1
while True:
    resultado *= i
    if i == n:
        break
    i += 1
print(f"El factorial de {n} es {resultado}")