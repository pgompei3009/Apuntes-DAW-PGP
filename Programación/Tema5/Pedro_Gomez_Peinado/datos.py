from datetime import date
from Banda import Banda
from BibliotecaBandas import Biblioteca_Bandas


def get_datos(indice: int) -> object:
    return coleccion_de_bandas[indice]


coleccion_de_bandas = [
    Biblioteca_Bandas(1, 'Los Grunge y Extremoduro',
    [Banda(1, 'Alice in Chains', ['Grunge', 'Metal alternativo', 'Heavy metal', 'Sludge metal'], 8.75, True, date(1990, 8, 21), date(2002, 4, 5), {'Layne Staley': 'Cantante', 'Jerry Cantrell': 'Guitarra', 'Sean Kinney': 'Bateria', 'Mike Starr': 'Bajo'}),

    Banda(2, 'Soundgarden', ['Grunge', 'Metal alternativo', 'Rock alternativo', 'Heavy Metal'], 9.07, False, date(1988, 10, 31), date(2017, 5, 18), {'Chris Cornell': 'Cantante', 'Kim Thayil': 'Guitarra', 'Matt Cameron': 'Bateria', 'Hiro Yamamoto': 'Bajo'}),

    Banda(3, 'Stone Temple Pilots', ['Grunge', 'Metal alternativo', 'Rock alternativo', 'Hard rock'], 8.33, True, date(1992, 9, 29), date(2015, 12, 3), {'Scott Weiland': 'Cantante', 'Dean DeLeo': 'Guitarra', 'Robert DeLeo': 'Bajo', 'Eric Kretz': 'Bateria'}),

    Banda(4, 'Audioslave', ['Rock alternativo', 'Metal alternativo', 'Hard rock', 'Post-grunge'], 8.66, False, date(2002, 11, 18), date(2017, 5, 18), {'Chris Cornell': 'Cantante', 'Tom Morello': 'Guitarra', 'Tim Commerford': 'Bajo', 'Brad Wilk': 'Bateria'}),

    Banda(5, 'Extremoduro', ['Rock transgresivo', 'Hard rock', 'Rock urbano', 'Rock'], 9.45, False, date(1990, 2, 2), date(2025, 12, 10),  {'Roberto Iniesta': 'Cantante y guitarra', 'Salo': 'Bajo', 'Von Fanta': 'Bateria'}),

    Banda(6, 'Nirvana', ['Grunge', 'Rock alternativo', 'Punk rock'], 8.0, False, date(1989, 6, 15), date(1994, 4, 5), {'Kurt Cobain': 'Cantante y guitarra', 'Krist Novoselic': 'Bajo', 'Dave Grohl': 'Bateria'}),

    Banda(7, 'Linkin Park', ['Metal alternativo', 'Nu metal', 'Rock alternativo', 'Rap metal'], 9.0, True, date(2000, 10, 24), date(2017, 7, 20), {'Chester Bennington': 'Cantante', 'Mike Shinoda': 'Cantante y teclado', 'Brad Delson': 'Guitarra', 'Dave Farrell': 'Bajo', 'Joe Hahn': 'DJ', 'Rob Bourdon': 'Bateria'}),

    Banda(8, 'Mother Love Bone', ['Grunge', 'Hard rock', 'Glam metal'], 8.5, False, date(1989, 3, 19), date(1990, 3, 16), {'Andrew Wood': 'Cantante', 'Stone Gossard': 'Guitarra', 'Bruce Fairweather': 'Guitarra', 'Jeff Ament': 'Bajo', 'Greg Gilmore': 'Bateria'}),

    Banda(9, 'Temple Of The Dog', ['Grunge', 'Rock alternativo'], 9.5, False, date(1991, 4, 16), date(2017, 5, 18), {'Chris Cornell': 'Cantante', 'Mike McCready': 'Guitarra', 'Stone Gossard': 'Guitarra', 'Jeff Ament': 'Bajo', 'Matt Cameron': 'Bateria'}),

    Banda(10, 'Mad Season', ['Grunge', 'Rock alternativo', 'Blues rock'], 8.0, False, date(1995, 3, 14), date(2002, 4, 5), {'Layne Staley': 'Cantante', 'Mike McCready': 'Guitarra', 'John Baker Saunders': 'Bajo', 'Barrett Martin': 'Bateria'})]),

    Biblioteca_Bandas(2, 'Rock y metal alternativo',
    [Banda(11, 'Static-X', ['Metal industrial', 'Nu metal', 'Metal alternativo'], 8.0, True, date(1999, 3, 23), date(2014, 11, 1), {'Wayne Static': 'Cantante y guitarra', 'Koichi Fukuda': 'Guitarra', 'Tony Campos': 'Bajo', 'Ken Jay': 'Bateria'}),

    Banda(12, 'Robe', ['Rock urbano', 'Hard rock', 'Rock'], 9.25, False, date(2015, 6, 9), date(2025, 12, 10), {'Roberto Iniesta': 'Cantante y guitarra'}),

    Banda(13, 'AWS', ['Post-hardcore', 'Metal alternativo', 'Metalcore'], 9.25, True, date(2018, 5, 4), date(2021, 2, 5), {'Örs Siklósi': 'Cantante', 'Bence Brucker': 'Guitarra', 'Dániel Kökényes': 'Guitarra', 'Áron Veress': 'Bateria'}),

    Banda(14, 'Velvet Revolver', ['Hard rock', 'Rock alternativo', 'Post-grunge'], 8.5, False, date(2004, 6, 8), date(2015, 12, 3), {'Scott Weiland': 'Cantante', 'Slash': 'Guitarra', 'Duff McKagan': 'Bajo', 'Matt Sorum': 'Bateria', 'Dave Kushner': 'Guitarra'}),

    Banda(15, 'Snot', ['Nu metal', 'Rap metal', 'Metal alternativo'], 9.5, True, date(1997, 10, 7), date(1998, 12, 11), {'Lynn Strait': 'Cantante', 'Mikey Doling': 'Guitarra', 'Sonny Mayo': 'Guitarra', 'John Fahnestock': 'Bajo', 'Jamie Miller': 'Bateria'}),

    Banda(16, 'Grey Daze', ['Post-grunge', 'Rock alternativo'], 9.0, False, date(1994, 6, 1), date(2017, 7, 20), {'Chester Bennington': 'Cantante', 'Jason Barnes': 'Guitarra', 'Mace Beyers': 'Bajo', 'Sean Dowdell': 'Bateria'}),

    Banda(17, 'Dead By Sunrise', ['Rock alternativo', 'Metal alternativo', 'Electronic rock'], 7.75, False, date(2009, 10, 13), date(2017, 7, 20), {'Chester Bennington': 'Cantante', 'Ryan Shuck': 'Guitarra', 'Amir Derakh': 'Guitarra', 'Brandon Belsky': 'Bajo', 'Elias Andra': 'Bateria'}),

    Banda(18, 'Drowning Pool', ['Nu metal', 'Metal alternativo', 'Hard rock'], 8.5, True, date(2001, 8, 14), date(2002, 8, 14), {'Dave Williams': 'Cantante', 'C.J. Pierce': 'Guitarra', 'Stevie Benton': 'Bajo', 'Mike Luce': 'Bateria'}),

    Banda(19, 'Screaming Trees', ['Grunge', 'Rock alternativo', 'Neo-psychedelia'], 8.5, False, date(1987, 6, 1), date(2022, 5, 22), {'Mark Lanegan': 'Cantante', 'Gary Lee Conner': 'Guitarra', 'Van Conner': 'Bajo', 'Mark Pickerel': 'Bateria'}),

    Banda(20, 'Art of Anarchy', ['Hard rock', 'Metal alternativo', 'Post-grunge'], 8.0, True, date(2015, 6, 2), date(2015, 12, 3), {'Scott Weiland': 'Cantante', 'Ron "Bumblefoot" Thal': 'Guitarra', 'John Moyer': 'Bajo', 'Jon Votta': 'Guitarra', 'Vince Votta': 'Bateria'})])
]
