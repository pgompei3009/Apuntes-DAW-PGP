import random

def imprimir_enfrentamientos(tenistas_top_8):
    numTenista = []
    tenista1 = tenista2 = None
    while True:
        num = random.randint(0,7)
        if tenista2 is not None:
            print(f"{tenista1}\t vs\t{tenista2}")
            tenista1 = tenista2 = None

        if len(numTenista) == 8:
            break

        if numTenista.count(num) == 0 and tenista1 is None:
            tenista1 = tenistas_top_8[num]
            numTenista.append(num)

        elif numTenista.count(num) == 0 and tenista2 is None:
            tenista2 = tenistas_top_8[num]
            numTenista.append(num)

tenistas_top_8 = [
    "Jannik Sinner",      # 11,330 puntos
    "Alexander Zverev",   # 8,135 puntos
    "Carlos Alcaraz",     # 7,410 puntos
    "Taylor Fritz",       # 4,900 puntos
    "Casper Ruud",        # 4,480 puntos
    "Daniil Medvedev",    # 3,930 puntos
    "Novak Djokovic",     # 3,900 puntos
    "Álex de Miñaur"      # 3,735 puntos
]

print("ENFRENTAMIENTOS:")
imprimir_enfrentamientos(tenistas_top_8)