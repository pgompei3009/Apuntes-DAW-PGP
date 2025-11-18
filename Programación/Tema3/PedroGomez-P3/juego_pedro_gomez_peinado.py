import funciones, random

vidas = 10
nivel1 = ['_', '_', '_', '_']
nivel2 = ['_', '_', '_', '_', '_', '_']
nivel3 = ['_', '_', '_', '_', '_', '_', '_', '_']
palabrasNivel1 = ['DEDO', 'GATO', 'LORO', 'GAFA', 'PATO', 'UOHO', 'ROBE', 'SALO']
palabrasNivel2 = ['PALOMA', 'TRITON', 'TARIFA', 'GIRAFA', 'ATRACO', 'CUÑADO', 'DUENDE', 'PARQUE']
palabrasNivel3 = ['ELEFANTE', 'FANTASMA', 'MONTAÑA', 'CAMISETA', 'DIAMANTE', 'MARIPOSA', 'CATEDRAL']
letrasUtilizadas = []
nivel = 1

while True:
      match nivel:
            case 1:
                  palabraNivel = palabrasNivel1[random.randint(0,7)]
                  funciones.imprimirNivel(nivel)
                  
                  while True:
                        if vidas == 0:
                              print('Has perdido')
                              SystemExit
                        if '_' not in nivel1:
                              print('Enhorabuena, has encontrado la palabra:\n'
                                    f'{nivel1}')
                              nivel += 1
                              break
                              
                        print(f'Tienes: {vidas} vidas\n'
                              f'Palabra que debes encontrar:\n {nivel1}')
                        letra = input('Inserta una letra: ')
                        nivel1, letrasUtilizadas, vidas = funciones.comprobarLetra(vidas, letra, nivel1, palabraNivel, letrasUtilizadas)

            case 2:
                  palabraNivel = palabrasNivel2[random.randint(0,7)]
                  letrasUtilizadas.clear()
                  funciones.imprimirNivel(nivel)
                  
                  while True:
                        if vidas == 0:
                              print('Has perdido')
                              SystemExit
                        if '_' not in nivel2:
                              print('Enhorabuena, has encontrado la palabra:\n'
                                    f'{nivel2}')
                              nivel += 1
                              break
                              
                        print(f'Tienes: {vidas} vidas\n'
                              f'Palabra que debes encontrar:\n {nivel2}')
                        letra = input('Inserta una letra: ')
                        nivel1, letrasUtilizadas, vidas = funciones.comprobarLetra(vidas, letra, nivel2, palabraNivel, letrasUtilizadas)

            case 3:
                  palabraNivel = palabrasNivel3[random.randint(0,7)]
                  letrasUtilizadas.clear()                  
                  funciones.imprimirNivel(nivel)
                  
                  while True:
                        if vidas == 0:
                              print('Has perdido')
                              SystemExit
                        if '_' not in nivel3:
                              print('Enhorabuena, has encontrado la palabra:\n'
                                    f'{nivel3}\n'
                                    'Has ganado!!!')
                              nivel += 1
                              break
                              
                        print(f'Tienes: {vidas} vidas\n'
                              f'Palabra que debes encontrar:\n {nivel3}')
                        letra = input('Inserta una letra: ')
                        nivel1, letrasUtilizadas, vidas = funciones.comprobarLetra(vidas, letra, nivel3, palabraNivel, letrasUtilizadas)