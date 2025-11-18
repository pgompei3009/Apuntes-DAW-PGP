import random

def operacion_aleatoria() -> str:
    operacion = random.randint(1,3)
    match operacion:
        case 1:
            operador = "+"

        case 2:
            operador = "-"

        case 3:
            operador = "x"

    return operador

def cuentas_aleatorias(inicio: int, final: int) -> int:
    num1 = random.randint(inicio, 10)
    num2 = random.randint(1, 10)

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

    if respuestaUsuario == resultado:
        print("Muy bien!!!")
    else:
        print(f"Mal, la respuesta era: {resultado}")


print("Benvenuti al pre-calculatron >:3")

for i in range (1, 11, 1):
    print(f"Operación {i}:")
    operador = operacion_aleatoria()
    cuentas_aleatorias()