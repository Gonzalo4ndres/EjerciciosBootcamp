def calculadora():
    print("Calculadora en Python")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elige una opción (1/2/3/4): ")

    if opcion in ('1', '2', '3', '4'):
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            resultado = num1 + num2
            print(f"La suma es: {resultado}")
        elif opcion == '2':
            resultado = num1 - num2
            print(f"La resta es: {resultado}")
        elif opcion == '3':
            resultado = num1 * num2
            print(f"La multiplicación es: {resultado}")
        elif opcion == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"La división es: {resultado}")
            else:
                print("Error: No se puede dividir por cero.")
    else:
        print("Opción no válida. Intenta de nuevo.")

calculadora()