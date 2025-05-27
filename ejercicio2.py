# Inicializamos un arreglo bidimensional para almacenar nombres y calificaciones
datos = []
# Capturamos los datos de 5 estudiantes
for i in range(5):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    
    # Capturamos 3 calificaciones
    calificaciones = []
    for j in range(3):
        calificacion = float(input(f"Ingrese la calificación {j + 1}: "))
        calificaciones.append(calificacion)
    
    # Agregamos el nombre y las calificaciones como una lista a la lista principal
    datos.append([nombre] + calificaciones)
    
# Procesamos y mostramos el promedio de cada estudiante
print("\nPromedios de los estudiantes:")
for estudiante in datos:
    nombre = estudiante[0]
    promedio = sum(estudiante[1:]) / 3
    print(f"El promedio de {nombre} es: {promedio:.2f}")



