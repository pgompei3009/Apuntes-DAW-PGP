from pathlib import Path

ruta = Path(__file__).parent.parent / '.txt' / 'ej16.txt'

with open(ruta, 'r+', encoding='utf-8') as f:
    for linea in f:
        ultima_linea = linea

    try:
        contador = int(ultima_linea)
    except:
        contador = 1
        f.write(f'{contador}\n')

print(f'{contador}')

with open(ruta, 'a', encoding='utf-8') as f:
    while True:
        opcion = input('Enter para incrementar contador o "s" para salir: ')
        if opcion == 's':
            break

        contador += 1
        print(f'{contador}')
        f.write(f'{contador}\n')