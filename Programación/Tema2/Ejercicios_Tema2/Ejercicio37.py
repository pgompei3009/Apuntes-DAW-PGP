num = int(input("Dime un número: "))
resultado = 1

for i in range(1, num+1, 1):
    resultado *= i
    
print(f"El factorial de {num} es {resultado}")