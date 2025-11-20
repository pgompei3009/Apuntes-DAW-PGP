import funciones, random

vidas = 10
palabrasNiveles = (('DEDO', 'GATO', 'LORO', 'GAFA', 'PATO', 'UOHO', 'ROBE', 'SALO'), #NIVEL 1
                   ('PALOMA', 'TRITON', 'TARIFA', 'GIRAFA', 'ATRACO', 'CUÑADO', 'DUENDE', 'PARQUE'), #NIVEL 2
                   ('ELEFANTE', 'FANTASMA', 'MONTAÑA', 'CAMISETA', 'DIAMANTE', 'MARIPOSA', 'CATEDRAL', 'ALEGRIA') ) #NIVEL 3
nivel = 0

while True:
      if nivel == 3:
            print('Has ganado!!!')
            break     
      palabraNivel, enunciadoNivel = funciones.generarNivel(palabrasNiveles, nivel)
      funciones.imprimirNivel(nivel)
      nivel, vidas = funciones.jugar_nivel(nivel, vidas, enunciadoNivel, palabraNivel)