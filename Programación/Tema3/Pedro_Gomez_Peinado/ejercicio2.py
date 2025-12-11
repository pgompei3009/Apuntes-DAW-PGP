pedrolos = [
    ["Cuarzo",     2.65, False],
    ["Pirita",     5.02, False],
    ["Hematita",   5.26, False],
    ["Galena",     7.6,  False],
    ["Fluorita",   3.18, False],
    ["Calcita",    2.71, False],
    ["Magnetita",  5.17, True ],
    ["Malaquita",  3.9,  False],
    ["Obsidiana",  2.4,  False],
    ["Apatito",    3.2,  False]
]

pesoMedio = 0
for pedrolo in pedrolos:
    pesoMedio += pedrolo[1]
pesoMedio /= len(pedrolos)

pedrolosPT = []
for pedrolo in pedrolos:
    if 'p' in pedrolo[0] or 'P' in pedrolo[0]:
        if 't' in pedrolo[0] or 'T' in pedrolo[0]:
            pass
        else:
            pedrolosPT.append(pedrolo[0])
    elif 't' in pedrolo[0] or 'T' in pedrolo[0]:
        if 'p' in pedrolo[0] or 'P' in pedrolo[0]:
            pass
        else:
            pedrolosPT.append(pedrolo[0])

print(f'Apartado a): {[pedrolo[0] for pedrolo in pedrolos if len(pedrolo[0]) <= 7 and pedrolo[0][-1] != 'a']}')

print(f'Apartado b): {[pedrolo[0] for pedrolo in pedrolos if pedrolo[2] == False and pedrolo[1] > pesoMedio]}')

print(f'Apartado c): {pedrolosPT}')

print(f'Apartado d): {[pedrolo[0] for pedrolo in pedrolos if pedrolo[2] == True and len(pedrolo[0])%2 != 0]}')