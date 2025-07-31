def calcular_promedio(lista_notas):
    suma = 0
    for nota in lista_notas:
        suma = suma + nota
    promedio = suma / len(lista_notas)
    return promedio

def mostrar_resultado(promedio):
    if promedio >= 4.0:
        print("El estudiante ha aprobado con un promedio de", promedio)
    else:
        print("El estudiante ha reprobado con un promedio de", promedio)

notas = []

cantidad = input("¿Cuántas notas deseas ingresar? ")

for i in range(int(cantidad)):
    nota = float(input("Ingresa una nota: "))
    notas.append(nota)


# Falta aquí una línea para calcular el promedio con la función correspondiente

mostrar_resultado(calcular_promedio(notas))

#Se agrega int en el rango y se mejora sistema de salida
