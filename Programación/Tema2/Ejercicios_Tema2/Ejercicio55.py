import math

def hipotenusa(cat1: float, cat2: float) -> float:
    resultado = math.sqrt(cat1**2 + cat2**2)
    return resultado

cat1 = float(input("Dame la longitud del primer cateto: "))
cat2 = float(input("Dame la longitud del segundo cateto: "))

resultado = hipotenusa(cat1, cat2)
print(f"La hipotenusa mide {resultado}")
