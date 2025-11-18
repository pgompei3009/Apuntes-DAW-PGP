dinero = int(input("Dime la cantidad de dinero que quieres sacaer: "))
b50 = dinero//50
b20 = (dinero-b50)//20
b10 = (dinero-b50-b20)//10
b5 = (dinero-b50-b20-b10)//5

print(f"Toma {b50} billetes de 50, {b20} billetes de 20, {b10} billetes de 10, {b5}, billetes de 5")