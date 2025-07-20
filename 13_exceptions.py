##Excepciones##

# 1. Crea una funciÃ³n que intente dividir dos nÃºmeros proporcionados por el usuario. Usa try-except para capturar cualquier error de divisiÃ³n (por ejemplo, divisiÃ³n por cero).
número_1 = int(input("Un número por aquí: " ))
número_2 = int(input("Otro número por aca: " )) 
try : 
    division = número_1 / número_2  
    print(f"El resutlado es {division}")
except :
    número_2 == 0
    print("It's impossible make divisions with denominator 0 ")  
finally: 
    print("I hope your results are help")


# 2. Crea una funciÃ³n que tome una cadena e intente convertirla en un nÃºmero entero. Usa try-except para capturar cualquier error en la conversiÃ³n.
#And what error can be in write a int or str :hyperthink:

try:
    my_cadena = int(input("Write something : "))
    print(" You wrote a integer number ofc")
except :
      
    print("Error : You did not wrote a number")

# 3. Crea una funciÃ³n que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.
#Archivo can be a dict/list or tupla . Maybe . Then We will make a fuction for open It . After open It we need to work with try-except for manage the stock of folders .

archivo = {"Folder1":"Pepe"} 
try:
     print("Folder1" in archivo)
    
except : 
    print("It can't show to you the folder ")

# 4. Crea una funciÃ³n que realice mÃºltiples operaciones (suma, resta, divisiÃ³n, multiplicaciÃ³n) con dos nÃºmeros. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.
# So .. we can use the conditionals to do the calculations . Then ask 2 numbers . print the result . try with calculations - except for division/0  - else : Se ejecuta si no se produce una excepción - finally : print something . 
ask = int(input("Write a number : "))
ask2 = int(input("Write another number : "))

try : 
    sum = ask + ask2
    rest = ask - ask2
    divison1 = ask / ask2
    multi = ask * ask2
    print(f"The sum is {sum} , rest is {rest} , the division is {divison1} and multiplication is {multi}")
except ZeroDivisionError: 
    ask2 == 0
    print(f"{ask2} is not possible make division with this denominator ")
    print(f"The sum is {sum} , rest is {rest} , the division Non-viable and multiplication is 0")
else : 
    print("All good")

finally : 
    print("I hope it will works well ahhahaha") 

# 5. Crea una funciÃ³n que le pida al usuario su edad y lance un ValueError si la entrada no es un nÃºmero entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.



try : 
    askAge = input("Write here your age please : " )  # Ask the age 
    age = int(askAge)      
    if age < 0 :
        raise ValueError ("The number can't be negative")                
except ValueError as age :   
    print(f"Error:{age}. Introduce a positive number please")
else:
    print(f"You have {age} years old" )
                                    
       



    





