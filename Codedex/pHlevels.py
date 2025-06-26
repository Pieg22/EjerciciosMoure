#Create a program for checks el nivel de pH; basic , acidic or neutral .

ph = input("Que valor de pH tiene el producto?")
ph_value = float(ph) 
#Make the If for determinate the values wich the program runs. 
if ph_value < 0 or ph_value > 14 :               
    print("Error , the value of pH should be betwen 0 and 14")
#Now we make the points of every kind of pH 

elif ph_value < 7 :
    print("Acid")

elif ph_value == 7 :
    print("Neutral")

else: # If pH isn't < 0 , ~ > 14 , ~ < 7 , ~ == 7 . It should be > 7 and <==14 , equal to basic!
    print("Basic")
    







