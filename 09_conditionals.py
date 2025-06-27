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
