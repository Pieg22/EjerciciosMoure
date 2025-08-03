##Modulos

# 1. Crea un mÃ³dulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos nÃºmeros. Importa este mÃ³dulo en otro archivo y usa sus funciones.

def calculadora(a, b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# 2. Crea un mÃ³dulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este mÃ³dulo y realice conversiones.     

def convert_F(F):
    Farenheit_to_Celsius = (F - 32) * (5/9)
    result_convertFarenheit = Farenheit_to_Celsius
    return result_convertFarenheit
def convert_C(C):
    Celsius_to_Farenheit = (C + 9) / 5 + 32
    result_convertCelsius = Celsius_to_Farenheit
    return result_convertCelsius

# 3. Crea un mÃ³dulo que contenga una lista de nombres de estudiantes y una funciÃ³n que imprima todos los nombres. Importa este mÃ³dulo en otro archivo y usa la funciÃ³n para mostrar la lista.

def impresion_alumnado():             #We do not add parameters because we make the list inside of the fuction            
   name_alums = ["Leandro", "Maik" , "Kontrol" , "Moure" , "El chico que habla xino"]     #The list of names
   print(name_alums)                                       #Here is just a order to do in the fuction 
 
# 4. Crea un mÃ³dulo llamado "geometry" que tenga una funciÃ³n para calcular el Ã¡rea de un cÃ­rculo y un cuadrado. Usa este mÃ³dulo en otro archivo para calcular Ã¡reas.
#Para calcular el area de un circulo es  , pi * r2  , and for the square , we need to do side x side = S2

def geometry_circulo(radio):
    import math
    circle = math.pi * (radio**2)
    return circle
def geometry_square(side1,side2):
    square = side1 * side2
    return square
   
# 5. Escribe un mÃ³dulo que contenga una funciÃ³n que acepte cualquier nÃºmero de argumentos y devuelva su suma. Importa y usa la funciÃ³n en otro archivo.

def suma_general(*numbers):  #if I do not remeber wrong , the * is the key for accept a lot of arguments 
    alotof_numbers = sum (numbers )
    return alotof_numbers
    

# 6. Crea un mÃ³dulo que defina una clase llamada "Car" con propiedades como marca, modelo y aÃ±o. Importa este mÃ³dulo en otro archivo y crea una instancia de la clase "Car".

class Car :
    def __init__(self , brand , model , year):
        self.brand = brand
        self.model = model
        self.year = year
      
        

# 7. Escribe un mÃ³dulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.
#texto1.py
def read_file(filename): #Here is the point where , we suppose introduce the txt file
    with open(filename,'r') as file :  #use 'r' for read 
        return file.read()
    
def writte_file(filename, content):
    with open(filename, 'w') as file :
        file.write(content)
    


# 8. Crea un mÃ³dulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de nÃºmeros. Usa este mÃ³dulo para calcular estos valores en una lista dada.
#We will use here : statistics.mean ( para el promedio ) y statistics.median() para la mediana( valor central) . 
lista_numbers = [1,2,2,3,4,5,5,7,7,8,8,8,9]
def statistics ():
    import statistics
    calculo_average = statistics.mean(lista_numbers)
    calculo_median = statistics.median(lista_numbers)
    print(f"La media es {calculo_average} y la mediana {calculo_median}")

statistics()    

   
# 9. Crea un mÃ³dulo que contenga una funciÃ³n para contar cuÃ¡ntas veces aparece una palabra en un texto. Escribe un programa que importe el mÃ³dulo y lo use para contar palabras en una cadena.
#Here we can use .count() , it accept 2 optional parameters ofc  count(<sub>[, <start>[, <end>]]) . 
def contador(wordd):
    palabra = wordd.count("me")
    return palabra
    
# 10 Crea un mÃ³dulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este mÃ³dulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas especÃ­ficas.
#We will work with module of datatime  , following we make a variable wich value will be datetime.datetime.now() 
import datetime
def dates():
 date_And_Time_Actual = datetime.datetime.now()  #es un objeto especial de Python que contiene información detallada sobre el año, mes, día, hora, minuto, segundo e incluso microsegundo.           
 print(date_And_Time_Actual)
 if date_And_Time_Actual                                              #Here we obtain the actual date n time ! 
#Okay now we have the sketch real time . And now we must do the little calculation of , (now and future) , and( now and past) , (now and 4 dimension? ) XD 
# So , future is actual is sum(+), and past is substract(-) , I'm not sure , I need looking for some philosophy explanation of time  . But I guess is on this way . 
    

