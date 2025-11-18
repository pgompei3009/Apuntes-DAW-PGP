numTerminos = int(input("Dame un número: "))
num1 = 0
num2 = 1
i = 3

if numTerminos >= 1:
    print("Término 1: ",num1)
if numTerminos >= 2:
    print("Término 2: ",num2)
if numTerminos >= 3:
    while True:
        numResiduo = num2
        num2 += num1
        num1 = numResiduo
        print(f"Término {i}: {num2}")
        if i == numTerminos:
            break
        i += 1