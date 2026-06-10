from random import randint
from pathlib import Path


def leer_config(ruta: str):
    config = {}

    with open(ruta, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if linea:    
                clave, valor = linea.split('=')
                if clave == 'tablas':    
                    config[clave] = valor.split(',')
                else:
                    config[clave] = valor
    return config


def jugar(config):
    tablas = config['tablas']
    if config['preguntas'] != 'infinito':
        preguntas = int(config['preguntas'])
        infinito = False
    else:
        infinito = True

    while True:
        tabla = randint(0, len(tablas)-1)
        num = randint(0, 9)
        resultado = tabla*num
        respuesta = int(input(f'{tabla} x {num} = '))
        if respuesta == resultado:
            print('Correcto!!!')
        else:
            print(f'El resultado era {resultado}')

        if infinito == False:
            preguntas -= 1
            if preguntas == 0:
                break

if __name__ == '__main__':
    ruta = Path(__file__).parent.parent / '.txt' / 'ej7.txt'
    jugar(leer_config(ruta))