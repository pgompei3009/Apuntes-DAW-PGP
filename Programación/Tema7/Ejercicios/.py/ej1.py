from pathlib import Path

ruta = Path(__file__).parent.parent / '.txt' / 'quijote.txt'

with open(ruta, 'r', encoding='utf-8') as f:
    lineas = f.readlines()

print(f'El quijote tiene {len(lineas)} lineas')