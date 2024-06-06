#Write a Python program to remove duplicates from a list

first = [1,2,3,4,56,1,2,3,4,]
unique = []
for x in first:
    if x not in unique:
        unique.append(x)
print(unique)