import math


def area_cuadrado(lado: float) -> float:
    """Calcula el area de un cuadrado
    :lado: longitud del lado
    :lado: float

    :return: devuelve el area del cuadrado cuyo lado es el pasado como parámetro
    :rtype: float
    """
    return lado * lado


def perimetro_rectangulo(base: float, altura: float) -> float:
    """Calcula el perímetro de un rectángulo
    :base: base del rectángulo
    :base: float
    :altura: altura del rectángulo
    :altura: float

    :return: devuelve el perímetro del rectángulo cuya base y altura son las pasadas como parámetros
    :rtype: float
    """
    return 2 * (base + altura)


def area_circulo(radio: float) -> float:
    """Calcula el area de un circulo
    :radio: radio del circulo
    :radio: float

    :return: devuelve el area del circulo cuyo radio es el pasado como parámetro
    :rtype: float
    """
    return math.pi * radio * radio


def area_triangulo(base: float, altura: float) -> float:
    """Calcula el area de un triángulo
    :base: base del triángulo
    :base: float
    :altura: altura del triángulo
    :altura: float

    :return: devuelve el area del triángulo cuya base y altura son las pasadas como parámetros
    :rtype: float
    """
    return (base * altura) / 2


def hipotenusa(cateto1: float, cateto2: float) -> float:
    """Calcula la hipotenusa de un triángulo
    :cateto1: primer cateto del triángulo
    :cateto1: float
    :cateto2: segundo cateto del triángulo
    :cateto2: float

    :return: devuelve la hipotenusa del tríangulo cuyos catetos son pasados como parámetros
    :rtype: float
    """
    return math.sqrt(cateto1 ** 2 + cateto2 ** 2)


def distancia_puntos(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calcula la distancia entre dos puntos en un plano 2D
    :x1: coordenada x del punto 1
    :x1: float
    :y1: coordenada y del punto 1
    :y1: float
    :x2: coordenada x del punto 2
    :x2: float
    :y2: coordenada y del punto 2
    :y2: float

    :return: devuelve la distancia entre dos puntos en un plano 2D cuyas coordenadas son las pasadas como parámetros
    :rtype: float
    """
    dx = x2 - x1
    dy = y2 - y1
    distancia = math.sqrt(dx ** 2 + dy ** 2)
    return distancia


def area_triangulo_lados(a: float, b: float, c: float) -> float:
    """Calcula el area de un triángulo dados sus lados
    :a: lado a del triángulo
    :a: float
    :b: lado b del triángulo
    :b: float
    :c: lado c del triángulo
    :c: float

    :return: devuelve el area de un triángulo dado sus lados siendo estos los pasados como parámetros
    :rtype: float
    """
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def es_triangulo_valido(a: float, b: float, c: float) -> bool:
    """Valida si con los datos introducidos se puede haceer un triángulo
    :a: lado a del triángulo
    :a: float
    :b: lado b del triángulo
    :b: float
    :c: lado c del triángulo
    :c: float

    :return: devuelve un booleano que informa si se puede hacer un triángulo válido con los lados siendo estos los pasados como parámetros
    :rtype: bool
    """
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True


def volumen_prisma_rectangular(ancho: float, fondo: float, altura: float) -> float:
    """Calcula el volúmen de un prisma rectangular
    :ancho: ancho del prisma rectangular
    :ancho: float
    :fondo: fondo del prisma rectangular
    :fondo: float
    :altura: altura del prisma rectangular
    :altura: float

    :return: devuelve el volúmen del prisma cuyo ancho, fondo y altura son los pasados como parámetros
    :rtype: float
    """
    base = ancho * fondo
    volumen = base * altura
    return volumen


def area_corona_circular(radio_exterior: float, radio_interior: float) -> float:
    """Calcula el area de una corona circular
    :radio_exterior: radio exterior de la corona circular
    :radio_exterior: float
    :radio_interior: radio interior de la corona circular
    :radio_interior: float

    :return: devuelve el area de la corona circular cuyos radios son los pasados como parámetros
    :rtype: float
    """
    area_exterior = math.pi * radio_exterior ** 2
    area_interior = math.pi * radio_interior ** 2
    area = area_exterior - area_interior
    return area