# Elabora una función que reciba un número n y devuelva la suma de todos los números desde 1 hasta n.

def arma_x(x):
    ran = range(x)
    result = sum(ran)
    return result

n = int(input("Ingrese el número: ")) + 1
print(arma_x(n))