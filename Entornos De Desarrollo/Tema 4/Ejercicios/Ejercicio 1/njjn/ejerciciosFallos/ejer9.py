
lunes_jueves_individual = 30
lunes_jueves_doble = 50

viernes_sabado_individual = 45
viernes_sabado_doble = 70

domingo_individual = 40
domingo_doble = 60

euro = "€"

dia = input("Introduzca el dia de la semana (L, M, X, J, V, S, D): ")
tipo_habitacion = input("introduzca el tipo de habitación (tipo individual o doble): ")
festivo = input("¿Ese dia es festivo? (si o no): ")
cupon = input("¿Tiene cupón de descuento? (si o no): ")

if dia == "L" or dia == "M" or dia == "X" or dia == "J":
    if tipo_habitacion == "individual":
        if festivo == "si":
            if cupon == "si":   
                descuento = int(input("¿Cuanto es el porcentaje a descuentar? (0 a 100): "))
                descuento = descuento / 100
                descuento = viernes_sabado_individual * descuento
                print(f"El precio con descuento aplicado es: {viernes_sabado_individual-descuento}")
            elif cupon == "no":
                print(f"El precio a pagar es: {viernes_sabado_individual}{euro}")

        elif festivo == "no":
            if cupon == "si":   
                descuento = int(input("¿Cuanto es el porcentaje a descuentar? (0 a 100): "))
                descuento = descuento / 100
                descuento = lunes_jueves_individual * descuento
                print(f"El precio con descuento aplicado es: {lunes_jueves_individual-descuento}")
            elif cupon == "no":
                print(f"El precio a pagar es: {lunes_jueves_individual}{euro}")

    elif tipo_habitacion == "doble":
        if festivo == "si":
            if cupon == "si":   
                descuento = int(input("¿Cuanto es el porcentaje a descuentar? (0 a 100): "))
                descuento = descuento / 100
                descuento = viernes_sabado_doble * descuento
                print(f"El precio con descuento aplicado es: {viernes_sabado_doble-descuento}")
            elif cupon == "no":
                print(f"El precio a pagar es: {viernes_sabado_doble}{euro}")

        elif festivo == "no":
            if cupon == "si":   
                descuento = int(input("¿Cuanto es el porcentaje a descuentar? (0 a 100): "))
                descuento = descuento / 100
                descuento = lunes_jueves_doble * descuento
                print(f"El precio con descuento aplicado es: {lunes_jueves_doble-descuento}")
            if cupon == "no":
                print(f"El precio a pagar es: {lunes_jueves_doble}{euro}")

elif dia == "V" or dia == "S": 
    if tipo_habitacion == "individual":     
            if cupon == "si":   
                descuento = int(input("¿Cuanto es el porcentaje a descuentar? (0 a 100): "))
                descuento = descuento / 100
                descuento = viernes_sabado_individual * descuento
                print(f"El precio con descuento aplicado es: {viernes_sabado_individual-descuento}")
            elif cupon == "no":
                print(f"El precio a pagar es: {viernes_sabado_individual}{euro}")

    elif tipo_habitacion == "doble":
            if cupon == "si":   
                descuento = int(input("¿Cuanto es el porcentaje a descuentar? (0 a 100): "))
                descuento = descuento / 100
                descuento = viernes_sabado_doble * descuento
                print(f"El precio con descuento aplicado es: {viernes_sabado_doble-descuento}")
            elif cupon == "no":
                print(f"El precio a pagar es: {viernes_sabado_doble}{euro}")

elif dia == "D":
    if tipo_habitacion == "individual":
        if festivo == "si":
            if cupon == "si":   
                descuento = int(input("¿Cuanto es el porcentaje a descuentar? (0 a 100): "))
                descuento = descuento / 100
                descuento = viernes_sabado_individual * descuento
                print(f"El precio con descuento aplicado es: {viernes_sabado_individual-descuento}")
            elif cupon == "no":
                print(f"El precio a pagar es: {viernes_sabado_individual}{euro}")

        elif festivo == "no":
            if cupon == "si":   
                descuento = int(input("¿Cuanto es el porcentaje a descuentar? (0 a 100): "))
                descuento = descuento / 100
                descuento = domingo_individual * descuento
                print(f"El precio con descuento aplicado es: {domingo_individual-descuento}")
            elif cupon == "no":
                print(f"El precio a pagar es: {domingo_individual}{euro}")

    elif tipo_habitacion == "doble":
        if festivo == "si":
            if cupon == "si":   
                descuento = int(input("¿Cuanto es el porcentaje a descuentar? (0 a 100): "))
                descuento = descuento / 100
                descuento = viernes_sabado_doble * descuento
                print(f"El precio con descuento aplicado es: {viernes_sabado_doble-descuento}")
            elif cupon == "no":
                print(f"El precio a pagar es: {viernes_sabado_doble}{euro}")

        elif festivo == "no":
            if cupon == "si":   
                descuento = int(input("¿Cuanto es el porcentaje a descuentar? (0 a 100): "))
                descuento = descuento / 100
                descuento = domingo_doble * descuento
                print(f"El precio con descuento aplicado es: {domingo_doble-descuento}")
            elif cupon == "no":
                print(f"El precio a pagar es: {domingo_doble}{euro}")