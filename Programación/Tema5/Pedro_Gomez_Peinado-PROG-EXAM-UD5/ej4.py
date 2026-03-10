from datos import get_productos


productos = get_productos()

reporte_cantidad = {}
reporte_precios = {}

for p in productos:
    for c in p.categorias:
        if c not in reporte_cantidad:
            reporte_cantidad[c] = 1
            reporte_precios[c] = p.precio
        else:
            reporte_cantidad[c] += 1
            reporte_precios[c] += p.precio

for cat, num in reporte_cantidad.items():
    reporte_precios[cat] /= num
    reporte_precios[cat] = round(reporte_precios[cat], 2)

for cat, num in reporte_cantidad.items():
    print(f'{cat} -- Número productos: {num} -- Precio medio: {reporte_precios[cat]}€')