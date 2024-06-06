

#Input a two-digit natural number and output the sum of its digits. You canassume that the input will be a two-digit number and need not check that programmatically.
first = int(input("enter a two-digit number ")) 
if len(str(first)) < 2:
     print("your number must me two-digit")
result = int(str(first)[0]) + int(str(first)[1])
print("the sum of two digits of number is equal -", result)    



    

    
    

  