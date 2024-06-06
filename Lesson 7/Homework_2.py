# Count all letters, digits, and special symbols from a given string


word = "bAAdn/6722e"
digit = 0
symb = 0
lett = 0
for x in word:
    if x.isdigit():
        digit += 1
    elif 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122:
        lett += 1
    else: symb += 1
        
print("digit = ",digit,"lett = ",lett,"symbols = ",symb)