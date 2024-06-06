#Input three integers. Output the word “Sorted” if the numbers are listed in
#a non-increasing or non-decreasing order and “Unsorted” otherwise.

first = int(input("write an integer - "))
second = int(input("write an integer - "))
third = int(input("write an integer - "))
if first < second < third:
    print("sorted")
else: print("unsorted")
