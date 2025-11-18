capicua = True

num = input("Introduce un número: ")
for i in range(1, len(num)//2+1, 1):
    if num[i-1] != num[len(num)-i]:
        capicua = False
        break

if capicua == True:
    print(f"El número {num} es capicua")
else:
    print(f"El número {num} no es capicua")