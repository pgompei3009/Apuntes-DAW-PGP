from pathlib import Path

ruta = Path(__file__).parent.parent / '.txt' / 'tablas_multiplicar.txt'

with open(ruta, 'w', encoding='utf-8') as f:
    for i in range(1, 11):
        f.write(f'---Tabla del {i}---\n')
        j = 1
        while j <= 10:
            f.write(f'{i} x {j} = {i*j}\n')
            j += 1
