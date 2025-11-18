import random
inicio = int(input("Dime el inicio del intervalo: "))
fin = int(input("Dime el fin del intervalo: "))
nVeces = int(input("Dime el número de veces que quieres generar números: "))
for i in range(1, nVeces+1, 1):
    aleatorio = random.randint(inicio, fin-1)
    aleatorioDecimal = aleatorio+random.random()
    print(round(aleatorioDecimal, 2))