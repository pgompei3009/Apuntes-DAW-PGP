from ej1 import Cuenta, CuentaAhorro, CuentaCorriente


cc1 = CuentaCorriente('Ana López', 'ES001', 500.0, 300.0)
cc2 = CuentaCorriente('Carlos Ruiz', '0ES002', 100.0, 200.0)
ca1 = CuentaAhorro('Marta Gómez', 'ES003', 1000.0, 2.5)
ca2 = CuentaAhorro('Luis Torres', 'ES004', 2500.0, 3.0)

print('=== ESTADO INICIAL ===')
print(cc1)
print(cc2)
print(ca1)
print(ca2)

print('\n=== INGRESOS (200€ para Ana y 500€ para Marta) ===')
CuentaCorriente.ingresar(cc1, 200)
CuentaCorriente.ingresar(ca1, 500)
print(cc1)
print(ca1)

print('\n=== RETURADAS (250€ para Carlos y 2000€ para Marta) ===')
print('Retirada cc2 (250): ', CuentaCorriente.retirar(cc2, 250))
print('Retirada ca1 (2000): ', CuentaAhorro.retirar(ca1, 2000))
print(cc2)
print(ca1)

print('\n=== INTERESES ===')
CuentaAhorro.aplicar_intereses(ca2)
print(ca2)

print('\n=== COBRO COMISION ===')   
CuentaCorriente.cobrar_comision(cc1)
CuentaCorriente.cobrar_comision(cc2)
print(cc1)
print(ca1)

print('\n=== COMPROBAR IGUALDAD Y HASH ===')
print('Para == creamos una cuenta corriente con mismo número que cc1 pero datos distintos')
cc1_duplicada = CuentaCorriente('iljhdia', 'ES001', 13, 5)
print('cc1 == cc1_duplicada: ', cc1 == cc1_duplicada)
print('Creamos un set con ambas cuentas (debería haber solo una)')
listacosa = [cc1, cc1_duplicada]
setcosa = set(listacosa)
print('Número de cuentas en set: ', len(setcosa))