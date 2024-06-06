# Exercise 4: Palindrome Checker
# Write a program that prompts the user to enter a word and checks if it is
# a palindrome. A palindrome is a word that reads the same backward as
# forward. Use string slicing and an if-else statement to compare the
# original word with its reverse.

word = input("Please enter an word - ")
word_1 = word[::-1]
if word == word_1:
    print("Your word is a palindrome ! ")
else: print("Your word is not a palindrome")
    