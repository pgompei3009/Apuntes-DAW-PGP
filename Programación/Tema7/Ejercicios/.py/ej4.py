from pathlib import Path

ruta = Path(__file__).parent.parent / '.txt' / 'quijote.txt'

with open(ruta, 'r', encoding='utf-8') as f:
    sumatoria = 0
    for lineas in f:
        print(lineas)

