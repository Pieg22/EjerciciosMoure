#En este apartado empezamos con las variables ofc . 

"""1. Declara y asigna valores a las siguientes variables:
name: una cadena que contenga tu nombre.
age: un número entero que represente tu edad.
height: un número flotante que represente tu altura.
Imprime cada variable en una línea separada.
"""

import math


name = "Pere"
age = 31
height = 1,80

print(name)
print(age)
print(height)

"""2. Convierte la variable edad de entero a cadena y
concatenala con un texto que diga cuántos años tienes.

"""
age = "31"
print(" Tengo " + age + " años ")

"""3. Declara una variable booleana is_student que indique si
eres estudiante o no. Usa True o False según corresponda
e imprímela.
"""

is_student = input("Eres estudiante?")
print(is_student)

if is_student == "yes" : 
    print("Si es estudiante")
elif is_student == "no" : 
    print("No es estudiante")

else:
    print("Respuesta no válida.Introduce yes or no . ")
    
#Con este último me he flipado , pero no quería hacerlo tan basic . sorry

"""4. Usa la funciÃ³n len() para calcular cuÃ¡ntos caracteres tiene tu nombre completo, almacenado en una variable."""

nombre = len("PereBerceroTrigell")
print(nombre)


"""5. Declara tres variables en una sola lÃ­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores."""
#Esto de imprimir las variables en la misma línea , creo que dijo moure que no era la mejor práctica . pero...

name , second_name , city = "Pere" , "Bercero" , "Sentmenat"
print(name , second_name , city)

"""# 6. Usa la funciÃ³n input() para solicitar al usuario su color favorito y almacÃ©nalo en una variable color. Luego, imprime el valor ingresado."""

color = input("Cual es tu color favorito?") 

print(color)

#Pequeño pharenseis of codedex , for calculate de conversation of F to Celsius ofc . 

# Write code below 💖
t_actual = 74
#celsius?
celsius = t_actual - 32
result = celsius / 1.8
print(result) 

# Lo podría haber hecho todo en la misma línea ofc  : like : 
#celsisus+result= (t_actual - 32) / 1.8

#Calculando el Body Mass Index de locos , BMI = mass(kg)/highm2. 

mass = 65 #kg
height = 1,80 #meters
result = 1.80**2 

bmi = mass/result

print(bmi)

#Creando pythagoras en python 


ask_a = int(input(" Introduce valor de A "))
print(ask_a)

ask_b = int(input(" Introduce value of B "))
print(ask_b)

c = (ask_a**2 + ask_b**2)

result = (c**0.5)

print(result)

#Bonus: If you are looking for a harder challenge, try the Quadratic formula! 


a = int(input(" Introduce valor de A "))
print(a)

b = int(input(" Introduce value of B "))
print(b)

c= int(input(" Introduce value of C"))
print(c)


x1 = (-b +(b*b - 4*a*c)**0.5) /(2 * a)  

print(x1) 

x2 = (-b -(b*b - 4*a*c)**0.5) /(2 * a)  

print(x2)

# 7. Declara una variable fruit e inicialÃ­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.

fruit = 5  #este es int
print(fruit)

fruit = "Manzana" #Este es 'str'

print(fruit)

# 8. Convierte un nÃºmero decimal, almacenado en la variable price, a un nÃºmero entero y luego imprÃ­melo.

price = 20.96 #Float 

print(int(price))

## 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direcciÃ³n usando la funciÃ³n len(). Imprime el resultado.

address_len = len("Calle de las perras")
print(address_len)

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurÃ¡ndote de que siempre serÃ¡ un nÃºmero. Luego, cambia su valor a un nÃºmero diferente y verifica el tipo de la variable con type().

phone = 223 
phone = 588
print(type(phone))






    
    






