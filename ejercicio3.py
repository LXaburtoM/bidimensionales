#Programa que permita la linealizacion de un arreglo bidimensional por columnas
#Los datos del arreglo bidimensional serán tomados de la tabla
matriz = [
    [120, 150, 180],
    [200, 250, 300],
    [400, 450, 500]
]
print("Matriz original:")
for fila in matriz:
    print(fila)
# Linealizar la matriz por columnas
linealizado = []
filas = len(matriz)
columnas = len(matriz[0])
for col in range(columnas):
    for fila in range(filas):
        linealizado.append(matriz[fila][col])
print("\nMatriz linealizada por columnas:")
print(linealizado)