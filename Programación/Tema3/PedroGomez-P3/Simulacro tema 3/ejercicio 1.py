animales = ["Perro", "Gato", "Conejo", "Hámster", "Loro", "Pez", "Tortuga", "Cobaya", "Hurón", "Canario"]

pesoAnimales = [10, 4, 2, 0.1, 0.3, 0.2, 1.5, 1, 1.2, 0.05]


pesoMin = pesoAnimales[0]

for pesoAnimal in pesoAnimales:
    if pesoAnimal < pesoMin:
        pesoMin = pesoAnimal
        animalMin = pesoAnimales.index(pesoAnimal)

print(f'El animal con el peso medio menor es el {animales[animalMin]} con {pesoMin} Kg \n')

pesoMedio = sum(pesoAnimales)/len(pesoAnimales)

print(f'Los animales que tienen un peso medio menor a {pesoMedio} son:')
for pesoAnimal in pesoAnimales:
    if pesoAnimal < pesoMedio:
        print(animales[pesoAnimales.index(pesoAnimal)])