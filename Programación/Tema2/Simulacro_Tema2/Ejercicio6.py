def multiplos(n: int, inicio: int, final: int) -> int:
    for i in range(inicio, final):
        if i%n == 0:
            print(i)

n = int(input("Introduce un número: "))
inicio = int(input("Introduce el inicio: "))
final = int(input("Introduce el final: "))

print(f"Entre {inicio} y {final} el número {n} tiene los siguientes múltiplos:")
multiplos(n, inicio, final)