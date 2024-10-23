# Usando condicionales, determina si un número es mayor, menor o igual a cero.

a = int(input("Introduce el número: "))
cero = 0

if a == cero:
    print("El número es igual a cero")
elif a < cero:
    print("El número es menor a cero")
else:
    print("El número es mayor a cero")