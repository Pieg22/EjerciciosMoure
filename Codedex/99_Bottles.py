#99 Bottles BootStrap "99 Bottles of Beer" 
#With for loop and range() we need make the complete song . 
# Text of the song : 99 bottles of beer on the wall  , 99 bottles of beer , Take one down , pass it around , 98 bottles of beer on the wall . 
#Interpolation 



for b in range(99, 0 , -1):
    print(f"{b} bottles of beer on the wall \n {b} bottles of beer \n Take one down \n pass it around \n {b-1} bottles of beer on the wall .")


