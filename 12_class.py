#Clases#

# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un mÃ©todo "make_sound" que imprima un sonido genÃ©rico.
# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacÃ©nala en una propiedad pÃºblica. AÃ±ade el mÃ©todo "make_sound" que imprima un sonido dependiendo de la especie.
class Animal :
    def __init__(self,species): #Constructor + parameters ( Also it is a metod / fuction)
        self.species = species             # Atributo
                                        # PROBLEMA 1: El constructor recibe un parámetro de más.
    def make_sound(self):               # PROBLEMA 2: El método no usa la especie para decidir el sonido.    
        print("Sonido animal")
    
perro = Animal( "mamifero","Guau miau") # PROBLEMA 3: La forma de crear el objeto y llamar al método es incorrecta.
print(perro.make_sound) # Esto no ejecuta el método, solo lo referencia.

#Correction : 
class Animal:
    # 1. El constructor solo recibe 'species', como pide el enunciado.
    def __init__(self, species):
        self.species = species

    # 2. El método USA la propiedad 'self.species' para tomar una decisión.
    def make_sound(self):
        if self.species == "dog":
            print("Guau")
        elif self.species == "cat":
            print("Miau")
        else:
            print("Sonido animal genérico")
   


# 3. Crea una clase llamada "Car" con las propiedades pÃºblicas "brand" y "model". AdemÃ¡s, debe tener una propiedad privada "_speed" que inicialmente serÃ¡ 0.
# 4. AÃ±ade a la clase "Car" un mÃ©todo llamado "accelerate" que aumente la velocidad en 10 unidades. AÃ±ade tambiÃ©n un mÃ©todo "brake" que reduzca la velocidad en 10 unidades. AsegÃºrate de que la velocidad no sea negativa.
class Car:
    def __init__(self,brand,model):    # Fuction/metod + constructor + parameters 
        self.speed = speed            # Atributo
        # PROBLEMA 1: La variable 'speed' no existe aquí. Dará un error.
        # Además, debía ser una propiedad privada (_speed) e inicializada a 0.
        self.brand = brand
        self.model = model
    def velocity(self):              #metod
        self.accelerate = speed + 10        #atributo 
        # No modifica 'self.speed'. Lee la variable 'speed' global.
    def brake(self):                  #metod/fuction
        # PROBLEMA 4: Esto crea un nuevo atributo 'self.brake', no frena.
        self.brake = speed - 10
        # PROBLEMA 5: Un número (como 'speed') no tiene un método '.min()'.
        # Esto es sintaxis incorrecta y dará un error.
        speed.max(0)     
       

# PROBLEMA 6: 'speed' es una variable global. Cada coche debería tener su propia velocidad.
speed = 0                          #Object

#Correction : 
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # Correcto: La velocidad es un atributo DEL OBJETO (self) y se inicializa a 0.
        # Usa guion bajo para la convención de "privado".
        self._speed = 0

    def accelerate(self):
        # Correcto: Modifica el atributo de velocidad DEL PROPIO OBJETO.
        self._speed += 10

    def brake(self):
        # Correcto: Modifica el atributo de velocidad DEL PROPIO OBJETO
        # y usa max() para asegurar que no baje de 0.
        self._speed = max(0, self._speed - 10)



# 5. Crea una clase "Book" que tenga propiedades como "title" (pÃºblico) y "author" (privado). AÃ±ade un mÃ©todo para obtener el autor y otro para cambiar el tÃ­tulo del libro.
class Book :
    def __init__(self, title, author):
        self.title = title 
        self._author = author
    def obtain_author(self):
        return self._author
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
        return sum(self.notes) / len(self.notes)

        
# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". AÃ±ade mÃ©todos para depositar y retirar dinero, asegurÃ¡ndote de que no se pueda retirar mÃ¡s de lo que hay en la cuenta.
class BankAccount :
    def __init__(self, owner , balance):
        self.owner = owner
        self.balance = balance
    def insert_money(self,amount):
        self.balance += amount
    def with_draw_money(self,amount):
        self.balance -= amount 
        if self.balance <=  0 :
            print("Insufficient balance")
        
    

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
     




        


        
        


  



        
        

        
    
        
        
        
        
