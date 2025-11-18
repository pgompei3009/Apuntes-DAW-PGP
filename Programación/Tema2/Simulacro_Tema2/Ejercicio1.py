nPalabras = int(input("¿Cuántas palabras vas a insertar? "))

for i in range(nPalabras):
    palabra = input("Inserte una palabra: ")
    if i == 0:
        palabraLarga = palabraCorta = palabra
    if len(palabra) > len(palabraLarga):
        palabraLarga = palabra
    elif len(palabra) < len(palabraCorta):
        palabraCorta = palabra

print(f"La palabra con más letras es: {palabraLarga} y la que tiene menos: {palabraCorta}")