word = input("Enter your password: ")

if word == "seKr3t":
    print("Welcome!")
elif word == "":
    print("You didn't enter anything.")
else:
    print("Access denied.")

#make the string uppercase
message = input("What do you want me to say? ")
uppermessage = message.upper()
print(uppermessage, "!!!")
print(uppermessage, "!!!")
print(uppermessage, "!!!")


#Or we can reuse the same variable name:

message = input("What do you want me to say? ")
message = message.upper()
print(message, "!!!")
print(message, "!!!")
print(message, "!!!")


#Or we can convert the message to uppercase right away on the first line:
message = input("What do you want me to say? ").upper()
print(message, "!!!")
print(message, "!!!")
print(message, "!!!")

#Plaindrome

palindrome_input = input("Enter a string: ")
if palindrome_input == palindrome_input[::-1]:
    print("This string is a palindrome")
else:
    print("This string is not a palindrome")