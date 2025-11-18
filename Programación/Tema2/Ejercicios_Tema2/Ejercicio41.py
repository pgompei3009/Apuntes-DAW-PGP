cuenta = 1
print("Escribe un texto:")
text = input()

for i in range(1, len(text)+1, 1):
    if text[i-1] == " ":
        cuenta += 1

print(f"El texto tiene {cuenta} palabras")