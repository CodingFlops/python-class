xedni = input("Type a word ")
lant = input("Now choose your direction like this: \ (Type r) or this | (Type d) or this / (Type l) ").lower()
index = 0
space = ""
if lant == "l":
    space = " "*len(xedni)
print("Your word is " + xedni)
for i in range(len(xedni)):
    if lant == "r":
        space = space + " "
    elif lant == "l":
        space = space[:-1]
    print(space + xedni[index] + "!")
    index = index + 1
