# Inicializamos un arreglo bidimensional para almacenar nombres y calificaciones
datos = []

# Capturamos los datos de 5 estudiantes
for i in range(5):
    nombre = input("Ingrese el nombre del estudiante {}: ".format(i + 1))
    
    # Capturamos 3 calificaciones
    calificaciones = []
    for j in range(3):
        calificacion = float(input("Ingrese la calificación {}: ".format(j + 1)))
        calificaciones.append(calificacion)
    
    # Agregamos el nombre y las calificaciones como una lista a la lista principal
    datos.append([nombre] + calificaciones)

# Procesamos y mostramos el promedio de cada estudiante
print("\nPromedios de los estudiantes:")
for estudiante in datos:
    nombre = estudiante[0]
    promedio = sum(estudiante[1:]) / 3
    print("El promedio de {} es: {:.2f}".format(nombre, promedio))




