# Write a program to check if two strings are balanced. For example, strings s1 and
# s2 are balanced if all the characters in the s1 are present in s2. The character’s
# position doesn’t matter

wo_1 = "skj"
wo_2 = "voske"
jim = True
 
for x in wo_1:
    if x not in wo_2:
        jim = False
if jim == True:
    print("True")
else: print("false")
