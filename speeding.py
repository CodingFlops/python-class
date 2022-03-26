bday = input("is it your bday? ").lower()
if bday == "yes":
    Bday = True
else:
    Bday = False
speed = int(input("enter a number "))
if speed <= 60:
    print("You were not caught speeding you have to pay no ticket")
elif speed > 60 and speed <= 80:
    print("You were caught speeding you have to pay a small ticket $10")
elif speed > 80 and Bday == True:
    if speed > 85:
        print("You were caught speeding you have to pay a big ticket $25")
    else:
        print("Yay! It is your b-day! FREE PASS")
elif speed > 80 and Bday == False:
    print ("You were caught speeding you have to pay a big ticket $25")
