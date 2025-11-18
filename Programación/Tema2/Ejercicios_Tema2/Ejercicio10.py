print("Hola, ¿quieres saber cuanto pesa tu coche?")
peso = float(input("Introduce el peso de tu coche en toneladas: "))

if peso < 1:
    print("Tienes un coche de peso ligero")
elif peso >= 1 and peso < 2:
    print("Tienes un coche de peso mediano")
else:
    print("Tienes un coche de peso pesado")