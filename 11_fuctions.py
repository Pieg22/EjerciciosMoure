##Fuctions##

# 1. Crea una funciÃ³n llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningÃºn nombre, debe saludar diciendo "Hola, desconocido".

def personalized_greeting(name="unkown"):
    print(f"Hola , {name}")

   
        


# 2. Escribe una funciÃ³n llamada "multiply" que reciba dos nÃºmeros como argumentos y retorne el resultado de multiplicarlos.

def multiply(number_one, number_two) :

    print(number_one * number_two)       #def multiply(a, b):
                                         #return a * b , easy peasy! 

multiply(5, 18)

# 3. Crea una funciÃ³n llamada "is_even" que reciba un nÃºmero entero como argumento y retorne True si es par y False si es impar.

def is_even(number): 
   return number % 2 == 0

# 4. Escribe una funciÃ³n llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayÃºsculas.
def convert_to_uppercase(str):  #It must be convert_to_uppercase(text) , is non recomendable use ! Because str is a fundamental data , and It can make problems ! 
    return str.upper()          

# 5. Crea una funciÃ³n llamada "arbitrary_sum" que reciba un nÃºmero arbitrario de nÃºmeros como argumentos y retorne la suma de todos ellos.
#def arbitrary_sum(a,b):   #Esta mal , ya que he limitado la operación a dos números y no es lo que pide el ejercicio ofc.
    sum = a + b
    return  sum
#Correction : 
def arbitrary_sum(*numbers): # De esta manera el parámetro *numbers  puede recibir un número variable de argumentos.The key on this exercice is on the * (*argument) . 
    return sum(numbers)      # sum() will sum all the elements in *numbers 


# 6. Escribe una funciÃ³n llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.

def generate_full_greeting(name, surname):
    return (f"Hola , {name} {surname}")

# 7. Crea una funciÃ³n llamada "power" que reciba dos nÃºmeros: base y exponente, y retorne el resultado de elevar la base al exponente.

def power(base, exponent):
    return base ** exponent 

# 8. Escribe una funciÃ³n llamada "calculate_average" que reciba tres nÃºmeros y retorne su promedio.

def calculate_average(a, b, c):
    calculate = a+b+c
    average = calculate/3
    return average 
#Short mod of do this : return (a + b + c) / 3


# 9. Crea una funciÃ³n llamada "count_characters" que reciba una cadena de texto y retorne el nÃºmero de caracteres que contiene.

def count_characters(str):
    return str.count()

# 10. Escribe una funciÃ³n llamada "display_messages" que reciba un nÃºmero indefinido de cadenas y las imprima en mayÃºsculas, una por una, tal como se hizo en el archivo proporcionado.

def display_messages(*message):
    for messages in message : 
        print(messages(str.upper)) # print(message.upper()) Correction ofc. 

   
    





    



