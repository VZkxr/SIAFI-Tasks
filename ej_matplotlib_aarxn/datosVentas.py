import matplotlib.pyplot as plt

# Datos de ventas mensuales
data_ventas = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Producto_A': [1500, 1800, 1700, 1900, 2200, 2100],
    'Producto_B': [2000, 2100, 2300, 2000, 1900, 2100],
    'Producto_C': [2300, 3000, 3200, 2600, 2700, 2900]
}

# Hagan un gráfico de líneas :D

plt.plot(data_ventas['Mes'], data_ventas['Producto_A'], label='Producto A', marker='o')
plt.plot(data_ventas['Mes'], data_ventas['Producto_B'], label='Producto B', marker='o')
plt.plot(data_ventas['Mes'], data_ventas['Producto_C'], label='Producto C', marker='o')

plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.title('Ventas Mensuales por Producto')
plt.legend()
plt.grid(True)
plt.show()
