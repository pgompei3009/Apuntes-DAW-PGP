class Coche:
    def __init__(self, marca: str, modelo: str, año_fabricacion: int, peso: int, tipo_motor: str, potencia: int, automatico: bool, num_puertas: int, num_asientos: int, consumo: float, deposito: float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.año_fabricacion = año_fabricacion
        self.peso = peso
        self.tipo_motor = tipo_motor
        self.potencia = potencia
        self.automatico = automatico
        self.num_puertas = num_puertas
        self.num_asientos = num_asientos
        self.consumo = consumo
        self.deposito = deposito

    
    def __str__(self) -> str:
        return (
            f'Marca: {self.marca}\n'
            f'Modelo: {self.modelo}, '
            f'Año de fabricación: {self.año_fabricacion}, '
            f'Peso: {self.peso}, '
            f'Tipo motor: {self.tipo_motor}, '
            f'Potencia: {self.potencia}, '
            f'Automático: {self.automatico}, '
            f'Número de puertas: {self.num_puertas}, '
            f'Número de asientos: {self.num_asientos}, '
            f'Consumo: {self.consumo} L/100Km, '
            f'Depósito: {self.deposito}'
        )
    

    def autonomia(self) -> float:
        return self.consumo/self.deposito*100
    

    def __gt__(self, other) -> bool:
        return self.potencia > other.potencia
    

    def __eq__(self, other) -> bool:
        for i, atributo in enumerate(self.items()):
            if self[i] != other[i]:
                return False
            
        return True
    
    