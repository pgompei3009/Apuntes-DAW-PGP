from datos import get_datos, get_datos_competencia


datos = get_datos()
datosCompetencia = get_datos_competencia()

#Apartado A
nosotros = [d.direccion[0] + ' ' + str(d.direccion[1]) + ', ' + d.direccion[2] for d in datos]
ellos = [d.direccion[0] + ' ' + str(d.direccion[1]) + ', ' + d.direccion[2] for d in datosCompetencia]

ambas = set(nosotros) & set(ellos)

print('### APARTADO A ###\nLas siguientes direcciones han pedido a ambas empresas:')

[print('\t', a) for a in ambas]

#Apartado B
reporte = {}
localidades = ['Monachil', 'Cájar', 'Huétor Vega', 'La Zubia', 'Granada']
for l in localidades:
    diferencia = 0

    for d in datos:
        if d.direccion[2] == l:
            diferencia += 1
        
    for d in datosCompetencia:
        if d.direccion[2] == l:
            diferencia -= 1

    reporte[l] = diferencia


print('### APARTADO B ###\nDiferencia de pedidos por localidad (nuestra empresa - competencia):')

for r in reporte:
    print(f'{r}: {reporte[r]}')

