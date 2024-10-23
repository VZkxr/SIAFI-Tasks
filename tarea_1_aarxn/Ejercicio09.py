# Elabora una función que devuelva si un numero es par o impar y que determine si es positivo, negativo o cero.

def arma_x(x):
    if x > 0:
        if x%2 == 0:
            print("El número es positivo y además es par")
        else:
            print("El número es positivo y además es impar")
    elif x < 0:
        if x%2 == 0:
            print("El número es negativo y además es par")
        else:
            print("El número es negativo y además es impar")
    elif x == 0:
        print("El número es igual a 0")

n = int(input("Ingrese el número: "))        
arma_x(n)