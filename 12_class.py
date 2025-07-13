#Clases#

# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un mÃ©todo "make_sound" que imprima un sonido genÃ©rico.
# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacÃ©nala en una propiedad pÃºblica. AÃ±ade el mÃ©todo "make_sound" que imprima un sonido dependiendo de la especie.
class Animal :
    def __init__(self,species,make_sound): #Constructor + parameters ( Also it is a metod / fuction)
        self.species = species             # Atributo
        self.make_sound = make_sound       # Atributo modificado a partir del ejercicio 2 
    def make_sound(self):                   
        print(Animal)
    
perro = Animal( "mamifero","Guau miau") #Make the object from animal clas
print(perro.make_sound)

   


# 3. Crea una clase llamada "Car" con las propiedades pÃºblicas "brand" y "model". AdemÃ¡s, debe tener una propiedad privada "_speed" que inicialmente serÃ¡ 0.
# 4. AÃ±ade a la clase "Car" un mÃ©todo llamado "accelerate" que aumente la velocidad en 10 unidades. AÃ±ade tambiÃ©n un mÃ©todo "brake" que reduzca la velocidad en 10 unidades. AsegÃºrate de que la velocidad no sea negativa.
class Car:
    def __init__(self,brand,model):    # Fuction/metod + constructor + parameters 
        self.speed = speed             # Atributo
        self.brand = brand
        self.model = model
    def velocity(self):              #metod
        self.accelerate = speed + 10        #atributo 
        self.brake = speed - 10
        speed.min(0)     
       

speed = 0                              #Object


# 5. Crea una clase "Book" que tenga propiedades como "title" (pÃºblico) y "author" (privado). AÃ±ade un mÃ©todo para obtener el autor y otro para cambiar el tÃ­tulo del libro.
class Book :
    def __init__(self, title, author):
        self.title = title 
        self.author = author
    def obtain_author(self):
        return self.author
    def change_title(self):
        new_title = input("Change the title: " )  
        self.title = new_title

    
        
        

  

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. AÃ±ade un mÃ©todo para calcular y devolver la nota media del estudiante.
class Student :
    def __init__(self, name , surname , notes):
        self.name = name
        self.surname = surname
        self.notes = notes

    def media(self):
        return self.notes / len(self.notes)

        
# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". AÃ±ade mÃ©todos para depositar y retirar dinero, asegurÃ¡ndote de que no se pueda retirar mÃ¡s de lo que hay en la cuenta.
class BankAccount :
    def __init__(self, owner , balance):
        self.owner = owner
        self.balance = balance
    def insert_money(self):
        self.insert_money
    def with_draw_money(self):
        self.with_draw_money
        max(self.balance)
    

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". AÃ±ade un mÃ©todo que calcule la distancia entre dos puntos.
class Point:
    def __init__(self,x,x1,y,y1):
        self.x = x
        self.x1 = x1
        self.y = y
        self.y1 = y1
    def distance_calculation(self,calculation):
        import math
        self.calculation = calculation
        calculation = math.sqrt((self.x1 - self.x)**2 + (self.y1 - self.y2)**2)
        print(self.calculation)

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". AÃ±ade un mÃ©todo que calcule el pago total basado en las horas trabajadas y el salario por hora.

class Employee : 
    def __init__(self,name,hourly_wage,hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
    def calculation(self,total_pay):
        self.total_pay = total_pay
        total_pay = self.hourly_wage * self.hours_worked
        print(total_pay)

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). AÃ±ade un mÃ©todo para agregar un producto al inventario y otro para mostrar todos los productos disponibles.

class Store:                 #Making the new mold
    def __init__(self):      #Fuction / metod + consctructor 
        self.inventory = []  #This is a empty list
    def add_product_to_inventory(self):          #Fuction for add product
        new_product = input("Add a new prodcut to the inventory : ")  #Introduce de name of product 
        self.inventory.append(new_product)                            # Adding the product 
        print(f"The product {new_product} has been added to inventory") #Finaly product it's in ! 
    def show_inventory_products(self):
        print(f"This is all the products : {self.inventory}")
     




        


        
        


  



        
        

        
    
        
        
        
        
