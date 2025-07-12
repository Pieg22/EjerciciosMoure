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

especie = Animal()     #This is another object ofc 
print(Animal.make_sound)

# 3. Crea una clase llamada "Car" con las propiedades pÃºblicas "brand" y "model". AdemÃ¡s, debe tener una propiedad privada "_speed" que inicialmente serÃ¡ 0.
# 4. AÃ±ade a la clase "Car" un mÃ©todo llamado "accelerate" que aumente la velocidad en 10 unidades. AÃ±ade tambiÃ©n un mÃ©todo "brake" que reduzca la velocidad en 10 unidades. AsegÃºrate de que la velocidad no sea negativa.
class Car:
    def __init__(self,brand,model):    # Fuction/metod + constructor + parameters 
        self.speed = speed             # Atributo
    def accelerate(self):
        accelerate = speed + 10 
        brake = speed - 10
    

speed = 0                              #Object
if speed < 0 :
    sum(speed + 10 )

# 5. Crea una clase "Book" que tenga propiedades como "title" (pÃºblico) y "author" (privado). AÃ±ade un mÃ©todo para obtener el autor y otro para cambiar el tÃ­tulo del libro.
class Book :
    def __init__(self, title):
        author = author
        self.title = title

        pass




        
        

        
    
        
        
        
        
