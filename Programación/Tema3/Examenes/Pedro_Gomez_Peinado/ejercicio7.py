minerales_magneticos = ["Magnetita", "Hematita", "Pirita", "Ilmenita", "Cobaltoita"]
minerales_metalicos  = ["Pirita", "Galena", "Hematita", "Bornita", "Calcopirita", "Cobaltoita"]
minerales_no_metalicos = ["Cuarzo", "Calcita", "Fluorita", "Pirita", "Yeso", "Malaquita"]

metalMagnet = set(minerales_magneticos) & set(minerales_metalicos)
otrosNoMetal = (set(minerales_magneticos) | set(minerales_no_metalicos)) - set(minerales_metalicos)

#1
print(f'1. Metálicos y magnéticos: {metalMagnet}')

#2
print(f'2. No metálicos: {otrosNoMetal}')