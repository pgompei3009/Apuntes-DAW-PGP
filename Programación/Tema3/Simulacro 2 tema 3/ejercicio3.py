pokemones = [
   ["Pikachu", ["Eléctrico"]],
   ["Charmander", ["Fuego"]],
   ["Bulbasaur", ["Planta", "Veneno"]],
   ["Squirtle", ["Agua"]],
   ["Gengar", ["Fantasma", "Veneno"]],
   ["Onix", ["Roca", "Tierra"]],
   ["Machamp", ["Lucha"]],
   ["Zapdos", ["Eléctrico", "Volador"]],
   ["Dragonite", ["Dragón", "Volador"]],
   ["Eevee", ["Normal"]]
]

print('Pokemones tipo eléctrico:')
print(pokemon[0] for pokemon in pokemones if pokemon[1][0] == "Eléctrico")

print('Pokemones tipo eléctrico y otros:')
for pokemon in pokemones:
    if "Eléctrico" in pokemon[1] and len(pokemon[1]) > 1:
        print(f'\t {pokemon[0]}')