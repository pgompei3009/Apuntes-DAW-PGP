from pathlib import Path
from random import choice, randint


def leer_config(ruta: Path) -> dict:
    config = {}
    if not ruta.exists():
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write('tablas=1,2,3,4,5,6,7,8,9\n'
                    'preguntas=10')
    with open(ruta, 'r', encoding='utf=8') as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                clave, valor = linea.split('=')
                config[clave] = valor
    return config


def jugar(config: dict) -> None:
    tablas = config['tablas'].split(',')
    preguntas = config['preguntas']
    if preguntas.isdigit():
        preguntas = int(preguntas)
        infinito = False
    else:
        infinito = True

    while True:
        num = randint(0, 9)
        tabla = int(choice(tablas))
        resultado = num*tabla
        respuesta = int(input(f'{num} x {tabla} = '))
        if respuesta == resultado:
            print('Correcto!')
        else:
            print(f'Fallaste... Era {resultado}')
        if infinito == False:
            preguntas -= 1
            if preguntas == 0:
                break


if __name__ == '__main__':
    ruta = Path(__file__).parent.parent / '.txt' / 'ej7.txt'

    config = leer_config(ruta)
    jugar(config)