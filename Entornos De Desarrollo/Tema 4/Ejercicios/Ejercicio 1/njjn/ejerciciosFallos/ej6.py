"""Ejercicio 6 (1 punto). Crea un programa que lea palabras hasta que introduzcas la palabra ‘fin’.
 El programa deberá mostrar la cantidad de palabras de 5 o menos letras introducidas (no tener en cuenta la palabra ‘fin’)."""
count=0
palabra=None

while palabra!="fin":
    palabra=input("Introduce una palabra: ")
    if len(palabra)<5 and palabra!="fin":
        count+=1
print("La cantidad de palabras es: ", count)