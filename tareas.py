tareas = []

while True:
    nombre_tarea = input("Ingrese el nombre de la tarea o 'x' para terminar: ")
    if nombre_tarea.lower() == "x":
        break
    nueva_tarea = {"nombre de la tarea": nombre_tarea}
    tareas.append(nueva_tarea)
    print("Tarea agregada")

if not tareas:
    print("No hay tareas disponibles.")
else:
    print("Lista de tareas:")
    for tarea in tareas:
        print(f"Nombre: {tarea['nombre']}")
