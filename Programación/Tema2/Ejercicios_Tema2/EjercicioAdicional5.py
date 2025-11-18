hora = int(input("Dame una hora: "))
min = int(input("Dame los minutos: "))

if hora == 12:
    momentoDia = "PM"

elif hora == 00:
    hora += 12
    momentoDia = "AM"

elif hora > 12:
    hora -= 12
    momentoDia = "PM"

elif hora < 12:
    momentoDia = "AM"

if hora < 10:
    hora = "0"+str(hora)

if min < 10:
    min = "0"+str(min)

print(f"Son las {hora}:{min} {momentoDia}")