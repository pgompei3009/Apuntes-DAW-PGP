matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]

empiezaVocal = 0

for fila in matriz:
    for pal in fila:
        if pal[0] in ("AEIOU"):
            empiezaVocal += 1

print(f"{empiezaVocal} palabras empiezan por vocal")