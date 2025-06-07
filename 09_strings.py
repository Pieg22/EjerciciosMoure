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

palabra_slice = palabra2 [2:7] #[3:7]This only prints "gram", we want to print "ogram"
print(palabra_slice)

# 7. Invierte la cadena â€œPythonâ€ usando slicing y muestra el resultado.











