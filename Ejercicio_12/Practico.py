
def countvowels(word: str) ->int:
    vowels = 'aeiouAEIOU' 
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

def is_palindrome(word: str) ->bool:
   word = word.lower()
   reversed_word = word[::-1]
   return word == reversed_word
   
def get_positives(numbers: list[int]) -> list[int]:
    lista_numeros = []
    for number in numbers:
        if number > 0:
            lista_numeros.append(number)
    return lista_numeros

def get_negatives(numbers: list[int]) -> list[int]:
    lista_numeros = []
    for number in numbers:
        if number < 0:
            lista_numeros.append(number)
    return lista_numeros

def get_average(numbers:list[int]) -> float:
    if not numbers:
        return 0.0
    total = sum(numbers)
    cantidad = len(numbers)
    promedio = total / cantidad
    return promedio

def main():
  print("Bienvenido al desafio de funciones")
  print("Opciones disponibles:")
  print("1. Devuelve la cantidad de vocales en una palabra.")
  print("2. Devuelve si la palabra es un palíndromo.")
  print("3. Retorna una nueva lista que contiene solo números positivos")
  print("4. Retorna una lista con los números negativos.")
  print("5. Devuelve el promedio de los números.")
 
  opcion = input("Elige una opción (1/2/3/4/5):")
 
  if opcion == "1":
      palabra = input("Ingresa una palabra: ")
      print("Cantidad de vocale:",countvowels(palabra))

  if opcion == "2":
      palabra = input("Ingresa una palabra: ")
      if is_palindrome(palabra):
          print("Es un palíndromo.")
      else:
          print("No es un palíndromo.")
  if opcion == "3":
        numeros = [-3, 2, 0, 8, -1, 10]
        resultado = get_positives(numeros)
        print("Numeros positivos",resultado)
  if opcion == "4":
        numeros = [-3, 2, 0, 8, -1, 10]
        resultado = get_negatives(numeros)
        print("Numeros negativos",resultado)
  if opcion == "5":
        numeros = [10, 20, 30, 40]
        print("Promedio:", get_average(numeros))
  else :
      print("Opcion no valida.")

  main()
