import random

def generar_carta():
    valor = random.randint(1,13)
    match valor:
        case 11:
            str(valor)
            valor = "J"
        case 12:
            str(valor)
            valor = "Q"
        case 13:
            str(valor)
            valor = "K"

    palo = random.randint(1, 4)
    match palo:
        case 1:
            str(palo)
            palo = "picas"
        case 2:
            str(palo)
            palo = "diamantes"
        case 3:
            str(palo)
            palo = "tréboles"
        case 4:
            str(palo)
            palo = "corazones"

    cartaGenerada = (f"{valor} de {palo}")
    return cartaGenerada

cartaEncontrada = False
tirada = 1

carta = input("Elige una carta: ")
while True:
    cartaGenerada = generar_carta()
    print(f"Tirada {tirada}: {cartaGenerada}")
    if cartaGenerada == carta and cartaEncontrada == True:
        break
    if cartaGenerada == carta:
        primera = tirada
        cartaEncontrada = True
    tirada += 1

print(f"La primera vez que sacó la carta {carta} fue en la 'tirada': {primera}")