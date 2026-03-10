from collections import Counter
from Carta import Carta

class Mano:
    def __init__(self, cartas: list[Carta]):
        """Metodo constructor que inicializa la mano.
        """
        self.cartas = cartas

    def calcular_puntuacion(self) -> tuple[int, int]:
        """Metodo que calcula la puntuacion y valor jerarquico de la jugada de la mano.
        
        :return: Devuelve una tupla que contiene el valor jerarquico de la jugada y el valor de la carta mayor de esta.
        :rtype: tuple[int, int]
        """

        orden_valor = sorted([c.valor for c in self.cartas])
        palos_mano = [c.palo for c in self.cartas]
        cantidad_valores = Counter(orden_valor)
        cantidad_palos = Counter(palos_mano)

        es_color = len(cantidad_palos) == 1
        es_escalera = orden_valor == list(range(orden_valor[0], orden_valor[0] + 5))

        if es_escalera and es_color:
            return (8, max(orden_valor))
        if 4 in cantidad_valores.values():
            return (7, max(valor for valor, cartas_mismo_valor in cantidad_valores.items() if cartas_mismo_valor == 4))
        if sorted(cantidad_valores.values()) == [2, 3]:
            return (6, max(valor for valor, cartas_mismo_valor in cantidad_valores.items() if cartas_mismo_valor == 3))
        if es_color:
            return (5, max(orden_valor))
        if es_escalera:
            return (4, max(orden_valor))
        if 3 in cantidad_valores.values():
            return (3, max(valor for valor, cartas_mismo_valor in cantidad_valores.items() if cartas_mismo_valor == 3))
        if list(cantidad_valores.values()).count(2) == 2:
            return (2, max(valor for valor, cartas_mismo_valor in cantidad_valores.items() if cartas_mismo_valor == 2))
        if 2 in cantidad_valores.values():
            return (1, max(valor for valor, cartas_mismo_valor in cantidad_valores.items() if cartas_mismo_valor == 2))
        return (0, max(orden_valor))
    
    def imprimir_jugada(self) -> str:
        """Metodo que imprime la jugada segun su valorar jerarquico.
        
        :return: Jugada que se usa en la mano jugada
        :rtype: str
        """
        valor_jerarquico, _ = self.calcular_puntuacion()
        return [
            "Carta alta",
            "Pareja",
            "Doble pareja",
            "Trío",
            "Escalera",
            "Color",
            "Full",
            "Póker",
            "Escalera de color"
        ][valor_jerarquico]

    def __str__(self) -> str:
        """Metodo sobrecargado de los elementos strings. Estructura la mano para que aparezca la lista de cartas como un string con sus respectivos valores y palos.
        
        :return: Representacion de la mano en string.
        :rtype: str
        """
        return " ".join(str(c) for c in self.cartas)