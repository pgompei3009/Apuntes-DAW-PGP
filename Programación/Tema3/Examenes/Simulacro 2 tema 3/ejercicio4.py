nums = []

while True:
    num = int(input('Inserte un número: '))
    if num == 0:
        break
    nums.append(num)

media = sum(nums)/len(nums)
               
print(f'La media de los números es {round(media, 2)}')
print(f'Los números mayores a la media son {[n for n in nums if n > media]}')
print(f'Los números menores a la media son {[n for n in nums if n < media]}')
print(f'El número máximo: {max(nums)}')
print(f'El número mínimo: {min(nums)}')

nums.sort()
tam = len(nums)

if len(nums)%2 == 0:
    mediana = (nums[(tam//2)-1] + nums[(tam//2)]) / 2
else:
    mediana = nums[(tam//2)]

print(f'La mediana: {mediana}')