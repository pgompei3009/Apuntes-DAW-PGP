from pathlib import Path

ruta = Path(__file__).parent.parent / '.txt' / 'quijote.txt'
contador = 0

with open(ruta, 'r', encoding='utf-8') as f:
    for linea in f:
        if 'caballero' in linea:
            contador += 1

print(f'El quijote tiene la palabra "caballero" en {contador} lineas')