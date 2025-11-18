cuenta = 0
total = 0
num = 1
numMaximo = 0
numMinimo = 0

while num != 0:
    num = int(input("Dame número (0 para terminar): "))
    total += num
    cuenta += 1
    if num > numMaximo:
        numMaximo = num
    elif num < numMinimo:
        numMinimo = num

print(f"La media es : {total/cuenta}\n" \
      f"El número máximo es {numMaximo}\n" \
      f"El número mínimo es {numMinimo}")