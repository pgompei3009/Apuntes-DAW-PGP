mobs_hostiles = ["Zombie", "Skeleton", "Creeper", "Creeper", "Enderman", "Ghast", "Piglin"]
mobs_pacíficos = ["Cow", "Sheep", "Pig", "Villager", "Villager", "Enderman"]
mobs_del_Nether = ["Ghast", "Piglin", "Hoglin", "Blaze", "Piglin", "Enderman"]

print('1.')
print(f'Hostiles: {set(mobs_hostiles)}')
print(f'Pacíficos: {set(mobs_pacíficos)}')
print(f'Nether: {set(mobs_del_Nether)}\n')

print('2.')
print(f'Overworld: {set(mobs_pacíficos)|set(mobs_hostiles)}\n')

print('3.')
print(f'Pacificos Nether: {set(mobs_pacíficos)&set(mobs_del_Nether)}\n')

print('4.')
print(f'Todas las listas: {set(mobs_hostiles)&set(mobs_pacíficos)&set(mobs_del_Nether)}\n')

print('5.')
print(f'Todos los mobs: {set(mobs_hostiles)|set(mobs_pacíficos)|set(mobs_del_Nether)}\n')

print('6.')
print(f'Nether pacificos: {set(mobs_pacíficos)&set(mobs_del_Nether)}\n')

print('7.')
print(f'Hostiles: {mobs_hostiles != set(mobs_hostiles)}')
print(f'Pacíficos: {mobs_pacíficos != set(mobs_pacíficos)}')
print(f'Nether: {mobs_del_Nether != set(mobs_del_Nether)}\n')

print('8.')
print(f'No Nether: {(set(mobs_pacíficos)|set(mobs_hostiles))-set(mobs_del_Nether)}')