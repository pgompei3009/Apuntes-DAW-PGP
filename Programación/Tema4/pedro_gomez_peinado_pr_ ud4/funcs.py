from Usuario import Usuario


def login(usuarios: list[list[object]]) -> list[bool, float, int]:
    nombre_usuario = input('Login: ')
    while nombre_usuario not in (usuario.nombre for usuario in usuarios):
        nombre_usuario = input('El nombre de usuario no existe\nInserte de nuevo el nombre: ')

    intentos_contraseña = 3
    contraseña = input('Contraseña: ')
    while contraseña not in (usuario.contra for usuario in usuarios if usuario.nombre == nombre_usuario):
        intentos_contraseña -= 1
        if intentos_contraseña == 0:
            return False, None, None

        contraseña = input('Contraseña Incorrecta, inserte de nuevo la contraseña: ')

    for usuario in usuarios:
        if usuario.nombre == nombre_usuario and usuario.contra == contraseña:
            return True, usuario.saldo, Usuario.edad(usuario)


def imprimir_juegos(juegos: list[list[object]]) -> None:
    print('JUEGOS DISPONIBLES PARA COMPRAR:')
    [print(f'[{juegos.index(juego) + 1}]. {juego.nombre}, precio: {juego.precio_final(0.21, 0)}€') for juego in juegos]


def imprimir_saldo(saldo: float) -> None:
    print(f'Actualmente tienes: {round(saldo, 2)}€')


def imprimir_opciones() -> None:
    print('[V]er mis juegos\n[I]ngresar dinero\nIr al [c]arrito\n[S]alir')


def imprimir_pagina_principal(saldo: float, juegos: list[list[object]]) -> None:
    imprimir_juegos(juegos)
    print('--------------------------------------------\n')
    imprimir_saldo(saldo)
    print('--------------------------------------------\n')
    imprimir_opciones()


def imprimir_biblioteca(biblioteca: list[list[object]]) -> None:
    if len(biblioteca) == 0:
        print('No tienes ningun juego, comprate algo anda...')
    else:
        print('Tienes los siguientes juegos:')
        [print(juego.nombre) for juego in biblioteca]    
    input()


def ingresar_dinero(saldo: float) -> float:
    while True:
        try:
            dinero = float(input('Cantidad a ingresar: '))

        except Exception as error:
            print('Escribe un numero mayor que cero y con dos decimales como maximo.')
        
        else:
            while dinero <= 0 or dinero*100%1 != 0:
                dinero = float(input('Inserta una cantidad valida de dinero: '))         
            break

    return saldo+dinero


def seleccionar_juego(opcion: str, juegos: list[list[object]], carrito: list[list[object]],) -> list[list[list[object]], list[list[object]]]:    
    try:
        opcion = int(opcion)
    except Exception as error:
        print('Opcion no valida')

    else:
        if opcion >= len(juegos):
            print('Producto no disponible')

        else:
            print(juegos[opcion-1])
            opcion_añadir = input('¿Quieres añadir el juego al carrito? (S/N): ')
            if opcion_añadir == 'S':
                carrito.append(juegos.pop(opcion-1))
                print('Producto añadido al carrito!')

    input()
    return juegos, carrito


def imprimir_carrito(saldo: int, carrito: list[list[object]], biblioteca: list[list[object]]) -> list[float, list[list[object]], list[list[object]]]:
    if len(carrito) == 0:
        print('El carrito esta vacio...')
        input()
        return saldo, carrito, biblioteca

    else:
        [print(f'{juego.nombre} -- precio: {juego.precio_final(0.21, 0)}€') for juego in carrito]
        precio = calcular_total(carrito)
        print(f'El precio total es: {precio}€')
        print('[P]agar\n[V]olver')
        opcion = input('¿Que quieres hacer?: ')
        if opcion == 'P':
            return pagar_carrito(saldo, precio, carrito, biblioteca)
        else:
            return saldo, carrito, biblioteca             


def calcular_total(carrito: list[list[object]]) -> float:
        return sum(juego.precio_final(0.21, 0) for juego in carrito)


def pagar_carrito(saldo: int, precio: int, carrito: list[list[object]], biblioteca: list[list[object]]) -> list[float, list[list[object]], list[list[object]]]:
    if saldo < precio:
        print('No tienes suficiente dinero...')
        input()
        return saldo, carrito, biblioteca
    
    else:
        saldo -= precio
        biblioteca.extend(carrito)
        carrito.clear()

        print('Compra realizada con exito!')
        input()
        return saldo, carrito, biblioteca   

        