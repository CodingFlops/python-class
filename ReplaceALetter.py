word = input("Write a word ")
number = int(input("Write a number "))
def replace(string, index):
    print(string[:index - 1] + "-" + string[index:])
replace(word, number)
