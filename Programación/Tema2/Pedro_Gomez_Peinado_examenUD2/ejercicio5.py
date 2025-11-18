import random

num1 = random.randint(1, 10)
print(num1)

while True:
    num2 = random.randint(1,10)
    print(num2)
    if num2 == num1:
        break
    num1 = num2