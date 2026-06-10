from pathlib import Path


class Elemento():
    def __init__(self, nombre: str, simbolo: str, numero_atomico: int, masa_atomica: float, grupo: int) -> None:
        self.nombre = nombre
        self.simbolo = simbolo
        self.numero_atomico = numero_atomico
        self.masa_atomica = masa_atomica
        self.grupo = grupo

    def __str__(self) -> str:
        return (
            f'{self.nombre}({self.simbolo}) - Numero atómico: {self.numero_atomico} - Masa atomica: {self.masa_atomica} - Grupo: {self.grupo}'
        )
    

if __name__ == '__main__':

    ruta = Path(__file__).parent / 'datos' / 'elementos.csv'

    with open(ruta, 'r', encoding='utf-8') as f:
        elementos_grupo_1 = []
        masa_atomica_resto = 0
        masa_atomica_grupo_1 = 0
        cuenta_elementos_resto = 0
        next(f)
        for linea in f:
            linea = linea.strip()
            if linea:
                nombre, simbolo, numero_atomico, masa_atomica, grupo = linea.split(',')
                if grupo == '1':
                    nuevo_elemento = Elemento(nombre, simbolo, int(numero_atomico), float(masa_atomica), int(grupo))
                    elementos_grupo_1.append(nuevo_elemento)
                    masa_atomica_grupo_1 += float(masa_atomica)
                else:
                    masa_atomica_resto += float(masa_atomica)
                    cuenta_elementos_resto += 1


    print('Elementos del grupo 1')
    for e in elementos_grupo_1:
        print(e.nombre)

    media_masa_atomica_grupo_1 = masa_atomica_grupo_1/len(elementos_grupo_1)
    medua_masa_atomica_resto = masa_atomica_resto/cuenta_elementos_resto
    print('\nMedia grupo 1: ', media_masa_atomica_grupo_1)
    print('Media resto: ', medua_masa_atomica_resto)