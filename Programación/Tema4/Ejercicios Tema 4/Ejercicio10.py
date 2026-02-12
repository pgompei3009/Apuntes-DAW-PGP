from Libro import Libro
from Ejercicio9 import libros

print('1. Encontrar los libros escritos por Dostoievski con más de 1000 páginas')
[print(libro.nombre) for libro in libros if 'Fiódor Dostoievski' in libro.autores and libro.paginas > 1000]

print('2. Encontrar los libros con menos de 400 páginas')
[print(libro.nombre) for libro in libros if libro.paginas < 400]

print('3. Encontrar los libros cuyo nombre es un número')
libro_nombre_numero = []

for libro in libros:
    try:
        nombre_int = int(libro.nombre)
    
    except Exception as error:
        pass

    else:
        libro_nombre_numero.append(libro.nombre)

print(libro_nombre_numero)

print('4. Encontrar (sin repetir) los escritores de la lista ')
autores = []

for libro in libros:
    for autor in libro.autores:
        autores.append(autor)

[print(autor) for autor in set(autores)]