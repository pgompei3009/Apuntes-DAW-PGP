nums = []

while True:
    num = int(input("Dame un número: "))
    if num == 0:
        break

    nums.append(num)

nums.sort()
nums.reverse()

print(f"Números ordenados: {nums}")