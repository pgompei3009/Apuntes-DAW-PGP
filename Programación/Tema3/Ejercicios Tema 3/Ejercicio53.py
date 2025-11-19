alumnos = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

suspensos = []

for alumno in alumnos:
    if min(alumno[1:]) < 5:
        suspensos.append(alumno[0])

print(f"Lista de alumnos con asignaturas suspensas {suspensos}")