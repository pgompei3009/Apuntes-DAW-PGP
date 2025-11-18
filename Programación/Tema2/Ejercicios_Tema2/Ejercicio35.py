altura = int(input("Dime la altura: "))
anchura = int(input("Dime la anchura: "))
caracter = input("Dime el caracter: ")
print("Dibujo del rectángulo: ")
y = 1

while True:
    x = 1
    while True:
        print(caracter, end="")
        if x == anchura:
            break
        x += 1
    if y == altura:
        break
    y += 1
    print("")