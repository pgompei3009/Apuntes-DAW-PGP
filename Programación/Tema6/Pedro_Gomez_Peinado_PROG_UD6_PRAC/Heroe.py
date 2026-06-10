from random import randint


class Heroe:
    def __init__(self, nombre: str, hp_max: int, stamina: int, arma: dict[str, float], nivel: int) -> None:
        self.nombre = nombre
        self.hp_max = hp_max
        self.hp_actual = hp_max
        self.stamina = stamina
        self.arma = arma
        self.nivel = nivel
        self.cooldown_parry = 0


    def __str__(self) -> str:
        return (
            f'{self.nombre} | HP: {self.hp_actual}/{self.hp_max} | Stamina: {self.stamina} | Nivel: {self.nivel}'
        )
    

    def ataque(self, other: Heroe) -> int:
        danio = sum(self.arma.values())//len(self.arma)
        print(f'{self.nombre} ha hecho {danio} de daño a {other.nombre}')
        self.cooldown_parry = self.actualizacion_cooldown()
        return other.hp_actual - danio


    def parry(self) -> int:
        if self.cooldown_parry == 0:
            dado = randint(0, 1)
            if dado == 0:
                print('Parry fallado...')
            else:
                print('Parry exitoso!')      
            return 2
        else:
            print('El cooldown no ha terminado')
            return self.cooldown_parry
        

    def actualizacion_cooldown(self) -> int:
        if self.cooldown_parry != 0:
            self.cooldown_parry -= 1
            if self.cooldown_parry == 0:
                print('El parry esta listo!')
            else:
                print(f'Puedes volver a utilizar el parry en {self.cooldown_parry} turnos.')
            return self.cooldown_parry
        return 0


if __name__ == '__main__':
    lash = Heroe('Jacob Lash', 2500, 3, {'Tale of the Tape': 150}, 17)
    espantapajaros = Heroe('Espantapajaros', 9999999, 0, {'Puño de paja': 0}, 99)

    print('=== Personajes creados ===')
    print(lash)
    print(espantapajaros)
    input()
    print('=== Probando ataque ===')
    espantapajaros.hp_actual = lash.ataque(espantapajaros)
    print(espantapajaros)
    input()
    print('=== Probando Parry ===')
    lash.cooldown_parry = lash.parry()
    input()
    print('=== Probando a recargar el parry ===')
    espantapajaros.hp_actual = lash.ataque(espantapajaros)
    lash.cooldown_parry = lash.parry()
    espantapajaros.hp_actual = lash.ataque(espantapajaros)
    lash.cooldown_parry = lash.parry()
