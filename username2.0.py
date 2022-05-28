usrnm = input("Enter your username ").upper()
if len(usrnm) < 6:
    print("USENAME INVALID")
elif "_" not in usrnm:
    print("USENAME INVALID")
else:
    if "_S" in usrnm:
        print("You are a student")
        if "01" in usrnm:
            print("You are in grade 1")
        if "02" in usrnm:
            print("You are in grade 2")
        if "03" in usrnm:
            print("You are in grade 3")
        if "04" in usrnm:
            print("You are in grade 4")
        if "05" in usrnm:
            print("You are in grade 5")
        if "06" in usrnm:
            print("You are in grade 6")
        if "07" in usrnm:
            print("You are in grade 7")
        if "08" in usrnm:
            print("You are in grade 8")
        if "09" in usrnm:
            print("You are in grade 9")
        if "10" in usrnm:
            print("You are in grade 10")
        if "11" in usrnm:
            print("You are in grade 11")
        if "12" in usrnm:
            print("You are in grade 12")
    else:
        print("You are staff")
    print(usrnm[2:-2])
    if "_S" in usrnm:
        print("You are a student")
    elif "_A" in usrnm:
        print("You are a admin")
    else:
        print("You are a teacher")
