# 11. Function Exercise:
# Write a function that checks if a given string is a valid email address.

def valid_email(email):
    if email.count('@') != 1:
        return False
    first,domain = email.split('@')
    
    if not first or not domain:
        return False
    
    if domain.count('.') != 1:
        return False
    
    return True
print(valid_email("Serob@mail.ru"))