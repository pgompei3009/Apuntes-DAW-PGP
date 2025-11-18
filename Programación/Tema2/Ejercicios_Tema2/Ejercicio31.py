while True:
    print("------Menu------ \n" \
        "1. Suma\n" \
        "2. Resta\n" \
        "3. Multiplicación\n" \
        "4. División\n" \
        "5. División entera\n" \
        "6. Resto de dos números")
    
    operacion = input("Elige la operación que quieres realizar (escribe 'fin' para terminar): ")
    if operacion == "fin":
        break

    num1 = int(input("Dame el primer dato: "))
    num2 = int(input("Dame el segundo dato: "))
    match operacion:
        case "1":
            print(f"{num1} + {num2} = {num1+num2}")
        case "2":
            print(f"{num1} - {num2} = {num1-num2}")
        case "3":
            print(f"{num1} x {num2} = {num1*num2}")
        case "4":
            print(f"{num1} : {num2} = {num1/num2}")
        case "5":
            print(f"{num1} // {num2} = {num1//num2}")
        case "6":
            print(f"{num1} % {num2} = {num1%num2}")