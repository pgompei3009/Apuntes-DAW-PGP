from datetime import date

class Mantecado:
    def __init__(self, id: int, tipo: str, fecha_creacion: date, fecha_caducidad: date, precio: float, ingredientes: list[str]):
        self.id = id
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion
        self.fecha_caducidad = fecha_caducidad
        self.precio = precio
        self.ingredientes = ingredientes

    
    def __eq__(self, other):
        if isinstance:
            if self.id == other.id:
                return True
            return False


    def __str__(self) -> str:
        if len(self.ingredientes) > 1:
            str_ingredientes = (" ,".join(self.ingredientes[:-1]))
            str_ingredientes += " y ", self.ingredientes[-1]

        return (
            f"ID: {self.id} - Tipo: {self.tipo} - Fecha de creacion: {self.fecha_creacion} - Fecha de caducidad: {self.fecha_caducidad}, Precio: {self.precio} - Ingredientes: {str_ingredientes}"
        )
    

    def dias_para_caducar(self) -> int:
        fecha_actual = date.today()
        return (self.fecha_caducidad - fecha_actual).days
    

    def esta_caducado(self) -> bool:
        dias_caducidad = self.dias_para_caducar()
        if dias_caducidad < 0:
            return True
        return False


if __name__ == "__main__":
    m1 = Mantecado(1, 'Chocolate', date(2025, 12, 1), date(2025, 12, 31), 3.5, ["harina", "azúcar", "manteca", "cacao"])
    m2 = Mantecado(1, "Chocolate Especial", date(2025, 12, 5), date(2026, 1, 5), 4, ["harina", "azúcar", "manteca", "cacao", "almendra"])

    print("Días para caducar:")
    print(Mantecado.dias_para_caducar(m1))

    print("\n¿Está caducado?")
    print(Mantecado.esta_caducado(m1))

    print("\nComparación por id (m1 == m2):")
    print(m1 == m2)