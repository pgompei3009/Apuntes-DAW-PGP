from random import randint

l = []

for _ in range(0, 10):
    numRand = randint(1, 5)
    l.append(numRand)

def sin_repetidos(l: list[int]):
    l2 = []
    for num in l:
        if l2.count(num) == 0:
            l2.append(num)
    return l2

print(f'Lista original: {l}')
print(f'Lista sin repeticiones: {sin_repetidos(l)}')