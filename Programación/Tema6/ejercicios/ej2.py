from math import floor
from datetime import datetime, timedelta


class Empleado:
    def __init__(self, nombre: str, fecha_inicio: datetime, sueldo: float) -> None:
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.sueldo = sueldo


class EmpleadoFijo(Empleado):
    def __init__(self, nombre: str, fecha_inicio: datetime, sueldo: float) -> None:
        super().__init__(nombre, fecha_inicio, sueldo)

    def trienios(self) -> int:
        return (datetime.today().year - self.fecha_inicio.year)//3
    

class EmpleadoTemporal(Empleado):
    def __init__(self, nombre: str, fecha_inicio: datetime, sueldo: float, fecha_fin: datetime) -> None:
        super().__init__(nombre, fecha_inicio, sueldo)
        self.fecha_fin = fecha_fin

    def meses_restantes(self) -> int:
        diferencia = (self.fecha_fin - datetime.today()).days//30.4375
        return max(diferencia, 0)
    
    def ampliar_contrato(self, meses: int) -> None:
        self.fecha_fin = datetime(self.fecha_fin.year, self.fecha_fin.month + meses, self.fecha_fin.day)


if __name__ == '__main__':
    emp_fijo = EmpleadoFijo('Jacinto', datetime(2019, 7, 9), 2100)
    emp_temp = EmpleadoTemporal('Venancio', datetime(2024, 11, 5), 1900, datetime(2026, 6, 21))

    print(EmpleadoFijo.trienios(emp_fijo))
    print(EmpleadoTemporal.meses_restantes(emp_temp))
    EmpleadoTemporal.ampliar_contrato(emp_temp, 2)
    print(EmpleadoTemporal.meses_restantes(emp_temp))

    