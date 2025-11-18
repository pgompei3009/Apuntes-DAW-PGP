ciclo = input("Dime el ciclo en el que estás matriculad@: ")
curso = int(input("Dime el curso en el que estás: "))

if (ciclo == "DAW" or ciclo == "DAM") and curso == 1:
    print("Tienes programación")
else:
    print("No tienes programación")