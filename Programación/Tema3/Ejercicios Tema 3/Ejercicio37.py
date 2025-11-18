nums = []

while True:
    num = int(input("Dame un número: "))
    if num == 0:
        break

    nums.append(num)


print(f'El mayor es {max(nums)}\n'
      f'El menor es {min(nums)}\n'
      f'La media es {sum(nums)/len(nums)}')