"""Info 
1 CO (Colombian Peso)= 0,00024 USD
1 PE (Peruvian Soles)= 0,28 USD
1 RB ( Brazilian reais)= 0,17 USD 
"""

#Ask to the user 

CO_str = input(" How much CO do you have ? ")
PE_str = input(" How PE do you left ?  ")
RB_str = input(" Do you have some RB? tell me the amount ")

#Transform the str to floats , because we need to calculate It later 

CO = float(CO_str)
PE = float(PE_str)
RB = float(RB_str)

# Intercambio de moneda CO_M (Colombian Peso Money)

CO_M = 0.00024
PE_M = 0.28 
RB_M = 0.17  

#Calculates 

result_COM = CO_M * CO 
result_PEM = PE_M * PE
result_RBM = RB_M * RB

#Sum results and print in USD 

print("Do you have : ", result_COM + result_PEM + result_RBM ,"USD")






