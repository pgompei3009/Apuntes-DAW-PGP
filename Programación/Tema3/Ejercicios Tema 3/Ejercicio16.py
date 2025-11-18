import random

# Ejemplo de cómo crear una lista con 1000 números aleatorios entre 0 y 10
# Comenzamos creando una lista vacía
caraCruz = []
resultado = ["Cara", "Cruz"]

# Ahora creamos 1000 números aleatorios entre 0 y 10 y los vamos insertando en la lista
for _ in range(10):
   caraCruz.append(resultado[random.randint(1, 2) - 1])

print(caraCruz)