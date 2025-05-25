#Un almacén registra la cantidad de productos en 3 categorías diferentes en 4 sucursales.
#Matriz de 3x4
#Cada fila representa una categoía
#Cada columna representa una sucursal
inventario = [
    [120, 150, 200, 180],  
    [80, 90, 100, 110],    
    [50, 60, 70, 80]
]
print("Inventario por categoría y sucursal:")
for i, fila in enumerate(inventario):
    print(f"Categoría {i + 1}: {fila}")
# Calculo del total de productos por categoría
print("\nTotal de productos por categoría: ")
for i in range(len(inventario)):
    total_cat = sum(inventario[i])
    print(f"Categoría {i + 1}: {total_cat}")
total_suc = [0] * len(inventario[0])
for columna in range(4):
    for fila in range(3):
        total_suc[columna] += inventario[fila][columna]
#Cálculo del total de productos por sucursal
print("\nTotal de productos por sucursal: ")
for i in range(len(total_suc)):
    print(f"Sucursal {i + 1}: {total_suc[i]}")
#MAyor inventario acumulado
mayor_inv = 0
for i in range(len(inventario)):
    for j in range(len(inventario[i])):
        if inventario[i][j] > mayor_inv:
            mayor_inv = inventario[i][j]
            categoria_mayor = i + 1
            sucursal_mayor = j + 1
print(f"\nMayor inventario acumulado: {mayor_inv} en Categoría {categoria_mayor}, Sucursal {sucursal_mayor}")