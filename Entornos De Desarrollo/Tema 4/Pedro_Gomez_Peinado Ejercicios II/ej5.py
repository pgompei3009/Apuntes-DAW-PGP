def contar_letras(texto):
    res = {}
    for c in texto:
        if c not in res:
            res[c] = 1
        else:
            res[c] += 1
    return res