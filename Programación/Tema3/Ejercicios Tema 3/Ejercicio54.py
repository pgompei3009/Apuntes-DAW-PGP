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

mediaTotal = 0

for alumno in alumnos:
    mediaTotal += calcular_media(alumno)

print(f"La media de la clase es {mediaTotal/5}")