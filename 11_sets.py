# 1. Crea un set con los nÃºmeros del 1 al 5 e imprÃ­melo. 

my_fisrt_set = {1, 2, 3, 4, 5}

print(my_fisrt_set)
print(type(my_fisrt_set))


# 2. AÃ±ade el nÃºmero 6 al set {1, 2, 3, 4, 5} e imprÃ­melo.

my_fisrt_set.add(6)

print(my_fisrt_set)

# 3. Intenta aÃ±adir el nÃºmero 5 al set {1, 2, 3, 4, 5} nuevamente. Â¿QuÃ© sucede? 

my_fisrt_set.add(5) #It do not nothing , even no add but also It do not report a error. Just stay..

# 4. Verifica si el nÃºmero 3 estÃ¡ en el set {1, 2, 3, 4, 5} e imprime el resultado. 

if 3 in my_fisrt_set :
    print("El 3 esta en el set")

# 5. Elimina el nÃºmero 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.

my_fisrt_set.remove(4)
print(my_fisrt_set)

# 6. Usa el mÃ©todo clear() para vaciar un set y luego imprime su longitud.
my_fisrt_set.clear()
print(len(my_fisrt_set))

# 7. Convierte el set {"manzana", "naranja", "plÃ¡tano"} en una lista e imprime el primer elemento de la lista. 

fruit_set = {"manzana", "naranja", "platano"} #Make the set 
fruit_list = list(fruit_set) #Convert de set to list
#How to check It if set have not order , but list yes , so I think It works like usual list . 
print(fruit_list.pop(0))  # Wtf with same number It prints in random order . It do not care about the indication of number . 
#Un set es como un saco de canicas , 0 orden. 

