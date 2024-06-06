# Write a Python program that asks the user to enter a password. Keep asking for the
# password until the correct password "secret" is entered. Provide appropriate feedback
# to the user

entered = input("Write the password: ")
if entered != "secret":
    print("The password is incorrect: ")
else:   
    print("The password is correct: ")
