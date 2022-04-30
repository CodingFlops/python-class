word = input("Write a word ")
word2 = input("Type in a word ")
if len(word) > len(word2):
    print("your combo string is (drumroll please)... " + word2 + word + word2)
else:
    print("your combo string is (drumroll please)... " + word + word2 + word)
