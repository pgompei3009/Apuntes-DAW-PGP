def factorial(num: int) -> int:
    for i in range(1, num, 1):
        num *= i
    print(num)

num = int(input("Dame un número para hacer su factorial: "))
factorial(num)