#homework 7The program prompts the user their birth year. Assuming a person’s age
#is a non-negative integer not exceeding 120, output the user’s age or the
#words “Incorrect Year”. The sample outputs assume it’s currently the year
#2016. If you are writing this program during any other year, the correct
#answers may differ. Store the value of the current year in a variable.


current_year = 2024
birth_year = int(input("enter your birth year - "))
age = current_year - birth_year

if  birth_year > current_year:
  print("incorrect year" )
elif birth_year < 0:
    print("year cannot be negative ")
    
elif age > 120:
    print("year cannot be greater than 120")          
else: 
    print ("your age is equal - ",age)
    