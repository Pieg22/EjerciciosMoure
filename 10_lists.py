#I start with lists 

# 1. Crea una lista con los nÃºmeros del 1 al 5 e imprÃ­mela.
numeric_list = [1,2,3,4,5]
print(numeric_list)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50]. 
la_lista = [10,20,30,40,50]

print(la_lista.pop(3))

# 3. Agrega el nÃºmero 6 al final de la lista [1, 2, 3, 4, 5] e imprÃ­mela.
numeric_list.append(6)
print(numeric_list)

# 4. Inserta el nÃºmero 15 en la posiciÃ³n 2 de la lista [10, 20, 30, 40, 50]. 
la_lista.insert(2 , 15)
print(la_lista)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
la2_lista = [10,20,30,30,40,50]
la2_lista.remove(30)
print(la2_lista)

# 6. Usa la funciÃ³n pop() para eliminar el Ãºltimo elemento de la lista [1, 2, 3, 4, 5] y almacÃ©nalo en una variable. Imprime la variable y la lista.
#On point 3 , I did .append to incluyed n6 on the list . So now I should remove 5 and 6 , or format the list. Ok , en .pop just accept 1 argument not 2!
la3_lista = [1,2,3,4,5]
elimination = la3_lista.pop()
print(elimination)
print(la3_lista)
# 7. Invierte la lista [100, 200, 300, 400, 500] e imprÃ­mela.
big = [100, 200, 300, 400, 500]
big.reverse()
print(big)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprÃ­mela.

disorder = [3,1,4,2,5]
disorder.sort()
print(disorder)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
unodostres = [1,2,3]
cuatrocincoseis = [4,5,6]

longlist = [unodostres, cuatrocincoseis]
print(longlist)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posiciÃ³n 1 hasta la 3 (sin incluir la posiciÃ³n 3).