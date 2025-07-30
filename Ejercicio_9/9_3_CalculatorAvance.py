def addmultiplenumbers(numbers):
  return sum(numbers)

def multiplymultiplenumbers(numbers):
  resultado = 1
  for num in numbers:
    resultado *= num
  return resultado

def isiteven(num):
  return isinstance(num, int) and num % 2 == 0

def isitaninteger(num):
  return isinstance(num, int) or (isinstance(num, float) and num.is_integer())


def main():
    print("Bienvenido a la Calculadora Avanzada\n")
    print("Opciones disponibles:")
    print("1. Sumar varios números")
    print("2. Multiplicar varios números")
    print("3. Verificar si un número es par")
    print("4. Verificar si un número es entero")

    opcion = input("Elige una opción (1/2/3/4): ")

    if opcion == "1":
        entrada = input("Escribe los números separados por coma (ej: 1,2,3): ")
        numeros = [float(n) for n in entrada.split(",")]
        resultado = addmultiplenumbers(numeros)
        print(f"La suma es: {resultado}")

    elif opcion == "2":
        entrada = input("Escribe los números separados por coma (ej: 2,3,4): ")
        numeros = [float(n) for n in entrada.split(",")]
        resultado = multiplymultiplenumbers(numeros)
        print(f"El producto es: {resultado}")

    elif opcion == "3":
        num = float(input("Ingresa un número: "))
        print(f"¿Es par? {isiteven(num)}")

    elif opcion == "4":
        num = float(input("Ingresa un número: "))
        print(f"¿Es entero? {isitaninteger(num)}")

    else:
        print("Opción no válida.")

if __name__=="__main__":
  main()