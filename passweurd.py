passweurd = input("Enter a password ")
if len(passweurd) >= 8:
    pts = 5
else:
    pts = 0
punktuwtioun = False
letteur = False
neumbeur = False
LETTEUR = False
for i in range(len(passweurd)):
    if 97 <= ord(passweurd[i]) <= 122:
        letteur = True
    if 65 <= ord(passweurd[i]) <= 90:
        LETTEUR = True
    if 48 <= ord(passweurd[i]) <= 57:
        neumbeur = True
    if ord(passweurd[i]) == 33 or ord(passweurd[i]) == 63 or ord(passweurd[i]) == 59  or ord(passweurd[i]) ==  46  or ord(passweurd[i]) == 44:
        punktuwtioun = True
if neumbeur == True and letteur == True or LETTEUR == True and neumbeur == True:
    pts = pts + 10
if punktuwtioun == True:
    pts = pts + 5
if letteur == True and LETTEUR == True:
    pts = pts + 10
pts = str(pts)
print("Your password has rated " + pts + "/30")
