nums = []

while True:
    num = int(input("Inserte un número: "))
    if nums.count(num) != 1:
        nums.append(num)
    
    print(f"Contenido de la lista: {nums}")