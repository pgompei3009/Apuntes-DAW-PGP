via = input("Dime la via por la que vas: ")
vehiculo = input("Dime el vehículo en el que vas: ")

if via == "autovía":
    if vehiculo == "coche":
        print("Velocidad: 120 km/h")
    elif vehiculo == "autobús":
        print("Velocidad: 110 km/h")
    else:
        print("Velocidad: 100 km/h")
else:
    if vehiculo == "coche" or vehiculo == "autobús":
        print("Velocidad: 100 km/h")
    else:
        print("Velocidad: 90 km/h")    