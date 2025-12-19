def cuenta_palabras(txt: str) -> list[tuple[str, int]]:
    txt = txt.lower()
    textoDividido = txt.split()
    palabrasContadas = []
    for pal in textoDividido:
        cuentaPalabra = (pal, textoDividido.count(pal))
        if cuentaPalabra not in palabrasContadas:              
            palabrasContadas.append(cuentaPalabra)

    return palabrasContadas   

def imprimir_reporte(palabrasContadas: str):
    palabrasContadas = cuenta_palabras(texto_quijote)
    for palabra in palabrasContadas:
        print(f'Palabra: {palabra[0]} | nº veces: {palabra[1]}')

texto_quijote = 'En un lugar de la Mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero adarga antigua rocín flaco y galgo corredor'

imprimir_reporte(cuenta_palabras(texto_quijote))