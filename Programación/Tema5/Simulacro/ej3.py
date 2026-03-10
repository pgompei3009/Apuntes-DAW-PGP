from datos import get_empleados
from Empleado import Empleado
from datetime import date


def f3a(empleados: list[Empleado]) -> float:
    return sum([e.sueldo for e in empleados])/len(empleados)

def f3b (empleados: list[Empleado]) -> Empleado:
    return max(empleados, key=lambda e: e.sueldo)

def f3c (empleados: list[Empleado], n: float) -> list[Empleado]:
    return [e for e in empleados if e.sueldo > n]

def f3d (empleados: list[Empleado], n: int) -> list[Empleado]:
    return [e for e in empleados if (date.today() - e.fecha_ingreso).days > n*365]

def f3e (empleados: list[Empleado]) -> Empleado:
    return min(empleados, key=lambda e: e.fecha_ingreso)

def f3f (empleados: list[Empleado]) -> list[Empleado]:
    lista_fechas = [e.fecha_ingreso for e in empleados]
    sorted(lista_fechas)
    empleados_ordenados = []

    for f in lista_fechas:
        for e in empleados:
            if e.fecha_ingreso == f:
                empleados_ordenados.append(e)
    return empleados_ordenados


def f3g (empleados: list[Empleado], anio: int) -> list[Empleado]:
    empleados_filtrados = []

    for e in empleados:
        if e.fecha_ingreso.year == anio:
            empleados_filtrados.append(e)
    return empleados_filtrados

def f3h (empleados: list[Empleado], departamento: str) -> list[Empleado]:
    empleados_filtrados = []

    for e in empleados:
        if departamento in e.departamentos:
            empleados_filtrados.append(e)
    return empleados_filtrados

def f3i (empleados: list[Empleado]) -> dict[str, int]:
    reporte = {}

    for e in empleados:
        for d in e.departamentos:
            if d in reporte:
                reporte[d] += 1
            else:
                reporte[d] = 1
    return reporte

def f3j (empleados: list[Empleado]) -> dict[str, float]:
    reporte = {}
    num_empleados_departamentos = list(f3i(empleados).values())

    for e in empleados:
        for d in e.departamentos:
            if d in reporte:
                reporte[d] += e.sueldo
            else:
                reporte[d] = e.sueldo

    for i, depart in enumerate(reporte.keys()):
        reporte[depart] /= num_empleados_departamentos[i]
    return reporte


empleados = get_empleados()


print('===== f3a Sueldo medio =====')
print(f3a(empleados))

print('\n===== f3b Sueldo más alto =====')
emple_sueldo_mayor = f3b(empleados)
print(f'{emple_sueldo_mayor.nombre} - {emple_sueldo_mayor.sueldo} €')

print('\n===== f3c Sueldos > 2000 =====')
empleados_filtrados = f3c(empleados, 2000)
[print(f'{e.nombre} - {e.sueldo} €') for e in empleados_filtrados]

print('\n===== f3d Más de 3 años en empresa =====')
empleados_filtrados = f3d(empleados, 3)
[print(f'{e.nombre} - {e.fecha_ingreso}') for e in empleados_filtrados]

print('\n===== f3e Empleado más antiguo =====')
print(f3e(empleados))

print('\n===== f3f Ordenados por antigüedad =====')
emple_ordenados = f3f(empleados)
[print(f'{e.nombre} - {e.fecha_ingreso}') for e in emple_ordenados]

print('\n===== f3g Contratados en año concreto. (2022) =====')
empleados_filtrados = f3g(empleados, 2022)
[print(f'{e.nombre} - {e.fecha_ingreso}') for e in empleados_filtrados]

print('\n===== f3h Departamento IT =====')
empleados_filtrados = f3h(empleados, 'IT')
[print(e) for e in empleados_filtrados]

print('\n===== f3i Reporte número empleados por departamento =====')
print(f3i(empleados))

print('\n===== f3j Reporte sueldo medio por departamento =====')
print(f3j(empleados))