something = "Python"

if something == "Python":
    print("Python is an interpreted, high-level, general-purpose programming language.")
elif something == "bug":
    print("A bug is a a common term for an error, flaw or fault in a computer program.")
else:
    print("I don't know what", something, "means.")

#ask a word and print
word = input("Enter a word: ")
print(word * 1000)


#add a space to the word before we print it.
word = input("Enter a word: ")
word += " "
print(word * 1000)

#We can also add the space right away on the first line:

word = input("Enter a word: ") + " "
print(word * 1000)


#this has lot more spaces so we can do something like this instead:
no_space = input("Enter a word: ")
yes_space = no_space + " "
print(yes_space*999 + no_space)


 





