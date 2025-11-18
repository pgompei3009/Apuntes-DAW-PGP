pals = []

while True:
    pal = input("Dame una palabra: ")
    if pal == "fin":
        break

    pals.append(pal)

pals.sort()

print(f"Palabras ordenadas: {pals}")