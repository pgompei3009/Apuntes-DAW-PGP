km = input("Dime los kilómetros recorridos")
dia = input("Dime el día de la semana: ")
hora = input("Dime la hora del día: ")

if dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves" or dia == "viernes":
    if hora >= 8 and hora <= 18:
        print(f"Tienes que pagar {km}€")
    elif hora >= 19 and hora <= 23:
        print(f"Tienes que pagar {km*1.2}€")
    else:
        print(f"Tienes que pagar {km*1.5}€")
elif dia == "sábado":
    if hora >= 8 and hora <= 18:
        print(f"Tienes que pagar {km*1.2}€")
    else:
        print(f"Tienes que pagar {km*1.5}€")
else:
    print(f"Tienes que pagar {km*1.5}€")