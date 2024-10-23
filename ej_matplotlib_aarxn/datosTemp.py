import matplotlib.pyplot as plt

# Datos de temperaturas diarias
data_temperaturas = {
    'Día': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'],
    'Ciudad_A': [22, 24, 23, 25, 26]
}

# Gráfico de barras
plt.bar(data_temperaturas['Día'], data_temperaturas['Ciudad_A'], color='red')
plt.xlabel('Día')
plt.ylabel('Temperatura (°C)')
plt.title('Temperaturas en Ciudad_A')
plt.show()