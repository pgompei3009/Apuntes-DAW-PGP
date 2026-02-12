from Ejercicio6 import planetas
from Planeta import Planeta


#1. Densidad todos los planetas
print('1. Densidad de todos los planetas:')
[print(f'{planeta.nombre}: {Planeta.get_densidad(planeta)}') for planeta in planetas]

#2. Planeta mayor densidad
print('\n2. Planeta con mayor densidad')
mayorDensidad = max(planetas, key=lambda planeta: Planeta.get_densidad(planeta))
planetaMayorDensidad = [planeta.nombre for planeta in planetas if Planeta.get_densidad(planeta) == mayorDensidad]

print(f'Planeta con mayor densidad --> {planetaMayorDensidad}: {mayorDensidad}')

#3. Lunas mas grandes que La Luna
print('\n3. Lunas más grandes que La Luna')
radioLuna = None
for planeta in planetas:
    for luna in planeta.lunas:
        if luna[0] == 'Luna':
            radioLuna = luna[2]
            break
    if radioLuna != None:
        break

[[print(f'{luna[0]}: {luna[2]}') for luna in planeta.lunas if luna[2] > radioLuna] for planeta in planetas]

#4. Luna más pequeña
print('\n4. Luna más pequeña')
radios = [[luna[2] for luna in planeta.lunas] for planeta in planetas]
radioMenor = min(radios)
print(radios)

for planeta in planetas:
    for luna in planeta.lunas:
        if luna[2] == radioMenor:
            print(f'La luna más pequeña es {luna[0]} con un radio de {radioMenor}')