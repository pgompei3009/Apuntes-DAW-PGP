def conversion(peso: float) -> float:
    pesoConvertido = peso/0.453592
    return pesoConvertido
    
while True:
    peso = float(input("Inserta un peso en kilogramos: "))
    if peso <= 0:
        break
    pesoConvertido = conversion(peso)
    print(f"{peso} kilos son {pesoConvertido} libras")