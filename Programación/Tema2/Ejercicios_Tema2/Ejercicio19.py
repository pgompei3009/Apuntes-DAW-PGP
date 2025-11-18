año = int(input("Dime un año y te diré el siglo: "))

if año < 1000:
    print(f"El año {año} está en el siglo 1")
elif año%1 == 0:
    print(f"El año {año} está en el siglo {int((año/100)//1)}")
else:
    print(f"El año {año} está en el siglo {int(((año/100)//1)+1)}")