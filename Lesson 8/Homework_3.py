# Write a Python function that takes two sets as input and returns a new set containing
# elements that are present in the first set but not in the second set.

first = str(input("Enter elements of first set by space: "))
second = str(input("Enter elements of second set by space: "))
fir = set(first.split())
sec = set(second.split())
res = fir - sec
if res:
    print("The elements that are in first but not in second: ",res)
else:
    print("There are not elements that are present in first but not in second")