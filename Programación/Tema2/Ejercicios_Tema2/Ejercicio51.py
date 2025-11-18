import math

def longitud_circunferencia(radio: float) -> float: 
    longitud = math.pi*radio**2
    print("La longitud de la circunferencia es:", longitud)

longitud_circunferencia(8.5)