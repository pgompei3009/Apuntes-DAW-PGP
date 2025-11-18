precipitaciones_granada_2023 = [
   40.2,  # Enero
   35.6,  # Febrero
   45.8,  # Marzo
   50.1,  # Abril
   30.3,  # Mayo
   10.4,  # Junio
   1.2,   # Julio
   5.6,   # Agosto
   20.8,  # Septiembre
   60.5,  # Octubre
   55.3,  # Noviembre
   42.7   # Diciembre
]

meses = [
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre"
]

mayor = precipitaciones_granada_2023[0]

for i, precipitacion in enumerate(precipitaciones_granada_2023):
    if precipitacion > mayor:
        mayor = precipitacion

print(f"El mes con mayor precipitaciones es {meses[i]} con {precipitacion} l/m^2")