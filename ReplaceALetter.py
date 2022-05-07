word = input("Write a word ")
number = int(input("Write a number "))
def replace(string, index):
    stringList = list(string)
    stringList.pop(index - 1)
    stringList.insert(index - 1, "-")
    newString = "".join(stringList)
    return newString
print(replace(word, number))