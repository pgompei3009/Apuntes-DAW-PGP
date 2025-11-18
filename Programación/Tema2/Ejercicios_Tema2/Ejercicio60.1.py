total = 0
cuenta = 0

while True:
    try:
        num = int(input("Inserta un número (0 para salir): "))
        if num == 0:
            break
        else:
            total += num
            cuenta += 1
    except Exception as error:
        print(f"No has insertado unos datos válidos. Error: {error}")

print(f"La media de los números introducidos es {total/cuenta}")