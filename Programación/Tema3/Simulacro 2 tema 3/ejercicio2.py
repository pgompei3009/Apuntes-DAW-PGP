from random import randint

numsAleatorios = [randint(0, 100) for _ in range(20)]

print(f'Lista de números aleatorios: {numsAleatorios}')

numsGuardados = [num for num in numsAleatorios if num % 5 == 0]

print(f'Lista de números terminados en 0 o en 5: {numsGuardados}')