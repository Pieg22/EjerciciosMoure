##Fuctions##

# 1. Crea una funciÃ³n llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningÃºn nombre, debe saludar diciendo "Hola, desconocido".

def personalized_greeting(name):
    if name :
        print(f"Hola {name}")
    
    elif not name :
        print("Hola , desconocido") 
        
personalized_greeting("Pere")

# 2. Escribe una funciÃ³n llamada "multiply" que reciba dos nÃºmeros como argumentos y retorne el resultado de multiplicarlos.

def multiply(number_one, number_two) :

    print(number_one * number_two)

multiply(5, 18)

# 3. Crea una funciÃ³n llamada "is_even" que reciba un nÃºmero entero como argumento y retorne True si es par y False si es impar.

