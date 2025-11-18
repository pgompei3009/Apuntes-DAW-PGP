pisoActual = 0
destino = 0
cuentaSubir = cuentaBajar = 0
while True:
    destino = int(input("Introduce el piso destino (-1 a 9, otro número para salir): "))
    if destino < -1 or destino > 9:
        break

    if destino > pisoActual:
        print(f"Subiendo {destino-pisoActual} pisos hasta el piso {destino}")
        cuentaSubir += destino-pisoActual
    elif destino < pisoActual:
        print(f"Bajando {pisoActual-destino} pisos hasta el piso {destino}")
        cuentaBajar += pisoActual-destino
    elif destino == pisoActual:
        print("Ya estás en ese piso...")

    pisoActual = destino

print("\nNúmero no válido. Fin del programa\n"
      f"Ha subido un total de {cuentaSubir} pisos\n"
      f"Ha bajado un total de {cuentaBajar} pisos")