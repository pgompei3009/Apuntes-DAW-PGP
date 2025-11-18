while True:
    print("MENÚ DE CÁLCULOS FÍSICOS")
    print("1. Fuerza = masa * aceleración")
    print("2. Velocidad = espacio / tiempo")
    print("3. Presión = fuerza / superficie")
    print("4. Densidad = masa / volumen")
    print("5. Salir")
    opcion = int(input("Elige una opción (1-5): "))
    if opcion == 5:
        break

    match opcion:
        case 1:
            m = int(input("Introduce la masa (kg): "))
            a = int(input("Introduce la masa (m/s^2): "))
            print(f"La fuerza es {m*a} N")

        case 2:
            d = int(input("Introduce el espacio (m): "))
            t = int(input("Introduce el tiempo (s): "))
            print(f"La velocidad es {d/t} m/s")
        case 3:
            f = int(input("Introduce la fuerza (N): "))
            s = int(input("Introduce la superficie (m^2): "))
            print(f"La presión es {f/s} Pa")
        case 4:
            m = int(input("Introduce la masa (kg): "))
            v = int(input("Introduce el volumen (m/l): "))
            print(f"La fuerza es {m/v} (kg/m^3)")

    print("") 

print("Fin del programa.")