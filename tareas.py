tareas = []


tareas.insert(0, {"nombre": "Estudiar"})
tareas.insert(1, {"nombre": "Limpiar"})
tareas.insert(2, {"nombre": "Ordenar"})


if tareas:
    tarea_eliminada = tareas.pop()
    print(f"Tarea eliminada: {tarea_eliminada['nombre']}")
else:
    print("No hay tareas para eliminar.")


if not tareas:
    print("No hay tareas disponibles.")
else:
    print("Lista de tareas:")
    for tarea in tareas:
        print(f"Nombre: {tarea['nombre']}")
