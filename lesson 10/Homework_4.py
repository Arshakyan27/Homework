# Write a Python program that generates a random number between 1 and 100 and asks
# the user to guess the number. The program should give hints whether the guessed
# number is too high or too low until the correct number is guessed.

entered = int(input("Enter your number: "))

import random
random_number = random.randint(1, 100)
if entered == random_number:
    print("You guessed")

elif entered < random_number:
    print("The number is too low: ")
else: 
    print("The number is too high: ")
print("The random nummber was: ", random_number)
print("Your number: ", entered)
    
