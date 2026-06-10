from pathlib import Path


ruta = Path(__file__).parent.parent / ".txt" / "quijote.txt"


with open(ruta, "r", encoding="utf-8") as f:
    for linea in f:
        linea_mas_larga = max(f, key=lambda linea: len(linea))

print(f'La linea mas larga en el quijote es "{linea_mas_larga} con {len(linea_mas_larga)} caracteres')