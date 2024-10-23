# Elabora una calculadora usando funciones con las siguientes operaciones matemáticas.

def suma(a,b):
    x = a + b
    return x

def resta(a,b):
    x = a - b
    return x

def multi(a,b):
    x = a * b
    return x

def div(a,b):
    x = a / b
    return x

op = int(input("""
           1. Suma
           2. Resta
           3. Multiplicación
           4. División
           
           Elija la operación a realizar: """))

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if op == 1:
    result = suma(a,b)
    print(f"El resultado de la suma es: {result}")
elif op == 2:
    result = resta(a,b)
    print(f"El resultado de la resta es: {result}")
elif op == 3:
    result = multi(a,b)
    print(f"El resultado de la multiplicación es: {result}")
elif op == 4:
    try:
        result = div(a,b)
        print(f"El resultado de la división es: {result}")
    except:
        print("No se puede dividir entre 0")
else:
    print("Elección de operación inválida")