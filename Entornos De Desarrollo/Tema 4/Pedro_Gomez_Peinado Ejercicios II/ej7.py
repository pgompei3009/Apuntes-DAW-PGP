def es_primo_horror(n):
    if n <= 1:
        return False

    divisores = 0
    for i in range(n, 0, -1):
        if n % i == 0:
            divisores += 1

        if divisores == 2 and i != 1:
            return False

    return True