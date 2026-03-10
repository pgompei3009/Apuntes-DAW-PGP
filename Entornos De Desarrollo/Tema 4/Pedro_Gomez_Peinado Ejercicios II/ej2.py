def contar_superiores(valores: list[int], porcentaje: float):
    contador = 0
    limite = max(valores) * porcentaje
    for v in valores:
        if v > limite:
            contador += 1
    return contador