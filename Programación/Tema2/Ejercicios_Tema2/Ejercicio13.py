operacion = int(input("1. Suma\n" \
                      "2. Resta\n" \
                      "3. Multiplicación\n" \
                      "4. División\n"
                      "Introduce la operacion que quieres realizar: "))

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if operacion == 1:
    print(f"El resultado es {num1+num2}")
elif operacion == 2:
    print(f"El resultado es {num1-num2}")
elif operacion == 3:
    print(f"El resultado es {num1*num2}")
else:
    print(f"El resultado es {num1/num2}")