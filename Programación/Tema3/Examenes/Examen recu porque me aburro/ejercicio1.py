sabores = ["Fresa", "Melocoton", "Naranja", "Arandanos", "Higo", "Albaricoque", "Mango", "Frambuesa", "Ciruela", "Limon"]
azucar = [55, 48, 52, 60, 45, 50, 58, 62, 49, 47]
es_light = [False, True, False, False, True, True, False, False, True, True]

# Muestra por pantalla el nombre de las mermeladas que no sean light y cuyo nombre tenga 6 letras o menos.
print('Apartado a):')
print([sabor for sabor in sabores if es_light[sabores.index(sabor)] == False and len(sabor) <= 6])

# Muestra por pantalla el nombre de las mermeladas que no sean light y cuyo contenido de azúcar sea inferior a la media de todas las mermeladas (independientemente de si son light o no).
mediaAzucar = sum(azucar)/len(azucar)

print('\nApartado b):')
print([sabor for sabor in sabores if es_light[sabores.index(sabor)] == False and azucar[sabores.index(sabor)] < mediaAzucar])