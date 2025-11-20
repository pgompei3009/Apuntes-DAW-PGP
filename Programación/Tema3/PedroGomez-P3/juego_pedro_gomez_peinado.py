import funciones, random

vidas = 10
palabrasNiveles = (('DEDO', 'GATO', 'LORO', 'GAFA', 'PATO', 'UOHO', 'ROBE', 'SALO'),
                   ('PALOMA', 'TRITON', 'TARIFA', 'GIRAFA', 'ATRACO', 'CUÑADO', 'DUENDE', 'PARQUE'),
                   ('ELEFANTE', 'FANTASMA', 'MONTAÑA', 'CAMISETA', 'DIAMANTE', 'MARIPOSA', 'CATEDRAL', 'ALERGIA'))
nivel = 0

while True:
      if nivel == 3:
            print('Has ganado!!!')
            break     
      palabraNivel, enunciadoNivel = funciones.generarNivel(palabrasNiveles, nivel)
      funciones.imprimirNivel(nivel)
      nivel, vidas = funciones.jugar_nivel(nivel, vidas, enunciadoNivel, palabraNivel)