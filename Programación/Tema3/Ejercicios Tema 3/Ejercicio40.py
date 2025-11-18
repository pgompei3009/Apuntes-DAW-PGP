numsSeparados = []

nums = input('Escribe números separados por punto y coma: ')

numsSeparados = nums.split(';')

print(f'El número mayor es: {max(numsSeparados)}\n'
      f'El número menor es: {min(numsSeparados)}\n'
      f'La suma es: {sum(numsSeparados)}\n'
      f'La media es: {sum(numsSeparados)/len(numsSeparados)}')