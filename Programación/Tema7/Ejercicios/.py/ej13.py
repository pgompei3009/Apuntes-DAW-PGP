from pathlib import Path


ruta = Path(__file__).parent.parent / '.txt' / 'ej13.txt'
lista_palabras = []
while True:
    palabra = input('Inserte una palabra: ')
    if palabra == 'fin':
        break
    lista_palabras.append(palabra)

with open(ruta, 'w', encoding='utf-8') as f:
    for p in lista_palabras:
        f.write(f'{p}\n')

