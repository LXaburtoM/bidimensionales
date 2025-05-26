
encabezados = ["Tienda/Mes", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


tabla_ventas = [
    ["ABSA 1", 50000, 60000, 65000, 62000, 78000, 95000],
    ["ABSA 2", 89000, 90000, 98000, 80000, 85000, 90000],
    ["ABSA 3", 65000, 72000, 85000, 72000, 83000, 98000],
    ["ABSA 4", 92000, 88000, 90000, 76000, 82000, 93000]
]


print("Estado de cuenta de las Sucursales ABSA en el segundo semestre 2022")
print("-" * 80)


for encabezado in encabezados:
    print(f"{encabezado:<12}", end="")
print()


for fila in tabla_ventas:
    for valor in fila:
        print(f"{str(valor):<12}", end="")
    print()
