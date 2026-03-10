from datetime import datetime, timedelta


class Mascota:
    def __init__(self, id: int, nombre: str, tipo: str, fecha_entrada: datetime, precio: float, fecha_nacimiento: datetime, fecha_venta: datetime, vacunas: list[str]|None) -> None:
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.fecha_entrada = fecha_entrada
        self.precio = precio
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_venta = fecha_venta
        self.vacunas = vacunas

    def __eq__(self, other) -> bool:
        if isinstance(other, Mascota):
            return self.id == other.id
        return False
    
    def edad(self) -> int:
        return (datetime.today() - self.fecha_nacimiento).days
    
    def __str__(self) -> str:
        return (
            f'{self.tipo} - {self.edad()} días - {self.precio}€ [{self.id}]'
        )
    
    def se_vacuna(self) -> bool:
        return False if self.vacunas is None else True
    
if __name__ == "__main__":
    hoy = datetime.today()
    m1 = Mascota(1, 'Misu', 'Gato', hoy - timedelta(days=10), 120.0, hoy - timedelta(days=913.0), None, ['Rabia', 'Trivalente'])
    m2 = Mascota(2, 'Venom', 'Tarántula', hoy - timedelta(days=3), 45.5, hoy - timedelta(days=365), None, None)

    print('=== PRUEBAS DE MASCOTA ===')
    print('\nPruebas para el gato')
    print(m1)

    print('\nPruebas para la araña')
    print(m2)
    print('¿Se vacuna araña? ', Mascota.se_vacuna(m2))

    print('\n¿Es el gato igual a la araña? ', m1 == m2)
    print('¿Es la araña igual a ella misma? ', m1 == m1)