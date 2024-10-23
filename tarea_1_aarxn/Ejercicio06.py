# Usando ciclos, calcula el promedio de sólamente los números positivos de la siguiente lista.

lista = [ 20, 50, -12, 6, -60, -5, 8, -14, 80, 90, -56, 50 ]

positive = []

for i in lista:
    if i > 0:
        positive.append(i)

result = sum(positive) / len(positive)

print(result)