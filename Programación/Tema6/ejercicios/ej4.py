class Subscripcion:
    COMISION = 0.21

    def __init__(self, nombre_usuario: str, precio_base: float):
        self.nombre_usuario = nombre_usuario
        self.precio_base = precio_base

    def precio_final(self) -> float:
        return self.precio_base*(self.COMISION + 1)
    

if __name__ == '__main__':
    s1 = Subscripcion('Carmela', 10.99)
    s2 = Subscripcion('Skibidi', 100.99)

    print(f'Precio s1: {Subscripcion.precio_final(s1)}')
    print(f'Precio s2: {Subscripcion.precio_final(s2)}')

    Subscripcion.COMISION = 0.3

    print(f'Precio s1: {Subscripcion.precio_final(s1)}')
    print(f'Precio s2: {Subscripcion.precio_final(s2)}')