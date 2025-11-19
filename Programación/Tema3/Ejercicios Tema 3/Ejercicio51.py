alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

for alumno in alumnos:
    print(f"Media de {alumno[0]}: {(alumno[1]+alumno[2]+alumno[3])/3}")