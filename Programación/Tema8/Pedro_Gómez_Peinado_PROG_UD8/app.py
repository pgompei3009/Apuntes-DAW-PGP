from ZODB import DB
from ZODB.FileStorage import FileStorage
import transaction
from persistent import Persistent
from persistent.list import PersistentList
from random import choice
import os


os.makedirs('./Pedro_Gómez_Peinado_PROG_UD8', exist_ok=True)


class Frase(Persistent):
    def __init__(self, frase: str, autor: str):
        self.frase = frase
        self.autor = autor

    def __str__(self):
        return f"{self.frase} - {self.autor}"


def crear_nueva_frase() -> tuple[str, str]:
    frase = ''
    while frase == '':
        frase = input('Frase: ')
        if frase == '':
            print('La frase no puede estar vacia, introduzca de nuevo.')

    autor = input('Autor: ') or 'Anónimo'
    return frase, autor


def modificar_frase(frase_actual: Frase) -> tuple[str, str]:
    print('Deja en blanco para mantener el valor.')
    frase = input('Frase: ') or frase_actual.frase
    autor = input('Autor: ') or frase_actual.autor
    return frase, autor


storage = FileStorage("./Pedro_Gómez_Peinado_PROG_UD8/azucarillos.fs")
db = DB(storage)
connection = db.open()
root = connection.root()


if 'frases' not in root:
    root['frases'] = PersistentList()

frases = root['frases']


if frases:
    frase_actual = choice(frases)
    print(f'{frase_actual}')
else:
    print('No hay frases')

while True:
    print('\n[S]iguiente - [M]odificar - [B]orrar - [N]ueva frase')

    try:
        opcion = input('Opción: ')
    except:
        print('Saliendo...')
        break

    if opcion not in 'NSMB':
        print('\nOpción no válida')

    elif opcion == 'N':
        frase, autor = crear_nueva_frase()
        nueva_frase = Frase(frase, autor)
        frases.append(nueva_frase)
        transaction.commit()
        frase_actual = nueva_frase
        print(f'\n{frase_actual}')
    
    elif frases:
        if opcion == 'S':
            frase_actual = choice(frases)
            print(f'\n{frase_actual}')

        elif opcion == 'M':
            frase, autor = modificar_frase(frase_actual)
            frase_actual.frase = frase
            frase_actual.autor = autor
            transaction.commit()
            print(f'\n{frase_actual}')

        elif opcion == 'B':
            frases.remove(frase_actual)
            transaction.commit()
            print('\nFrase eliminada')
            if frases:
                frase_actual = choice(frases)
                print(f'\n{frase_actual}')

    else:
        print('\nNo hay frases')

connection.close()
db.close()  
storage.close() 