# Del archivo ventas.csv (En classroom: Clase04 Numpy y Pandas), carga el dataframe y calcula el promedio de ventas.

import pandas as pd

df = pd.read_csv('ventas.csv')

prom = df['Ventas'].mean()

print(f"El promedio de ventas es {prom}")