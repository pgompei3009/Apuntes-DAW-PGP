animales = ["Perro", "Gato", "Conejo", "Hámster", "Loro", "Pez", "Tortuga", "Cobaya", "Hurón", "Canario"]

pesoAnimales = [
    [5, 40],   # Perro (depende de la raza)
    [2, 8],    # Gato
    [1, 3],    # Conejo
    [0.08, 0.25], # Hámster
    [0.2, 1.5],   # Loro
    [0.1, 2],  # Pez (varía mucho según la especie)
    [0.5, 2],  # Tortuga (pequeñas domésticas)
    [0.7, 1.5],  # Cobaya
    [0.5, 2],  # Hurón
    [0.02, 0.06] # Canario
]

maxDif = pesoAnimales[0][1]-pesoAnimales[0][0]
animalMaxDif = 0

for pesoAnimal in pesoAnimales:
    if pesoAnimal[1]-pesoAnimal[0] > maxDif:
        maxDif = pesoAnimal[1]-pesoAnimal[0]
        animalMaxDif = pesoAnimales.index(pesoAnimal)

print(f'El animal con la mayor diferencia entre su mayor y menor es el {animales[animalMaxDif]}')