# Imprime la tabla de multiplicar de un número n.
# Pista: Usa ciclos.

n = int(input("Ingrese el número: "))
table = list(range(11))

for i in table:
    result = i * n
    print(f"{i} x {n} = {result}")