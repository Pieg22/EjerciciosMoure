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

#Now we need to make the values of the choices . But first I need to create de variables of the scores. 
#Houses :
#"Gryffindor" 
#"Ravenclaw"
#"Hufflepuff"
#"Slytherin"

#Scores: Maybe I can do a list with the diferent scores directly with the answers 
 
score_House1 = 0
score_House2 = 0
score_House3 = 0
score_House4 = 0 
total_score = score_House1 , score_House2 , score_House3 , score_House4
#Values of the choices
#First question with their values from it's answers
if Question1 == Answer1_1 : # Creo que me estoy liando mucho hahahahha
    total_score = 1 
    score_House1 = 1
    score_House2 = 1
elif Question1 == Answer2_1 : 
    total_score = 1 
    score_House3 = 1
    score_House4 = 1
#else : 
    #print("Wrong input")  # This is better wat If I put it on the first line , with the question ofc 


#Choices of second question + values 

if Question2 == Answer1_2 : 
    total_score = 2 + total_score
    score_House3 = 2 + score_House3
elif Question2 == Answer2_2 :
    total_score = 2 + total_score
    score_House4 = 2 + score_House4 
elif Question2 == Answer3_2 :
    total_score = 2 + total_score
    score_House2 = 2 + score_House2
elif Question2 == Answer4_2 :
    total_score = 2 + total_score 
    score_House1 = 2 + score_House1

# Third question

if Question3 == Answer1_3 :
    total_score = 4 + total_score
    score_House4 = 4 + score_House4 
elif Question3 == Answer2_3 :
    total_score = 4 + total_score
    score_House3 = 4 + score_House3
elif Question3 == Answer3_3 :
    total_score = 4 + total_score
    score_House2 = 4 + score_House2
elif Question3 == Answer3_4 :
    total_score = 4 + total_score
    score_House1 = 4 + score_House1

 

# Now we make the total_score depends of the houses names  . Then the winner house will be print.

score_houses = {"Gryffindor" : score_House1 , "Ravenclaw" : score_House2 , "Hufflepuff" : score_House3 , "Slytherin" : score_House4 }

# I need to make the import from the scores , who had the best score? 
# So I need the fuction max() for determinate the best one .
# Also I need call the itemgetter(1) like a fuction of operator , who help to find every element of the tupla (key ,value)

from operator import itemgetter

winner_house, total_score = max(score_houses.items(), key=itemgetter(1))

print(f"You will go to {winner_house} with {total_score} points")




