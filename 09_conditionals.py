##Condiciones de la life , si o no ofc .
# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.
import random
numero = random.randint(-10, 10)

if numero >= 0.1: 
    print("Es positivo")
elif numero <= -0.1:
    print("Is negative")
else :
    print("Es cero")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.
edad = input("Que edad tienes?")
number =  int(edad)

if number >= 18:
    print("You are adult")
elif number < 18:
    print("You are young") 
else:
    print("You do not exist")

# 3. Escribe un programa que verifique si una cadena de texto estÃ¡ vacÃ­a y muestre un mensaje en consecuencia.
cadena = "Esto no esta vacío"
if not cadena  :
    print("Esto esta vacío")
elif cadena  :
    print("This is not empty") 

    
# 4. Crea un programa que solicite dos nÃºmeros al usuario y compare cuÃ¡l es mayor. Si son iguales, muestra un mensaje indicando la igualdad.

dime1 = input("Write one number : ")
dime2 = input("Tell me another number : ")

if dime1 > dime2 :
    print(f"{dime1} es mayor que {dime2}")
elif dime1 == dime2:
    print(f"{dime1} is equal to {dime2}")
elif dime1 < dime2 :
    print(f"{dime1} is lower than {dime2}")

# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo. 
import random 
numero_div = random.randint(1 , 15)

if numero_div % 3 == 0 and numero_div % 5 == 0 :
    print(f"{numero_div} is divisible of three and five")
elif numero_div % 3 != 0 and numero_div % 5 != 0 : 
    print(f"This {numero_div} is not divisible for both numbers")



