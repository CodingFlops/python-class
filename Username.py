grade = input("Are you staff? ").lower()
if grade == "no":
    grade = input("What grade are you in? ")
    role = "_S"
    if len(grade) == 1:
        grade = "0" + grade
else:
    grade = "00"
    roles = input("Are you a admin? ").lower()
    if roles == "no":
        role = "_T"
    else:
        role = "_A"
first_initial = input("What is your first name? ").upper()
first_initial = first_initial[:1]
last_name = input("What is your last name? ").upper()
username = grade + first_initial + last_name + role
print("Your username is " + username)
print(username)
