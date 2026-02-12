#Crea un programa que lea palabras hasta que introduzcas la palabra ‘fin’. #
#El programa deberá mostrar la cantidad de palabras de 5 o menos letras introducidas (no tener en cuenta la palabra ‘fin’).
cantidad_palabra = 0
palabra=" "
while True:
    palabra = input("Inserta una palabra: ")
   
    if palabra == "fin":
        break
    if len(palabra) <=5:
        cantidad_palabra=cantidad_palabra+1

    print(f"El número de palabras con cinco letras o menos es {cantidad_palabra}")