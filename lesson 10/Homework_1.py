# Write a Python program that prompts the user to enter a positive integer and then prints
# all the numbers from 1 to that number using a while loop

entered = int(input("Please enter a number: "))
y = 0
while y < entered:
    print(y)
    y += 1