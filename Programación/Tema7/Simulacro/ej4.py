from random import randint


def leer_config(nombre_config: str):
    config = {}

    with open(nombre_config, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if linea:    
                clave, valor = linea.split('=')    
                config[clave] = valor
    return config


def tirar_dados(nombre_sim: str, config: dict):
    numero_caras = int(config['tipo_dado'][1:])
    numero_tiradas = int(config['num_tiradas'])
    with open(nombre_sim, 'w', encoding='utf-8') as f:
        for _ in range(numero_tiradas + 1):
            f.write(f'{randint(1, numero_caras)}\n')


def configurar(nombre_config: str):
    tipo_dado = input('Nuevo tipo de dado: ')
    num_tiradas = input('Nuevo número de tiradas: ')
    with open(nombre_config, 'w', encoding='utf-8') as f:
        f.write(f'tipo_dado={tipo_dado}\n')
        f.write(f'num_tiradas={num_tiradas}')


def jugar(nombre_sim: str, nombre_config, config: dict):
    while True:
        print('1. Simular\n2. Configurar\n0. Salir')
        opcion = int(input('Elige una opción: '))
        match opcion:
            case 1:
                tirar_dados(nombre_sim, config)
                print('Simulación realizada correctamente.')

            case 2:
                print(f'Configuración actual: {config['tipo_dado']}, {config['num_tiradas']} tiradas')
                opcion = input('¿Quieres cambiar la configuración? (S/N): ')
                if opcion == 'S':
                    configurar(nombre_config)
                    print('Configuración guardada correctamente.')

            case 0:
                print('Saliendo del programa...')
                break


if __name__ == '__main__':
    nombre_config = 'config.txt'
    nombre_sim = 'simulacion.txt'
    config = leer_config(nombre_config)

    jugar(nombre_sim, nombre_config, config)