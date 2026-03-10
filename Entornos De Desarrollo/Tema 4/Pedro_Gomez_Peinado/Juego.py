from Mano import Mano
from Baraja import Baraja

baraja = Baraja()

while True:
    if len(baraja.baraja) < 5:
        print("Sin cartas suficientes. Fin.")
        break

    opcion = input("1 = robar | 0 = salir: ")
    if opcion == "0":
        break
    if opcion != "1":
        continue

    cartas = baraja.actualizar_baraja(5)
    if cartas is None:
        print("Sin cartas suficientes. Fin.")
        break

    mano = Mano(cartas)
    print(mano)
    print(mano.calcular_puntuacion())
    print(mano.imprimir_jugada())