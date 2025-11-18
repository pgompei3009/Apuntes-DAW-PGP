nums = []
numsInv = []

while True:
    num = int(input("Dime un número: "))
    if num == 0:
        break
    nums.append(num)


for _ in range(len(nums)):
    numsInv.append(nums.pop())


print(numsInv)