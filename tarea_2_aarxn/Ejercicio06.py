# Crea un dataframe con las columnas nombre, edad y ciudad para 5 personas (ponle los datos que desees).
# Añade una nueva columna llamada ocupación con los valores de tu elección.

import pandas as pd

data = {'Nombre':['Samuel', 'Yael', 'Alan', 'Paulina', 'Sandra'],
        'Edad':['20', '21', '21', '20', '26'],
        'Ciudad':['Estado de México', 'CDMX', 'CDMX', 'Chihuahua', 'Colima']}

col = {'Ocupación':['Abogado', 'Actuario', 'Biblotecario', 'Quant', 'Analista de datos']}
df = pd.DataFrame(data)

df['Ocupación'] = col['Ocupación']
print(df)