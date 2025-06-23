#Diccionarios 

# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.

my_dic = {
    "name" : "Pieg", 
    "age": 31, 
    "country": "Spain",
}

print(my_dic)

# 2. Accede al valor de la clave name en el diccionario. 

my_dic["name"]

# 3. AÃ±ade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
my_dic["job"] = "Programador"

print(my_dic)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
my_dic["age"] = 38 

print(my_dic)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del my_dic["country"]
print(my_dic)

# 6. Crea un diccionario donde las claves sean nÃºmeros del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
num_dic = {
    1: 1,
    2: 4,
    3:9,
    4:16,
    5:25,   
}

# Correction : 
#squares = {x: x**2 for x in range(1, 6)}
#print(squares)

# 7. Verifica si la clave age estÃ¡ presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.

moure_dic = {"name": "Brais", "age": 37, "country": "Galicia"}

print("age" in moure_dic)  #True ofc 

# 8. Imprime solo las claves del diccionario. 

print(moure_dic.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
transform = list(moure_dic.keys()) 
print(transform)

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".

claves = ["name", "age", "job"] #Make the list

new_keys = dict.fromkeys(claves) #This is the transformation of list to dict . I think 
# Una vez tenemos la transformación creada , Now we must declare the value of the key's
new_values = new_keys.fromkeys(claves, "Unknow"  ) 
print(new_values) 

#Correction 
# my_keys = ["name", "age", "job"]
#my_new_dict = dict.fromkeys(my_keys, "Desconocido") #Aquí ya esta transformando la lsita a un diccionario y añadiendo sus valores .
#Por lo que mi paso de new_keys = dict.fromkeys(claves) me lo podría ahorrar . 
 
 #print(my_new_dict)

 









