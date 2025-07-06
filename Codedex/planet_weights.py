#🧑‍🚀 Planet Weights

#So we need to calculate the weight of the user on the destiny planet .
#Asks the user what their Earth weight is (as a float).
#Asks the user for a planet number (as an int).
#Maybe we can make a dictionary of all planets with the value of relative gravity 
#Exercice bases is with if/elif/else . after the input of the destiny the fuction can search on the dictionary the key(planet) for calculate the total weight. 
# 1 create dictionary 2 engage the dictionary wiht conditions  . Calculation : destination weight = Earth weight x relative gravity

# Dicts of planets , similar to {   name : { position: , gravity : }}

planets = {
    "Mercury" : {"Number" : 1 , "Gravity": 0.38} ,
     "Venus" : {"Number": 2 , "Gravity": 0.91} ,
     "Mars" : {"Number": 3 , "Gravity" : 0.38} ,
     "Jupiter" : { "Number": 4 , "Gravity" : 2.53} ,
     "Saturn" : {"Number": 5 , "Gravity" : 1.07} ,
     "Uranus" : {"Number": 6 , "Gravity" : 0.89} ,
     "Neptune" : {"Number" : 7 , "Gravity" : 1.14} 
}

#First Question
earth_weight = float(input("How much do you weight ? "))
#Second Question 
print(f"Information planets :{planets}")
destination_planet = int(input("Write the planet destiny  here : ")) 

#Conditions 
#if destination_planet == 1 :
    

