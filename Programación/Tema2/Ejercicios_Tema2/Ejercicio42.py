cuenta = 0
print("Escribe un texto:")
text = input()
text.lower

for i in range(1, len(text)+1, 1):
    if text[i-1] == "a" or text[i-1] == "e" or text[i-1] == "i" or text[i-1] == "o" or text[i-1] == "u":
        cuenta += 1

print(f"El texto tiene {cuenta} vocales")