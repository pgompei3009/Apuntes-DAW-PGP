def contar_mas_largos_horror(textos):
    contador = 0
    texto_corto = min(len(t) for t in textos)
    for t in textos:
        if len(t) > texto_corto:
            contador += 1

    return contador