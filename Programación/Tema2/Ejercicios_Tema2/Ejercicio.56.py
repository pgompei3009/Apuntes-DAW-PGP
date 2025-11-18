def contar_palabras(text: str) -> int:
    cuenta = 1
    for i in range(1, len(text)+1, 1):
        if text[i-1] == " ":
            cuenta += 1
    print(f"Tu texto tiene {cuenta} palabras")

text = input("Escribe un texto para que cuente las palabras: ")
contar_palabras(text)