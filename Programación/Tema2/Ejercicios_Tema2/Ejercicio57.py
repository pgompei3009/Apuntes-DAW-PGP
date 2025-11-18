def tabla(n: int) -> int:
    for i in range(0, 11, 1):
        print(f"{n} x {i} = {n*i}")


for n in range(1, 11, 1):
    tabla(n)