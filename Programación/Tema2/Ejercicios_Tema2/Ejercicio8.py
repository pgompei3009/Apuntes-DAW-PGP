ciclo = input("Dime el ciclo en el que estás matriculad@: ")
curso = int(input("Dime el curso en el que estás"))

if ciclo == "ASIR" and curso == 1 or ciclo == "DAW" and curso == 2:
    print("Tienes despliegue de páginas web")
else:
    print("No tienes despliegue de páginas web")