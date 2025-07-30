#numero = int(input("Ingresa tu numero :"))
#numero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


limite = int(input('Hasta que numero quieres jugar FizzBuzz :'))

numero = range(1,limite + 115)#agrega uno para que corte 

for numero in numero:
    
     if numero % 3 == 0 and numero % 5 == 0:
       print("Fizzbuzz")
     elif numero % 3 == 0:
       print("Fizz")
    
     elif numero % 5 == 0:
       print("Buzz")

     else:
       print(numero) 
