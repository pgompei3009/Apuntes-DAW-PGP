from pathlib import Path


def incrementar_denominador(denominador: list[int], itera: int):
    denominador[0] = 2 + 2*(itera - 2)
    denominador[1] = 3 + 2*(itera - 2)
    denominador[2] = 4 + 2*(itera - 2)
    return denominador


ruta = Path(__file__).parent.parent / '.txt' / 'pi.txt'
denominador = [2, 3, 4]

if ruta.exists():
    with open(ruta, 'r+', encoding='utf-8') as f:
        for linea in f:
            ultima_linea = linea

        try:
            itera, pi = ultima_linea.split(';')
            itera = int(itera)
            pi = float(pi)
        except:
            itera = 1
            pi = 3.0
            f.write(f'{itera};{pi}\n')
else:
    with open(ruta, 'w', encoding='utf-8') as f:
        itera = 1
        pi = 3.0
        f.write(f'{itera};{pi}\n')  

print(f'Iteración {itera} --> π ≈ {pi}')

with open(ruta, 'a', encoding='utf-8') as f:
    while True:
        opcion = input('Enter para siguiente iteración o "s" para salir: ')
        if opcion == 's':
            break

        itera += 1
        denominador = incrementar_denominador(denominador, itera)
        if itera%2 != 0:
            pi -= 4/(denominador[0]*denominador[1]*denominador[2])
        else:
            pi += 4/(denominador[0]*denominador[1]*denominador[2])

        print(f'{itera} -> π ≈ {pi}')
        f.write(f'{itera};{pi}\n')

        