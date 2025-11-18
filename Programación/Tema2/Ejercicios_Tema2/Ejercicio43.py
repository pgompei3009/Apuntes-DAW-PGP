i = 1
palabraLarga = ""
palabraCorta = ""

while True:
    palabra = input("Dame una palabra: ")

    if palabra == "fin":
        break

    if i == 1:
        palabraCorta = palabra
        palabraLarga = palabra
        i += 1
    elif len(palabra) < len(palabraCorta):
        palabraCorta = palabra
    elif len(palabra) > len(palabraLarga):
        palabraLarga = palabra

if i != 1:
    print(f"La palabra más larga es {palabraLarga} y la palabra más corta es {palabraCorta}")
else:
    print("No has escrito ninguna palabra")