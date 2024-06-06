#Write a Python program to find the second smallest number in a list.

first = [1,4,3,4,5,6,7]
smallest = first[0]
second_smallest = 0
for x in first:
    if smallest < x:
        second_smallest = x
     

        