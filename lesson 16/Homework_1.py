# String Length Checker
# Write a function that checks the length of a string provided by the user. Handle the
# TypeError by raising a custom exception if the input is not a string.
def lenght_checker(inputed):

    if  not isinstance(inputed,str):
        raise  TypeError("You must input a string")
    else:
        return len(inputed)
            
print(lenght_checker(651))