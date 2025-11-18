nums = []

while True:
    num = int(input("Dame un número: "))
    if num*(-1) in nums:
        nums.remove(num*(-1))
    else:
        nums.append(num)

    print(f"Lista de números introducidos {nums}")