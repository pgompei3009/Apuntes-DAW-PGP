from datos import get_empleados

empleados = get_empleados()
veces_por_empleado = {}
anho = 2023

for e in empleados:
    veces_por_empleado[e.nombre] = 0
    for v in e.empleado_del_mes:
        if v.year == anho:
            veces_por_empleado[e.nombre] += 1

lista_empleados = list(veces_por_empleado.keys())
lista_premios = list(veces_por_empleado.values())

max_veces = max(lista_premios)
print(f'{lista_empleados[lista_premios.index(max_veces)]} - {max_veces}')