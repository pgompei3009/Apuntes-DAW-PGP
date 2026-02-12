import random


def lanzar_moneda() -> str:
    """Lanza una moneda y resuleve el resultado
    
    :return: devuelve el resultado del lanzamiento
    :rtype: str
    """
    resultado = random.randint(0, 1)
    if resultado == 0:
        return 'CARA'
    else:
        return 'CRUZ'
    

def lanzar_dado() -> int:
    """Lanza un dado y devuelve el resultado
    
    :return: resultado del lanzamiento
    :rtype: int
    """
    return random.randint(1, 6)


def generar_matriz(filas: int, columnas: int) -> list[list[int]]:
    """Genera una matríz
    
    :filas: filas que tiene la matríz
    :filas: int
    :columnas: columnas que tiene la matríz
    :columnas: int

    :return: devuelve una matríz aleatoria cuyas medidas son las proporcionadas como parámetros
    :rtype: list[list[int]]
    """
    matriz = []
    fila = []
    for _ in range(filas):
        for _ in range(columnas):
            fila.append(random.randint(0, 9))
        
        matriz.append(fila.copy())
        fila.clear()
        
    return matriz


def generar_numero() -> int:
    """Genera un numero aleatorio
    
    :return: Devuelve un número aleatorio
    :rtype: int
    """
    return random.randint(0, 100)


def adivinar_numero() -> None:
    """
    Juego de adivinar un número generado por la máquina
    """
    numeroSecreto = random.randint(0,100)
    numeroUsuario = -1
    intentos = 0

    while numeroUsuario != numeroSecreto:
        intentos += 1
        numeroUsuario = int(input("Dime un número entre 0 y 100: "))

        if numeroUsuario < numeroSecreto:
            print(f"El número es mayor que {numeroUsuario}, prueba de nuevo ;)")
        elif numeroUsuario > numeroSecreto:
            print(f"El número es menor que {numeroUsuario}, prueba de nuevo ;)")
        else:
            print("Felicidades!!!\n" \
                f"Solo te ha costado {intentos} intentos")