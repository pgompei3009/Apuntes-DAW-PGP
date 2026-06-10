from random import randint
from pathlib import Path

ruta = Path(__file__).parent.parent / '.txt' / 'ej6.txt'

def leer_config(ruta: str):
    config = {}

    with open(ruta, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if linea:    
                clave, valor = linea.split('=')    
                config[clave] = valor
    return config
            
def jugar(config: dict):
    intentos = int(config["intentos"])
    valor_maximo = int(config["valor_maximo"])
    valor_minimo = int(config["valor_minimo"])
    pistas = config["pistas"] == "si"
    numero_secreto = randint(valor_minimo, valor_maximo)

    while True:
        numero_usuario = int(input(f"Dime un número entre {valor_minimo} y {valor_maximo}: "))
        if numero_usuario == numero_secreto:
            print("Felicidades!!! El número secreto era: ", numero_secreto)
            break
        
        intentos -= 1
        if intentos == 0:
            print('Has perdido, el número quedará secreto')
            break
        
        if pistas == True:
            if numero_usuario < numero_secreto:
                print(f"El número es mayor que {numero_usuario}, prueba de nuevo ;)")
            else:
                print(f"El número es menor que {numero_usuario}, prueba de nuevo ;)")
            
if __name__ == '__main__':
    jugar(leer_config(ruta))