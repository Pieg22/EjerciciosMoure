#Empezamos aquí con los operadores 

## 1. Realiza las siguientes operaciones aritmÃ©ticas:
suma = 15+15
resta = 50-22
Multi = 8*7 
Division = 100/20
print(suma, resta, Multi, Division)

# 2. Calcula el resto de la divisiÃ³n de 37 entre 5 y almacÃ©nalo en una variable remainder. Luego imprÃ­melo.

remainder = 37%5 
print(remainder)

# 3. Convierte el nÃºmero 7 en una cadena de texto y concatÃ©nalo con la frase â€œ es mi nÃºmero favoritoâ€. Imprime el resultado.

print("Este es mi número favorito " + str(7))

# 4. Repite la palabra â€œPythonâ€ 10 veces usando el operador de multiplicaciÃ³n para cadenas y luego imprÃ­mela.

print("Hola"*10) 

# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si A es mayor que B y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.
        
a = 12
b = 8 

resultado = a > b

print(resultado)

# 6. Compara dos cadenas de texto (â€œappleâ€ y â€œbananaâ€) usando los operadores > y < y explica cuÃ¡l tiene mayor orden alfabÃ©tico.

comparación = ("apples" < "bannanas")
comparación_1 = ("apples" > "bannanas")

print(comparación, comparación_1)

# definición por posición alfabética ; A=1 P=16 P=16 L=11 E=4 S=19  . B=2 A=1 N=13 N=13 A=1 N=13 A=1 S=19 . Bannana win's .

# 7. Realiza una comparaciÃ³n lÃ³gica usando and para verificar si el nÃºmero 10 es mayor que 5 y menor que 20. Imprime el resultado.

print ( 10>5 and 10<20)

# 8. Usa el operador or para verificar si el nÃºmero 7 es menor que 3 o mayor que 5. Imprime el resultado.

print(7<3 or 7>5)

# 9. Aplica el operador not para invertir el resultado de la comparaciÃ³n 15 > 20. Â¿CuÃ¡l es el resultado?

print(not(15>20)) #True 

# 10. Combina operadores aritmÃ©ticos y lÃ³gicos: Verifica si el nÃºmero resultante de la expresiÃ³n (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.

calculo = 5*3
print ( int(calculo) +2 > 10 and int(calculo) < 20 )

