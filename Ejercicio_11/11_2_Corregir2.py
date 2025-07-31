def es_par (numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def sumar_pares(lista):
    suma = 0
    for n in lista:
        if es_par(n):
         suma += n
    return suma

cantidad = int(input("¿Cuántos números deseas ingresar?: "))

numeros = []

for i in range(cantidad):
    num = int(input("Ingresa un número: "))
    numeros.append(num)

resultado = sumar_pares(numeros)
print(f"La suma de los pares es: {resultado}")


#Arreglo de sintaxis y defenicion de variable