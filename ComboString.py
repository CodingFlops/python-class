word = input("Write a word ")
word2 = input("Type in a word ")
if len(word) > len(word2):
    print("your combo string is (drumroll please)... " + word2 + word + word2)
    word2 + word + word2
elif len(word) < len(word2):
    print("your combo string is (drumroll please)... " + word + word2 + word)
    later = word + word2 + word
else:
    print("ERROR")
    print("VARIBALES SAME SIZE")
print(later)
