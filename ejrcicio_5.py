def main():
    vendedores = 3
    zonas = 4

    # Crear matriz para almacenar datos
    ventas = []

    print("Ingrese la cantidad de computadores vendidos por cada vendedor en cada zona:")

    for i in range(vendedores):
        fila = []
        for j in range(zonas):
            valor = int(input(f"Vendedor {i+1}, Zona {j+1}: "))
            fila.append(valor)
        ventas.append(fila)

    # a) Zona con más computadores vendidos (suma por columna)
    suma_zonas = []
    for j in range(zonas):
        suma_col = sum(ventas[i][j] for i in range(vendedores))
        suma_zonas.append(suma_col)
    max_ventas_zona = max(suma_zonas)
    zona_max = suma_zonas.index(max_ventas_zona) + 1

    # b) Vendedor que menos computadores vendió (suma por fila)
    suma_vendedores = []
    for i in range(vendedores):
        suma_fila = sum(ventas[i])
        suma_vendedores.append(suma_fila)
    min_ventas_vendedor = min(suma_vendedores)
    vendedor_min = suma_vendedores.index(min_ventas_vendedor) + 1

    # c) Cantidad total vendida
    total_ventas = sum(suma_vendedores)

    # Mostrar resultados
    print(f"\nZona con más computadores vendidos: Zona {zona_max} con {max_ventas_zona} ventas.")
    print(f"Vendedor que menos computadores vendió: Vendedor {vendedor_min} con {min_ventas_vendedor} ventas.")
    print(f"Cantidad total de computadores vendidos por todos los vendedores en todas las zonas: {total_ventas}")

if __name__ == '__main__':
    main()
