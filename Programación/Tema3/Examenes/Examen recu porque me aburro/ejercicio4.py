def menu() -> None:
    print('MENÚ\n'
          '1) Ver mermeladas\n'
          '2) Insertar mermelada\n'
          '0) Salir')

def verMermeladas(mermeladas: list[str, list[str], int, bool]) -> None:
    if len(mermeladas) == 0:
        print('No hay mermeladas registradas.')
    else:
        for mermelada in mermeladas:
            print(mermelada)

def insertarMermelada() -> list[str, list[str], int, bool]:
    mermelada = []
    mermelada.append(input('Nombre de la mermelada: '))
    mermelada.append(input('Ingredientes (separados por comas): ').split(','))
    mermelada.append(input('Cantidad de azucar: '))
    mermelada.append(True if input('¿Es ecológica? (S/N): ') == 'S' else False)
    
    return mermelada

mermeladas = []

while True:
    menu()
    opcion = int(input('Elige una opción: '))

    match opcion:
        case 1:
            verMermeladas(mermeladas)
        case 2:
            mermelada = insertarMermelada()
            mermeladas.append(mermelada.copy())
            print('Mermelada insertada.')
        case 0:
            break

    print()