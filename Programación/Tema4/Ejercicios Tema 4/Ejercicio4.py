from Ejercicio1 import Juegos

for Juego in Juegos:
    descuento = 0
    if 'RPG' in Juego.generos:
        descuento = 0.25
        
    [print(f'{Juego.nombre} \n {Juego.precio_final(0.21, descuento)}\n') for Juego in Juegos if 'RPG' in Juego.generos]