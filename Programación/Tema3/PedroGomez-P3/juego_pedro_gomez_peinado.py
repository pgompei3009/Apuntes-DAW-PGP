import funciones, random

vidas = 10
palabrasNiveles = (('DEDO', 'GATO', 'LORO', 'GAFA', 'PATO', 'UOHO', 'ROBE', 'SALO'),
                   ('PALOMA', 'TRITON', 'TARIFA', 'GIRAFA', 'ATRACO', 'CUÑADO', 'DUENDE', 'PARQUE'),
                   ('ELEFANTE', 'FANTASMA', 'MONTAÑA', 'CAMISETA', 'DIAMANTE', 'MARIPOSA', 'CATEDRAL'))
letrasUtilizadas = []
nivel = 0

while True:
      if nivel == 3:
            break     
      palabraNivel, enunciadoNivel = funciones.generarNivel(palabrasNiveles, nivel)
      funciones.imprimirNivel(nivel)
      match nivel:
            case 0:    
                  while True:
                        if vidas == 0:
                              print('Has perdido')
                              SystemExit
                        if '_' not in enunciadoNivel:
                              print('Enhorabuena, has encontrado la palabra:\n'
                                    f'{enunciadoNivel}')
                              nivel += 1
                              break
                              
                        print(f'Tienes: {vidas} vidas\n'
                              f'Palabra que debes encontrar:\n {enunciadoNivel}')
                        letra = input('Inserta una letra: ')
                        enunciadoNivel, letrasUtilizadas, vidas = funciones.comprobarLetra(vidas, letra, enunciadoNivel, palabraNivel, letrasUtilizadas)

            case 1:                  
                  letrasUtilizadas.clear()
                  
                  while True:
                        if vidas == 0:
                              print('Has perdido')
                              SystemExit
                        if '_' not in enunciadoNivel:
                              print('Enhorabuena, has encontrado la palabra:\n'
                                    f'{enunciadoNivel}')
                              nivel += 1
                              break
                              
                        print(f'Tienes: {vidas} vidas\n'
                              f'Palabra que debes encontrar:\n {enunciadoNivel}')
                        letra = input('Inserta una letra: ')
                        enunciadoNivel, letrasUtilizadas, vidas = funciones.comprobarLetra(vidas, letra, enunciadoNivel, palabraNivel, letrasUtilizadas)

            case 2:                  
                  letrasUtilizadas.clear()                  
                  
                  while True:
                        if vidas == 0:
                              print('Has perdido')
                              SystemExit
                        if '_' not in enunciadoNivel:
                              print('Enhorabuena, has encontrado la palabra:\n'
                                    f'{enunciadoNivel}\n'
                                    'Has ganado!!!')
                              nivel += 1
                              break
                              
                        print(f'Tienes: {vidas} vidas\n'
                              f'Palabra que debes encontrar:\n {enunciadoNivel}')
                        letra = input('Inserta una letra: ')
                        enunciadoNivel, letrasUtilizadas, vidas = funciones.comprobarLetra(vidas, letra, enunciadoNivel, palabraNivel, letrasUtilizadas)