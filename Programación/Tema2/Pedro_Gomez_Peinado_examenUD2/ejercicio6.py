hora = int(input("¿Qué hora es? (Usa formato 24h): "))
min = int(input("¿Qué minuto es?: "))

if hora < 10:
    horaTxt = "0"+str(hora)
else:
    horaTxt = str(hora)

if min < 10:
    minTxt = "0"+str(min)
else:
    minTxt = str(min)

minHastaAlarma = int(input(f"Perfecto son las {horaTxt}:{minTxt}. ¿En cuántos minutos quieres poner la alarma? "))

minHastaAlarma += min
horasHastaAlarma = minHastaAlarma // 60
minAlarma = minHastaAlarma % 60

horaAlarma = hora + horasHastaAlarma
if horaAlarma > 23:
    dias = horaAlarma // 24
    horaAlarma = horaAlarma - (24*dias)

if horaAlarma < 10:
    horaAlarmaTxt = "0"+str(horaAlarma)
else:
    horaAlarmaTxt = str(horaAlarma)

if minAlarma < 10:
    minAlarmaTxt = "0"+str(minAlarma)
else:
    minAlarmaTxt = str(minAlarma)

print(f"La alarma sonará a las {horaAlarmaTxt}:{minAlarmaTxt}")