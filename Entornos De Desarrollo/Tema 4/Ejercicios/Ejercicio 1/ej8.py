#""" Crea un programa que lea palabras hasta que introduzcas la palabra ‘fin’.
#El programa deberá mostrar la cantidad de palabras de 5 o menos letras introducidas (no tener en cuenta la palabra ‘fin’)."""
nPalabras = 0
palabra = None

while palabra != "fin":
    palabra = input("Ingrese una palabra: ")
    if len(palabra) <= 5 and palabra != "fin":
        nPalabras += 1

print(f"El número de palabras de 5 o menos letras es: {nPalabras}")