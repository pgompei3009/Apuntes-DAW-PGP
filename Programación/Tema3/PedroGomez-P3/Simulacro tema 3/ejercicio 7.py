planetas = [
    ["Mercurio", True, 2439.7],
    ["Venus", True, 6051.8],
    ["Tierra", True, 6371.0],
    ["Marte", True, 3389.5],
    ["Júpiter", False, 69911],
    ["Saturno", False, 58232],
    ["Urano", False, 25362],
    ["Neptuno", False, 24622],
    ["Plutón", True, 1188.3]  # Incluyendo a Plutón
]

def r_medio_gas(planetas: list[list[str, bool, int]]) -> int:
    totalGas = cuentaGas = 0
    for planeta in planetas:
        if planeta[1] == False:
            totalGas += planeta[2]
            cuentaGas += 1

    return totalGas/cuentaGas

def r_medio_rock(planetas: list[list[str, bool, int]]) -> int:
    totalRock = cuentaRock = 0
    for planeta in planetas:
        if planeta[1] == True:
            totalRock += planeta[2]
            cuentaRock += 1

    return totalRock/cuentaRock

def gas_mayor_rock(planetas: list[list[str, bool, int]]) -> bool:
    gas = []
    rock = []
    for planeta in planetas:
        if planeta[1] == True:
            rock.append(planeta[2])
        else:
            gas.append(planeta[2])

    if min(gas) < max(rock):
        return True
    else:
        return False
    
def terminacion_no(planetas: list[list[str, bool, int]]) -> list[str]:
    planetasNo = []
    for planeta in planetas:
        if planeta[0][-2:] == 'no':
            planetasNo.append(planeta[0])

    return planetasNo

print(f'Radio medio gaseosos: {r_medio_gas(planetas)}\n'
      f'Radio medio rocosos: {r_medio_rock(planetas)}\n'
      f'¿Existe algún rocoso más grande que un gaseoso?: {gas_mayor_rock(planetas)}\n'
      f'Planetas terminados en "no": {terminacion_no(planetas)}')