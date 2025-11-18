import random

nums = []
masRep = 1

for _ in range(1000):
    nums.append(random.randint(1, 100))


for i in range(2, 100):
    if nums.count(i) > nums.count(i-1):
        mayorRep = i

print(f"El número más repetido es el {mayorRep}, que se repite {nums.count(mayorRep)}")