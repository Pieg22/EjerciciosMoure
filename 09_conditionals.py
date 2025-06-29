##Condiciones de la life , si o no ofc .
# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.
import random
numero = random.randint(-10, 10)

if numero >= 0.1:               #Correction . number > 0 
    print("Es positivo")          
elif numero <= -0.1:            # number <0 
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
p1 = input("Write one number : ")
p2 = input("Tell me another number : ")      #Better like 
dime1 = int(p1)                              #number1 = int(input("Introduce el primer nÃºmero: "))
dime2 = int(p2)                              #number2 = int(input("Introduce el segundo nÃºmero: "))

if dime1 > dime2 :
    print(f"{dime1} es mayor que {dime2}")
elif dime1 == dime2:
    print(f"{dime1} is equal to {dime2}")
elif dime1 < dime2 :
    print(f"{dime1} is lower than {dime2}")
# I saw error after do the exercice and I will be : When I wrote a big number than 99 , like dime1 = 99  and dime2 = 100 , the program execute the last elif . And the error was , because I did not do the viariable 
# transforming on int().. :) So now It work on right way!

# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo. 
import random 
numero_div = random.randint(1 , 60)

if numero_div % 3 == 0 and numero_div % 5 == 0 :
    print(f"{numero_div} is divisible of three and five")
elif numero_div % 3 != 0 and numero_div % 5 != 0 : 
    print(f"This {numero_div} is not divisible for both numbers")

# 6. Solicita al usuario que ingrese un nÃºmero y verifica si es par o impar.

solicito = input( "Let me see that number : ")
numerasao = int(solicito)

if numerasao % 2 == 0 :
    print("Pair number")
elif numerasao % 2 != 0 :
    print("This is odd number")

# 7. Escribe un programa que determine si una persona puede votar en funciÃ³n de su edad(mayor o igual a 18). Si tiene 16 o 17 aÃ±os, indica que puede votar con permiso especial.
check_age = input("Cual es su edad ?")
age_confirm = int(check_age)                                    #age 

if age_confirm >= 18 :
    print("This person can vote")
elif age_confirm <= 17 and age_confirm >= 16 :                  # Interessting way elif 16 <= age < 18:
    print("This person can vote with special permission")
else:
    print("This person can not vote")

# 8. Crea un programa que solicite una contraseÃ±a al usuario y verifique si coincide con una contraseÃ±a predefinida. Si no coincide, muestra un mensaje de error.
password = "123moure456" 

introduce_pass = input("Write here your password : ")

if introduce_pass == password :
    print("Correct acces")
elif introduce_pass != password :
    print("Error : wrong password") 

# 9. Escribe un programa que determine si un nÃºmero estÃ¡ entre 10 y 20 (ambos incluidos).
#I try to avail the program of exercice 5 for this one too! We will see what happens 
#So the try was fail . why ? I must do a new variable just for this program ofc. 
import random
numerito = random.randint(1 , 30)
if numerito >= 10 and numerito <=20 :
    print(f"{numerito} is betwen teen and twenty")
elif numerito == 10 :
    print(f"{numerito} is teen")
elif numerito == 20 :
    print(f"{numerito} is twenty")
else:
    print(f"{numerito} Is not be betwen teen and twenty ")
# 10. Escribe un programa que simule un semÃ¡foro: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.

situation = input("Wich color have traffic light?(red, yellow , green) ")
rojo = "red"
amarillo = "yellow"
verde = "green"

if situation == rojo :
    print("Do not pass")
elif situation == amarillo :
    print("Be careful, watch the way out") 
elif situation == verde :
    print("You can pass")
else : 
    print("Wrong input")


