from pathlib import Path


ruta = Path(__file__).parent.parent / ".txt" / "quijote.txt"


cuenta = 0
with open(ruta, "r", encoding="utf-8") as f:
    lineas = f.readlines()
    for l in lineas:
        if l.strip().split(" ")[0].lower() == 'don':
            cuenta += 1

print(f'En el quijote {cuenta} lineas empiezan por "Don"')