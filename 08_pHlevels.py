#Create a program for checks el nivel de pH; basic , acidic or neutral .

ph = input("Que valor de pH tiene el producto?")
ph_value = float(ph) 
#Make the If <=7 for Basic
if ph_value > 7:               
    print("Basic")
if ph_value < 7:
    print("Acid")
    
else:
    print("Neutral")

