#homework 6  Input two positive integers, and output a line describing their relation.
#Follow the sample format.

first_int = int(input("write a positive number - "))
second_int = int(input("write a positive number - "))
if (first_int or second_int) < 0:
    print("numbers cannot be negative")
elif first_int > second_int:
    print(first_int,">",second_int)
elif first_int == second_int:
    print(first_int,"=",second_int)
else: 
    print(first_int,"<",second_int)