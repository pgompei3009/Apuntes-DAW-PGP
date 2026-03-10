import random
from Carta import Carta

class Baraja:
    def __init__(self):
        """Metodo constructora que inicializa la baraja y las baraja.
        """
        self.baraja = [Carta(valor, palo) for valor in range(2, 15) for palo in ["♠", "♥", "♦", "♣"]]
        random.shuffle(self.baraja)

    def eliminar_carta(self) -> list[object]:
        """Metodo usado para eliminar la carta de la baraja tras robarlas.
        
        :return: `pop()` y elimina la carta si la baraja tiene cartas suficientes para jugar, `None` si no hay.
        :rtype: list[object]
        """
        if not self.baraja:
            return None
        return self.baraja.pop()

    def actualizar_baraja(self, tamanho_mano: int) -> list[object]:
        """Metodo usado para actualizar la baraja.
        
        :param tamanho_mano: Cantidad de cartas que hay por mano jugada.
        :type tamanho_mano: int

        :return: `eliminar_carta()` si la baraja tiene cartas suficientes para jugar, `None` si no hay.
        """
        if len(self.baraja) < tamanho_mano:
            return None
        return [self.eliminar_carta() for _ in range(tamanho_mano)]