def cuenta_palabras(txt: str) -> dict[str, int]:
    textoDividido = txt.lower().split()
    cuentaPalabras = {}
    for pal in textoDividido:
        if pal not in cuentaPalabras:
            cuentaPalabras[pal] = textoDividido.count(pal)

    return cuentaPalabras   

texto = input('Escribe un texto:\n')

cuentaPalabras = cuenta_palabras(texto)
print('Frecuencia de palabras:')
for palabra, frecuencia in cuentaPalabras.item():
    print(f'{palabra}: {frecuencia}')