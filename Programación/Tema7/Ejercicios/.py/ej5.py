from pathlib import Path

ruta = Path(__file__).parent.parent / '.txt' / 'quijote.txt'

with open(ruta, 'r', encoding='utf-8') as f:
    lineas = f.readlines()

    mas_larga = max(lineas, key=lambda l: len(l))

print(f'El quijote tiene {len(mas_larga)} caracteres en la linea más larga')