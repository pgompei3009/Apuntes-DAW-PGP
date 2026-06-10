from pathlib import Path
import random


def leer_config(ruta_config) -> dict:
    config  = {}
    if not ruta_config.exists():
        with open(ruta_config, 'w', encoding='utf-8') as f:
            f.write('longitud=20\n'
                    'modo=3')

    with open(ruta_config, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                clave, valor = linea.split('=')
            config[clave] = valor
    return config


def actualizar_config(config) -> list:
    longitud = int(config['longitud'])
    modo = int(config['modo'])
    return longitud, modo


def imprimir_menu() -> None:
    print('MENÚ PRINCIPAL')
    print('==============')
    print('1. Crear contraseña')
    print('2. Configurar')
    print('3. Salir')


def imprimir_configuracion(longitud: int, modo: int) -> None:
    print('\nCONFIGURACIÓN ACTUAL')
    print('====================')
    print(f'Longitud de la contraseña: {longitud}')
    print(f'Modo: {modo}')

    if modo == 1:
        print('Tipo: Solo minúsculas')

    elif modo == 2:
        print('Tipo: Solo mayúsculas')

    else:
        print('Tipo: Minúsculas y mayúsculas')


def generar_contraseña(longitud: int, modo: int) -> str:
    contraseña = ''
    if modo == 1:
        for _ in range(longitud):
            codigo_ascii = random.randint(97, 122)
            contraseña += chr(codigo_ascii)

    elif modo == 2:
        for _ in range(longitud):
            codigo_ascii = random.randint(65, 90)
            contraseña += chr(codigo_ascii)

    else:
        for _ in range(longitud):
            tipo = random.randint(0, 1)
            if tipo == 0:
                codigo_ascii = random.randint(97, 122)
                contraseña += chr(codigo_ascii)
            else:
                codigo_ascii = random.randint(65, 90)
                contraseña += chr(codigo_ascii)

    return contraseña
        

if __name__ == '__main__':
    ruta_config = Path(__file__).parent / 'config.txt'
    config = leer_config(ruta_config)
    longitud, modo = actualizar_config(config)

    while True:
        imprimir_menu()
        opcion = int(input('Elige una opción: '))
        match opcion:
            case 1:
                contraseña = generar_contraseña(longitud, modo)
                print(f'Contraseña generada: {contraseña}')

            case 2:
                imprimir_configuracion(longitud, modo)
                opcion = input('\n¿Quieres cambiar la configuración? (s/n): ')
                if opcion == 's':
                    config['longitud'] = input('\nNueva longitud de la contraseña: ')
                    print('\nModos disponibles:')
                    print('1. Solo minúsculas')
                    print('2. Solo mayúsculas')
                    print('3. Minúsculas y mayúsculas')
                    config['modo'] = int(input('Nuevo modo: '))

                    with open(ruta_config, 'w', encoding='utf-8') as f:
                        for clave, valor in config.items():
                            f.write(f'{clave}={valor}\n')
                    
                    print('Configuración guardada correctamente.')
                    longitud, modo = actualizar_config(config)
            
            case 3:
                break
            
        print('')

        