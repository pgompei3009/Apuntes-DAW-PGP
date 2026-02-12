
dia=input("elige que dia de la semana se quiere hospedar:")
habitacion=input("que tipo de habitacion desea doble o individual?:")
festivo=input("si el dia es festivo diga si de lo contrario diga no:")
cuponDes=input("si dispone de un cupon de descuento diga si de lo contradio diga no:")
if cuponDes=="si":
    cupon=float(input("Introduce cupon: (0-100)"))
    cupon=cupon*0.01
if dia== "viernes" or "sabado" and habitacion=="individual":
    precio=45
    if cuponDes == "si":
        precio = precio *(1-cupon)

    else:
        precio = 45

else:
    precio=70
    if cuponDes == "si":
        precio = precio * (1 - cupon)

    else:
        precio=70

if dia=="domingo" and habitacion=="individual":
    if festivo=="si":
        precio=45

        if cuponDes == "si":
            precio = precio * (1 - cupon)

        else:
            precio=40
            if cuponDes == "si":
                precio = precio * (1 - cupon)
else:
    if festivo=="si":
        precio=70
        if cuponDes == "si":
                precio = precio * (1 - cupon)
    else:
        precio = 60
        if cuponDes == "si":
            precio = precio * (1 - cupon)

if dia=="lunes" or dia=="martes" or dia=="miercoles" or dia=="jueves" and habitacion=="individual":
    if festivo=="si":
        precio=45
        if cuponDes == "si":
            precio = precio * (1 - cupon)
    else:
        precio=30
        if cuponDes == "si":
            precio = precio * (1 - cupon)
else:
    if festivo=="si":
        precio=70
        if cuponDes == "si":
            precio = precio * (1 - cupon)
    else:
        precio = 50
        if cuponDes == "si":
            precio = precio * (1 - cupon)

print(precio)











