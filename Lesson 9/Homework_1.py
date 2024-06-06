# Print the even numbers from 0 to 20 using a for loop and the range function
li = []
for a in range(0,21):
    if a % 2 == 0:
        li.append(a)
print(li)