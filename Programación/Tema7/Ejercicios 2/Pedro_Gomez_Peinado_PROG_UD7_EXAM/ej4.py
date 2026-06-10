from pathlib import Path
from random import randint


def es_primo(n: int, d: int = 2) -> bool:
    return False if n < 2 else True if d * d > n else False if n % d == 0 else es_primo(n, d + 1)


def leer_config(ruta_config: Path) -> dict:
    if not ruta_config.exists():
        with open(ruta_config, 'w', encoding='utf-8') as f:
            f.write(f'inicio:10\n'
                'fin:100\n'
                'cantidad:5\n'
                'salida:pantalla\n'
                'solo_primos:false')
            
    with open(ruta_config, 'r', encoding='utf-8') as f:
        config = {}
        for linea in f:
            linea = linea.strip()
            if linea:
                clave, valor = linea.split(':')
                config[clave] = valor

    return config


def actualizar_config(config: dict) -> list:
    inicio = int(config['inicio'])
    fin = int(config['fin'])
    cantidad = int(config['cantidad'])
    salida = config['salida']
    solo_primos = config['solo_primos']
    return inicio, fin, cantidad, salida, solo_primos



ruta_config = Path(__file__).parent / 'ej4-config.txt'
ruta_resultado = Path(__file__).parent / 'ej4-resultado.txt'
config = leer_config(ruta_config)

inicio, fin, cantidad, salida, solo_primos = actualizar_config(config)

while True:
    print('--- MENU ---\n'
            '1. Calcular\n'
            '2. Configurar\n'
            '3. Salir')
    opcion = int(input('Elige opcion: '))

    match opcion:
        case 1:
            numeros = []
            while len(numeros) < cantidad:
                num = randint(inicio, fin)
                if solo_primos == 'true':
                    if es_primo(num):
                        numeros.append(num)
                else:
                    numeros.append(num)
            
            if salida == 'pantalla':
                print(f'Resultados:\n{numeros}')
            else:
                with open(ruta_resultado, 'w', encoding='utf-8') as f:
                    for i, n in enumerate(numeros, start=1):
                        f.write(f'{i}, {n}\n')

        case 2:
            print('\n--- CONFIGURACON ACTUAL ---')
            for clave, valor in config.items():
                print(f'{clave}: {valor}')
            opcion = input('\n¿Quieres modificar la configuracion? (s/n): ')

            print('\n--- EDITAR CONFIGURACION ---')
            config['inicio'] = int(input(f'Inicio ({inicio})'))
            config['fin'] = int(input(f'Fin ({fin}): '))
            config['cantidad'] = int(input(f'Cantidad ({cantidad}): '))
            config['salida'] = input(f'Salida [pantalla/fichero] ({salida}): ')
            config['solo_primos'] = input(f'Solo primos [true/false] ({solo_primos}): ')
            inicio, fin, cantidad, salida, solo_primos = actualizar_config(config)

            with open(ruta_config, 'w', encoding='utf-8') as f:
                for clave, valor in config.items():
                    f.write(f'{clave}:{valor}\n')
            print('Configuracion guardada.')

        case 3:
            break
