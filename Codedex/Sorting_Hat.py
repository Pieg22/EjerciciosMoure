#Sorting Hat program.

#Do the first question with both possibles answers #Below here we will put all the questions --> 

#First Question
Answer1_1 = "Dawn"
Answer2_1 = "Dusk"
Question1 = input("Do you like Dawn or Dusk?")

#Second Question
Answer1_2 = "The Good"
Answer2_2 = "The Great"
Answer3_2 = "The Wise"
Answer4_2 = "The Bold"
Question2 = input(f"When I'm dead, I want people to remember me as:({Answer1_2}/{Answer2_2}/{Answer3_2}/{Answer4_2}) ?")

#Third Question
Answer1_3 = "The violin"
Answer2_3 = "The trumpet"
Answer3_3 = "The piano" 
Answer3_4 = "The drum" 
Question3 = input(f"Wich kind of instrument most pleases your ear? ({Answer1_3}/{Answer2_3}/{Answer3_3}/{Answer3_4}):")

#Now we need to make the values of the choices . But first I need to create de variables of the houses and scores. 
#Houses :
House1 = "Gryffindor" 
House2 = "Ravenclaw"
House3 = "Hufflepuff"
House4 = "Slytherin"

#Scores: Maybe I can do a list with the diferent scores directly with the answers 
total_score = 0

#Values of the choices
if Question1 == Answer1_1:
    sum(1)
