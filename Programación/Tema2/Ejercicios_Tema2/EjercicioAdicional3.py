mes1 = int(input("Dime un mes (1-12): "))
mes2 = int(input("Dime un otro mes (1-12): "))

if (mes1 == 1 or mes1 == 3 or mes1 == 5 or mes1 == 7 or mes1 == 8 or mes1 == 10 or mes1 == 12) and (mes2 != 1 or mes2 != 3 or mes2 != 5 or mes2 != 7 or mes2 != 8 or mes2 != 10 or mes2 != 12):
    print(f"El primer mes {mes1} tiene más días que el segundo mes {mes2}")
elif (mes1 == 1 or mes1 == 3 or mes1 == 5 or mes1 == 7 or mes1 == 8 or mes1 == 10 or mes1 == 12) and (mes1 == 1 or mes1 == 3 or mes1 == 5 or mes1 == 7 or mes1 == 8 or mes1 == 10 or mes1 == 12):
    print(f"El seugndo mes {mes2} tiene más días que el primer mes {mes1}")
else:
    print(f"Los dos meses, {mes1} y {mes2}, tienen el mismo número de días")