# Type Conversion:
# Write a function that prompts the user to enter a number and tries to convert it to an
# integer. Handle the TypeError exception by printing a message indicating that the input
# is not a valid number. Use a finally block to print "Type conversion process completed."

import math
def convert_to_int(inputed):
    try:
        return math.floor(inputed)
        
    except ValueError :
        print("The input should be a number")
print(convert_to_int(1233.5))