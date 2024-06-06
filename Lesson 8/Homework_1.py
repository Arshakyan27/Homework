# Write a Python function that takes two sets as input and returns a new set containing
# elements that are present in both input sets.
first = str(input("Enter elements by space - "))
second = str(input("enter elements by space - "))
fir = set(first.split())
sec = set(second.split())
res = fir & sec
if res:
    print("commons: ",res)
else: print("There isn't any common element ")