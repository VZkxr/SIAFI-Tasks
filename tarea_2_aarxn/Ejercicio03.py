# Dado un array de 10 elementos, selecciona los valores que son mayores a 5. Reemplaza los valores mayores a 8 por 0.

import numpy as np
import random

arr0 = []

for i in range(10):
  number = random.randint(1,10)
  arr0.append(number)

arr1 = np.array(arr0)
print(f"El array es: {arr1}")

arr2 = []
for j in arr1:
  if 5 < j:
    arr2.append(j)
for k in range(len(arr2)):
  if arr2[k] > 8:
    arr2[k] = 0

print(f"Entonces el array nuevo es: {arr2}")