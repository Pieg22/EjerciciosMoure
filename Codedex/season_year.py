#🗓️ Seasons of the Year

month = int(input("Wich month is it? "))

if month >= 1 and month <= 3: 
    print("Winter 🌨️")
elif month >= 4 and month <= 6:
    print("Spring 🌱")
elif month >= 7 and month <= 9:
    print("Summer 🌻")
elif month >= 10 and month <= 12 :
    print("Autumn 🍂")
else:
    print("Invalid")
