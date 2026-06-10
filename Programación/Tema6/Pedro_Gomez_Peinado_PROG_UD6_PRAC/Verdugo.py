from Heroe import Heroe


class Verdugo(Heroe):
    def __init__(self, nombre: str, hp_actual: int, stamina: int, arma: dict[str, float], nivel: int) -> None:
        super().__init__(nombre, hp_actual, stamina, arma, nivel)
        self.sed = 0

    def __str__(self) -> str:
        base = super().__str__()
        return (
            f'{base} | Sed: {self.sed*25}%'
        )
    

    def ataque(self, other: Heroe) -> list[float, int]:
        danio_base = sum(self.arma.values())//len(self.arma)
        danio_final = round(danio_base*(1 + (0.1*self.sed)), 2)
        print(f'{self.nombre} ha hecho {danio_final} de daño a {other.nombre}')
        self.sed += 1
        if self.sed >= 4:
            print('El olor a sangre se intensifica')
        self.cooldown_parry = self.actualizacion_cooldown()
        return other.hp_actual - danio_final, self.sed
    

    def ejecutar(self, other: Heroe) -> list[float, int]:
        if self.sed < 4:
            print('Te falta odio...')
            return other.hp_actual, self.sed
        else:
            if other.hp_actual <= other.hp_max/4:
                print(f'{other.nombre} a sido ejecutado')
                return 0, 0
            else:
                danio_base = sum(self.arma.values())//len(self.arma)
                danio_final = round(danio_base*(1 + (0.1*self.sed))*2, 2)
                print('Eso va a dejar marca...')
                print(f'{self.nombre} ha hecho {danio_final} de daño a {other.nombre}')
                return other.hp_actual - danio_final, 0
   
            
if __name__ == '__main__':
    drifter = Verdugo('Drifter', 2500, 3, {'Agarre Carmesi': 175}, 20)
    espantapajaros = Heroe('Espantapajaros', 9999999, 0, {'Puño de paja': 0}, 99)

    print('=== Personajes creados ===')
    print(drifter)
    print(espantapajaros)
    input()
    print('=== Probando ataque ===')
    espantapajaros.hp_actual, drifter.sed = drifter.ataque(espantapajaros)
    print(espantapajaros)
    input()
    print('=== Probando ejecutar incompleto ===')
    espantapajaros.hp_actual, drifter.sed = drifter.ejecutar(espantapajaros)
    input()
    print('=== Probando ejecucion fallida ===')
    espantapajaros.hp_actual, drifter.sed = drifter.ataque(espantapajaros)
    espantapajaros.hp_actual, drifter.sed = drifter.ataque(espantapajaros)
    espantapajaros.hp_actual, drifter.sed = drifter.ataque(espantapajaros)
    espantapajaros.hp_actual, drifter.sed = drifter.ejecutar(espantapajaros)
    input()
    print('=== Probando ejecucion conseguida ===')
    espantapajaros.hp_actual = espantapajaros.hp_max/4
    drifter.sed = 4
    espantapajaros.hp_actual, drifter.sed = drifter.ejecutar(espantapajaros)
    print(espantapajaros)