ruta = 'lazarillo.txt'
n_lineas = n_palabras = n_letras = 0
linea_mas_larga = ''

with open(ruta, 'r', encoding='utf-8') as f:
    for linea in f:
        n_lineas += 1
        n_palabras += len(linea.strip().split())
        n_letras += sum(p.isalpha() for p in linea)
        if len(linea) > len(linea_mas_larga):
            linea_mas_larga = linea

print(f'Líneas: {n_lineas}')
print(f'Palabras: {n_palabras}')
print(f'Letras: {n_letras}')
print(f'Línea más larga:\n{linea_mas_larga}')