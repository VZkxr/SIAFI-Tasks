# Crea una serie de 10 elementos con los números del 1 al 10.
# Cambia los índices de la serie por los nombres de los primeros 10 países según su población.

import pandas as pd

list = [1,2,3,4,5,6,7,8,9,10]
serie = pd.Series(list)

country = ["India","China","Estados Unidos", "Indonesia", "Pakistán", "Nigeria", "Brasil", "Bangladés", "Rusia", "México"]

serie = pd.Series(list, index = country)

print(serie)