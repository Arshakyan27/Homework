# Random Password Generator:
# ○ Write a function that generates a random password for the user. Allow the user to
# specify the length and complexity of the password (include letters, numbers, and
# symbols).
# Ogtvel random u string module-neric (string.ascii_letters,
# string.digits,string.punctuation, )
import random
import string
def password_creator(lenght,complexity):
    
    if lenght < 8:
        print("The length should be equal or greater than 8: ")
        return ""
    
    else:
        if complexity == "hard":
            result = (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
        elif complexity == "medium":
            result = (string.ascii_letters + string.digits)
        elif complexity == "easy":
            result = (string.digits)
    return "".join(random.choices(result,k = lenght))
            
print(password_creator(12,"easy"))

# if hard symbols true letters true numbers True
# if medium symbols true ltters True
# if easy symb false letters false numbe true