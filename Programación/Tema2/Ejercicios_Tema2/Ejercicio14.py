temperatura = float(input("Dime una temperatura: "))
escala = input("Celsius o Farenheit: ")

if escala == "Celsius":
    print("La temperatura en Farenheit es ", (9/5)*temperatura+32)
else:
    print("La temperatura en Celsius es ", (temperatura-32)*(5/9))