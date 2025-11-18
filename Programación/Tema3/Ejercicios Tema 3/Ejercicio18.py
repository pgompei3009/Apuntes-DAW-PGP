pares = []

a = int(input("Dame el inicio del intervalo: "))
b = int(input("Dame el final del intervalo: "))

for i in range(a, b):
    if i%2 == 0:
        pares.append(i)

print(pares)