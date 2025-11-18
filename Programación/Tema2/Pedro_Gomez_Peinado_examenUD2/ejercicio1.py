palLarga = palCorta = None
totalChar = cuenta = 0

while True:
    pal = input("Inserta una cadena de texto: ")
    if pal == "fin":
        break
    
    if palLarga is None:
        palLarga = palCorta = pal

    if len(pal) > len(palLarga):
        palLarga = pal
    elif len(pal) < len(palCorta):
        palCorta = pal

    cuenta += 1
    totalChar += len(pal)

if palLarga is None:
    print("No has insertado ninguna cadena distinta de fin")
else:
    print(f"a) Número de cadenas de texto insertadas: {cuenta}")
    print(f"b)Longituf media: {totalChar/cuenta}")
    print(f"c) La cadena de texto más larga es: {palLarga}")
    print(f"d) La cadena de texto más corta es: {palCorta}")