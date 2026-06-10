from pathlib import Path


ruta = Path(__file__).parent.parent / ".txt" / "quijote.txt"


cuenta = 0
with open(ruta, "r", encoding="utf-8") as f:
    for linea in f:
        cuenta += 1

print(f'El quijote tiene {cuenta} lineas')