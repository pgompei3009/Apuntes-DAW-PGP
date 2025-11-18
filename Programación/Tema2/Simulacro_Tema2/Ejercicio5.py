import random

opcion = input("¿Qué eliges (pares o nones)?: ")
while opcion != "pares" and opcion != "nones":
    opcion = input("Elección no válida. Elige entre pares o nones: ")

dedosUsuario = int(input("¿Cuántos dedos sacas?: "))
while dedosUsuario < 0 or dedosUsuario > 10:
    dedosUsuario = int(input("Número de dedos no válido (entre 0 y 10): "))

dedosMaquina = random.randint(0, 10)
total = dedosMaquina + dedosUsuario

print(f"Tu has sacado {dedosUsuario} dedos u la máquina {dedosMaquina}")
if ((total%2) == 0 and opcion == "pares") or ((total%2) != 0 and opcion == "nones"):
    print("Enhorabuena has ganado!!!")
else:
    print("Has perdido")