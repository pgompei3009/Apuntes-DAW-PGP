from pathlib import Path


ruta = Path(__file__).parent.parent / ".txt" / "quijote.txt"


cuenta_palabras = 0
cuenta_lineas = 0
with open(ruta, "r", encoding="utf-8") as f:
    for linea in f:
        cuenta_palabras += len(linea)
        cuenta_lineas += 1

print(f'El quijote tiene una media de {cuenta_palabras/cuenta_lineas} caracteres por linea')