#Exercice from modules 
#convertir temperaturas entre Celsius y Fahrenheit
def converter(c,f):
    CtoF = c + 9 / 5 + 32
    FtoC = f - 32 * 5 / 9 
    return CtoF , FtoC
