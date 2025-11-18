nota = int(input("Introduce tu nota: "))

if nota < 60:
    print("Tienes una F")
elif nota >= 60 and nota <= 69:
    print("Tienes una D")
elif nota >= 70 and nota <= 79:
    print("Tienes una C")
elif nota >= 80 and nota <= 89:
    print("Tienes una B")
elif nota >= 90 and nota <= 100:
    print("Tienes una A")