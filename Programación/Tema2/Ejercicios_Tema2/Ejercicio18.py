unidades = int(input("Dime cuántas unidades quieres comprar: "))

if unidades <= 10:
    print(f"El precio es {unidades*8.75}")
elif unidades >= 11 and unidades <= 50:
    print(f"El precio es {unidades*8.75*0.95}")
elif unidades >= 51 and unidades <= 100:
    print(f"El precio es {unidades*8.75*0.90}")
else:
    print(f"El precio es {unidades*8.75*0.85}")