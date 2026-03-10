from datetime import datetime, timedelta


class Vehiculo:
    def __init__(self, matricula: str, marca: str, fecha_matriculacion: datetime, fecha_ultima_itv: datetime):
        self.matricula = matricula
        self.marca = marca
        self.fecha_matriculacion = fecha_matriculacion
        self.fecha_ultima_itv = fecha_ultima_itv


class Coche(Vehiculo):
    def __init__(self, matricula: str, marca: str, fecha_matriculacion: datetime, fecha_ultima_itv: datetime, num_puertas: int, combustible: str):
        super().__init__(matricula, marca, fecha_matriculacion, fecha_ultima_itv)
        self.num_puertas = num_puertas
        self.combustible = combustible


    def proxima_itv(self) -> datetime:
        if (datetime.today() - self.fecha_matriculacion).days < 4*365 + 1:
            return self.fecha_matriculacion + timedelta(days=4*365 + 1)
        elif (datetime.today() - self.fecha_matriculacion).days >= 4*365 + 1 < 10*365 + 2:
            return self.fecha_ultima_itv + timedelta(days=2*365)
        else:
            return self.fecha_ultima_itv + timedelta(days=365)


class Moto(Vehiculo):
    def __init__(self, matricula: str, marca: str, fecha_matriculacion: datetime, fecha_ultima_itv: datetime, cilindrada: int):
        super().__init__(matricula, marca, fecha_matriculacion, fecha_ultima_itv)
        self.cilindrada = cilindrada


    def proxima_itv(self) -> datetime:
        if (datetime.today() - self.fecha_matriculacion).days < 4*365 + 1:
            return self.fecha_matriculacion + timedelta(days=4*365 + 1)
        else:
            return self.fecha_ultima_itv + timedelta(days=2*365)


if __name__ == '__main__':
    c = Coche('5241JAW', 'Nose', datetime(2026, 1, 5), None, 4, 'Diesel')
    m = Moto('5412LAX', 'Yoquese', datetime(2017, 5, 2), datetime(2025, 7, 21), 12)

    print(Coche.proxima_itv(c))
    print(Moto.proxima_itv(m))