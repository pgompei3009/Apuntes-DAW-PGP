pals = input("Introduce palabras separadas por comas: ")

palsSeparadas = pals.split(",")

pMax = palsSeparadas[0]
pMin = palsSeparadas[0]

for p in palsSeparadas:
    if len(p) > len(pMax):
        pMax = p
    
    elif len(p) < len(pMin):
        pMin = p

print(f"La palabra con más letras es: {pMax}\n"
      f"La palabra con menos letras es: {pMin}")