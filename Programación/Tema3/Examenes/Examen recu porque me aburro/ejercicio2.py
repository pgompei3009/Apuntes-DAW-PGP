mermeladas = [
    ["DulceSol Fresa", ["fresa", "limon"], 55, False],
    ["VerdeBosque Arandanos", ["arandanos", "manzana"], 60, True],
    ["CampoClaro Melocoton", ["melocoton", "limon"], 48, True],
    ["SolAndaluz Naranja", ["naranja"], 52, False],
    ["MonteMiel Mango", ["mango", "limon"], 58, False],
    ["EcoHuerta Higo", ["higo"], 45, True],
    ["RocaDulce Ciruela", ["ciruela"], 49, True],
    ["BosqueRojo Frambuesa", ["frambuesa", "manzana"], 62, False]
]

# Muestra por pantalla el nombre de todas las mermeladas ecológicas.
print('Apartado a):')
print([mermelada[0] for mermelada in mermeladas if mermelada[3] == True])

# Muestra por pantalla el nombre de las mermeladas que tienen más de un ingrediente y que NO son ecológicas.
print('Apartado b):')
print([mermelada[0] for mermelada in mermeladas if len(mermelada[1]) > 1 and mermelada[3] == False])

# Muestra por pantalla el nombre de las mermeladas cuya cantidad de azúcar sea superior a la media de todas las mermeladas.
media = 0
for mermelada in mermeladas:
    media += mermelada[2]

media /= len(mermeladas)

print('Apartado c):')
print([mermelada[0] for mermelada in mermeladas if mermelada[2] > media])

# Muestra por pantalla el nombre de las mermeladas no ecológicas que: tengan más de un ingrediente, contengan limón entre sus ingredientes y cuya cantidad de azúcar sea superior a la media de todas las mermeladas.
print('Apartado d):')
print([mermelada[0] for mermelada in mermeladas if len(mermelada[1]) > 1 and 'limon' in mermelada[1] and mermelada[2] > media])