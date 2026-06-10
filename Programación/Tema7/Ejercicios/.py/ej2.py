from pathlib import Path

ruta = Path(__file__).parent.parent / '.txt' / 'quijote.txt'

with open(ruta, 'r', encoding='utf-8') as f:
    lineas = f.readlines()
    contador = len([l for l in lineas if l.split(" ")[0] == 'Don'])

print(f'El quijote tiene {contador} lineas que empiezan por "Don"')