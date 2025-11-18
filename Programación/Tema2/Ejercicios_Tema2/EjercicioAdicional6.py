frase = input("Escribe una frase: ")
palabra = input("Dame una palabra que buscar: ")
aparecePalabra = False
j = 0

for i in range(1, len(frase), 1):
    if frase[i-1] == palabra[j]:
        aparecePalabra = True
        break

    j += 1

if aparecePalabra == True:
    print(f"La palabra {palabra} aparece")
else:
    print(f"La palabra {palabra} no aparece")