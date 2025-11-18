import random

#Función que imprime el menu
def imprimirMenu():
    print("Bienvenido al Calculatrón 2.0!!!\n"
          "1. Jugar\n"
          "2. Configuración\n"
          "3. Estadísticas\n"
          "4. Logros\n"
          "0. Salir")

#Función que selecciona la operación
def operacion_aleatoria() -> str:
    operacion = random.randint(1,5)
    match operacion:
        case 1:
            operador = "+"
        case 2:
            operador = "-"
        case 3:
            operador = "x"
        case 4:
            operador = "÷"
        case 5:
            operador = "%"

    return operador

#Función que imprime la cuenta y calcula y comprueba el resultado. En el documento de la práctica pone que la función devuelva un int y ese int será el resultado pero he decidido que devuelva un bool porque veo más práctico que devuelva directamente si el resultado es correcto o no en vez de hacer la comprobación fuera en otra función o en el main.

def cuentas_aleatorias(numMin: int, numMax: int) -> bool:
    operador = operacion_aleatoria()
    num1 = random.randint(numMin, numMax)
    num2 = random.randint(numMin, numMax)
    if num2 == 0 and (operador == "÷" or operador == "%"):
        num2 += 1

    match operador:
        case "+":
            resultado = num1+num2
            respuestaUsuario = int(input(f"{num1} + {num2} = "))

        case "-":
            resultado = num1-num2
            respuestaUsuario = int(input(f"{num1} - {num2} = "))

        case "x":
            resultado = num1*num2
            respuestaUsuario = int(input(f"{num1} x {num2} = "))

        case "÷":
            resultado = num1//(num2)
            respuestaUsuario = int(input(f"{num1} ÷ {num2} = "))

        case "%":
            resultado = num1%(num2)
            respuestaUsuario = int(input(f"{num1} % {num2} = "))

    if respuestaUsuario == resultado:
        print("Correcto!")
        correcto = True
        return correcto
    else:
        print(f"Incorrecto, el resultado era: {resultado}")
        correcto = False
        return correcto

#Función que comprueba el logro de bronce
def comprobarBronce(racha: int, bronce: str) -> str:
    if racha == 3 and bronce == "NO conseguido :(":
        print("LOGRO DE BRONCE DESBLOQUEADO!!!")
        bronce = "SI conseguido :D"
    return bronce

#Función que comprueba el logro de plata
def comprobarPlata(racha: int, plata: str) -> str:
    if racha == 7 and plata == "NO conseguido :(":
        print("LOGRO PLATA DESBLOQUEADO!!!")
        plata = "SI conseguido :D"
    return plata

#Función que comprueba el logro de oro
def comprobarOro(racha: int, oro: str) -> str:
    if racha == 10 and oro == "NO conseguido :(":
        print("LOGRO ORO DESBLOQUEADO!!!")
        oro = "SI conseguido :D"
    return oro

#Función que comprueba el logro de platino
def comprobarPlatino(numMin: int, numMax: int, racha: int, platino: str) -> str:
    if racha == 15 and numMin > 10 and numMax > 15 and platino == "NO conseguido :(":
        print("LOGRO PLATINO DESBLOQUEADO!!!")
        platino = "SI conseguido :D"
    return platino

#Función de comprobación colectiva de logros
def comprobarLogros(numMin: int, numMax: int, racha: int, bronce: str, plata: str, oro: str, platino: str) -> str:
    bronce = comprobarBronce(racha, bronce)
    plata = comprobarPlata(racha, plata)
    oro = comprobarOro(racha, oro)
    platino = comprobarPlatino(numMin, numMax, racha, platino)
    return bronce, plata, oro, platino

#Función que imprime la configuración
def imprimirConfiguracion(vidasConfiguradas: int, numMin:int, numMax:int):
    print("La configuración actual es:\n"
         f"Número de vidas: {vidasConfiguradas}\n"
         f"Número mínimo: {numMin}\n"
         f"Número máximo: {numMax}\n"
          "1. Cambiar número de vidas\n"
          "2. Cambiar número mínimo\n"
          "3. Cambiar número máximo\n"
          "0. Salir")

#Función que configura las vidas
def configurarVidas() -> int:
    vidasConfiguradas = int(input("Inserte el número de vidas (Entre 1 y 10): "))
    while vidasConfiguradas < 1 or vidasConfiguradas > 10:
        vidasConfiguradas = int(input("Número no válido, ha de ser entre 1 y 10: "))
    if vidasConfiguradas == 7:
        print("¿Qué eres, un gato?")
    return vidasConfiguradas

#Función que configura el numero mínimo que puede salir en la operación
def configurarNumMin(numMax: int) -> int:
    numMin = int(input("Nuevo mínimo: "))
    while numMin >= numMax:
        numMin = int(input("El número mínimo debe ser menor al máximo: "))
    if numMin > 10:
        print("¿Te quieres poner a prueba?")
    return numMin

#Función que configura el numero máximo que puede salir en la operación
def configurarNumMax(numMin: int) -> int:
    numMax = int(input("Nuevo máximo: "))
    while numMax <= numMin:
        numMax = int(input("El número máximo debe ser mayor al mínimo: "))
    if numMax > 15:
        print("¿Te quieres poner a prueba?")
    return numMax

#Función que imprime las estadísticas
def imprimirEstadisticas(partidas: int, operacionesTotales: int, aciertosTotales: int, rachaMax: int):
    print(f"Has jugado un total de {partidas} partidas\n"
          f"Habiendo realizado un total de {operacionesTotales} operaciones\n"
          f"Has acertado un total de {aciertosTotales} operaciones\n"
          f"Tu porcentaje de acierto es del {aciertosTotales/operacionesTotales*100}%\n"
          f"Has fallado un total de {operacionesTotales-aciertosTotales} operaciones\n"
          f"Tu porcentaje de fallo es del {100-(aciertosTotales/operacionesTotales*100)}%\n"
          f"Tu máxima racha de aciertos consecutivos es: {rachaMax} aciertos")

#Función que imprime los logros    
def imprimirLogros(bronce: str, plata: str, oro: str, platino: str):
    print(f"Logro de bronce: acierta tres operaciones consecutivas en una misma partida -> {bronce}\n"
          f"Logro de plata: acierta siete operaciones consecutivas en una misma partida -> {plata}\n"
          f"Logro de oro: acierta diez operaciones consecutivas en una misma partida -> {oro}\n"
          f"Logro de platino: ponte a prueba ;)-> {platino}")