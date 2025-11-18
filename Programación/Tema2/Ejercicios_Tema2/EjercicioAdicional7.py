cifras = 1
num = int(input("Introduce un número y te digo las cifras: "))
while num >= 10:
    num /= 10
    cifras += 1

print(f"El número tiene {cifras} cifras")