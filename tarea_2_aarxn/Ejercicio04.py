# Crea dos matrices de 3x3 con números enteros aleatorios y realiza las operaciones de suma, resta y multiplicación de matrices.

import numpy as np

m1 = np.random.randint(0, 10, size=(3, 3))
m2 = np.random.randint(0, 10, size=(3, 3))

sum = m1 + m2
rest = m1 - m2
mult = np.dot(m1,m2)
print(f"Las matrices son: \n {m1} \n y \n {m2}")
print(f"La suma es: \n {sum}")
print(f"La resta es: \n {rest}")
print(f"La multiplicación es: \n {mult}")