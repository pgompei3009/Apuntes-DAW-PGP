class Cuenta:
    COMISION = 5

    def __init__(self, titular: str, numero_cuenta: str, saldo: float):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo


    def __eq__(self, other):
        if isinstance(other, Cuenta):
            return self.numero_cuenta == other.numero_cuenta
        return False
    

    def __hash__(self):
        return hash(self.numero_cuenta)


    def __str__(self):
        return (
            f"Cuenta | Titular: {self.titular} | Nº {self.numero_cuenta} | Saldo: {self.saldo}"
            )
    

    def ingresar(self, cantidad: float):
        self.saldo += cantidad


    def retirar(self, cantidad: float):
        if cantidad > self.saldo:
            return False
        else:
            self.saldo -= cantidad
            return True


    def cobrar_comision(self):
        self.saldo -= self.COMISION
    

class CuentaCorriente(Cuenta):
    def __init__(self, titular: str, numero_cuenta: str, saldo: float, limite_descubierto: float):
        super().__init__(titular, numero_cuenta, saldo)
        self.limite_descubierto = limite_descubierto

    
    def __str__(self):
        base = super().__str__().replace('Cuenta', 'Cuenta corriente')
        return (
            f'{base} | Limite descubierto: {self.limite_descubierto}'
        )


    def puede_retirar(self, cantidad: float) -> bool:
        if self.saldo - cantidad + self.limite_descubierto < 0:
            return False
        else:
            return True


    def retirar(self, cantidad: float):
        if self.puede_retirar(cantidad) == True:
            self.saldo -= cantidad
            return True
        else:
            return False


class CuentaAhorro(Cuenta):
    def __init__(self, titular: str, numero_cuenta: str, saldo: float, interes_anual: float):
        super().__init__(titular, numero_cuenta, saldo)
        self.interes_anual = interes_anual


    def aplicar_intereses(self):
        self.saldo *= 1 + (self.interes_anual/100)


    def __str__(self):
        base = super().__str__().replace('Cuenta', 'Cuenta ahorro')
        return (
            f'{base} | Interes anual: {self.interes_anual}%'
        )
    
