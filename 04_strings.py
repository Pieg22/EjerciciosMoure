# 1. Declara una variable text con la frase â€œAprendiendo Pythonâ€ y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(len(text))  # Esto nos imrpime la longitud del contenido, con el espacio incluyed. 

# 2. Concatena dos cadenas: â€œHolaâ€ y â€œPythonâ€, y muestra el resultado en una sola lÃ­nea.
print(" Hola " + " Python ")
# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.
print("Las mentorias \nson lo mejor")
# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name, surname , age =  "Pere" , "Bercero Trigell" , 31
# Interpreto que me pide .format o % 
print("Mi nombre es %s %s y tengo %d años " %(name,surname,age))
#O como la corrección indica
print(f"Mi nombre es  {name} {surname} y tengo {age} años ")
# 5. Desempaqueta los caracteres de la palabra â€œPythonâ€ en variables separadas y luego imprÃ­melos uno por uno. 
print(len("Pyhton")) # Contamos los caracteres que tiene la palabra . 

palabra = "Python"
a , b , c , d , e , f  = palabra 

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un â€œsliceâ€ de la palabra â€œProgramaciÃ³nâ€ para obtener los caracteres desde la posiciÃ³n 3 hasta la 7. 

palabra2 = "Programación" 

palabra_slice = palabra2 [3:8] #[3:7]This only prints "gram", we want to print "grama"
print(palabra_slice)

# 7. Invierte la cadena â€œPythonâ€ usando slicing y muestra el resultado.

reversed_language = palabra[::-1]
print(reversed_language)
 
# 8. Convierte la cadena â€œaprendiendo pythonâ€ en mayÃºsculas usando el mÃ©todo adecuado e imprÃ­mela.

cadena = "aprendiendo python"
print(cadena.upper()) 

# 9. Cuenta cuÃ¡ntas veces aparece la letra â€œnâ€ en la cadena â€œProgramaciÃ³n en Pythonâ€.

print(palabra .count("n"))
print(palabra2 .count("n")) 

# 10. Verifica si la cadena â€œ12345â€ es numÃ©rica usando el mÃ©todo adecuado e imprime el resultado.

cadena_n = "12345"
print (cadena_n.isnumeric())










