from datetime import date
from datos import get_datos
from Banda import Banda
from BibliotecaBandas import Biblioteca_Bandas


lista = get_datos(0)

while True:
    print('---Listado de bandas---')
    [print(f'ID: {b.id} | {b.nombre}: {b.nota_discografia}') for b in lista.bandas]

    print('\n[ID] Ver / Modificar\n'
          '[O] Ordenar\n'
          '[A] Añadir\n'
          '[B] Buscar\n'
          '[S] Salir\n')
    opcion = input('¿Que quieres hacer?: ')

    if opcion in 'OABS':
        match opcion:
            case 'O':
                lista_ordenada = []
                print('¿Por cuál atributo quieres ordenar?')
                print('1. Nombre\n'
                      '2. Nota\n'
                      '3. Actividad\n'
                      '4. Fecha de inicio\n'
                      '5. Fecha de la muerte del cantante')
                opcion = int(input('Elige un atributo: '))
                match opcion:
                    case 1:
                        Biblioteca_Bandas.ordenar_por_nombres(lista)
                        input()

                    case 2:
                        Biblioteca_Bandas.ordenar_por_nota(lista)
                        input()

                    case 3:
                        Biblioteca_Bandas.ordenar_por_actividad(lista)
                        input()

                    case 4:
                        Biblioteca_Bandas.ordenar_por_fecha_inicio(lista)
                        input()

                    case 5:
                        Biblioteca_Bandas.ordenar_por_fecha_muerte(lista)
                        input()

            case 'A':
                id = int(input('ID de la banda: '))
                nombre = input('Nombre de la banda: ')
                generos = (input('Generos de la banda (separados por ","): ')).split(',')
                nota = float(input('Nota de la discografia: '))
                opcion = input('Activa (S/N): ')
                if opcion == 'S':
                    activa = True
                else:
                    activa = False

                dia = int(input('Dia de la fecha del primer disco: '))
                mes = int(input('Mes dela fecha del primer disco: '))
                año = int(input('Año de la fecha del primer disco: '))
                fecha_primer_album = date(año, mes, dia)

                dia = int(input('Dia de la fecha de la muerte del cantante: '))
                mes = int(input('Mes de la fecha de la muerte del cantante: '))
                año = int(input('Año de la fecha de la muerte del cantante: '))
                fecha_muerte = date(año, mes, dia)

                integrantes = {}
                while True:
                    nuevo = input('Introduce el nombre del nuevo integrante: ')
                    integrantes[nuevo] = input('Introduce su rol en la banda: ')

                    opcion = input('¿Introducir otro integrante? (S/N): ')
                    if opcion == 'N':
                        break
                    
                banda = Banda(id, nombre, generos, nota, activa, fecha_primer_album, fecha_muerte, integrantes)
                Biblioteca_Bandas.añadir_banda(lista, banda)

            case 'B':
                print('1. Buscar por artista\n'
                      '2. Buscar por periodo de tiempo')
                opcion = int(input('Elige una opcion: '))

                match opcion:
                    case 1:
                        nombre_artista = input('Nombre del artista por el que quieres filtrar: ')
                        Biblioteca_Bandas.buscador_bandas_por_artista(lista, nombre_artista)
                    case 2:
                        inicio = int(input('Año inicio del intervalo: '))
                        fin = int(input('Año fin del intervalo: '))
                        Biblioteca_Bandas.aparicion_durante_periodo(lista, inicio, fin)
                input()

            case 'S':
                break

    else:
        opcion = int(opcion)
        if opcion < 0:
            Biblioteca_Bandas.eliminar_banda(lista, opcion*-1)
            input('Banda eliminada...')
        else:
            for b in lista.bandas:
                if b.id == opcion:
                    while True:
                        print('---Ficha de la banda---')
                        print(b)
                        print('0 - Volver al menu principal')
                        opcion = int(input('Seleccione la accion que quiere realizar: '))

                        match opcion:
                            case 1:
                                b.nombre = input('Nuevo nombre: ')

                            case 2:
                                while True:
                                    print('Integrantes:')
                                    for i, g in enumerate(b.generos):
                                        print(f'{i+1}. {g}')

                                    print('\n1. Añadir genero\n'
                                            '2. Eliminar genero\n'
                                            '0. Volver')   
                                    opcion = int(input('¿Qúe quieres hacer: '))

                                    match opcion:
                                        case 1:
                                            b.generos.append(input('Introduce el nombre del nuevo genero: '))

                                        case 2:
                                            posicion = int(input('¿Que genero quieres eliminar?: '))
                                            b.generos.pop(posicion-1)

                                        case 0:
                                            break

                                        case _:
                                            print('Opción no válida...')
                                            input()

                            case 3:
                                nota = float(input('Nueva nota: '))
                                while nota < 0 or nota > 10:
                                    nota = float(input('La nota debe ser entre 0 y 10: '))
                                b.nota_discografia = nota

                            case 4:
                                opcion = input('¿Esta la banda activa (S/N): ')
                                if opcion == 'S':
                                    b.activa = True
                                else:
                                    b.activa = False

                            case 5:
                                dia = int(input('Escribe el dia la fecha del primer disco: '))
                                mes = int(input('Escribe el mes la fecha del primer disco: '))
                                año = int(input('Escribe el año la fecha del primer disco: '))
                                b.fecha_primer_album = date(año, mes, dia)

                            case 6:
                                dia = int(input('Escribe el dia la fecha de la muerte del cantante: '))
                                mes = int(input('Escribe el mes la fecha de la muerte del cantante: '))
                                año = int(input('Escribe el año la fecha de la muerte del cantante: '))
                                b.fecha_muerte = date(año, mes, dia)

                            case 7:
                                while True:
                                    nombres_integrantes = list(b.integrantes.keys())
                                    roles_integrantes = list(b.integrantes.values())
                                    print('Integrantes:')
                                    for i, (integrante, rol) in enumerate(b.integrantes.items()):
                                        print(f'{i+1}. {integrante}: {rol}')

                                    print('\n1. Añadir integrante\n'
                                            '2. Eliminar integrante\n'
                                            '3. Modificar integrante\n'
                                            '0. Volver')  
                                    opcion = int(input('¿Qúe quieres hacer: '))

                                    match opcion:
                                        case 1:
                                            nuevo = input('Introduce el nombre del nuevo integrante: ')
                                            b.integrantes[nuevo] = input('Introduce su rol en la banda: ')

                                        case 2:
                                            posicion = int(input('¿Que integrante quieres eliminar?: '))
                                            b.integrantes.pop(nombres_integrantes[posicion-1])

                                        case 3:
                                            while True:
                                                posicion = int(input('¿Qué integrante quieres modificar?: '))
                                                print('1. Cambiar nombre\n'
                                                      '2. Cambiar rol\n'
                                                      '0. Volver')  
                                                opcion = int(input('¿Qúe quieres hacer: '))

                                                match opcion:
                                                    case 1:
                                                        nombre = input('Escribe el nombre que quieres poner al integrante: ')
                                                        b.integrantes[nombre] = b.integrantes.pop(nombres_integrantes[posicion-1]) 

                                                    case 2:
                                                        rol = input('Escribe el rol que quieres poner al integrante: ')
                                                        b.integrantes[nombres_integrantes[posicion-1]] = rol
                                                        
                                                    case 0:
                                                        break

                                                    case _:
                                                        print('Opción no válida...')
                                                        input()
                                                
                                                opcion = input('¿Quieres hacer mas cambios? (S/N): ')
                                                if opcion == 'N':
                                                    break
                                    
                                        case 0:
                                            break

                                        case _:
                                            print('Opción no válida...')
                                            input()
                            case 0:
                                break
            
