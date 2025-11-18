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

for i, precipitacion in enumerate(precipitaciones_granada_2023):
    if i > 0:
        precipitacionGuardada = precipitacion[i-1]
        if precipitacion > precipitacionGuardada:
            print(f"En el mes {meses[i]} llueve más que en el anterior con {precipitacion} l/m^2")