#En este apartado empezamos con las variables ofc . 

"""1. Declara y asigna valores a las siguientes variables:
name: una cadena que contenga tu nombre.
age: un número entero que represente tu edad.
height: un número flotante que represente tu altura.
Imprime cada variable en una línea separada.
"""

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







    
    






