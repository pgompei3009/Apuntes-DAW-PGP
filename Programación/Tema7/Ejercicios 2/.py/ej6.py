from pathlib import Path
from random import randint

def leer_configuracion(ruta: Path) -> dict:
    config = {}    
    if not ruta.exists():
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write('intentos=10\n'
                    'numero_minimo=1\n'
                    'numero_maximo=100\n'
                    'pistas_mayor_menor=si')
                
    with open(ruta, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                clave, valor = linea.split('=')
                config[clave] = valor
    return config

def jugar(config: dict) -> None:
    intentos = int(config['intentos'])
    numero_minimo = int(config['numero_minimo'])
    numero_maximo = int(config['numero_maximo'])
    pistas_mayor_menor = config['pistas_mayor_menor'] == 'si'
    numero_secreto = randint(numero_minimo, numero_maximo)
    while True:
        num = int(input('Introduce un número: '))
        if num == numero_secreto:
            print('Felicidades, has acertado!')
            break
        intentos -= 1

        if intentos == 0:
            print(f'Perdiste, el número era {numero_secreto}')
            break

        if pistas_mayor_menor == True:
            if num > numero_secreto:
                print(f'El número es menor que {num}')
            else:
                print(f'El número es mayor que {num}')
        print(f'Quedan {intentos} intentos')
            

if __name__ == '__main__':
    ruta = Path(__file__).parent.parent / '.txt' / 'ej6.txt'
    config = leer_configuracion(ruta)
    jugar(config)