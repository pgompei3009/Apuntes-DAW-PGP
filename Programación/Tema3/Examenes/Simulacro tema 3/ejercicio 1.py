animales = ["Perro", "Gato", "Conejo", "Hámster", "Loro", "Pez", "Tortuga", "Cobaya", "Hurón", "Canario"]

pesoAnimales = [10, 4, 2, 0.1, 0.3, 0.2, 1.5, 1, 1.2, 0.05]

print(f'El animal con el peso medio menor es el {animales[pesoAnimales.index(min(pesoAnimales))]} con {min(pesoAnimales)} Kg \n')

pesoMedio = sum(pesoAnimales)/len(pesoAnimales)

print(f'Los animales que tienen un peso medio menor a {pesoMedio} son:')
for pesoAnimal in pesoAnimales:
    if pesoAnimal < pesoMedio:
        print(animales[pesoAnimales.index(pesoAnimal)])