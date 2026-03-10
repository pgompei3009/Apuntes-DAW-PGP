class Carta:
    def __init__(self, valor: int, palo: str):
        """Metodo constructor que inicializa las cartas
        
        :param valor: Valor de la carta
        :type valor: int
        :param palo: Palo de la carta
        :type palo: str
        """
        self.valor = valor
        self.palo = palo

    def __str__(self) -> str:
        """Imprime las cartas de caras.

        :return: Devuelve las cartas de caras en formato string.
        :rtype: str
        """
        valores_caras = {11: "J", 12: "Q", 13: "K", 14: "A"}
        return f"{valores_caras.get(self.valor, self.valor)}{self.palo}"
    

    