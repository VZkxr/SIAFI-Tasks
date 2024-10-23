# Usando condicionales, determina la clasificación de las calificaciones de los siguientes miembros de SIAFI de acuerdo a la tabla.

dic_names = {"Yael":70, "Ilse":90, "Eduardo":80}

for i in dic_names:
    j = dic_names[i]
    if 90 < j <= 100:
        print(f"{i} está en la clasificación A")
    elif 80 < j <= 90:
        print(f"{i} está en la clasificación B")
    elif 70 < j <= 80:
        print(f"{i} está en la clasificación C")
    elif 60 < j <= 70:
        print(f"{i} está en la clasificación D")
    elif 0 < j < 60:
        print(f"{i} está en la clasificación F")
    else:
        print("Clasificación inválida")