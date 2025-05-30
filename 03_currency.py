"""Info 
1 CO (Colombian Peso)= 0,00024 USD
1 PE (Peruvian Soles)= 0,28 USD
1 RB ( Brazilian reais)= 0,17 USD 
"""

#Ask to the user 

CO = input(" How much CO do you have ? ")
PE = input(" How PE do you left ?  ")
RB = input(" Do you have some RB? tell me the amount ")

# Intercambio de moneda COM (Colombian Peso Money)

COM = (0.00024)
PEM =( 0,28 )
RBM =( 0,17 ) 

resultCOM = COM * CO 
resultPEM = PEM * PE
resultRBM = RBM * RB

#Sum results and print in USD 

print(COM + PEM + RBM)






