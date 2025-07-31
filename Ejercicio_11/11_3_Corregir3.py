def contar_mayores_100(lista_numeros):
    contador = 0
    for numero in lista_numeros:
        if numero > 100:
            contador = contador + 1
    return contador

cantidad = int(input("¿Cuántos números vas a ingresar?"))

lista_numero = []

for i in range(cantidad):
    numero = int(input("Ingresa un número: "))
    lista_numero.append(numero)

resultado = contar_mayores_100(lista_numero)

print(f"Cantidad de números mayores que 100: {resultado}")

#Correcion de sintaxis - creacion de lista - formato en la salida 