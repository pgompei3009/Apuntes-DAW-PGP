vocales = consonantes = 0

def cuantasVocales() -> int:
    cuentaVocal = 0
    for i in range(1, len(pal)+1, 1):
        if pal[i-1] == "a" or pal[i-1] == "e" or pal[i-1] == "i" or pal[i-1] == "o" or pal[i-1] == "u" or pal[i-1] == "A" or pal[i-1] == "E" or pal[i-1] == "I" or pal[i-1] == "O" or pal[i-1] == "U": 
            cuentaVocal += 1
    vocales = cuentaVocal
    return vocales

def cuantasConsonantes() -> int:
    cuentaVocal = cuantasVocales()
    consonantes = len(pal) - cuentaVocal
    return consonantes

pal = input("Escribe una palabra: ")

vocales = cuantasVocales()
consonantes = cuantasConsonantes()
print(f"La palabra tiene {vocales} vocales y {consonantes} consonantes")