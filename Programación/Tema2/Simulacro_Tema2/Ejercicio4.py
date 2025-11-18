def conversion(nota: str) -> str:
    match nota:
        case "DO":
            notaAnglo = "C"
        case "RE":
            notaAnglo = "D"
        case "MI":
            notaAnglo = "E"
        case "FA":
            notaAnglo = "F"
        case "SOL":
            notaAnglo = "G"
        case "LA":
            notaAnglo = "A"
        case "SI":    
            notaAnglo = "B"

    return notaAnglo

while True:
    nota = input("Inserta una nota: ")
    if nota == "fin":
        break
    notaAnglo = conversion(nota)
    print(f"{nota} en notación anglosajona es: {notaAnglo}")