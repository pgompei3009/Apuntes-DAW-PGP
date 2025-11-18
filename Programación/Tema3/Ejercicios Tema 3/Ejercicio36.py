nums = []
numsUlts = []

while True:
    num = int(input("Dame un número: "))
    if num == 0:
        break

    nums.append(num)

ultNums = int(input("Dime los últimos n números que quieres ver: "))

for i in range((len(nums)-ultNums), len(nums)):
    numsUlts.append(nums[i])

print(f"Los últimos {ultNums} números son: {numsUlts}")