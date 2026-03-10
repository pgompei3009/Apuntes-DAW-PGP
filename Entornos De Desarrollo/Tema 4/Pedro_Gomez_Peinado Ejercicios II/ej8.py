def hay_duplicados_horror(lista):
    for i in range(len(lista)):
        if lista.count(i) > 1:
                return True
    return False