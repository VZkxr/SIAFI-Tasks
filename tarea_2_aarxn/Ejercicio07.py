# Crea un dataframe con 5 ciudades y su temperatura en grados celsius.
# Añade una nueva columna que convierta las temperaturas a Fahrenheit.

import pandas as pd

def conv(c):
  f = c*1.8 + 32
  return f

city = {'Ciudad':['CDMX','Las Vegas','París','Madrid','Pekin'],
        'Temperatura (C)':[21,34,13,16,12]}

dfC = pd.DataFrame(city)

cel = city['Temperatura (C)']
far = []
for i in cel:
  k = conv(i)
  far.append(k)

far_t = {'Temperatura (F)':far}

dfC['Temperatura (F)'] = far_t['Temperatura (F)']
print(dfC)