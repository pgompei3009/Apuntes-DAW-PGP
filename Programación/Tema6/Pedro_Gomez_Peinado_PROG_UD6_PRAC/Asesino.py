from Heroe import Heroe
from random import randint


class Asesino(Heroe):
    BONUS_DAÑO = 0.15

    def __init__(self, nombre: str, hp_max: int, stamina: int, arma: dict[str, float], nivel: int, municion: int) -> None:
        super().__init__(nombre, hp_max, stamina, arma, nivel)
        self.municion = municion
        self.intimidar = False


    def __str__(self) -> str:
        base = super().__str__()
        return (
            f'{base} | Municion: {self.municion}'
        )
    

    def ataque(self, other: Heroe) -> list[float, bool]:
        danio_base = sum(self.arma.values())//len(self.arma)
        if self.critico() == True:
            print('CRITICO!!!')
            danio_base *= 2

        if self.intimidar == True:
            danio_final = round(danio_base*(1 + self.BONUS_DAÑO)*1.25, 2)
            
        else:
            danio_final = round(danio_base*(1 + self.BONUS_DAÑO), 2)
        print(f'{self.nombre} ha hecho {danio_final} de daño a {other.nombre}')
        self.cooldown_parry = self.actualizacion_cooldown()
        return (other.hp_actual - danio_final), False
    

    def usar_pistola(self) -> list[bool, int]:
        if self.intimidar == True:
            print('"Intimidar" ya esta activo')
            return True, self.municion
        elif self.municion != 0:     
            print('Intimidacion activada')
            return True, self.municion - 1
        else:
            print('No tienes municion')
            return False, 0
        
    
    def critico(self) -> bool:
        resultado = randint(0, 7)
        if resultado == 3:
            return True
        return False
   
            
if __name__ == '__main__':
    haze = Asesino('Haze', 1400, 3, {'Ametralladora1': 215, 'Ametralladora2': 215}, 20, 2)
    espantapajaros = Heroe('Espantapajaros', 9999999, 0, {'Puño de paja': 0}, 99)

    print('=== Personajes creados ===')
    print(haze)
    print(espantapajaros)
    input()
    print('=== Probando ataque ===')
    espantapajaros.hp_actual, haze.intimidar = haze.ataque(espantapajaros)
    print(espantapajaros)
    input()
    print('=== Probando intimidar ===')
    haze.intimidar, haze.municion = haze.usar_pistola()
    espantapajaros.hp_actual, haze.intimidar = haze.ataque(espantapajaros)
    input()
    print('=== Probando intimidar estando activo ===')
    haze.intimidar, haze.municion = haze.usar_pistola()
    haze.intimidar, haze.municion = haze.usar_pistola()
    espantapajaros.hp_actual, haze.intimidar = haze.ataque(espantapajaros)
    input()
    print('=== Probando intimidar sin municion ===')
    haze.intimidar, haze.municion = haze.usar_pistola()

