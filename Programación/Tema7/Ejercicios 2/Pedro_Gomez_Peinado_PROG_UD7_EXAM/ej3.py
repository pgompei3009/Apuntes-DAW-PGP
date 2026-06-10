from pathlib import Path


ruta_divina_comedia = Path(__file__).parent / 'datos' / 'divina-comedia.txt'
ruta_resultado = Path(__file__).parent / 'ej3-resultado.txt'


with open(ruta_divina_comedia, 'r', encoding='utf-8') as f:
    lineas = [linea.strip() for linea in f.readlines()]

apartado_a = lineas[6:27]    
apartado_b = max(lineas, key=lambda linea: len(linea))
apartado_c = max(lineas, key=lambda linea: linea.count('m'))

with open(ruta_resultado, 'w', encoding='utf-8') as f:
    f.write('### Apartado A:\n')
    for l in apartado_a:
        f.write(f'{l}\n')
    f.write('\n### Apartado B:\n'
            f'{apartado_b}\n'
            f'\n### Apartado C:\n'
            f'{apartado_c}')
