#Ejercicios Hola Mundo
#Ejercicio 1
#1. Imprime "¡Hola Mundo!" por consola.
print("¡Hola Mundo!")
print("Mi nombres es Pere y tengo 31 años")

#2. Escribe un comentario de una sola línea explicando qué
# hace el siguiente código del ejercicio 1
"""
El código de el primer ejercicio imprime por consola el texto "¡Hola Mundo!" y el segundo imprime mi nombre y edad.


"""
#3. Imprime tu nombre y edad en la misma línea utilizando la
#función print.

"""4. Usa la función type() para imprimir el tipo de dato de
una cadena de texto, un número entero y un número
decimal."""

print(type("Hola"))
print(type(3))
print(type(3.0))

"""
5. Escribe un comentario en varias líneas explicando qué
son los tipos de datos en Python.
"""
"""
Los tipos de datos en Python son una forma de clasificar los diferentes tipos de valores que pueden ser almacenados y manipulados en un programa. Python tiene varios tipos de datos incorporados, incluyendo enteros (int), números de punto flotante (float), cadenas de texto (str), listas (list), tuplas (tuple), conjuntos (set) y diccionarios (dict). Cada tipo de dato tiene sus propias características y métodos asociados, lo que permite a los programadores elegir el tipo más adecuado para sus necesidades específicas. Además, Python es un lenguaje dinámicamente tipado, lo que significa que no es necesario declarar el tipo de dato de una variable al momento de su creación.
"""

"""
6. Imprime el resultado de concatenar dos cadenas de texto,
por ejemplo: "Hola" y "Mundo".
"""

p = ("Hola")
H = ("world")
print(p + H)    

#o bien : 

print("Hola" + "Mundo") 

#Con un espacio
print("Hola" + " " + "Mundo")


print("Hola" + " " + "Mundo")

"""7. Crea una variable para almacenar tu nombre, otra para tu
edad, e imprime ambas en la misma línea."""

name = "Pere"
age = 31
print("Mi nombre es " + name + " mi edad es " + str(age))

""" 8. Escribe un programa que solicite al usuario su nombre y
lo imprima junto con un saludo.
"""

nombre = input("Name:")

print( " Hola que tal " + nombre + " un saludo guapo ")

#He creado una variable "nombre" y después hemos imrpimido la variable + un print fijo . 

"""9. Usa print() para mostrar el resultado de la suma de dos
números enteros y el tipo de dato resultante. 
""" 

print( 12 + 12 )
print(type(12+12))
#Moure hizo : 

result = 5 + 10
print("El resultado es:", result)
print("El tipo de dato del resultado es:", type(result))


"""10. Comenta el código del Ejercicio 9, y explica qué
hace cada línea usando comentarios de una sola línea. 
"""

# El print( 12 + 12 ) imprime el calculo de la suma , el + opera la suma entre los dos enteros . Print(type(12+12) nos dice que tipo de dato es esa suma.
#Initials codedex
print("PPPP    BBBB")
print("P    P  B    B")
print("P    P  B    B")
print("PPPP    BBBB")
print("P       B     B")
print("P       B     B") 
print("P       B BBBB")


















