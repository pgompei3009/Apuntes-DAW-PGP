# Lista de nombres de los 8 planetas
planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

# Lista de masas (en kilogramos)
masas = [3.30e23, 4.87e24, 5.97e24, 6.42e23, 1.90e27, 5.68e26, 8.68e25, 1.02e26]

# Lista de radios (en kilómetros)
radios = [2439.7, 6051.8, 6371.0, 3389.5, 69911.0, 58232.0, 25362.0, 24622.0]

opcion = input("Dime el planeta del que quieres saber su información: ")
print(f"Posición en el Sistema Solar: {planetas.index(opcion)+1}\n"
      f"Masa del planeta {masas[planetas.index(opcion)]}\n"
      f"Radio del planeta {radios[planetas.index(opcion)]}")