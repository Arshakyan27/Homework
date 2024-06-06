#Write a Python program to get the smallest number from a list.
first = [-1,8,9,15,56]
min = first[0]
for  x in first:
    if x < min:
        min = x
print(min)