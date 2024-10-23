# Elabora una función que devuelva los primeros n números de la secuencia de Fibonacci.


def fib(x):
    x = x - 1
    list_n = [1,1]
    ran = range(1,x)
    for i in ran:
        k = list_n[i] + list_n[i - 1]
        list_n.append(k)
    print(list_n)

n = int(input("Ingrese el número: "))

if 0 <= n < 2:
    print("El estado inicial de la sucesión de Fibonacci es: ")
    fib(n)
elif n >= 2:
    print(f"Los primeros {n} números de la secuencia de Fibonacci son: ")
    fib(n)
else:
    print("Entrada no válida")