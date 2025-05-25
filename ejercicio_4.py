# Programa para trabajar con una matriz de hasta 15 valores totales (filas x columnas)

def main():
    print("La matriz debe tener un total de valores máximo de 15 (filas * columnas ≤ 15).")
    n = int(input("Ingrese el número de filas (1-9): "))
    m = int(input("Ingrese el número de columnas (1-9): "))

    # Validar que n y m estén en el rango y el total de valores sea máximo 15
    if n < 1 or n >= 10 or m < 1 or m >= 10:
        print("Los valores de filas y columnas deben ser positivos y menores que 10.")
        return
    if n * m > 15:
        print(f"La cantidad total de valores (filas * columnas) no debe superar 15. Usted ingresó {n * m}.")
        return

    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            valor = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
            fila.append(valor)
        matriz.append(fila)

    print("\nSuma de cada fila:")
    for i in range(n):
        suma_fila = sum(matriz[i])
        print(f"Suma de la fila {i+1}: {suma_fila}")

    print("\nPromedio de cada columna:")
    for j in range(m):
        suma_columna = sum(matriz[i][j] for i in range(n))
        promedio_columna = suma_columna / n
        print(f"Promedio de la columna {j+1}: {promedio_columna:.2f}")

    mayor_valor = matriz[0][0]
    fila_mayor = 0
    columna_mayor = 0
    for i in range(n):
        for j in range(m):
            if matriz[i][j] > mayor_valor:
                mayor_valor = matriz[i][j]
                fila_mayor = i
                columna_mayor = j
    print(f"\nEl mayor valor en la matriz es {mayor_valor} en la posición ({fila_mayor + 1}, {columna_mayor + 1})")

main()

