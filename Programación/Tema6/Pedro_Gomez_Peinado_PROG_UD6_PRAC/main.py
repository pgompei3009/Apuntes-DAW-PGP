from Asesino import Asesino
from Verdugo import Verdugo


def crear_heroe() -> list[str, int, int, dict[str, int], int]:
    nombre = input('Nombre del heroe: ')
    hp = int(input('Vida del heroe: '))
    stamina = int(input('Stamina del heroe: '))
    armas = {}
    while True:
        nom_arma = input('Nombre del arma: ')
        if nom_arma in armas:
            print('El heroe ya tiene ese arma')
        else:
            armas[nom_arma] = int(input('Daño del arma: '))
        opcion = input('¿Quieres crear otro arma? (S/N): ')
        if opcion == 'N':
            break
    
    nivel = int(input('Nivel del heroe: '))
    return nombre, hp, stamina, armas, nivel


lista_asesinos = [
    Asesino('Haze', 1400, 3, {'Ametralladora1': 215, 'Ametralladora2': 215}, 20, 2)
]
lista_verdugos = [
    Verdugo('Drifter', 2500, 3, {'Agarre Carmesi': 175}, 20)
]


while True:
    print('===== DEADLOCK =====')
    print('1. Ver Asesinos\n'
          '2. Ver Verdugos\n'
          '3. Crear Asesino\n'
          '4. Crear Verdugo')
    opcion = int(input('Elige una opcion: '))

    match opcion:
        case 1:
            [print(a) for a in lista_asesinos]

        case 2:
            [print(v) for v in lista_verdugos]

        case 3:
            nombre, hp, stamina, armas, nivel = crear_heroe()
            municion = int(input('Municion del heroe: '))
            nuevo_asesino = Asesino(nombre, hp, stamina, armas, nivel, municion)
            lista_asesinos.append(nuevo_asesino)

        case 4:
            nombre, hp, stamina, armas, nivel = crear_heroe()
            nuevo_verdugo = Verdugo(nombre, hp, stamina, armas, nivel)
            lista_verdugos.append(nuevo_verdugo)
            
                