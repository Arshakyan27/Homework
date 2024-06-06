# Write a Python function that takes two sets as input and returns a new set containing all
# unique elements from both input sets.

first = str(input("Enter elements of first set by space: "))
second = str(input("Enter elements of second set by space: "))
fir = set(first.split())
sec = set(second.split())

res = fir | sec
if res:
    print("Commons: ",res)
else:  
    print("These sets doesn't have any common elment: ")