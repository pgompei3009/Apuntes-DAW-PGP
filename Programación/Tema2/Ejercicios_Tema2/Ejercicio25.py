import random

numeroSecreto = random.randint(0,100)
numeroUsuario = -1
intentos = 0

while numeroUsuario != numeroSecreto:
    intentos += 1
    numeroUsuario = int(input("Dime un número entre 0 y 100: "))
    if numeroUsuario < numeroSecreto:
        print(f"El número es mayor que {numeroUsuario}, prueba de nuevo ;)")
    elif numeroUsuario > numeroSecreto:
        print(f"El número es menor que {numeroUsuario}, prueba de nuevo ;)")
    else:
        print("Felicidades!!!\n" \
        f"Solo te ha costado {intentos} intentos")