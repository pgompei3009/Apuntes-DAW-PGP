import funcs

partidas = rachaMax = operacionesTotales = aciertosTotales = 0
bronce = plata = oro = platino = "NO conseguido :("
numMax = 10
numMin = 0
vidasConfiguradas = 3

while True:
    funcs.imprimirMenu()
    opcion = int(input("Selecciona una opción: "))
    if opcion == 0 and partidas != 0:
        print("Venga tío una partida más enrróllate...")
        break
    elif opcion == 0 and partidas == 0:
        print("Así se te acumulan los juegos en Steam, los compras y no los tocas :P")
        break

    match opcion:
        case 1:
            aciertos = 0
            operaciones = 0
            partidas += 1
            racha = rachaMaxPartida = 0
            vidas = vidasConfiguradas
            while vidas != 0:

                operaciones += 1                
                print(f"Operación {operaciones}:")
                correcto = funcs.cuentas_aleatorias(numMin, numMax)

                if correcto == True:
                    aciertos += 1
                    racha += 1
                    bronce, plata, oro, platino = funcs.comprobarLogros(numMin, numMax, racha, bronce, plata, oro, platino)
                else:
                    if rachaMaxPartida < racha:
                        rachaMaxPartida = racha
                    racha = 0
                    vidas -= 1
                    print(f"Te quedan {vidas} vidas")
                    
            if rachaMax < rachaMaxPartida:
                rachaMax = rachaMaxPartida
                
            aciertosTotales += aciertos
            operacionesTotales += operaciones
            print(f"En tu partida número {partidas} has acertado {aciertos} y has fallado {operaciones - aciertos}\n"
                  f"Has acertado un {aciertos/operaciones*100}% de las cuentas")

        case 2:
            while True:
                funcs.imprimirConfiguracion(vidasConfiguradas, numMin, numMax)
                opcion = int(input("¿Qué deseas hacer?: "))
                if opcion == 0:
                    break
                
                match opcion:
                    case 1:
                        vidasConfiguradas = funcs.configurarVidas()
                    
                    case 2:
                        numMin = funcs.configurarNumMin(numMax)
                    
                    case 3:
                        numMax = funcs.configurarNumMax(numMin)

        case 3:
            if partidas == 0:
                print("¿Si no has jugado que datos quieres que tenga?")
            else:
                funcs.imprimirEstadisticas(partidas, operacionesTotales, aciertosTotales, rachaMax)
            
        case 4:
            funcs.imprimirLogros(bronce, plata, oro, platino)