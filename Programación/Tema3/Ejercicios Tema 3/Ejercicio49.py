matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]

palLarga = matriz[0][0]

for fila in matriz:
    for pal in fila:
        if len(pal) > len(palLarga):
            palLarga = pal

print(f"La palabra más larga es {palLarga}")