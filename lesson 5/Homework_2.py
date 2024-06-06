#Write a Python program to get the largest number from a list.

first = [7,8,9,15,25]
#multiple = 1
max = first[0]
for  x in first:
    #multiple *= x
    if x > max:
        max = x
print(max)