from Ejercicio1 import Juegos

[print(Juego.nombre) for Juego in Juegos if Juego.PEGI < 18 and Juego.puntuacion >= 9]