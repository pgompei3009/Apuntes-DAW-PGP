from datos import get_juegos, get_usuarios
import funcs


juegos = get_juegos()
usuarios = get_usuarios()
biblioteca = []
carrito = []

acceso, saldo, edad = funcs.login(usuarios)

if acceso == False:
    print('Acceso denegado')
else:
    juegos_usuario = [juego for juego in juegos if juego.PEGI <= edad]

    while True:
        funcs.imprimir_pagina_principal(saldo, juegos_usuario)
        opcion = input('¿Que quieres hacer?: ')

        if opcion not in 'VIcs':
            juegos_usuario, carrito = funcs.seleccionar_juego(opcion, juegos_usuario, carrito)
        else:    
            match opcion:
                case 'V':
                    funcs.imprimir_biblioteca(biblioteca)

                case 'I':
                    saldo = funcs.ingresar_dinero(saldo)

                case 'c':
                    saldo, carrito, biblioteca = funcs.imprimir_carrito(saldo, carrito, biblioteca)

                case 'S':
                    print('Chao chao :P')
                    break
           
                