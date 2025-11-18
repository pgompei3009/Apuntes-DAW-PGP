import random

dato1 = random.randint(0, 20)
dato2 = random.randint(0, 20)
respuestaUsuario = int(input(f"Resuelve la operacion {dato1} + {dato2}"))

while True:
    respuestaUsuario = int(input(f"Resuelve la operacion {dato1} + {dato2}"))
    if respuestaUsuario == dato1 + dato2:
        break

print("Bien hecho")