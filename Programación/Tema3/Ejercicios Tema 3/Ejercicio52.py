def calcular_media(alumno: list) -> float:
    media = (alumno[1]+alumno[2]+alumno[3])/3
    return media

alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

mediaMenor = 11

for alumno in alumnos:
    media = calcular_media(alumno)
    if media < mediaMenor:
        mediaMenor = media
        alumnoMenor = alumno[0]

print(f"El alumno con la media más baja es {alumnoMenor} con un {mediaMenor}")