from Banda import Banda
from Vinilo import Vinilo
from pathlib import Path
import sqlite3


RUTA_BD = Path(__file__).parent / "coleccion_vinilos.db"


def conectar() -> sqlite3.Connection:
    conexion = sqlite3.connect(RUTA_BD)
    conexion.execute('PRAGMA foreign_keys = ON')
    return conexion


def obtener_bandas(conexion: sqlite3.Connection) -> list[Banda]:
    cursor = conexion.cursor()

    cursor.execute('''
        SELECT * 
        FROM grupos
        ORDER BY nombre
    ''')

    filas = cursor.fetchall()

    bandas = []

    for id, nombre in filas:
        bandas.append(Banda(id, nombre))

    return bandas


def obtener_vinilos(conexion: sqlite3.Connection) -> list[Vinilo]:
    cursor = conexion.cursor()

    cursor.execute('''
        SELECT v.id, v.nombre, g.nombre
        FROM vinilos v
        INNER JOIN grupos g ON v.id_grupo = g.id
        ORDER BY g.nombre
    ''')

    filas = cursor.fetchall()

    vinilos = []

    for id, nombre, banda in filas:
        vinilos.append(Vinilo(id, nombre, banda))

    return vinilos


def añadir_banda(conexion: sqlite3.Connection) -> None:
    nombre = input('Nombre de la nueva banda: ')
    cursor = conexion.cursor()

    while nombre == '':
        nombre = input('La banda debe tener un nombre\nNombre de la nueva banda: ')

    try:
        cursor.execute('''
            INSERT INTO grupos (nombre)
            VALUES (?)
        ''', (nombre,))

        conexion.commit()

    except sqlite3.IntegrityError as error:
        print(f'No se ha podido agregar la banda: {error}')


def elegir_banda(bandas: list[Banda], conexion: sqlite3.Connection) -> int:
    while True:
        print('Bandas disponibles\n'
        '------------------')
        for b in bandas:
            print(b)

        print('[N]ueva banda')
        opcion = input('Elige una banda por id o [N]ueva: ')

        if opcion.upper() == 'N':
            añadir_banda(conexion)
            bandas = obtener_bandas(conexion)

        elif opcion.isnumeric():
            for b in bandas:
                if int(opcion) == b.id:
                    return b.id

            print('No se ha encontrado la banda')


def añadir_vinilo(bandas: list[Banda], conexion: sqlite3.Connection) -> list[Vinilo]:
    nombre_vinilo = input('Nombre del vinilo: ')

    while nombre_vinilo == '':
        nombre_vinilo = input('El vinilo debe tener un nombre\nNombre del nuevo vinilo: ')

    cursor = conexion.cursor()
    banda = elegir_banda(bandas, conexion)

    try:
        cursor.execute('''
            INSERT INTO vinilos (nombre, id_grupo)
            VALUES (?, ?)
        ''', (nombre_vinilo, banda))
        
        conexion.commit()
        vinilos = obtener_vinilos(conexion)
        return vinilos

    except sqlite3.IntegrityError as error:
        print(f'No se ha podido agregar la banda: {error}')


def imprimir_menu() -> None:
    print('Menu\n'
    '----\n'
    '[M]ostrar colección\n'
    '[A]ñadir vinilo\n'
    '[S]alir')


def mostrar_coleccion(vinilos: list[Vinilo]) -> None:
    print('Coleccion de vinilos\n'
    '--------------------')
    for v in vinilos:
        print(v)


def main() -> None:
    conexion = None

    try:
        conexion = conectar()
    except sqlite3.Error as error:
        print(f"No se ha podido conectar con la base de datos: {error}")
        return
    
    bandas = obtener_bandas(conexion)
    vinilos = obtener_vinilos(conexion)
    mostrar_coleccion(vinilos)

    while True:
        imprimir_menu()
        opcion = input('Opción: ')
        print('')

        match opcion:
            case 'M':
                mostrar_coleccion(vinilos)

            case 'A':
                vinilos = añadir_vinilo(bandas, conexion)

            case 'S':
                break

    if conexion is not None:
        conexion.close()


if __name__ == '__main__':
    main()

    