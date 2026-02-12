from datetime import datetime
from Ejercicio2 import Banda

lista_bandas = [
    Banda(1, 'Alice in Chains', 8.75, True, datetime(1990, 8, 21), datetime(2002, 4, 5), ['Layne Stalye', 'Jerry Cantrell', 'Sean Kinney', 'Mike Starr']),
    Banda(1, 'Alice in Chains', 8.75, True, datetime(1990, 8, 21), datetime(2002, 4, 5), ['Layne Stalye', 'Jerry Cantrell', 'Sean Kinney', 'Mike Starr']),
    Banda(2, 'Soundgarden', 9.07, False, datetime(1988, 10, 31), datetime(2017, 5, 18), ['Chris Cornell', 'Kim Thayil', 'Matt Cameron', 'Hiro Yamamoto']),
    Banda(3, 'Stone Temple Pilots', 8.33, True,  datetime(1992, 9, 29), datetime(2015, 12, 3), ['Scott Weiland', 'Dean DeLeo', 'Eric Kretz', 'Robert DeLeo']),
    Banda(4, 'Audioslave', 8.66, False, datetime(2002, 11, 18), datetime(2017, 5, 18), ['Chris Cornell', 'Tom Morello', 'Brad Wilk', 'Tim Commerford']),
    Banda(5, 'Extremoduro', 9.45, False, datetime(1990, 2, 2), datetime(2025, 12, 10), ['Roberto Iniesta', 'Salo', 'Von Fanta'])
]

Banda.integrantes_comunes(lista_bandas[2], lista_bandas[4])

print(lista_bandas[0] == lista_bandas[1])
