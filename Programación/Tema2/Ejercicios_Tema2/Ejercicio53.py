def cuenta_vocales(text: str):
    cuenta = 0
    for i in range(1, len(text)+1, 1):
        if text[i-1] == "a" or text[i-1] == "e" or text[i-1] == "i" or text[i-1] == "o" or text[i-1] == "u":
            cuenta += 1
    print(f"Hay {cuenta} vocales")


text = input("Escribe una frase para que cuente las vocales: ")
cuenta_vocales(text)