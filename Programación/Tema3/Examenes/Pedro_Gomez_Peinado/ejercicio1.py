nombres = ["Cuarzo", "Pirita", "Hematita", "Galena", "Fluorita", "Calcita", "Magnetita", "Malaquita", "Obsidiana", "Apatito"]
pesos = [2.65, 5.02, 5.26, 7.6, 3.18, 2.71, 5.17, 3.9, 2.4, 3.2]
es_magnetico = [False, False, False, False, False, False, True, False, False, False]

print(f'Los minerales cuyo nombre tiene 7 o menos letras y que NO acaban con la letra a son: {[nombre for nombre in nombres if len(nombre) <= 7 and nombre[-1] != 'a']}')

pesoMedio = sum(pesos)/len(pesos)

print(f'Los minerales no magnéticos cuyo peso es superior a la media son: {[nombre for nombre in nombres if pesos[nombres.index(nombre)] > pesoMedio and es_magnetico[nombres.index(nombre)] == False]}')