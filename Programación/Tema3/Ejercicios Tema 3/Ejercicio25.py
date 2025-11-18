def mostrarTareas(tareas):
    for i, tarea in enumerate(tareas):
        print(f"{i+1}. {tareas[i]}")

def agregarTarea(tareas):
    nuevaTarea = input("Dame la tarea que quieres agregar: ")
    pos = int(input("Dime la posición en la que la quieres poner: "))
    tareas.insert((pos-1), nuevaTarea)
    return tareas

def completarTarea(tareas):
    completada = int(input("¿Has completado alguna tarea?: "))
    if completada > 0:
        if completada > len(tareas):
            print("La tarea no existe")
        else:
            tareas.remove(tareas[completada-1])
            print("Felicidades!!!")

    return tareas

tareas = ["Comprar fruta", "Estudiar programación", "Desinstalar el LOL"]

while True:
    print("Gestor de tareas:\n" \
          "1. Mostrar tareas\n" \
          "2. Agregar tarea\n" \
          "0. Salir")
    
    opcion = int(input("Dime que quieres hacer: "))

    match opcion:
        case 1:
            print("----------------\n" \
                  "LISTA DE TAREAS")
            mostrarTareas(tareas)
            print("----------------")
            tareas = completarTarea(tareas)
            print("----------------")

        case 2:
            tareas = agregarTarea(tareas)

        case 0:
            break