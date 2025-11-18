nums = []
total = 0

while True:
    num = int(input("Dame un número que guardad (0 para terminar): "))
    if num == 0:
        break

    total += num
    nums.append(num)
    
print("Números mayores que la media: ")
for num in nums:
    if num > (total/len(nums)):
        print(num)