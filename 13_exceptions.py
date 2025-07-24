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

# 6. Crea una funciÃ³n que intente acceder a un elemento de una lista por Ã­ndice. Usa try-except para manejar el caso donde el Ã­ndice estÃ© fuera de rango.
#So first we need to make the list ofc . 2 : we need to make the access to this list with the Index . 3: Make the try and exception for detect when the index is out of range . Now how I do this ? lol . 

    theList = [1,2,3,4,5]
def access():
    indice = int(input("For wich element do you looking for ?  "))
    return theList[indice]  # Aquí está la clave! Accedes al elemento por índice

    
    
try: 
   result = access() # Llama a la función y captura su resultado
   print(f"The element at the given index is: {result}") # Imprime el resultado si no hay error 
    
except IndexError :
    print("This list just have 0 to 4 elements to acces It ")  #Explota cuando pide un elemento no existente en la lista 


# 7. Crea una funciÃ³n que use try-except para manejar mÃºltiples excepciones: ZeroDivisionError, ValueError y TypeError.
#Make a simply calculation , no te motives ! 

def diferent_calculo():
    un_calculo = 10*2
    print(un_calculo)
   
   
try :
    result = diferent_calculo()
except ZeroDivisionError :
    print("Error : Denominator 0")
except ValueError : 
    print("The value is not correct")
except TypeError : 
    print("The type of data is incorrect")

# 8. Crea una funciÃ³n que simule una transacciÃ³n. Lanza una excepciÃ³n personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.
class InsufficientFundsError(Exception):
    
    def __init__(self,message="Insufficient funds"):
        super().__init__(message)  
     
        
def transaccion(balance,retirada):
    retirada = 5
    balance =  10
    if balance < retirada :
        raise InsufficientFundsError(" Your balance is lower than your demand")
    elif balance >= retirada:
        print("Extracting money...")
        existencial = balance - retirada
        print(f"you have {existencial} money left")
try:
    transaccion(balance= 10,retirada= 5)
except InsufficientFundsError as e: 
    raise InsufficientFundsError(" Your balance is lower than your demand")





    
    

       

    
     


    
    





# 9. Crea una funciÃ³n que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.

# 10. Crea una funciÃ³n que calcule la raÃ­z cuadrada de un nÃºmero. Lanza un ValueError si el nÃºmero es negativo.
                                    
       



    





