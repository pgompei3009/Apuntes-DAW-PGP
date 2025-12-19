clasicas = ["Fresa", "Melocoton", "Naranja", "Albaricoque", "Ciruela"]
ecologicas = ["Fresa", "Higo", "Ciruela", "Arandanos"]
gourmet = ["Frambuesa", "Arandanos", "Naranja", "Mango"]

# Muestra por pantalla las mermeladas que aparecen tanto en el catálogo ecológico como en el gourmet.
print(set(ecologicas) & set(gourmet))

# Muestra por pantalla las mermeladas que aparecen en el catálogo clásico o en el gourmet, pero que no aparecen en el catálogo ecológico.
print((set(clasicas) | set(gourmet)) - set(ecologicas))