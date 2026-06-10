from pathlib import Path


ruta_quijote = Path(__file__).parent.parent / '.txt' / 'quijote.txt'
ruta_datos = Path(__file__).parent.parent / '.txt' / 'quijote_datos.txt'
contador_lineas = contador_palabras = contador_letras = 0

with open(ruta_quijote, 'r', encoding='utf-8') as f:
    for linea in f:
        contador_lineas += 1
        contador_palabras += len(linea.strip().split())
        contador_letras += sum(letra.isalpha() for letra in linea)

with open(ruta_datos, 'w', encoding='utf-8') as f:
    f.write(f'El Quijote tiene {contador_lineas} lineas, {contador_palabras} palabras y {contador_letras} letras.')

