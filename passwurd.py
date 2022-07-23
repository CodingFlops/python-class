passwurd = input("Enter a password ")
if len(passwurd) >= 8:
    pts = 5
else:
    pts = 0
a = "abcdefghijklmnopqrstuvwxyz"
b = a.upper()
one = "1234567890"
c = "!?.,;"
punktuwtioun = False
lettur = False
numbur = False
LETTUR = False
for i in range(len(a)):
    if passwurd.find(a[i]) != -1:
        lettur = True
    if passwurd.find(b[i]) != -1:
        LETTUR = True
for i in range(len(one)):
    if passwurd.find(one[i]) != -1:
        numbur = True
for i in range(len(c)):
    if passwurd.find(c[i]):
        punktuwtioun = True
if numbur == True and lettur == True or LETTUR == True and numbur == True:
    pts = pts + 10
if punktuwtioun == True:
    pts = pts + 5
if lettur == True and LETTUR == True:
    pts = pts + 10
pts = str(pts)
print("Your password has rated " + pts + "/30")
