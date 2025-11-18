liga = ["Real Madrid", "Atlético de Madrid", "FC Barcelona", "Athletic Club",  "Villarreal CF", "RCD Mallorca", "Rayo Vallecano", "Girona FC", "Real Sociedad", "Real Betis", "CA Osasuna", "Sevilla FC", "RC Celta", "Getafe CF", "UD Las Palmas", "CD Leganés", "Deportivo Alavés", "RCD Espanyol", "Valencia CF", "Real Valladolid"]

try:
    equipo = input("Dime el equipo del que quieres saber la posición: ")
except Exception as error:
    print("El equipo no está dentro de la lista...")
else:
    print(f"La posición del equipo {equipo} es la nº{liga.index(equipo)+1}")

"""
Tambien se puede utilizar if liga.count(equipo) == 0 -> No existe
"""