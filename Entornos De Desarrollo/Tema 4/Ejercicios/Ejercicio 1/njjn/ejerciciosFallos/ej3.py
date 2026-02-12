
letra=input("Introduce una letra: ")
n_letras=0
palabra=0
while True:
    palabra = input("Inserta una palabra: ")
    if palabra == "fin":
        break

for caracter in palabra:
    if letra ==caracter:
        n_letras=n_letras+1
for n_letras in palabra:
    if palabra!="fin":
        n_letras=palabra+1

        #tengo que sumar la letra de todas las palabras. No llego a esto

print(f"La letra {letra} se repite {n_letras} veces")