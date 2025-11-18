cuenta = 0
print("Escribe un texto:")
text = input()
letra = input("Ahora dime la letra que quieres contar: ")

for i in range(1, len(text)+1, 1):
    if text[i-1] == letra:
        cuenta += 1

print(f"La letra '{letra}' aparece {cuenta} veces")