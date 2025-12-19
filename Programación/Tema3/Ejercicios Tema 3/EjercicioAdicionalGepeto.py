sabores = ["Fresa", "Melocoton", "Arandanos", "Naranja", "Frambuesa", "Mango", "Ciruela", "Albaricoque", "Higo", "Kiwi"]
precios = [2.40, 2.85, 3.10, 2.20, 3.50, 2.95, 2.60, 2.75, 3.00, 2.30]
es_sin_azucar = [False, False, True, False, True, False, False, False, True, False]

# Muestra por pantalla los sabores de las mermeladas que estén en posiciones impares de la lista y que sean sin azúcar. (0.5 puntos)
print([sabor for sabor in sabores if sabores.index(sabor)%2 == 1])

# Muestra por pantalla los sabores de las mermeladas cuyo precio sea el máximo o el mínimo de la lista de precios. (0.5 puntos)
print([sabores[precios.index(min(precios))], sabores[precios.index(max(precios))]])