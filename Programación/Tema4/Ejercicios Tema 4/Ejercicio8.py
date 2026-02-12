from Planeta import Planeta
from Ejercicio6 import planetas
from datetime import datetime

planetas_trappist = [
    Planeta("TRAPPIST-1b", 0.85 * 5.972e24, 1.116 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1c", 1.38 * 5.972e24, 1.097 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1d", 0.388 * 5.972e24, 0.788 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1e", 0.692 * 5.972e24, 0.920 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1f", 1.04 * 5.972e24, 1.045 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1g", 1.32 * 5.972e24, 1.127 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1h", 0.326 * 5.972e24, 0.755 * 6.371e6, datetime(2017, 2, 22), [])
]

#1. Masa media mayor
print('1. Masa media mayor')
masaMediaSolar = sum([planeta.masa for planeta in planetas])/len(planetas)
masaMediaTrappist = sum([planeta.masa for planeta in planetas_trappist])/len(planetas_trappist)

if masaMediaSolar > masaMediaTrappist:
    print('El Sistema Solar tiene mayor masa media')
else:
    print('El sistema Trappist tiene mayor masa media')

#2. El planeta más denso de cada uno
print('\n2. Planeta más denso de cada sistema')
densidades = [Planeta.get_densidad(planeta) for planeta in planetas]
planetas_densidades = [planeta.nombre for planeta in planetas]
mayorDensidad = max(densidades)

print(f'Planeta con mayor densidad --> {planetas_densidades[densidades.index(mayorDensidad)]}: {mayorDensidad}')

densidades_trappist = [Planeta.get_densidad(planeta) for planeta in planetas_trappist]
planetas_trappist_densidades = [planeta.nombre for planeta in planetas_trappist]
mayorDensidad_trappist = max(densidades_trappist)
planeta_trappist_mayor_densidad = [planeta for planeta in planetas_trappist if Planeta.get_densidad(planeta) == mayorDensidad_trappist][0]

print(f'Planeta con mayor densidad --> {planeta_trappist_mayor_densidad}: {mayorDensidad_trappist}')

#3. El planeta de Trappist más parecido densamente a la Tierra
print('\n3. Planeta cuay densidad más se acerca a la de La Tierra')
densidad_tierra = 0
for planeta in planetas:
    if planeta.nombre == 'Tierra':
        densidad_tierra = Planeta.get_densidad(planeta)
        break

diferencias_densidad = [abs(densidad_tierra-densidad) for densidad in densidades_trappist]
diferencia_minima = min(diferencias_densidad)

print(f'El planeta con la diferencia de densidad menor respecto a La Tierra es {planetas_trappist_densidades[diferencias_densidad.index(diferencia_minima)]} con una diferencia mínima de {diferencia_minima} Kg/l')