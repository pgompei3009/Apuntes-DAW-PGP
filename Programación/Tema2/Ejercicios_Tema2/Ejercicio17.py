ingresos = float(input("Dime tus ingresos: "))

if ingresos <= 10000:
    print("No tienes que pagar impuestos, te quedas con tus moneys")
elif ingresos > 10000 and ingresos <= 20000:
    print(f"Tienes que pagar {ingresos*0.1} euros")
elif ingresos > 20000 and ingresos <= 40000:
    print(f"Tienes que pagar {10000*0.1+(ingresos-20000)*0.2} euros")
elif ingresos > 40000:
    print(f"Tienes que pagar {10000*0.1+20000*0.2+(ingresos-40000)*0.3} euros")